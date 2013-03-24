#include <unistd.h>

void pfm_shell_rmfile(const char *fname)
{
    unlink(fname);
}
