cmake_minimum_required(VERSION 2.6)
project(DRAFT)

include(FindLua51)

include_directories(${LUA_INCLUDE_DIR})

add_executable(main main.c)

target_link_libraries(main ${LUA_LIBRARIES})

