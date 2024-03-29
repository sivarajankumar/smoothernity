find_package(Lua51 REQUIRED)
find_package(SDL 1.2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(GLEW REQUIRED)

include_directories(${LUA_INCLUDE_DIR}
                    ${SDL_INCLUDE_DIR}
                    ${GLEW_INCLUDE_DIRS}
                    ${OPENGL_INCLUDE_DIR}
                    ${CMAKE_SOURCE_DIR}/utilc
                    ${CMAKE_SOURCE_DIR}/utilcpp
                    ${CMAKE_SOURCE_DIR}/physics
                    ${CMAKE_SOURCE_DIR}/platform)

add_executable(main
               cmain.c cmpool.c ctimer.c crender.c cphysics.c
               cthread.c crbuf.c cvector.c cinput.c cmatrix.c
               cbuf.c cinterp.c cprog.c cvao.c cutil.c clog.c)

target_link_libraries(main
                      physics platform utilc utilcpp
                      ${LUA_LIBRARIES}
                      ${SDL_LIBRARY}
                      ${GLEW_LIBRARIES}
                      ${OPENGL_LIBRARIES})

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11
                    -DGL_GLEXT_PROTOTYPES=1
                    -DGL_GLXEXT_PROTOTYPES=1)
endif()
