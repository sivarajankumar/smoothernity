#ifndef YPHYSCPP_H
#define YPHYSCPP_H

int yphyscpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int wld_count, int cs_count, int rb_count, int veh_count);
void yphyscpp_done(void);
int yphyscpp_wld_update(int wldi, float dt);
int yphyscpp_wld_ddraw(int wldi);
int yphyscpp_wld_ddraw_mode(int wldi, int mode);
int yphyscpp_wld_gravity(int wldi, float *v);
int yphyscpp_wld_move(int wldi, float*);
int yphyscpp_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout);
int yphyscpp_cs_alloc_box(int csi, float *size);
int yphyscpp_cs_alloc_sphere(int csi, float r);
int yphyscpp_cs_alloc_hmap(int csi, float *hmap, int width, int length,
                          float hmin, float hmax, float *scale);
int yphyscpp_cs_alloc_comp(int csi);
int yphyscpp_cs_comp_add(int parenti, float *matrix, int childi);
int yphyscpp_cs_free(int csi);
int yphyscpp_rb_alloc(int rbi, int wldi, int csi, float *matrix,
                     float mass, float frict, float roll_frict);
int yphyscpp_rb_free(int rbi);
int yphyscpp_rb_fetch_tm(int rbi, float *matrix);
int yphyscpp_veh_alloc(int vehi, int wldi, int shapei, int inerti, float *tm,
                      float mass, float ch_frict, float ch_roll_frict,
                      float sus_stif, float sus_comp, float sus_damp,
                      float sus_trav, float sus_force, float slip_frict);
int yphyscpp_veh_free(int vehi);
int yphyscpp_veh_add_wheel(int *wheel, int vehi, float *pos, float *dir,
                          float *axl, float sus_rest, float roll,
                          float radius, int front);
int yphyscpp_veh_set_wheel(int vehi, int wheel, float engine,
                          float brake, float steer);
int yphyscpp_veh_fetch_chassis_tm(int vehi, float *matrix);
int yphyscpp_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix);
int yphyscpp_veh_transform(int vehi, float *matrix);
int yphyscpp_veh_wheel_contact(int vehi, int wheel, int *in_contact);

#endif /* YPHYSCPP_H */

