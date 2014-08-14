setlocal
set PATH=%PATH%;C:\Devel\Lua;C:\Devel\SDL\lib\x86;C:\Devel\glew\bin
set SMOOTHERNITY_SAVE_DIR=C:\Temp\smoothernity\save_stable
set SMOOTHERNITY_CACHE_DIR=G:\TEMP\smoothernity\cache_stable
mkdir %SMOOTHERNITY_SAVE_DIR%
mkdir %SMOOTHERNITY_CACHE_DIR%
cd repo.stable\scripts
G:\TEMP\smoothernity\build_rel_stable\core\Release\main main.lua
cd ..\..


