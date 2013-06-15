include_directories(${CMAKE_SOURCE_DIR}/utilcpp)

add_library(utilc vlog.c)

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c11)
endif()

