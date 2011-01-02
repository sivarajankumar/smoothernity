#ifndef _shy_common_engine_render_consts_included
#define _shy_common_engine_render_consts_included

class shy_common_engine_render_consts
{
public :
    static void init ( ) ;
public :
    static so_called_type_platform_math_num_whole texture_width ;
    static so_called_type_platform_math_num_whole texture_height ;
    static so_called_type_platform_math_const_int_32 texture_size_pow2_base_int = 8 ;
    static so_called_type_platform_math_const_int_32 texture_size_int = 1 << texture_size_pow2_base_int ;
} ;
    
#endif
