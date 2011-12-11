del /q /s ..\..\..\..\build\windows\debug
msbuild smoothernity.sln /p:Configuration=Debug /m
del /q /s /a ipch
del /q /s /a *.user
del /q /s /a *.suo
del /q /s /a *.sdf
del /q /s /a *.opensdf
rmdir /s /q ipch