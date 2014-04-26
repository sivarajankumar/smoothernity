g++ hellobullet.cpp -o hellobullet $(pkg-config --libs --cflags bullet)
./hellobullet
