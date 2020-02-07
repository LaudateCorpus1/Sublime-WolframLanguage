import shutil
import os
import sublime
import threading
import subprocess

from LSP.plugin.core.handlers import LanguageHandler
from LSP.plugin.core.settings import ClientConfig, LanguageConfig, read_client_config


package_path = os.path.dirname(__file__)
server_path = os.path.join(package_path, 'node_modules', '@elm-tooling', 'elm-language-server', 'out', 'index.js')


def plugin_loaded():
    is_server_installed = os.path.isfile(server_path)
    print('LSP-wolfram: Server {} installed.'.format('is' if is_server_installed else 'is not' ))

    # install if not installed
    if not is_server_installed:
        # this will be called only when the plugin gets:
        # - installed for the first time,
        # - or when updated on package control
        logAndShowMessage('LSP-wolfram: Installing server.')

        runCommand(
            onCommandDone,
            ["npm", "install", "--verbose", "--prefix", package_path, package_path]
        )


def onCommandDone():
    logAndShowMessage('LSP-wolfram: Server installed.')


def runCommand(onExit, popenArgs):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    onExit when the subprocess completes.
    onExit is a callable object, and popenArgs is a list/tuple of args that
    would give to subprocess.Popen.
    """
    def runInThread(onExit, popenArgs):
        try:
            if sublime.platform() == 'windows':
                subprocess.check_call(popenArgs, shell=True)
            else:
                subprocess.check_call(popenArgs)
            onExit()
        except subprocess.CalledProcessError as error:
            logAndShowMessage('LSP-wolfram: Error while installing the server.', error)
        return
    thread = threading.Thread(target=runInThread, args=(onExit, popenArgs))
    thread.start()
    # returns immediately after the thread starts
    return thread


def is_node_installed():
    return shutil.which('node') is not None


def logAndShowMessage(msg, additional_logs=None):
    print(msg, '\n', additional_logs) if additional_logs else print(msg)
    sublime.active_window().status_message(msg)


class LspElmPlugin(LanguageHandler):
    @property
    def name(self) -> str:
        return 'lsp-wolfram'

    @property
    def config(self) -> ClientConfig:
        settings = sublime.load_settings("LSP-wolfram.sublime-settings")
        client_configuration = settings.get('client')

        default_configuration = {
            "command": [
                'node',
                server_path,
                '--stdio'
            ],
            "languages": [
                {
                    "languageId": "wolfram",
                    "scopes": ["source.wolfram"],
                    "syntaxes": ["Packages/User/WolframLanguage/WolframLanguage.sublime-syntax"]
                }
            ],
            "initializationOptions": {
                "elmAnalyseTrigger": "change"
            }
        }
        default_configuration.update(client_configuration)
        return read_client_config('lsp-wolfram', default_configuration)

    def on_start(self, window) -> bool:
        if not is_node_installed():
            sublime.status_message('Please install Node.js for the Elm Language Server to work.')
            return False
        return True

    def on_initialized(self, client) -> None:
        pass   # extra initialization here.