cmake_minimum_required(VERSION 2.6)
project(SMOOTHERNITY)

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-pedantic-errors -Wall -Wextra -Werror
                    -DCOMPILER_IS_GNU)
elseif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    add_definitions(-W3 -DCOMPILER_IS_MSVC)
endif()

subdirs(core)
subdirs(platform)
subdirs(util)
subdirs(physics)
