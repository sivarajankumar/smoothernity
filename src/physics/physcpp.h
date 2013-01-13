#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int cs_count, int rb_count);
void physcpp_done(void);
void physcpp_update(float dt);
void physcpp_set_gravity(float *v);
int physcpp_cs_alloc_box(int *csi, float mass, float *size);
int physcpp_cs_free(int csi);
int physcpp_rb_alloc(int *rbi, int csi, float *matrix);
int physcpp_rb_free(int rbi);
int physcpp_rb_get_new_matrix(int rbi, float *matrix);
