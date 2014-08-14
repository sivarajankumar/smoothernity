set OPENCLROOT=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v5.0
rd /S /Q G:\TEMP\smoothernity_draft\build_rel
mkdir G:\TEMP\smoothernity_draft\build_rel
g:
cd G:\TEMP\smoothernity_draft\build_rel
cmake C:\Attic\Projects\smoothernity\repo\draft
msbuild ALL_BUILD.vcxproj /t:Rebuild /p:Configuration=Release 
c:
cd C:\Attic\Projects\smoothernity

