#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int wld_count, int cs_count, int rb_count, int veh_count);
void physcpp_done(void);
void physcpp_left(int *wld_left, int *cs_left, int *rb_left, int *veh_left);
int physcpp_wld_update(float dt);
int physcpp_wld_alloc(int *wldi);
int physcpp_wld_free(int wldi);
int physcpp_wld_tscale(int wldi, float);
int physcpp_wld_ddraw(int wldi);
int physcpp_wld_ddraw_mode(int wldi, int mode);
int physcpp_wld_gravity(int wldi, float *v);
int physcpp_wld_move(int wldi, float*);
int physcpp_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout);
int physcpp_cs_alloc_box(int *csi, float *size);
int physcpp_cs_alloc_sphere(int *csi, float r);
int physcpp_cs_alloc_hmap(int *csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale);
int physcpp_cs_alloc_comp(int *csi);
int physcpp_cs_comp_add(int parenti, float *matrix, int childi);
int physcpp_cs_free(int csi);
int physcpp_rb_alloc(int *rbi, int wldi, int csi, float *matrix,
                     float mass, float frict, float roll_frict);
int physcpp_rb_free(int rbi);
int physcpp_rb_fetch_tm(int rbi, float *matrix);
int physcpp_veh_alloc(int *vehi, int wldi, int shapei, int inerti, float *tm,
                      float mass, float ch_frict, float ch_roll_frict,
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
