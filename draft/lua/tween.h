#pragma once

int tween_init(int len);
void tween_done(void);
void tween_update(float dt);
struct tween_t * tween_get(int);
int tween_alloc(void);
void tween_free(int);
void tween_play_sine(int tween, float shift, float ampl, float period);
