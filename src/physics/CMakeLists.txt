include(FindLua51)
include(FindBullet)

include_directories(${LUA_INCLUDE_DIR}
                    ${BULLET_INCLUDE_DIRS})

add_library(physics physics.cpp)

target_link_libraries(physics ${BULLET_LIBRARIES})

add_definitions(-ansi -pedantic-errors -Wall -Wextra)
