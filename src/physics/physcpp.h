#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int cs_count, int rb_count, int veh_count);
void physcpp_done(void);
void physcpp_update(float dt);
void physcpp_ddraw(void);
void physcpp_ddraw_set_mode(int mode);
void physcpp_set_gravity(float *v);
void physcpp_left(int *cs_left, int *rb_left, int *veh_left);
int physcpp_cs_alloc_box(int *csi, float mass, float *size);
int physcpp_cs_alloc_hmap(int *csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale);
int physcpp_cs_free(int csi);
int physcpp_rb_alloc(int *rbi, int csi, float *matrix,
                     float frict, float roll_frict);
int physcpp_rb_free(int rbi);
int physcpp_rb_fetch_tm(int rbi, float *matrix);
int physcpp_veh_alloc(int *vehi, int csi, float *matrix,
                      float ch_frict, float ch_roll_frict,
                      float sus_stif, float sus_comp, float sus_damp,
                      float sus_trav, float sus_force, float slip_frict);
int physcpp_veh_free(int vehi);
int physcpp_veh_add_wheel(int *wheel, int vehi, float *pos, float *dir,
                          float *axl, float sus_rest, float roll,
                          float radius, int front);
int physcpp_veh_set_wheel(int vehi, int wheel, float engine,
                          float brake, float steer);
int physcpp_veh_fetch_chassis_tm(int vehi, float *matrix);
int physcpp_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix);
int physcpp_veh_transform(int vehi, float *matrix);
int physcpp_veh_wheel_contact(int vehi, int wheel, int *in_contact);
