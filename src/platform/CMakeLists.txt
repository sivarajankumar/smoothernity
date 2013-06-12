if ("${PLATFORM}" STREQUAL "WINDOWS")
    set(SRC ${SRC} ptimer_win.c)
elseif ("${PLATFORM}" STREQUAL "LINUX")
    set(SRC ${SRC} ptimer_posix.c)
endif()

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11)
    set(SRC ${SRC} pmem_gcc.c)
endif()

add_library(platform ${SRC})
