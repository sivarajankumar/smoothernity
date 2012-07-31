mkdir -p ../../build
rm ../../build/continuation
gcc continuation.c -pedantic -o ../../build/continuation && ../../build/continuation
