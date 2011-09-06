class shy_common_engine_rect_stateless
{
public :
    static void add_border
        ( so_called_common_engine_rect_type & result
        , so_called_common_engine_rect_type to_what
        , so_called_platform_math_num_fract_type border_width
        , so_called_platform_math_num_fract_type border_height
        ) ;
    static void dims
        ( so_called_platform_math_num_fract_type & width
        , so_called_platform_math_num_fract_type & height
        , so_called_common_engine_rect_type of_what
        ) ;
    static void rect_from_axes
        ( so_called_common_engine_rect_type & rect
        , so_called_platform_math_num_fract_type half_width
        , so_called_platform_math_num_fract_type half_height
        ) ;
    static void rect_from_dims
        ( so_called_common_engine_rect_type & rect
        , so_called_platform_math_num_fract_type width
        , so_called_platform_math_num_fract_type height
        ) ;
} ;
