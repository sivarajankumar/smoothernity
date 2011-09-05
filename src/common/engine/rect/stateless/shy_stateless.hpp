void shy_common_engine_rect_stateless :: fit_to_center
    ( so_called_platform_math_num_fract_type & scale
    , so_called_common_engine_rect_type what
    , so_called_common_engine_rect_type where
    )
{
    so_called_platform_math_num_fract_type what_height ;
    so_called_platform_math_num_fract_type what_width ;
    so_called_platform_math_num_fract_type where_height ;
    so_called_platform_math_num_fract_type where_width ;
    so_called_platform_math_num_fract_type scale_height ;
    so_called_platform_math_num_fract_type scale_width ;

    so_called_common_engine_rect_stateless :: dims ( what_height , what_width , what ) ;
    so_called_common_engine_rect_stateless :: dims ( where_height , where_width , where ) ;

    if ( so_called_platform_conditions :: fract_greater_than_fract ( what_height , where_height ) )
        so_called_platform_math :: div_fracts ( scale_height , where_height , what_height ) ;
    else
        so_called_platform_math :: div_fracts ( scale_height , what_height , where_height ) ;

    if ( so_called_platform_conditions :: fract_greater_than_fract ( what_width , where_width ) )
        so_called_platform_math :: div_fracts ( scale_width , where_width , what_width ) ;
    else
        so_called_platform_math :: div_fracts ( scale_width , what_width , where_width ) ;

    so_called_common_engine_math_stateless :: min_fract ( scale , scale_height , scale_width ) ;
}

void shy_common_engine_rect_stateless :: dims
    ( so_called_platform_math_num_fract_type & width
    , so_called_platform_math_num_fract_type & height
    , so_called_common_engine_rect_type of_what
    )
{
    so_called_platform_math :: sub_fracts ( width , of_what . right , of_what . left ) ;
    so_called_platform_math :: sub_fracts ( height , of_what . top , of_what . bottom ) ;
}
