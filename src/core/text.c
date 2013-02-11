#include "text.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>
#include <GL/glut.h>

static const size_t TEXT_SIZE = 64;
static const size_t TEXT_STRING_ALIGN = 16;

enum text_font_e
{
    TEXT_FONT_8_BY_13 = 0,
    TEXT_FONT_9_BY_15 = 1,
    TEXT_FONT_TIMES_ROMAN_10 = 2,
    TEXT_FONT_TIMES_ROMAN_24 = 3,
    TEXT_FONT_HELVETICA_10 = 4,
    TEXT_FONT_HELVETICA_12 = 5,
    TEXT_FONT_HELVETICA_18 = 6,
    TEXT_FONTS_TOTAL = 7
};

struct text_t
{
    char *string;
    void *font;
    GLint pos[2];
    int vacant;
    struct text_t *prev;
    struct text_t *next;
};

struct texts_t
{
    int size;
    int count;
    int left;
    int left_min;
    int allocs;
    int frees;
    char *pool;
    struct text_t *vacant;
    struct text_t *active;
};

static struct texts_t g_texts;

static struct text_t * text_get(int texti)
{
    if (texti >= 0 && texti < g_texts.count)
        return (struct text_t*)(g_texts.pool + TEXT_SIZE * texti);
    else
        return 0;
}

