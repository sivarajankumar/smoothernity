del /q /s ..\..\..\..\build\windows\release
msbuild smoothernity.sln /p:Configuration=Release
del /q /s /a ipch
del /q /s /a *.suo
del /q /s /a *.sdf
del /q /s /a *.opensdf
rmdir /s /q ipch