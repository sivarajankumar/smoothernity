cmake_minimum_required(VERSION 2.6)
project(DRAFT)

include(FindLua51)
include(FindSDL)

include_directories(${LUA_INCLUDE_DIR} ${SDL_INCLUDE_DIR})

add_executable(main main.c mpool.c machine.c timer.c)

target_link_libraries(main ${LUA_LIBRARIES} ${SDL_LIBRARY})
