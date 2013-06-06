add_library(mp thread.cpp)

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c++11)
endif()

