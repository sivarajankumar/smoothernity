msbuild smoothernity.sln /t:Clean /p:Configuration=Debug
msbuild smoothernity.sln /t:Clean /p:Configuration=Release
del /q /s /a ..\..\..\..\temp\windows
del /q /s /a ..\..\..\..\build\windows
