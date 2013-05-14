#include <windows.h>

void pfm_shell_rmfile(const char *fname)
{
    DeleteFile(fname);
}

