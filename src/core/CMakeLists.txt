find_package(Lua51 REQUIRED)
find_package(SDL 1.2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${GLEW_INCLUDE_DIRS}
                    ${OPENGL_INCLUDE_DIR})

add_executable(main
               main.c mpool.c timer.c render.c physics.c thread.c rbuf.c
               vector.c input.c matrix.c buf.c interp.c prog.c vao.c util.c)

target_link_libraries(main
                      physics platform util
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${GLEW_LIBRARIES}
                      ${OPENGL_LIBRARIES})

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11
                    -DGL_GLEXT_PROTOTYPES=1
                    -DGL_GLXEXT_PROTOTYPES=1)
endif()
