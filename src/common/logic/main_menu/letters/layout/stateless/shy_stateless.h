class shy_common_logic_main_menu_letters_layout_stateless
{
public :
    static void compute_unscaled_menu_size 
        ( so_called_type_platform_math_num_fract & unscaled_menu_width
        , so_called_type_platform_math_num_fract & unscaled_menu_height
        , so_called_type_platform_math_num_whole max_cols
        , so_called_type_platform_math_num_whole max_rows
        , so_called_type_platform_math_num_fract horizontal_spacing
        , so_called_type_platform_math_num_fract vertical_spacing
        , so_called_type_platform_math_num_fract horizontal_border
        , so_called_type_platform_math_num_fract vertical_border
        , so_called_type_platform_math_num_fract letter_mesh_size
        ) ;
    static void compute_menu_scale 
        ( so_called_type_platform_math_num_fract & menu_scale
        , so_called_type_platform_math_num_fract aspect_width
        , so_called_type_platform_math_num_fract aspect_height
        , so_called_type_platform_math_num_fract unscaled_menu_width
        , so_called_type_platform_math_num_fract unscaled_menu_height
        ) ;
    static void compute_menu_rect 
        ( so_called_type_common_engine_rect & menu_rect
        , so_called_type_platform_math_num_fract menu_scale
        , so_called_type_platform_math_num_fract unscaled_menu_width
        , so_called_type_platform_math_num_fract unscaled_menu_height
        ) ;
    static void compute_row_rect
        ( so_called_type_common_engine_rect & row_rect
        , so_called_type_platform_math_num_whole row
        , so_called_type_platform_math_num_whole cols
        , so_called_type_platform_math_num_fract menu_scale
        , so_called_type_common_engine_rect menu_rect
        , so_called_type_platform_math_num_fract vertical_border
        , so_called_type_platform_math_num_fract horizontal_spacing
        , so_called_type_platform_math_num_fract vertical_spacing
        , so_called_type_platform_math_num_fract letter_mesh_size
        ) ;
    static void compute_letter_rect 
        ( so_called_type_common_engine_rect & letter_rect
        , so_called_type_platform_math_num_whole col
        , so_called_type_platform_math_num_fract menu_scale
        , so_called_type_common_engine_rect row_rect
        , so_called_type_platform_math_num_fract letter_mesh_size
        , so_called_type_platform_math_num_fract horizontal_spacing
        ) ;
    static void compute_letter_position 
        ( so_called_type_platform_vector_data & letter_position
        , so_called_type_common_engine_rect letter_rect
        , so_called_type_platform_math_num_fract letter_position_z
        ) ;
} ;
