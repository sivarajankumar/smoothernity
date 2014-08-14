export SMOOTHERNITY_SAVE_DIR=~/.smoothernity/save
export SMOOTHERNITY_CACHE_DIR=/tmp/smoothernity/$USER/cache
mkdir -p $SMOOTHERNITY_SAVE_DIR
mkdir -p $SMOOTHERNITY_CACHE_DIR
cd repo/scripts
time /tmp/smoothernity/build_rel/core/main main.lua
cd ../..
