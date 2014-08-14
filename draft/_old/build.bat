set SDLDIR=C:\Devel\SDL
set LUA_DIR=C:\Devel\Lua
rd /S /Q G:\TEMP\smoothernity\build_rel
mkdir G:\TEMP\smoothernity\build_rel
g:
cd G:\TEMP\smoothernity\build_rel
cmake -DSDL_LIBRARY_TEMP="C:\Devel\SDL\lib\x86\SDL.lib" ^
      -DCMAKE_INCLUDE_PATH="C:\Devel\glew\include" ^
      -DCMAKE_FRAMEWORK_PATH="C:\Devel\glew\lib" ^
      -DBULLET_ROOT="C:\Devel\bullet" ^
      -DPLATFORM="WINDOWS" ^
      C:\Attic\Projects\smoothernity\repo\src
msbuild ALL_BUILD.vcxproj /t:Rebuild /p:Configuration=Release 
c:
cd C:\Attic\Projects\smoothernity
