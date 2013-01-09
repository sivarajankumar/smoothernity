#pragma once

int mesh_init(int count);
void mesh_done(void);

void mesh_query(int *left);

int mesh_spawn(int type, int vb, int ib, int tx, int space);
void mesh_kill(int mesh);
