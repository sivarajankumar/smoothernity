find_package(GLEW REQUIRED)
find_package(Bullet REQUIRED)

include_directories(${GLEW_INCLUDE_DIRS}
                    ${BULLET_INCLUDE_DIRS}
                    ${CMAKE_SOURCE_DIR}/utilc
                    ${CMAKE_SOURCE_DIR}/platform)

add_library(physics yphyscpp.cpp ycolshape.cpp ymstate.cpp yphysdbg.cpp
            rigidbody.cpp yddraw.cpp vehicle.cpp world.cpp)

target_link_libraries(physics util ${BULLET_LIBRARIES})

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c++11)
endif()
