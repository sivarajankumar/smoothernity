template < typename mediator >
class shy_logic_main_menu_letters_layout_stateless
{
    typedef typename mediator :: engine_math :: rect rect ;
    typedef typename mediator :: logic_text_stateless :: logic_text_letter_id logic_text_letter_id ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

public :

    class logic_main_menu_letters_layout_stateless_consts_type
    {
    public :
        logic_main_menu_letters_layout_stateless_consts_type ( ) ;
    public :
        num_fract letter_size_fract_horizontal_spacing ;
        num_fract letter_size_fract_vertical_spacing ;
        num_fract letter_size_fract_horizontal_border ;
        num_fract letter_size_fract_vertical_border ;
        num_fract menu_position_z ;
    } ;

    class logic_main_menu_letters_layout_messages
    {
    public :
        class logic_main_menu_letters_layout_position_reply { public : num_whole row ; num_whole col ; vector_data position ; num_fract scale ; } ;
        class logic_main_menu_letters_layout_position_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_layout_row_rect_reply { public : num_whole row ; rect row_rect ; } ;
        class logic_main_menu_letters_layout_row_rect_request { public : num_whole row ; } ;
    } ;

    template < typename receivers >
    class logic_main_menu_letters_layout_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_letters_layout_messages :: logic_main_menu_letters_layout_position_reply ) ;
        void send ( typename logic_main_menu_letters_layout_messages :: logic_main_menu_letters_layout_position_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_letters_layout_stateless ( ) ;
    static void compute_unscaled_menu_size 
        ( num_fract & unscaled_menu_width
        , num_fract & unscaled_menu_height
        , num_whole max_cols
        , num_whole max_rows
        , num_fract horizontal_spacing
        , num_fract vertical_spacing
        , num_fract horizontal_border
        , num_fract vertical_border
        , num_fract letter_mesh_size
        ) ;
    static void compute_menu_scale 
        ( num_fract & menu_scale
        , num_fract aspect_width
        , num_fract aspect_height
        , num_fract unscaled_menu_width
        , num_fract unscaled_menu_height
        ) ;
    static void compute_menu_rect 
        ( rect & menu_rect
        , num_fract menu_scale
        , num_fract unscaled_menu_width
        , num_fract unscaled_menu_height
        ) ;
    static void compute_row_rect
        ( rect & row_rect
        , num_whole row
        , num_whole cols
        , num_fract menu_scale
        , rect menu_rect
        , num_fract vertical_border
        , num_fract horizontal_spacing
        , num_fract vertical_spacing
        , num_fract letter_mesh_size
        ) ;
    static void compute_letter_rect 
        ( rect & letter_rect
        , num_whole col
        , num_fract menu_scale
        , rect row_rect
        , num_fract letter_mesh_size
        , num_fract horizontal_spacing
        ) ;
    static void compute_letter_position 
        ( vector_data & letter_position
        , rect letter_rect
        , num_fract letter_position_z
        ) ;
private :
    shy_logic_main_menu_letters_layout_stateless < mediator > & operator= ( const shy_logic_main_menu_letters_layout_stateless < mediator > & ) ;
public :
    const logic_main_menu_letters_layout_stateless_consts_type logic_main_menu_letters_layout_stateless_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_layout_stateless < mediator > :: logic_main_menu_letters_layout_stateless_consts_type :: logic_main_menu_letters_layout_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( letter_size_fract_horizontal_spacing , 0 , 10 ) ;
    platform_math :: make_num_fract ( letter_size_fract_vertical_spacing , 10 , 10 ) ;
    platform_math :: make_num_fract ( letter_size_fract_horizontal_border , 1 , 1 ) ;
    platform_math :: make_num_fract ( letter_size_fract_vertical_border , 1 , 1 ) ;
    platform_math :: make_num_fract ( menu_position_z , - 3 , 1 ) ;
}

