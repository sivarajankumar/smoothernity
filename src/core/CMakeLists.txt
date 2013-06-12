find_package(Lua51 REQUIRED)
find_package(SDL 1.2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${GLEW_INCLUDE_DIRS}
                    ${OPENGL_INCLUDE_DIR}
                    ${CMAKE_SOURCE_DIR}/util
                    ${CMAKE_SOURCE_DIR}/platform)

add_executable(main
               main.c mpool.c timer.c render.c physics.c cthread.c rbuf.c
               vector.c cinput.c matrix.c cbuf.c interp.c prog.c vao.c util.c)

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
