#pragma once

int tween_init(int len);
void tween_done(void);
void tween_update(float dt);
int tween_spawn(void);
void tween_kill(int);
void tween_play_sine(int tween, float shift, float ampl, float period);
float tween_value(int);
