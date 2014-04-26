g++ -std=c++11 hellosdl.cpp -o hellosdl $(pkg-config --cflags --libs sdl2)
./hellosdl
