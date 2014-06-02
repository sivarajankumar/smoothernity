cmake_minimum_required(VERSION 2.6)
project(SANDBOX)

find_package(Lua51 REQUIRED)
include_directories(${LUA_INCLUDE_DIR})
add_executable(sandbox sandbox.c)
target_link_libraries(sandbox ${LUA_LIBRARIES})

endif()
