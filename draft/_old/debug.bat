set SDLDIR=C:\Devel\SDL
set LUA_DIR=C:\Devel\Lua
rd /S /Q G:\TEMP\smoothernity\build_dbg
mkdir G:\TEMP\smoothernity\build_dbg
g:
cd G:\TEMP\smoothernity\build_dbg
cmake -DSDL_LIBRARY_TEMP="C:\Devel\SDL\lib\x86\SDL.lib" ^
      -DCMAKE_INCLUDE_PATH="C:\Devel\glew\include" ^
      -DCMAKE_FRAMEWORK_PATH="C:\Devel\glew\lib" ^
      -DBULLET_ROOT="C:\Devel\bullet" ^
      -DPLATFORM="WINDOWS" ^
      -DCMAKE_BUILD_TYPE=Debug ^
      C:\Attic\Projects\smoothernity\repo\src
msbuild ALL_BUILD.vcxproj /t:Rebuild /p:Configuration=Debug 
c:
cd C:\Attic\Projects\smoothernity

