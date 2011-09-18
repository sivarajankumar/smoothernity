namespace shy_guts
{
    static void compute_letters_row
        ( so_called_common_engine_rect_type & result
        , so_called_platform_math_num_whole_type letters
        , so_called_platform_math_num_fract_type letter_height
        , so_called_platform_math_num_fract_type letter_width
        , so_called_platform_math_num_fract_type step
        ) ;
    static void compute_letter_position
        ( so_called_platform_math_num_fract_type & letter_x
        , so_called_platform_math_num_whole_type letter_index
        , so_called_platform_math_num_whole_type letters
        , so_called_platform_math_num_fract_type letter_height
        , so_called_platform_math_num_fract_type letter_width
        , so_called_platform_math_num_fract_type step
        ) ;
    static void fit_to_center
        ( so_called_platform_math_num_fract_type & scale
        , so_called_common_engine_rect_type what
        , so_called_common_engine_rect_type where
        ) ;
}

void shy_guts :: fit_to_center
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

void shy_guts :: compute_letters_row
    ( so_called_common_engine_rect_type & result
    , so_called_platform_math_num_whole_type letters
    , so_called_platform_math_num_fract_type letter_height
    , so_called_platform_math_num_fract_type letter_width
    , so_called_platform_math_num_fract_type step
    )
{
    so_called_platform_math_num_fract_type letters_count ;
    so_called_platform_math_num_fract_type letters_width ;
    so_called_platform_math_num_fract_type steps_count ;
    so_called_platform_math_num_fract_type steps_width ;
    so_called_platform_math_num_fract_type row_width ;
    so_called_platform_math_num_fract_type row_height ;

    so_called_platform_math :: make_fract_from_whole ( letters_count , letters ) ;
    so_called_platform_math :: sub_fracts ( steps_count , letters_count , so_called_platform_math_consts :: fract_1 ) ;

    so_called_platform_math :: mul_fracts ( letters_width , letters_count , letter_width ) ;
    so_called_platform_math :: mul_fracts ( steps_width , steps_count , step ) ;
    
    row_height = letter_height ;
    so_called_platform_math :: add_fracts ( row_width , letters_width , steps_width ) ;

    so_called_platform_math :: div_fracts ( result . left , row_width , so_called_platform_math_consts :: fract_minus_2 ) ;
    so_called_platform_math :: div_fracts ( result . right , row_width , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: div_fracts ( result . bottom , row_height , so_called_platform_math_consts :: fract_minus_2 ) ;
    so_called_platform_math :: div_fracts ( result . top , row_height , so_called_platform_math_consts :: fract_2 ) ;
}

void shy_guts :: compute_letter_position
    ( so_called_platform_math_num_fract_type & letter_x
    , so_called_platform_math_num_whole_type letter_index_whole
    , so_called_platform_math_num_whole_type letters
    , so_called_platform_math_num_fract_type letter_height
    , so_called_platform_math_num_fract_type letter_width
    , so_called_platform_math_num_fract_type step
    )
{
    so_called_platform_math_num_fract_type letter_index ;
    so_called_platform_math_num_fract_type letter_width_with_step ;
    so_called_platform_math_num_fract_type letter_offset_left ;
    so_called_platform_math_num_fract_type letter_offset_center ;
    so_called_platform_math_num_fract_type letter_half_width ;
    so_called_common_engine_rect_type row ;

    so_called_platform_math :: add_fracts ( letter_width_with_step , letter_width , step ) ;
    so_called_platform_math :: div_fracts ( letter_half_width , letter_width , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: make_fract_from_whole ( letter_index , letter_index_whole ) ;
    shy_guts :: compute_letters_row ( row , letters , letter_height , letter_width , step ) ;

    so_called_platform_math :: mul_fracts ( letter_offset_left , letter_width_with_step , letter_index ) ;

    so_called_platform_math :: add_fracts ( letter_offset_center , letter_offset_left , letter_half_width ) ;

    so_called_platform_math :: add_fracts ( letter_x , row . left , letter_offset_center ) ;
}

void shy_common_logic_text_stateless :: are_letters_equal
    ( so_called_platform_math_num_whole_type & result
    , so_called_common_logic_text_letter_id_type a
    , so_called_common_logic_text_letter_id_type b
    )
{
    so_called_platform_math :: make_num_whole ( result , so_called_platform_conditions :: wholes_are_equal ( a . _letter_id , b . _letter_id ) ) ;
}

so_called_common_logic_text_letter_id_type shy_common_logic_text_stateless :: init_letter_id ( so_called_platform_math_const_int_32_type num )
{
    so_called_common_logic_text_letter_id_type letter ;
    so_called_platform_math :: make_num_whole ( letter . _letter_id , num ) ;
    return letter ;
}

void shy_common_logic_text_stateless :: get_letter_id ( so_called_platform_math_num_whole_type & result , so_called_common_logic_text_letter_id_type letter )
{
    result = letter . _letter_id ;
}

void shy_common_logic_text_stateless :: layout_letters_in_a_row
    ( so_called_platform_vector_data_type & letter_position
    , so_called_platform_math_num_fract_type & letter_scale
    , so_called_platform_math_num_whole_type letter_index
    , so_called_platform_math_num_whole_type letters
    , so_called_platform_math_num_fract_type letter_height
    , so_called_platform_math_num_fract_type letter_width
    , so_called_platform_math_num_fract_type step
    , so_called_platform_math_num_fract_type border_width
    , so_called_platform_math_num_fract_type border_height
    , so_called_platform_math_num_fract_type aspect_width
    , so_called_platform_math_num_fract_type aspect_height
    )
{
    so_called_platform_math_num_fract_type letter_x_scaled ;
    so_called_platform_math_num_fract_type letter_x_unscaled ;
    so_called_common_engine_rect_type row ;
    so_called_common_engine_rect_type row_bordered ;
    so_called_common_engine_rect_type screen ;
    
    shy_guts :: compute_letter_position ( letter_x_unscaled , letter_index , letters , letter_height , letter_width , step ) ;
    shy_guts :: compute_letters_row ( row , letters , letter_height , letter_width , step ) ;
    so_called_common_engine_rect_stateless :: rect_from_axes ( screen , aspect_width , aspect_height ) ;

    so_called_common_engine_rect_stateless :: add_border ( row_bordered , row , border_width , border_height ) ;

    shy_guts :: fit_to_center ( letter_scale , row_bordered , screen ) ;

    so_called_platform_math :: mul_fracts ( letter_x_scaled , letter_x_unscaled , letter_scale ) ;

    so_called_platform_vector :: xyz
        ( letter_position
        , letter_x_scaled
        , so_called_platform_math_consts :: fract_0
        , so_called_platform_math_consts :: fract_0
        ) ;
}

