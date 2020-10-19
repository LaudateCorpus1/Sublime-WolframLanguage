BeginPackage["SublimeWolframLanguage`Generate`GenerateSources`"]

buildDirFlagPosition

buildDir

srcDirFlagPosition

srcDir

script

generatedWLDir

dataDir


importedLongNames

importedUnsupportedLongNames


longNameToCharacterCode

longNameToHexDigits

codePointToHexDigits


Begin["`Private`"]

longNameToCharacterCode[name_] := importedLongNames[name][[2]]



buildDirFlagPosition = FirstPosition[$CommandLine, "-buildDir"]

If[MissingQ[buildDirFlagPosition],
  Print["Cannot proceed; Unsupported build directory"];
  Quit[1]
]

buildDir = $CommandLine[[buildDirFlagPosition[[1]] + 1]]

If[!DirectoryQ[buildDir],
  Print["Cannot proceed; Unsupported build directory"];
  Quit[1]
]

srcDirFlagPosition = FirstPosition[$CommandLine, "-srcDir"]

If[MissingQ[srcDirFlagPosition],
  Print["Cannot proceed; Unsupported src directory"];
  Quit[1]
]

srcDir = $CommandLine[[srcDirFlagPosition[[1]] + 1]]

If[!DirectoryQ[srcDir],
  Print["Cannot proceed; Unsupported src directory"];
  Quit[1]
]

scriptPosition = FirstPosition[$CommandLine, "-script"]

If[MissingQ[scriptPosition],
  Print["Cannot proceed; Unsupported script"];
  Quit[1]
]

script = $CommandLine[[scriptPosition[[1]] + 1]]



generatedWLDir = FileNameJoin[{buildDir, "generated", "wl"}]


dataDir = FileNameJoin[{srcDir, "SublimeWolframLanguage", "Data"}]



importedLongNames = Get[FileNameJoin[{dataDir, "LongNames.wl"}]]

importedUnsupportedLongNames = Keys[Select[importedLongNames, #[[1]] === UnsupportedCharacter &]]



End[]

EndPackage[]
