include(FindGLEW)

include_directories(${GLEW_INCLUDE_DIRS})

if ("${PLATFORM}" STREQUAL "WINDOWS")
    add_library(platform timer_win.c render_win.c shell_win.c)
elseif ("${PLATFORM}" STREQUAL "LINUX")
    add_library(platform timer_posix.c)
endif()

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11)
endif()

target_link_libraries(platform util ${GLEW_LIBRARIES})
