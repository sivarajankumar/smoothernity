#include <SDL.h>
#include "display.h"

struct display_t
{
    SDL_Surface *screen;
    int width;
    int height;
};

static struct display_t g_display;

int display_set_mode(int width, int height, int bpp)
{
	g_display.screen = SDL_SetVideoMode(width, height, bpp, SDL_HWSURFACE);
    if (g_display.screen == 0)
        return 1;
    g_display.width = width;
    g_display.height = height;
    return 0;
}

void display_get_mode(int *width, int *height)
{
    *width = g_display.width;
    *height = g_display.height;
}
