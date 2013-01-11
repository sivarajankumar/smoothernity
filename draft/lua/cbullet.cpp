#include <iostream>

extern "C" int cbullet_init(void)
{
    std::cout << "cbullet_init" << std::endl;
    return 0;
}

extern "C" void cbullet_done(void)
{
    std::cout << "cbullet_done" << std::endl;
}
