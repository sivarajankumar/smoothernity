class shy_common_engine_rect_stateless
{
public :
    static void add_border
        ( so_called_common_engine_rect_type & result
        , so_called_common_engine_rect_type to_what
        , so_called_platform_math_num_fract_type border_width
        , so_called_platform_math_num_fract_type border_height
        ) ;
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
    static void dims
        ( so_called_platform_math_num_fract_type & width
        , so_called_platform_math_num_fract_type & height
        , so_called_common_engine_rect_type of_what
        ) ;
    static void fit_to_center
        ( so_called_platform_math_num_fract_type & scale
        , so_called_common_engine_rect_type what
        , so_called_common_engine_rect_type where
        ) ;
} ;
