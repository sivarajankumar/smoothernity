#pragma once

int mesh_init(int len);
void mesh_done(void);

int mesh_triangle_fan(int vb, int ib, int tx);
int mesh_triangle_strip(int vb, int ib, int tx);
int mesh_triangle_list(int vb, int ib, int tx);

void mesh_kill(int mesh);
