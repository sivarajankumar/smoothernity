PROJECTDIR=`pwd`
rm -rfv /tmp/smoothernity/build_dbg
mkdir -pv /tmp/smoothernity/build_dbg
cd /tmp/smoothernity/build_dbg
cmake $PROJECTDIR/repo/src -DCMAKE_BUILD_TYPE=Debug
make -j8
cd $PROJECTDIR/repo/scripts
gdb /tmp/smoothernity/build_dbg/core/main
cd $PROJECTDIR
