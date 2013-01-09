#include "text.h"
#include <stdlib.h>
#include <string.h>
#include <GL/glut.h>

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
    struct text_t *pool;
    struct text_t *vacant;
    struct text_t *active;
};

static struct texts_t g_texts;

int text_init(int size, int count)
{
    int i;
    g_texts.pool = calloc(count, sizeof(struct text_t));
    if (g_texts.pool == 0)
        return 1;
    for (i = 0; i < count; ++i)
    {
        if (i > 0)
            g_texts.pool[i].prev = g_texts.pool + i - 1;
        if (i < count - 1)
            g_texts.pool[i].next = g_texts.pool + i + 1;
        g_texts.pool[i].string = calloc(size, sizeof(char));
        if (g_texts.pool[i].string == 0)
            goto cleanup;
        g_texts.pool[i].vacant = 1;
    }
    g_texts.size = size;
    g_texts.count = count;
    g_texts.left = count;
    g_texts.vacant = g_texts.pool;
    return 0;
cleanup:
    for (i = 0; i < count; ++i)
    {
        if (g_texts.pool[i].string)
            free(g_texts.pool[i].string);
    }
    free(g_texts.pool);
    g_texts.pool = 0;
    return 1;
}

void text_done(void)
{
    int i;
    if (g_texts.pool)
    {
        for (i = 0; i < g_texts.count; ++i)
            free(g_texts.pool[i].string);
        free(g_texts.pool);
        g_texts.pool = 0;
    }
}

void text_query(int *size, int *left)
{
    *size = g_texts.size;
    *left = g_texts.left;
}

void text_draw(void)
{
    int i;
    struct text_t *text;
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

int text_alloc(const char *string, int font, int x, int y)
{
    size_t size;
    struct text_t *text;

    if (g_texts.vacant == 0)
        return -1;
    if (font < 0 || font >= TEXT_FONTS_TOTAL)
        return -1;
    if (*string == 0)
        return -1;

    --g_texts.left;

    text = g_texts.vacant;
    g_texts.vacant = g_texts.vacant->next;

    if (g_texts.active)
        g_texts.active->prev = text;
    text->prev = 0;
    text->next = g_texts.active;
    g_texts.active = text;

    size = strlen(string);
    if (size > (size_t)g_texts.size)
        size = (size_t)g_texts.size;
    memcpy(text->string, string, size);

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

    return text - g_texts.pool;
}

void text_free(int texti)
{
    struct text_t *text;
    if (texti < 0 || texti >= g_texts.count)
        return;
    text = g_texts.pool + texti;
    if (text->vacant)
        return;
    text->vacant = 1;
    ++g_texts.left;

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
}
