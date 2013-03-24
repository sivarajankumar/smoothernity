#include "render.h"
#include "../util/util.h"
#include <GL/glew.h>

#define PFM_RENDER_CTX_ALIGN 16

struct pfm_render_ctx_t
{
    int dummy; /* TODO */
};

struct pfm_render_ctx_t * pfm_render_create_shared_ctx(void)
{
    struct pfm_render_ctx_t *ctx;
    ctx = util_malloc(PFM_RENDER_CTX_ALIGN, sizeof(struct pfm_render_ctx_t));
    if (ctx == 0)
        return 0;
    return ctx;
}

void pfm_render_destroy_ctx(struct pfm_render_ctx_t *ctx)
{
    util_free(ctx);
}

void pfm_render_select_ctx(struct pfm_render_ctx_t *ctx)
{
    ctx->dummy = 1;
}

void pfm_render_unselect_ctx(void)
{
}
