msbuild smoothernity.sln /t:Clean /p:Configuration=Debug
msbuild smoothernity.sln /t:Clean /p:Configuration=Release
del /q /s /a ..\..\..\..\temp\windows
del /q /s /a ..\..\..\..\build\windows
rmdir /q /s ..\..\..\..\temp\windows
rmdir /q /s ..\..\..\..\build\windows