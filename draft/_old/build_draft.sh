PROJECTDIR=`pwd`
rm -rfv /tmp/smoothernity_draft/build_rel
mkdir -pv /tmp/smoothernity_draft/build_rel
cd /tmp/smoothernity_draft/build_rel
cmake $PROJECTDIR/repo/draft
time make -j8
cd $PROJECTDIR

