#ifndef CVECTOR_H
#define CVECTOR_H

#include "lua.h"

#define CVECTOR_ARGVS 5
#define CVECTOR_ARGMS 2

enum cvector_ipl_e {
    CVECTOR_IPL_LINEAR,
    CVECTOR_IPL_SPLINE,
    CVECTOR_IPLS_TOTAL
};

enum cvector_e {
    CVECTOR_CONST,
    CVECTOR_RUBBER,
    CVECTOR_WSUM,
    CVECTOR_SEQ,
    CVECTOR_MPOS,
    CVECTOR_CORD,
    CVECTOR_PICK,
    CVECTOR_CAST
};

struct cvector_t {
    float value[4]; /* Must go first to ensure alignment. */
    enum cvector_e type;
    struct cvector_t *argv[CVECTOR_ARGVS];
    struct cmatrix_t *argm[CVECTOR_ARGMS];

    int update_tag, cast_wldi, cast_csi, seq_cur, seq_start, seq_len, seq_loop;
    float cord_min, cord_max, seq_t;
    enum cvector_ipl_e seq_ipl;
};

int cvector_init(lua_State *lua, int count, int nesting);
void cvector_done(void);
struct cvector_t * cvector_get(int);
int cvector_update(struct cvector_t *vector, float dt, int update_tag, int force);
int cvector_nesting(struct cvector_t *vector, int limit);
void cvector_cross(float *out, float *v1, float *v2);
float cvector_len(float *v);
void cvector_wsum(float *out, float w1, float *v1, float w2, float *v2);

#endif /* CVECTOR_H */

