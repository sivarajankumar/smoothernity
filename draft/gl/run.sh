gcc hellogl.c -o hellogl -Wall -std=c99 $(pkg-config --libs --cflags sdl2 gl glew)
./hellogl
