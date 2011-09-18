class shy_common_logic_main_menu_letters_layout_stateless
{
public :
    static void compute_unscaled_menu_size 
        ( so_called_platform_math_num_fract_type & unscaled_menu_width
        , so_called_platform_math_num_fract_type & unscaled_menu_height
        , so_called_platform_math_num_whole_type max_cols
        , so_called_platform_math_num_whole_type max_rows
        , so_called_platform_math_num_fract_type horizontal_spacing
        , so_called_platform_math_num_fract_type vertical_spacing
        , so_called_platform_math_num_fract_type horizontal_border
        , so_called_platform_math_num_fract_type vertical_border
        , so_called_platform_math_num_fract_type letter_mesh_size
        ) ;
    static void compute_menu_scale 
        ( so_called_platform_math_num_fract_type & menu_scale
        , so_called_platform_math_num_fract_type aspect_width
        , so_called_platform_math_num_fract_type aspect_height
        , so_called_platform_math_num_fract_type unscaled_menu_width
        , so_called_platform_math_num_fract_type unscaled_menu_height
        ) ;
    static void compute_menu_rect 
        ( so_called_common_engine_rect_type & menu_rect
        , so_called_platform_math_num_fract_type menu_scale
        , so_called_platform_math_num_fract_type unscaled_menu_width
        , so_called_platform_math_num_fract_type unscaled_menu_height
        ) ;
    static void compute_row_rect
        ( so_called_common_engine_rect_type & row_rect
        , so_called_platform_math_num_whole_type row
        , so_called_platform_math_num_whole_type cols
        , so_called_platform_math_num_fract_type menu_scale
        , so_called_common_engine_rect_type menu_rect
        , so_called_platform_math_num_fract_type vertical_border
        , so_called_platform_math_num_fract_type horizontal_spacing
        , so_called_platform_math_num_fract_type vertical_spacing
        , so_called_platform_math_num_fract_type letter_mesh_size
        ) ;
    static void compute_letter_rect 
        ( so_called_common_engine_rect_type & letter_rect
        , so_called_platform_math_num_whole_type col
        , so_called_platform_math_num_fract_type menu_scale
        , so_called_common_engine_rect_type row_rect
        , so_called_platform_math_num_fract_type letter_mesh_size
        , so_called_platform_math_num_fract_type horizontal_spacing
        ) ;
    static void compute_letter_position 
        ( so_called_platform_vector_data_type & letter_position
        , so_called_common_engine_rect_type letter_rect
        , so_called_platform_math_num_fract_type letter_position_z
        ) ;
} ;
