# Sublime-WolframLanguage

Sublime Text 3 support for the [Wolfram Language](https://en.wikipedia.org/wiki/Wolfram_Language), the language used in Mathematica.

- Syntax highlighting.
- Auto completion for built-in functions.
- Requires Sublime Text 3 Build 3103 or later. This package uses the new syntax format `sublime-syntax`.


## Setup

Sublime-WolframLanguage depends on the CodeParser, CodeInspector, CodeFormatter, and LSPServer paclets. Make sure that the paclets can be found on your system:
```
In[1]:= Needs["CodeParser`"]
      Needs["CodeInspector`"]
      Needs["CodeFormatter`"]
      Needs["LSPServer`"]
```

[CodeParser on github.com](https://github.com/<<TODO_placeholder_for_actual_link>>)
[CodeInspector on github.com](https://github.com/<<TODO_placeholder_for_actual_link>>)
[CodeFormatter on github.com](https://github.com/<<TODO_placeholder_for_actual_link>>)
[CodeParser on github.com](https://github.com/<<TODO_placeholder_for_actual_link>>)

Install LSPServer and dependencies from the CodeTools paclet server:
```
In[1]:= PacletUpdate["CodeParser", "Site" -> "<<TODO_placeholder_for_actual_link>>", "UpdateSites" -> True]
      PacletUpdate["CodeInspector", "Site" -> "<<TODO_placeholder_for_actual_link>>", "UpdateSites" -> True]
      PacletUpdate["CodeFormatter", "Site" -> "<<TODO_placeholder_for_actual_link>>", "UpdateSites" -> True]
      PacletUpdate["LSPServer", "Site" -> "<<TODO_placeholder_for_actual_link>>", "UpdateSites" -> True]

Out[1]= PacletObject[CodeParser, 1.0, <>]
Out[2]= PacletObject[CodeInspector, 1.0, <>]
Out[3]= PacletObject[CodeFormatter, 1.0, <>]
Out[4]= PacletObject[LSPServer, 1.0, <>]
```

If you haven't already, [install Package Control](https://packagecontrol.io/installation), then select `WolframLanguage` from the `Package Control: Install Package` dropdown list in the Command Palette.


In the Command Palette: LSP: Enable Language Server Globally, and select wolfram


Restart Sublime

You should now have syntax highlighting and linting of Wolfram `.m` and `.wl` files working.

Test this by typing this into a new `.m` file and saving it:
```
Which[a, b, a, b]
```

You should see warnings about duplicate clauses.


### Settings

`Package Settings > Wolfram Language > Settings`

```
{
  "kernel": "/Applications/Mathematica121.app/Contents/MacOS/WolframKernel"
}

```


## Troubleshooting


Make sure that the required packages are up-to-date:
sublime-wolframlanguage
LSP package

make sure older versions are not present

Package Control > List Packages


LSP with URL https://github.com/tomv564/LSP
Remove Package


WolframLanguage with URL https://github.com/ViktorQvarfordt/Sublime-WolframLanguage
Remove Package

### Debugging

Turn on debug LSP settings


LSP > Settings

```
{
  "log_debug": true,
  "log_server": true,
  "log_payloads": true,
  "log_stderr": true
}
```

### Windows

You may need to double-up quotations marks in the command:

``"Needs[\"\"LSPServer`\"\"];LSPServer`StartServer[]"``



