include(FindLua51)
include(FindSDL)
include(FindOpenGL)
include(FindGLUT)
include(FindThreads)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${GLUT_INCLUDE_DIR}
                    ${OPENGL_INCLUDE_DIR})

add_executable(main
               main.c mpool.c machine.c timer.c render.c text.c
               physics.c vector.c input.c vbuf.c ibuf.c mesh.c
               matrix.c buf.c rop.c storage.c)

target_link_libraries(main
                      physics
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${GLUT_LIBRARIES}
                      ${OPENGL_LIBRARIES}
                      ${CMAKE_THREAD_LIBS_INIT})

add_definitions(-std=c99 -ansi -pedantic-errors -Wall -Wextra -Werror
                -DGL_GLEXT_PROTOTYPES=1
                -DGL_GLXEXT_PROTOTYPES=1)
