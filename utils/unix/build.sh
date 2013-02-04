PROJECTDIR=`pwd`
rm -rfv /tmp/smoothernity/build_rel
mkdir -pv /tmp/smoothernity/build_rel
cd /tmp/smoothernity/build_rel
cmake $PROJECTDIR/repo/src
time make -j8
cd $PROJECTDIR
