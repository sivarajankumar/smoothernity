#pragma once

struct pfm_render_ctx_t;

struct pfm_render_ctx_t * pfm_render_create_shared_ctx(void);
void pfm_render_destroy_ctx(struct pfm_render_ctx_t*);
void pfm_render_select_ctx(struct pfm_render_ctx_t*);
void pfm_render_unselect_ctx(void);
