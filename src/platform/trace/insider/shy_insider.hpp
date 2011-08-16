namespace shy_guts
{
    static so_called_lib_std_int32_t current_frame = 0 ;
}

void shy_platform_trace_insider :: next_frame ( )
{
    ++ shy_guts :: current_frame ;
}

void shy_platform_trace_insider :: get_current_frame ( so_called_lib_std_int32_t & result )
{
    result = shy_guts :: current_frame ;
}
