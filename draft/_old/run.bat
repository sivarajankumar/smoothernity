setlocal
set PATH=%PATH%;C:\Devel\Lua;C:\Devel\SDL\lib\x86;C:\Devel\glew\bin
set SMOOTHERNITY_SAVE_DIR=C:\Temp\smoothernity\save
set SMOOTHERNITY_CACHE_DIR=G:\TEMP\smoothernity\cache
mkdir %SMOOTHERNITY_SAVE_DIR%
mkdir %SMOOTHERNITY_CACHE_DIR%
cd repo\scripts
G:\TEMP\smoothernity\build_rel\core\Release\main main.lua
cd ..\..

