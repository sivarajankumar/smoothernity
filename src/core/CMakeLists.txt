include(FindLua51)
include(FindSDL)
include(FindOpenGL)
include(FindGLEW)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${GLEW_INCLUDE_DIRS}
                    ${OPENGL_INCLUDE_DIR})

add_executable(main
               main.c mpool.c timer.c render.c physics.c thread.c
               vector.c input.c vbuf.c ibuf.c mesh.c matrix.c buf.c
               storage.c shuni.c shprog.c sync.c pbuf.c tex.c query.c)

target_link_libraries(main
                      physics
                      platform
                      thread
                      util
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${GLEW_LIBRARIES}
                      ${OPENGL_LIBRARIES})
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11
                    -DGL_GLEXT_PROTOTYPES=1
                    -DGL_GLXEXT_PROTOTYPES=1)
endif()