static int api_text_alloc(lua_State *lua)
{
    const char *string;
    int font, x, y;
    size_t size;
    struct text_t *text;

    if (lua_gettop(lua) != 4 || !lua_isstring(lua, 1)
    || !lua_isnumber(lua, 2) || !lua_isnumber(lua, 3)
    || !lua_isnumber(lua, 4))
    {
        lua_pushstring(lua, "api_text_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    
    string = lua_tostring(lua, 1);
    font = lua_tointeger(lua, 2);
    x = lua_tointeger(lua, 3);
    y = lua_tointeger(lua, 4);
    lua_pop(lua, 4);

    if (g_texts.vacant == 0)
    {
        lua_pushstring(lua, "api_text_alloc: out of texts");
        lua_error(lua);
        return 0;
    }

    if (font < 0 || font >= TEXT_FONTS_TOTAL)
    {
        lua_pushstring(lua, "api_text_alloc: invalid font");
        lua_error(lua);
        return 0;
    }

    if (*string == 0)
    {
        lua_pushstring(lua, "api_text_alloc: string is empty");
        lua_error(lua);
        return 0;
    }

    ++g_texts.allocs;
    --g_texts.left;
    if (g_texts.left < g_texts.left_min)
        g_texts.left_min = g_texts.left;

    text = g_texts.vacant;
    g_texts.vacant = g_texts.vacant->next;

    if (g_texts.active)
        g_texts.active->prev = text;
    text->prev = 0;
    text->next = g_texts.active;
    g_texts.active = text;

    size = strlen(string);
    if (size >= (size_t)g_texts.size)
        size = (size_t)(g_texts.size - 1);
    memcpy(text->string, string, size);
    text->string[size] = 0;

    if (font == (int)TEXT_FONT_8_BY_13)
        text->font = GLUT_BITMAP_8_BY_13;
    else if (font == (int)TEXT_FONT_9_BY_15)
        text->font = GLUT_BITMAP_9_BY_15;
    else if (font == (int)TEXT_FONT_TIMES_ROMAN_10)
        text->font = GLUT_BITMAP_TIMES_ROMAN_10;
    else if (font == (int)TEXT_FONT_TIMES_ROMAN_24)
        text->font = GLUT_BITMAP_TIMES_ROMAN_24;
    else if (font == (int)TEXT_FONT_HELVETICA_10)
        text->font = GLUT_BITMAP_HELVETICA_10;
    else if (font == (int)TEXT_FONT_HELVETICA_12)
        text->font = GLUT_BITMAP_HELVETICA_12;
    else
        text->font = GLUT_BITMAP_HELVETICA_18;

    text->pos[0] = x;
    text->pos[1] = y;
    text->vacant = 0;

    lua_pushinteger(lua, ((char*)text - g_texts.pool) / TEXT_SIZE);
    return 1;
}

static int api_text_free(lua_State *lua)
{
    struct text_t *text;

    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_text_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    text = text_get(lua_tointeger(lua, 1));
    lua_pop(lua, 1);

    if (text == 0 || text->vacant)
    {
        lua_pushstring(lua, "api_text_free: invalid text");
        lua_error(lua);
        return 0;
    }

    text->vacant = 1;
    ++g_texts.left;
    ++g_texts.frees;

    if (g_texts.active == text)
        g_texts.active = text->next;
    if (text->prev)
        text->prev->next = text->next;
    if (text->next)
        text->next->prev = text->prev;

    if (g_texts.vacant)
        g_texts.vacant->prev = text;
    text->prev = 0;
    text->next = g_texts.vacant;
    g_texts.vacant = text;
    return 0;
}

static int api_text_left(lua_State *lua)
{
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_text_left: incorrect argument");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_texts.left);
    return 2;
}

int text_init(lua_State *lua, int size, int count)
{
    int i;
    struct text_t *text;
    if (sizeof(struct text_t) > TEXT_SIZE
    ||  (size & (size - 1)) != 0)
    {
        fprintf(stderr, "Invalid sizes:\n"
                        "sizeof(struct text_t) == %i\n"
                        "size == %i\n",
                (int)sizeof(struct text_t),
                size);
        return 1;
    }
    g_texts.pool = util_malloc(TEXT_SIZE, TEXT_SIZE * count);
    if (g_texts.pool == 0)
        return 1;
    memset(g_texts.pool, 0, TEXT_SIZE * count);
    g_texts.size = size;
    g_texts.count = count;
    g_texts.left = count;
    g_texts.left_min = count;
    g_texts.vacant = text_get(0);
    for (i = 0; i < count; ++i)
    {
        text = text_get(i);
        text->prev = text_get(i - 1);
        text->next = text_get(i + 1);
        text->string = util_malloc(TEXT_STRING_ALIGN, sizeof(char) * size);
        if (text->string == 0)
            goto cleanup;
        memset(text->string, 0, sizeof(char) * size);
        text->vacant = 1;
    }

    lua_register(lua, "api_text_alloc", api_text_alloc);
    lua_register(lua, "api_text_free", api_text_free);
    lua_register(lua, "api_text_left", api_text_left);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(TEXT_FONT_8_BY_13);
    LUA_PUBLISH(TEXT_FONT_9_BY_15);
    LUA_PUBLISH(TEXT_FONT_TIMES_ROMAN_10);
    LUA_PUBLISH(TEXT_FONT_TIMES_ROMAN_24);
    LUA_PUBLISH(TEXT_FONT_HELVETICA_10);
    LUA_PUBLISH(TEXT_FONT_HELVETICA_12);
    LUA_PUBLISH(TEXT_FONT_HELVETICA_18);

    return 0;
cleanup:
    for (i = 0; i < count; ++i)
    {
        text = text_get(i);
        if (text->string)
            util_free(text->string);
    }
    util_free(g_texts.pool);
    g_texts.pool = 0;
    return 1;
}

void text_done(void)
{
    int i;
    if (g_texts.pool == 0)
        return;
    printf("Texts usage: %i/%i, allocs/frees: %i/%i\n",
           g_texts.count - g_texts.left_min, g_texts.count,
           g_texts.allocs, g_texts.frees);
    for (i = 0; i < g_texts.count; ++i)
        util_free(text_get(i)->string);
    util_free(g_texts.pool);
    g_texts.pool = 0;
}

void text_draw(void)
{
    int i;
    struct text_t *text;
    glColor4f(1, 1, 1, 1);
    for (text = g_texts.active; text; text = text->next)
    {
        glRasterPos2iv(text->pos);
        for (i = 0; i < g_texts.size; ++i)
        {
            if (text->string[i] == 0)
                break;
            glutBitmapCharacter(text->font, text->string[i]);
        }
    }
}
