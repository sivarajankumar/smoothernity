cmake_minimum_required(VERSION 2.6)
project(DRAFT)

include(FindLua51)
include(FindSDL)
include(FindOpenGL)
include(FindGLUT)
include(FindBullet)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${BULLET_INCLUDE_DIRS}
                    ${GLUT_INCLUDE_DIR}
                    ${OPENGL_INCLUDE_DIR})

add_executable(main
               main.c mpool.c machine.c timer.c display.c text.c
               vector.c input.c vbuf.c ibuf.c mesh.c matrix.c)

add_library(physics physics.cpp)

add_definitions(-ansi -pedantic-errors -Wall -Wextra -Werror
                -DGL_GLEXT_PROTOTYPES=1
                -DGL_GLXEXT_PROTOTYPES=1)

target_link_libraries(physics ${BULLET_LIBRARIES})

target_link_libraries(main
                      physics
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${GLUT_LIBRARIES}
                      ${OPENGL_LIBRARIES})
