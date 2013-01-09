cmake_minimum_required(VERSION 2.6)
project(DRAFT)

include(FindLua51)
include(FindSDL)
include(FindOpenGL)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${OPENGL_INCLUDE_DIR})

add_executable(main
               main.c mpool.c machine.c timer.c display.c
               input.c tween.c vbuf.c ibuf.c space.c)

add_definitions(-std=c99 -ansi -pedantic-errors -Wall -Wextra -Werror
                -DGL_GLEXT_PROTOTYPES=1
                -DGL_GLXEXT_PROTOTYPES=1)

target_link_libraries(main
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${OPENGL_LIBRARIES})
