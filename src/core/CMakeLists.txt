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
               main.c mpool.c timer.c render.c text.c physics.c
               vector.c input.c vbuf.c ibuf.c mesh.c matrix.c buf.c
               storage.c shuni.c shprog.c sync.c pbuf.c tex.c query.c)

target_link_libraries(main
                      physics
                      util
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${GLUT_LIBRARIES}
                      ${OPENGL_LIBRARIES}
                      ${CMAKE_THREAD_LIBS_INIT})

add_definitions(-std=c11 -pedantic-errors -Wall -Wextra -Werror
                -DGL_GLEXT_PROTOTYPES=1
                -DGL_GLXEXT_PROTOTYPES=1)
