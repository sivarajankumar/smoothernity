pacman -S zeromq lua luarocks
luarocks install lzmq 0.3.5
lua hwserver.lua
lua hwclient.lua
