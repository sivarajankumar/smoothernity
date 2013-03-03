#include "render.h"
#include "../util/util.h"
#include <GL/glew.h>
#include <GL/wglew.h>

#define PFM_RENDER_CTX_ALIGN 16

struct pfm_render_ctx_t
{
    HDC dc;
    HGLRC glc;
};

struct pfm_render_ctx_t * pfm_render_create_shared_ctx(void)
{
    HGLRC glc;
    HDC dc;
    struct pfm_render_ctx_t *ctx;
    if (!WGL_ARB_create_context)
        return 0;
    ctx = util_malloc(PFM_RENDER_CTX_ALIGN, sizeof(struct pfm_render_ctx_t));
    if (ctx == 0)
        return 0;
    glc = wglGetCurrentContext();
    dc = wglGetCurrentDC();
    ctx->dc = dc;
    ctx->glc = wglCreateContextAttribsARB(dc, glc, 0);
    if (ctx->glc == 0)
    {
        util_free(ctx);
        return 0;
    }
    return ctx;
}

void pfm_render_destroy_ctx(struct pfm_render_ctx_t *ctx)
{
    wglDeleteContext(ctx->glc);
    util_free(ctx);
}

void pfm_render_select_ctx(struct pfm_render_ctx_t *ctx)
{
    wglMakeCurrent(ctx->dc, ctx->glc);
}
