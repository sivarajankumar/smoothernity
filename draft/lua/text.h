#pragma once

int text_init(int size, int count);
void text_done(void);
void text_query(int *size, int *left);
void text_draw(void);
int text_alloc(const char *string, int font, int x, int y);
void text_free(int text);
