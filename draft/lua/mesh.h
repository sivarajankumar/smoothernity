#pragma once

int mesh_init(int len);
void mesh_done(void);

int mesh_spawn(int vb, int ib, int tx, int type, int space);
void mesh_kill(int mesh);

void mesh_draw(void);
