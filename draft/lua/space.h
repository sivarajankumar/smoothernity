#pragma once

int space_init(int count);
void space_done(void);

void space_query(int *left);

int space_spawn(void);
void space_kill(int space);

struct space_t * space_get(int space);
void space_identity(int space);
void space_offset(int space, float x, float y, float z);
void space_offset_tween(int space, int x, int y, int z);
void space_scale(int space, float x, float y, float z);
void space_scale_tween(int space, int x, int y, int z);
void space_rotation(int space, float angle, float x, float y, float z);
void space_rotation_tween(int space, int angle, float x, float y, float z);
