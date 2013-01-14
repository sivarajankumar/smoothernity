#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int cs_count, int rb_count, int veh_count);
void physcpp_done(void);
void physcpp_update(float dt);
void physcpp_ddraw(void);
void physcpp_ddraw_set_mode(int mode);
void physcpp_set_gravity(float *v);
void physcpp_left(int *cs_left, int *rb_left);
int physcpp_cs_alloc_box(int *csi, float mass, float *size);
int physcpp_cs_alloc_hmap(int *csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale);
int physcpp_cs_free(int csi);
int physcpp_rb_alloc(int *rbi, int csi, float *matrix,
                     float frict, float roll_frict);
int physcpp_rb_free(int rbi);
int physcpp_rb_fetch_tm(int rbi, float *matrix);
