find_package(Lua51 REQUIRED)
find_package(SDL2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL2_INCLUDE_DIR}
                    ${GLEW_INCLUDE_DIRS}
                    ${OPENGL_INCLUDE_DIR})

add_executable(main
               main.c mpool.c timer.c render.c physics.c thread.c
               vector.c input.c matrix.c buf.c shell.c interp.c)

target_link_libraries(main
                      physics
                      platform
                      thread
                      util
                      ${LUA_LIBRARIES}
                      ${SDL2_LIBRARY}
                      ${GLEW_LIBRARIES}
                      ${OPENGL_LIBRARIES})

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11
                    -DGL_GLEXT_PROTOTYPES=1
                    -DGL_GLXEXT_PROTOTYPES=1)
endif()
