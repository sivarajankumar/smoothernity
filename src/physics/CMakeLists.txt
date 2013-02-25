include(FindLua51)
include(FindBullet)

include_directories(${LUA_INCLUDE_DIR}
                    ${BULLET_INCLUDE_DIRS})

add_library(physics physcpp.cpp colshape.cpp mstate.cpp 
            rigidbody.cpp ddraw.cpp vehicle.cpp world.cpp)

target_link_libraries(physics util ${BULLET_LIBRARIES})

if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    add_definitions(-std=c++11)
endif()
