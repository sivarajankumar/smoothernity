void shy_common_logic_main_menu_letters_layout_stateless :: compute_unscaled_menu_size 
    ( so_called_platform_math_num_fract_type & unscaled_menu_width
    , so_called_platform_math_num_fract_type & unscaled_menu_height
    , so_called_platform_math_num_whole_type max_cols
    , so_called_platform_math_num_whole_type max_rows
    , so_called_platform_math_num_fract_type horizontal_spacing
    , so_called_platform_math_num_fract_type vertical_spacing
    , so_called_platform_math_num_fract_type horizontal_border
    , so_called_platform_math_num_fract_type vertical_border
    , so_called_platform_math_num_fract_type letter_mesh_size
    )
{
    so_called_platform_math_num_fract_type letters_width ;
    so_called_platform_math_num_fract_type letters_height ;
    so_called_platform_math_num_fract_type letters_in_row ;
    so_called_platform_math_num_fract_type letters_in_col ;
    so_called_platform_math_num_fract_type spacings_width ;
    so_called_platform_math_num_fract_type spacings_height ;
    so_called_platform_math_num_fract_type spacings_in_row ;
    so_called_platform_math_num_fract_type spacings_in_col ;
    so_called_platform_math_num_fract_type borders_width ;
    so_called_platform_math_num_fract_type borders_height ;
    so_called_platform_math_num_fract_type menu_width ;
    so_called_platform_math_num_fract_type menu_height ;
    so_called_platform_math_num_fract_type fract_1 ;
    so_called_platform_math_num_fract_type fract_2 ;
    
    so_called_platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    
    so_called_platform_math :: make_fract_from_whole ( letters_in_row , max_cols ) ;
    so_called_platform_math :: make_fract_from_whole ( letters_in_col , max_rows ) ;
    
    so_called_platform_math :: sub_fracts ( spacings_in_row , letters_in_row , fract_1 ) ;
    so_called_platform_math :: sub_fracts ( spacings_in_col , letters_in_col , fract_1 ) ;
    
    letters_width = letters_in_row ;
    letters_height = letters_in_col ;

    so_called_platform_math :: mul_fracts ( spacings_width , horizontal_spacing , spacings_in_row ) ;
    so_called_platform_math :: mul_fracts ( spacings_height , vertical_spacing , spacings_in_col ) ;
    
    so_called_platform_math :: mul_fracts ( borders_width , horizontal_border , fract_2 ) ;
    so_called_platform_math :: mul_fracts ( borders_height , vertical_border , fract_2 ) ;
    
    so_called_platform_math :: add_fracts ( menu_width , letters_width , spacings_width ) ;
    so_called_platform_math :: add_fracts ( menu_height , letters_height , spacings_height ) ;
    
    so_called_platform_math :: add_to_fract ( menu_width , borders_width ) ;
    so_called_platform_math :: add_to_fract ( menu_height , borders_height ) ;

    so_called_platform_math :: mul_fracts ( unscaled_menu_width , menu_width , letter_mesh_size ) ;
    so_called_platform_math :: mul_fracts ( unscaled_menu_height , menu_height , letter_mesh_size ) ;    
}

void shy_common_logic_main_menu_letters_layout_stateless :: compute_menu_scale 
    ( so_called_platform_math_num_fract_type & menu_scale
    , so_called_platform_math_num_fract_type aspect_width
    , so_called_platform_math_num_fract_type aspect_height
    , so_called_platform_math_num_fract_type unscaled_menu_width
    , so_called_platform_math_num_fract_type unscaled_menu_height
    )
{
    so_called_platform_math_num_fract_type screen_ratio ;
    so_called_platform_math_num_fract_type menu_ratio ;
    so_called_platform_math_num_fract_type fract_2 ;
    
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    so_called_platform_math :: div_fracts ( screen_ratio , aspect_width , aspect_height ) ;
    so_called_platform_math :: div_fracts ( menu_ratio , unscaled_menu_width , unscaled_menu_height ) ;
    
    if ( so_called_platform_conditions :: fract_greater_than_fract ( menu_ratio , screen_ratio ) )
        so_called_platform_math :: div_fracts ( menu_scale , aspect_width , unscaled_menu_width ) ;
    else
        so_called_platform_math :: div_fracts ( menu_scale , aspect_height , unscaled_menu_height ) ;
    
    so_called_platform_math :: mul_fract_by ( menu_scale , fract_2 ) ;
}

void shy_common_logic_main_menu_letters_layout_stateless :: compute_menu_rect 
    ( so_called_common_engine_rect_type & menu_rect
    , so_called_platform_math_num_fract_type menu_scale
    , so_called_platform_math_num_fract_type unscaled_menu_width
    , so_called_platform_math_num_fract_type unscaled_menu_height
    )
{
    so_called_platform_math_num_fract_type scaled_menu_width ;
    so_called_platform_math_num_fract_type scaled_menu_height ;
    so_called_platform_math_num_fract_type fract_2 ;
    so_called_platform_math_num_fract_type fract_minus_2 ;
    
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_minus_2 , - 2 , 1 ) ;
    
    so_called_platform_math :: mul_fracts ( scaled_menu_width , unscaled_menu_width , menu_scale ) ;
    so_called_platform_math :: mul_fracts ( scaled_menu_height , unscaled_menu_height , menu_scale ) ;
    
    so_called_platform_math :: div_fracts ( menu_rect . left , scaled_menu_width , fract_minus_2 ) ;
    so_called_platform_math :: div_fracts ( menu_rect . right , scaled_menu_width , fract_2 ) ;
    so_called_platform_math :: div_fracts ( menu_rect . bottom , scaled_menu_height , fract_minus_2 ) ;
    so_called_platform_math :: div_fracts ( menu_rect . top , scaled_menu_height , fract_2 ) ;
}

