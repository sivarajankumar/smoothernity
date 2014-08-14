PROJECTDIR=`pwd`
rm -rfv /tmp/smoothernity/build_stable
mkdir -pv /tmp/smoothernity/build_stable
cd /tmp/smoothernity/build_stable
cmake $PROJECTDIR/repo/src
time make -j8
cd $PROJECTDIR
