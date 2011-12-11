void shy_common_engine_rect_stateless :: dims
    ( so_called_platform_math_num_fract_type & width
    , so_called_platform_math_num_fract_type & height
    , so_called_common_engine_rect_type of_what
    )
{
    so_called_platform_math :: sub_fracts ( width , of_what . right , of_what . left ) ;
    so_called_platform_math :: sub_fracts ( height , of_what . top , of_what . bottom ) ;
}

void shy_common_engine_rect_stateless :: add_border
    ( so_called_common_engine_rect_type & result
    , so_called_common_engine_rect_type to_what
    , so_called_platform_math_num_fract_type border_width
    , so_called_platform_math_num_fract_type border_height
    )
{
    so_called_platform_math :: sub_fracts ( result . left , to_what . left , border_width ) ;
    so_called_platform_math :: add_fracts ( result . right , to_what . right , border_width ) ;

    so_called_platform_math :: sub_fracts ( result . bottom , to_what . bottom , border_height ) ;
    so_called_platform_math :: add_fracts ( result . top , to_what . top , border_height ) ;
}

void shy_common_engine_rect_stateless :: rect_from_dims
    ( so_called_common_engine_rect_type & rect
    , so_called_platform_math_num_fract_type width
    , so_called_platform_math_num_fract_type height
    )
{
    so_called_platform_math :: mul_fracts ( rect . left , width , so_called_platform_math_consts :: fract_minus_2 ) ;
    so_called_platform_math :: mul_fracts ( rect . right , width , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: mul_fracts ( rect . bottom , height , so_called_platform_math_consts :: fract_minus_2 ) ;
    so_called_platform_math :: mul_fracts ( rect . top , height , so_called_platform_math_consts :: fract_2 ) ;
}

void shy_common_engine_rect_stateless :: rect_from_axes
    ( so_called_common_engine_rect_type & rect
    , so_called_platform_math_num_fract_type half_width
    , so_called_platform_math_num_fract_type half_height
    )
{
    so_called_platform_math :: mul_fracts ( rect . left , half_width , so_called_platform_math_consts :: fract_minus_1 ) ;
    so_called_platform_math :: mul_fracts ( rect . right , half_width , so_called_platform_math_consts :: fract_1 ) ;
    so_called_platform_math :: mul_fracts ( rect . bottom , half_height , so_called_platform_math_consts :: fract_minus_1 ) ;
    so_called_platform_math :: mul_fracts ( rect . top , half_height , so_called_platform_math_consts :: fract_1 ) ;
}