void shy_common_logic_main_menu_letters_layout_stateless :: compute_row_rect 
    ( so_called_common_engine_rect_type & row_rect
    , so_called_platform_math_num_whole_type row
    , so_called_platform_math_num_whole_type cols
    , so_called_platform_math_num_fract_type menu_scale
    , so_called_common_engine_rect_type menu_rect
    , so_called_platform_math_num_fract_type vertical_border
    , so_called_platform_math_num_fract_type horizontal_spacing
    , so_called_platform_math_num_fract_type vertical_spacing
    , so_called_platform_math_num_fract_type letter_mesh_size
    )
{
    so_called_platform_math_num_fract_type letters_width ;
    so_called_platform_math_num_fract_type spacings_width ;
    so_called_platform_math_num_fract_type border_height ;
    so_called_platform_math_num_fract_type letters_in_row ;
    so_called_platform_math_num_fract_type spacings_in_row ;
    so_called_platform_math_num_fract_type row_width ;
    so_called_platform_math_num_fract_type row_height ;
    so_called_platform_math_num_fract_type row_number ;
    so_called_platform_math_num_fract_type letter_size ;
    so_called_platform_math_num_fract_type fract_1 ;
    so_called_platform_math_num_fract_type fract_2 ;
    so_called_platform_math_num_fract_type fract_minus_2 ;
    
    so_called_platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_minus_2 , - 2 , 1 ) ;
    
    so_called_platform_math :: make_fract_from_whole ( letters_in_row , cols ) ;
    so_called_platform_math :: sub_fracts ( spacings_in_row , letters_in_row , fract_1 ) ;

    letters_width = letters_in_row ;
    border_height = vertical_border ;
    so_called_platform_math :: mul_fracts ( spacings_width , spacings_in_row , horizontal_spacing ) ;
    
    so_called_platform_math :: add_fracts ( row_width , letters_width , spacings_width ) ;
    so_called_platform_math :: add_fracts ( row_height , fract_1 , vertical_spacing ) ;
    
    so_called_platform_math :: mul_fracts ( letter_size , letter_mesh_size , menu_scale ) ;
    
    so_called_platform_math :: mul_fract_by ( row_width , letter_size ) ;
    so_called_platform_math :: mul_fract_by ( row_height , letter_size ) ;
    so_called_platform_math :: mul_fract_by ( border_height , letter_size ) ;
    
    so_called_platform_math :: make_fract_from_whole ( row_number , row ) ;

    so_called_platform_math :: mul_fracts ( row_rect . top , row_number , row_height ) ;
    so_called_platform_math :: add_to_fract ( row_rect . top , border_height ) ;
    so_called_platform_math :: neg_fract ( row_rect . top ) ;
    so_called_platform_math :: add_to_fract ( row_rect . top , menu_rect . top ) ;
    so_called_platform_math :: sub_fracts ( row_rect . bottom , row_rect . top , letter_size ) ;
    so_called_platform_math :: div_fracts ( row_rect . left , row_width , fract_minus_2 ) ;
    so_called_platform_math :: div_fracts ( row_rect . right , row_width , fract_2 ) ;
}

void shy_common_logic_main_menu_letters_layout_stateless :: compute_letter_rect 
    ( so_called_common_engine_rect_type & letter_rect
    , so_called_platform_math_num_whole_type col
    , so_called_platform_math_num_fract_type menu_scale
    , so_called_common_engine_rect_type row_rect
    , so_called_platform_math_num_fract_type letter_mesh_size
    , so_called_platform_math_num_fract_type horizontal_spacing
    )
{
    so_called_platform_math_num_fract_type col_number ;
    so_called_platform_math_num_fract_type col_width ;
    so_called_platform_math_num_fract_type letter_size ;
    so_called_platform_math_num_fract_type fract_1 ;
    
    so_called_platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    
    so_called_platform_math :: make_fract_from_whole ( col_number , col ) ;
    so_called_platform_math :: mul_fracts ( letter_size , letter_mesh_size , menu_scale ) ;
    
    so_called_platform_math :: add_fracts ( col_width , fract_1 , horizontal_spacing ) ;
    so_called_platform_math :: mul_fract_by ( col_width , letter_size ) ;
    
    letter_rect . top = row_rect . top ;
    so_called_platform_math :: sub_fracts ( letter_rect . bottom , letter_rect . top , letter_size ) ;
    so_called_platform_math :: mul_fracts ( letter_rect . left , col_number , col_width ) ;
    so_called_platform_math :: add_to_fract ( letter_rect . left , row_rect . left ) ;
    so_called_platform_math :: add_fracts ( letter_rect . right , letter_rect . left , letter_size ) ;
}

void shy_common_logic_main_menu_letters_layout_stateless :: compute_letter_position 
    ( so_called_platform_vector_data_type & letter_position
    , so_called_common_engine_rect_type letter_rect
    , so_called_platform_math_num_fract_type letter_position_z
    )
{
    so_called_platform_math_num_fract_type letter_position_x ;
    so_called_platform_math_num_fract_type letter_position_y ;
    so_called_platform_math_num_fract_type fract_2 ;
    
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    
    so_called_platform_math :: add_fracts ( letter_position_x , letter_rect . left , letter_rect . right ) ;
    so_called_platform_math :: add_fracts ( letter_position_y , letter_rect . bottom , letter_rect . top ) ;
    
    so_called_platform_math :: div_fract_by ( letter_position_x , fract_2 ) ;
    so_called_platform_math :: div_fract_by ( letter_position_y , fract_2 ) ;
    
    so_called_platform_vector :: xyz ( letter_position , letter_position_x , letter_position_y , letter_position_z ) ;
}

