export SMOOTHERNITY_SAVE_DIR=~/.smoothernity/save_stable
export SMOOTHERNITY_CACHE_DIR=/tmp/smoothernity/$USER/cache_stable
mkdir -p $SMOOTHERNITY_SAVE_DIR
mkdir -p $SMOOTHERNITY_CACHE_DIR
cd repo/scripts
time /tmp/smoothernity/build_stable/core/main main.lua
cd ../..
