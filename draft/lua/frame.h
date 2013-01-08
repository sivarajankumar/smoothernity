#pragma once

int frame_init(int len);
void frame_done(void);

int frame_spawn(void);
void frame_kill(int frame);

void frame_identity(int frame);
void frame_translation(int frame, float x, float y, float z);
void frame_translation_tween(int frame, int x, int y, int z);
void frame_rotation(int frame, float angle, float x, float y, float z);
void frame_rotation_tween(int frame, int angle, float x, float y, float z);
void frame_scale(int frame, float x, float y, float z);
void frame_scale_tween(int frame, int x, int y, int z);
