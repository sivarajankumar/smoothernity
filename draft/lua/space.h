#pragma once

struct space_t;

int space_init(int count);
void space_done(void);

void space_query(int *left);

int space_alloc(void);
void space_free(int space);

void space_compute(struct space_t *space);
void space_select(struct space_t *space);
struct space_t * space_get(int space);

void space_offset(int space, float x, float y, float z);
void space_offset_tween(int space, int x, int y, int z);
void space_scale(int space, float x, float y, float z);
void space_scale_tween(int space, int x, int y, int z);
void space_rotation(int space, int axis, float angle);
void space_rotation_tween(int space, int axis, int angle);