template < typename mediator >
shy_logic_main_menu_letters_layout_stateless < mediator > :: shy_logic_main_menu_letters_layout_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_layout_stateless < mediator > 
:: logic_main_menu_letters_layout_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_layout_stateless < mediator > 
:: logic_main_menu_letters_layout_sender < receivers > 
:: send ( typename logic_main_menu_letters_layout_messages :: logic_main_menu_letters_layout_position_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_layout_stateless < mediator > 
:: logic_main_menu_letters_layout_sender < receivers > 
:: send ( typename logic_main_menu_letters_layout_messages :: logic_main_menu_letters_layout_position_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_layout_position . get ( ) . receive ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_stateless < mediator > :: compute_unscaled_menu_size 
    ( num_fract & unscaled_menu_width
    , num_fract & unscaled_menu_height
    , num_whole max_cols
    , num_whole max_rows
    , num_fract horizontal_spacing
    , num_fract vertical_spacing
    , num_fract horizontal_border
    , num_fract vertical_border
    , num_fract letter_mesh_size
    )
{
    num_fract letters_width ;
    num_fract letters_height ;
    num_fract letters_in_row ;
    num_fract letters_in_col ;
    num_fract spacings_width ;
    num_fract spacings_height ;
    num_fract spacings_in_row ;
    num_fract spacings_in_col ;
    num_fract borders_width ;
    num_fract borders_height ;
    num_fract menu_width ;
    num_fract menu_height ;
    num_fract fract_1 ;
    num_fract fract_2 ;
    
    platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    
    platform_math :: make_fract_from_whole ( letters_in_row , max_cols ) ;
    platform_math :: make_fract_from_whole ( letters_in_col , max_rows ) ;
    
    platform_math :: sub_fracts ( spacings_in_row , letters_in_row , fract_1 ) ;
    platform_math :: sub_fracts ( spacings_in_col , letters_in_col , fract_1 ) ;
    
    letters_width = letters_in_row ;
    letters_height = letters_in_col ;

    platform_math :: mul_fracts ( spacings_width , horizontal_spacing , spacings_in_row ) ;
    platform_math :: mul_fracts ( spacings_height , vertical_spacing , spacings_in_col ) ;
    
    platform_math :: mul_fracts ( borders_width , horizontal_border , fract_2 ) ;
    platform_math :: mul_fracts ( borders_height , vertical_border , fract_2 ) ;
    
    platform_math :: add_fracts ( menu_width , letters_width , spacings_width ) ;
    platform_math :: add_fracts ( menu_height , letters_height , spacings_height ) ;
    
    platform_math :: add_to_fract ( menu_width , borders_width ) ;
    platform_math :: add_to_fract ( menu_height , borders_height ) ;

    platform_math :: mul_fracts ( unscaled_menu_width , menu_width , letter_mesh_size ) ;
    platform_math :: mul_fracts ( unscaled_menu_height , menu_height , letter_mesh_size ) ;    
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_stateless < mediator > :: compute_menu_scale 
    ( num_fract & menu_scale
    , num_fract aspect_width
    , num_fract aspect_height
    , num_fract unscaled_menu_width
    , num_fract unscaled_menu_height
    )
{
    num_fract screen_ratio ;
    num_fract menu_ratio ;
    num_fract fract_2 ;
    
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    platform_math :: div_fracts ( screen_ratio , aspect_width , aspect_height ) ;
    platform_math :: div_fracts ( menu_ratio , unscaled_menu_width , unscaled_menu_height ) ;
    
    if ( platform_conditions :: fract_greater_than_fract ( menu_ratio , screen_ratio ) )
        platform_math :: div_fracts ( menu_scale , aspect_width , unscaled_menu_width ) ;
    else
        platform_math :: div_fracts ( menu_scale , aspect_height , unscaled_menu_height ) ;
    
    platform_math :: mul_fract_by ( menu_scale , fract_2 ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_stateless < mediator > :: compute_menu_rect 
    ( rect & menu_rect
    , num_fract menu_scale
    , num_fract unscaled_menu_width
    , num_fract unscaled_menu_height
    )
{
    num_fract scaled_menu_width ;
    num_fract scaled_menu_height ;
    num_fract fract_2 ;
    num_fract fract_minus_2 ;
    
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    platform_math :: make_num_fract ( fract_minus_2 , - 2 , 1 ) ;
    
    platform_math :: mul_fracts ( scaled_menu_width , unscaled_menu_width , menu_scale ) ;
    platform_math :: mul_fracts ( scaled_menu_height , unscaled_menu_height , menu_scale ) ;
    
    platform_math :: div_fracts ( menu_rect . left , scaled_menu_width , fract_minus_2 ) ;
    platform_math :: div_fracts ( menu_rect . right , scaled_menu_width , fract_2 ) ;
    platform_math :: div_fracts ( menu_rect . bottom , scaled_menu_height , fract_minus_2 ) ;
    platform_math :: div_fracts ( menu_rect . top , scaled_menu_height , fract_2 ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_stateless < mediator > :: compute_row_rect 
    ( rect & row_rect
    , num_whole row
    , num_whole cols
    , num_fract menu_scale
    , rect menu_rect
    , num_fract vertical_border
    , num_fract horizontal_spacing
    , num_fract vertical_spacing
    , num_fract letter_mesh_size
    )
{
    num_fract letters_width ;
    num_fract spacings_width ;
    num_fract border_height ;
    num_fract letters_in_row ;
    num_fract spacings_in_row ;
    num_fract row_width ;
    num_fract row_height ;
    num_fract row_number ;
    num_fract letter_size ;
    num_fract fract_1 ;
    num_fract fract_2 ;
    num_fract fract_minus_2 ;
    
    platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    platform_math :: make_num_fract ( fract_minus_2 , - 2 , 1 ) ;
    
    platform_math :: make_fract_from_whole ( letters_in_row , cols ) ;
    platform_math :: sub_fracts ( spacings_in_row , letters_in_row , fract_1 ) ;

    letters_width = letters_in_row ;
    border_height = vertical_border ;
    platform_math :: mul_fracts ( spacings_width , spacings_in_row , horizontal_spacing ) ;
    
    platform_math :: add_fracts ( row_width , letters_width , spacings_width ) ;
    platform_math :: add_fracts ( row_height , fract_1 , vertical_spacing ) ;
    
    platform_math :: mul_fracts ( letter_size , letter_mesh_size , menu_scale ) ;
    
    platform_math :: mul_fract_by ( row_width , letter_size ) ;
    platform_math :: mul_fract_by ( row_height , letter_size ) ;
    platform_math :: mul_fract_by ( border_height , letter_size ) ;
    
    platform_math :: make_fract_from_whole ( row_number , row ) ;

    platform_math :: mul_fracts ( row_rect . top , row_number , row_height ) ;
    platform_math :: add_to_fract ( row_rect . top , border_height ) ;
    platform_math :: neg_fract ( row_rect . top ) ;
    platform_math :: add_to_fract ( row_rect . top , menu_rect . top ) ;
    platform_math :: sub_fracts ( row_rect . bottom , row_rect . top , row_height ) ;
    platform_math :: div_fracts ( row_rect . left , row_width , fract_minus_2 ) ;
    platform_math :: div_fracts ( row_rect . right , row_width , fract_2 ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_stateless < mediator > :: compute_letter_rect 
    ( rect & letter_rect
    , num_whole col
    , num_fract menu_scale
    , rect row_rect
    , num_fract letter_mesh_size
    , num_fract horizontal_spacing
    )
{
    num_fract col_number ;
    num_fract col_width ;
    num_fract letter_size ;
    num_fract fract_1 ;
    
    platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    
    platform_math :: make_fract_from_whole ( col_number , col ) ;
    platform_math :: mul_fracts ( letter_size , letter_mesh_size , menu_scale ) ;
    
    platform_math :: add_fracts ( col_width , fract_1 , horizontal_spacing ) ;
    platform_math :: mul_fract_by ( col_width , letter_size ) ;
    
    letter_rect . top = row_rect . top ;
    platform_math :: sub_fracts ( letter_rect . bottom , letter_rect . top , letter_size ) ;
    platform_math :: mul_fracts ( letter_rect . left , col_number , col_width ) ;
    platform_math :: add_to_fract ( letter_rect . left , row_rect . left ) ;
    platform_math :: add_fracts ( letter_rect . right , letter_rect . left , letter_size ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_stateless < mediator > :: compute_letter_position 
    ( vector_data & letter_position
    , rect letter_rect
    , num_fract letter_position_z
    )
{
    num_fract letter_position_x ;
    num_fract letter_position_y ;
    num_fract fract_2 ;
    
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    
    platform_math :: add_fracts ( letter_position_x , letter_rect . left , letter_rect . right ) ;
    platform_math :: add_fracts ( letter_position_y , letter_rect . bottom , letter_rect . top ) ;
    
    platform_math :: div_fract_by ( letter_position_x , fract_2 ) ;
    platform_math :: div_fract_by ( letter_position_y , fract_2 ) ;
    
    platform_vector :: xyz ( letter_position , letter_position_x , letter_position_y , letter_position_z ) ;
}
