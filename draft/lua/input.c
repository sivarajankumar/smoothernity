#include <SDL.h>
#include "input.h"

struct input_t
{
    int key_escape;
};

static struct input_t g_input;

void input_update(void)
{
    SDL_Event event;
    g_input.key_escape = 0;
    while (SDL_PollEvent(&event))
    {
        if (event.type == SDL_KEYDOWN)
        {
            if (event.key.keysym.sym == SDLK_ESCAPE)
                g_input.key_escape = 1;
        }
    }
}

int input_key_escape(void)
{
    return g_input.key_escape;
}
