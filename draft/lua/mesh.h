#pragma once

struct mesh_t;

int mesh_init(int count);
void mesh_done(void);

void mesh_query(int *left);

void mesh_draw(struct mesh_t *mesh);

int mesh_alloc(int type, int vb, int ib, int tx, int space,
               int ioffset, int icount);
void mesh_free(int mesh);
