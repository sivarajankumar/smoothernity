del /q /s ..\..\..\..\build\windows\debug
msbuild smoothernity.sln /p:Configuration=Debug
del /q /s /a ipch
del /q /s /a *.suo
del /q /s /a *.sdf
del /q /s /a *.opensdf