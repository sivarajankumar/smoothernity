template < typename mediator >
class shy_logic_main_menu_layout
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_main_menu_layout_consts_type
    {
    public :
        _logic_main_menu_layout_consts_type ( ) ;
    public :
        num_fract letter_size_fract_horizontal_spacing ;
        num_fract letter_size_fract_vertical_spacing ;
        num_fract letter_size_fract_horizontal_border ;
        num_fract letter_size_fract_vertical_border ;
        num_fract menu_position_z ;
    } ;

    class _rect
    {
    public :
        num_fract left ;
        num_fract right ;
        num_fract bottom ;
        num_fract top ;
    } ;

    class _logic_main_menu_layout_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        
        num_whole max_cols ;
        num_whole max_rows ;
        num_whole current_cols ;
        
        num_fract unscaled_menu_width ;
        num_fract unscaled_menu_height ;
        num_fract menu_scale ;
        _rect menu_rect ;
        _rect row_rect ;
        _rect decorated_row_rect ;
        _rect letter_rect ;
        vector_data letter_position ;
    } ;
    
    class _logic_main_menu_rows_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole rows ;
    } ;
    
    class _logic_main_menu_cols_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole replied ;
        num_whole cols ;
    } ;

    class _engine_render_aspect_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract width ;
        num_fract height ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_layout_position_request ) ;
    void receive ( typename messages :: logic_main_menu_rows_reply ) ;
    void receive ( typename messages :: logic_main_menu_cols_reply ) ;
    void receive ( typename messages :: logic_main_menu_add_letter ) ;
    void receive ( typename messages :: logic_main_menu_next_row ) ;
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    void _proceed_with_layout ( ) ;
    void _obtain_rows_count ( ) ;
    void _obtain_cols_count ( ) ;
    void _obtain_aspect_ratio ( ) ;
    void _reply_layout ( ) ;
    void _reply_computed_layout ( ) ;
    void _compute_layout ( ) ;
    void _compute_unscaled_menu_size ( ) ;
    void _compute_menu_scale ( ) ;
    void _compute_menu_rect ( ) ;
    void _compute_row_rect ( ) ;
    void _compute_decorated_row_rect ( ) ;
    void _compute_letter_rect ( ) ;
    void _compute_letter_position ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > _logic_main_menu_stateless_consts ;
    const _logic_main_menu_layout_consts_type _logic_main_menu_layout_consts ;
    
    _logic_main_menu_layout_state_type _logic_main_menu_layout_state ;
    _logic_main_menu_rows_state_type _logic_main_menu_rows_state ;
    _logic_main_menu_cols_state_type _logic_main_menu_cols_state ;
    _engine_render_aspect_state_type _engine_render_aspect_state ;    
} ;

template < typename mediator >
shy_logic_main_menu_layout < mediator > :: _logic_main_menu_layout_consts_type :: _logic_main_menu_layout_consts_type ( )
{
    platform_math :: make_num_fract ( letter_size_fract_horizontal_spacing , 1 , 10 ) ;
    platform_math :: make_num_fract ( letter_size_fract_vertical_spacing , 2 , 10 ) ;
    platform_math :: make_num_fract ( letter_size_fract_horizontal_border , 1 , 1 ) ;
    platform_math :: make_num_fract ( letter_size_fract_vertical_border , 1 , 1 ) ;
    platform_math :: make_num_fract ( menu_position_z , - 3 , 1 ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_stateless_consts ( _logic_main_menu_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _logic_main_menu_layout_state . max_cols = _platform_math_consts . get ( ) . whole_0 ;
    _logic_main_menu_layout_state . max_rows = _platform_math_consts . get ( ) . whole_1 ;
    _logic_main_menu_layout_state . current_cols = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: logic_main_menu_layout_position_request msg )
{
    _logic_main_menu_layout_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_layout_state . requested_col = msg . col ;
    _logic_main_menu_layout_state . requested_row = msg . row ;
    _proceed_with_layout ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: logic_main_menu_rows_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_rows_state . requested ) )
    {
        _logic_main_menu_rows_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_rows_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_rows_state . rows = msg . rows ;
        _proceed_with_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: logic_main_menu_cols_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_cols_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_cols_state . requested_row , msg . row )
       )
    {
        _logic_main_menu_cols_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_cols_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_cols_state . cols = msg . cols ;
        _proceed_with_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: engine_render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . requested ) )
    {
        _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_aspect_state . width = msg . width ;
        _engine_render_aspect_state . height = msg . height ;
        _proceed_with_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: logic_main_menu_add_letter )
{
    platform_math :: inc_whole ( _logic_main_menu_layout_state . current_cols ) ;
    engine_math :: math_max_whole 
        ( _logic_main_menu_layout_state . max_cols 
        , _logic_main_menu_layout_state . max_cols 
        , _logic_main_menu_layout_state . current_cols 
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: receive ( typename messages :: logic_main_menu_next_row )
{
    platform_math :: inc_whole ( _logic_main_menu_layout_state . max_rows ) ;
    _logic_main_menu_layout_state . current_cols = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _proceed_with_layout ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_layout_state . requested ) )
    {
        _logic_main_menu_layout_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_rows_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_rows_state . replied ) )
    {
        _logic_main_menu_rows_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_cols_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_cols_state . replied ) )
    {
        _logic_main_menu_cols_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_aspect_ratio ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . replied ) )
    {
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _obtain_cols_count ( )
{
    _logic_main_menu_cols_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_cols_state . requested_row = _logic_main_menu_layout_state . requested_row ;
    typename messages :: logic_main_menu_cols_request msg ;
    msg . row = _logic_main_menu_layout_state . requested_row ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _obtain_rows_count ( )
{
    _logic_main_menu_rows_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_rows_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _obtain_aspect_ratio ( )
{
    _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _reply_layout ( )
{
    _compute_layout ( ) ;
    _reply_computed_layout ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _reply_computed_layout ( )
{
    typename messages :: logic_main_menu_layout_position_reply msg ;
    msg . row = _logic_main_menu_layout_state . requested_row ;
    msg . col = _logic_main_menu_layout_state . requested_col ;
    msg . position = _logic_main_menu_layout_state . letter_position ;
    msg . scale = _logic_main_menu_layout_state . menu_scale ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_layout ( )
{
    _compute_unscaled_menu_size ( ) ;
    _compute_menu_scale ( ) ;
    _compute_menu_rect ( ) ;
    _compute_row_rect ( ) ;
    _compute_decorated_row_rect ( ) ;
    _compute_letter_rect ( ) ;
    _compute_letter_position ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_unscaled_menu_size ( )
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
    num_fract unscaled_menu_width ;
    num_fract unscaled_menu_height ;
    
    platform_math :: make_fract_from_whole ( letters_in_row , _logic_main_menu_layout_state . max_cols ) ;
    platform_math :: make_fract_from_whole ( letters_in_col , _logic_main_menu_layout_state . max_rows ) ;
    
    platform_math :: sub_fracts ( spacings_in_row , letters_in_row , _platform_math_consts . get ( ) . fract_1 ) ;
    platform_math :: sub_fracts ( spacings_in_col , letters_in_col , _platform_math_consts . get ( ) . fract_1 ) ;
    
    letters_width = letters_in_row ;
    letters_height = letters_in_col ;

    platform_math :: mul_fracts ( spacings_width , _logic_main_menu_layout_consts . letter_size_fract_horizontal_spacing , spacings_in_row ) ;
    platform_math :: mul_fracts ( spacings_height , _logic_main_menu_layout_consts . letter_size_fract_vertical_spacing , spacings_in_col ) ;
    
    platform_math :: mul_fracts ( borders_width , _logic_main_menu_layout_consts . letter_size_fract_horizontal_border , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: mul_fracts ( borders_height , _logic_main_menu_layout_consts . letter_size_fract_vertical_border , _platform_math_consts . get ( ) . fract_2 ) ;
    
    platform_math :: add_fracts ( menu_width , letters_width , spacings_width ) ;
    platform_math :: add_fracts ( menu_height , letters_height , spacings_height ) ;
    
    platform_math :: add_to_fract ( menu_width , borders_width ) ;
    platform_math :: add_to_fract ( menu_height , borders_height ) ;

    platform_math :: mul_fracts ( unscaled_menu_width , menu_width , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size ) ;
    platform_math :: mul_fracts ( unscaled_menu_height , menu_height , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size ) ;
    
    _logic_main_menu_layout_state . unscaled_menu_width = unscaled_menu_width ;
    _logic_main_menu_layout_state . unscaled_menu_height = unscaled_menu_height ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_menu_scale ( )
{
    num_fract screen_ratio ;
    num_fract menu_ratio ;
    num_fract menu_scale ;
    
    platform_math :: div_fracts ( screen_ratio , _engine_render_aspect_state . width , _engine_render_aspect_state . height ) ;
    platform_math :: div_fracts ( menu_ratio , _logic_main_menu_layout_state . unscaled_menu_width , _logic_main_menu_layout_state . unscaled_menu_height ) ;
    
    if ( platform_conditions :: fract_greater_than_fract ( menu_ratio , screen_ratio ) )
        platform_math :: div_fracts ( menu_scale , _engine_render_aspect_state . width , _logic_main_menu_layout_state . unscaled_menu_width ) ;
    else
        platform_math :: div_fracts ( menu_scale , _engine_render_aspect_state . height , _logic_main_menu_layout_state . unscaled_menu_height ) ;
    
    platform_math :: mul_fract_by ( menu_scale , _platform_math_consts . get ( ) . fract_2 ) ;
    
    _logic_main_menu_layout_state . menu_scale = menu_scale ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_menu_rect ( )
{
    num_fract scaled_menu_width ;
    num_fract scaled_menu_height ;
    _rect menu_rect ;
    
    platform_math :: mul_fracts ( scaled_menu_width , _logic_main_menu_layout_state . unscaled_menu_width , _logic_main_menu_layout_state . menu_scale ) ;
    platform_math :: mul_fracts ( scaled_menu_height , _logic_main_menu_layout_state . unscaled_menu_height , _logic_main_menu_layout_state . menu_scale ) ;
    
    platform_math :: div_fracts ( menu_rect . left , scaled_menu_width , _platform_math_consts . get ( ) . fract_minus_2 ) ;
    platform_math :: div_fracts ( menu_rect . right , scaled_menu_width , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: div_fracts ( menu_rect . bottom , scaled_menu_height , _platform_math_consts . get ( ) . fract_minus_2 ) ;
    platform_math :: div_fracts ( menu_rect . top , scaled_menu_height , _platform_math_consts . get ( ) . fract_2 ) ;
    
    _logic_main_menu_layout_state . menu_rect = menu_rect ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_row_rect ( )
{
    num_fract letters_width ;
    num_fract spacings_width ;
    num_fract border_height ;
    num_fract letters_in_row ;
    num_fract spacings_in_row ;
    num_fract row_width ;
    num_fract row_height ;
    num_fract row_number ;
    _rect row_rect ;
    num_fract letter_size ;
    
    platform_math :: make_fract_from_whole ( letters_in_row , _logic_main_menu_cols_state . cols ) ;
    platform_math :: sub_fracts ( spacings_in_row , letters_in_row , _platform_math_consts . get ( ) . fract_1 ) ;

    letters_width = letters_in_row ;
    border_height = _logic_main_menu_layout_consts . letter_size_fract_vertical_border ;
    platform_math :: mul_fracts ( spacings_width , spacings_in_row , _logic_main_menu_layout_consts . letter_size_fract_horizontal_spacing ) ;
    
    platform_math :: add_fracts ( row_width , letters_width , spacings_width ) ;
    platform_math :: add_fracts ( row_height , _platform_math_consts . get ( ) . fract_1 , _logic_main_menu_layout_consts . letter_size_fract_vertical_spacing ) ;
    
    platform_math :: mul_fracts ( letter_size , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size , _logic_main_menu_layout_state . menu_scale ) ;
    
    platform_math :: mul_fract_by ( row_width , letter_size ) ;
    platform_math :: mul_fract_by ( row_height , letter_size ) ;
    platform_math :: mul_fract_by ( border_height , letter_size ) ;
    
    platform_math :: make_fract_from_whole ( row_number , _logic_main_menu_layout_state . requested_row ) ;

    platform_math :: mul_fracts ( row_rect . top , row_number , row_height ) ;
    platform_math :: add_to_fract ( row_rect . top , border_height ) ;
    platform_math :: neg_fract ( row_rect . top ) ;
    platform_math :: add_to_fract ( row_rect . top , _logic_main_menu_layout_state . menu_rect . top ) ;
    platform_math :: sub_fracts ( row_rect . bottom , row_rect . top , row_height ) ;
    platform_math :: div_fracts ( row_rect . left , row_width , _platform_math_consts . get ( ) . fract_minus_2 ) ;
    platform_math :: div_fracts ( row_rect . right , row_width , _platform_math_consts . get ( ) . fract_2 ) ;
    
    _logic_main_menu_layout_state . row_rect = row_rect ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_decorated_row_rect ( )
{
    num_fract rect_vertical_extent ;
    num_whole last_row ;
    _rect decorated_row_rect ;

    platform_math :: div_fracts ( rect_vertical_extent , _logic_main_menu_layout_consts . letter_size_fract_vertical_spacing , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: sub_wholes ( last_row , _logic_main_menu_layout_state . max_rows , _platform_math_consts . get ( ) . whole_1 ) ;
    
    decorated_row_rect = _logic_main_menu_layout_state . row_rect ;
    
    platform_math :: add_to_fract ( decorated_row_rect . bottom , rect_vertical_extent ) ;
    if ( platform_conditions :: whole_greater_than_zero ( _logic_main_menu_layout_state . requested_row ) )
        platform_math :: add_to_fract ( decorated_row_rect . top , rect_vertical_extent ) ;
    if ( platform_conditions :: whole_less_than_whole ( _logic_main_menu_layout_state . requested_row , last_row ) )
        platform_math :: add_to_fract ( decorated_row_rect . bottom , rect_vertical_extent ) ;        
        
    _logic_main_menu_layout_state . decorated_row_rect = decorated_row_rect ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_letter_rect ( )
{
    num_fract col_number ;
    num_fract col_width ;
    num_fract letter_size ;
    _rect letter_rect ;
    
    platform_math :: make_fract_from_whole ( col_number , _logic_main_menu_layout_state . requested_col ) ;
    platform_math :: mul_fracts ( letter_size , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size , _logic_main_menu_layout_state . menu_scale ) ;
    
    platform_math :: add_fracts ( col_width , _platform_math_consts . get ( ) . fract_1 , _logic_main_menu_layout_consts . letter_size_fract_horizontal_spacing ) ;
    platform_math :: mul_fract_by ( col_width , letter_size ) ;
    
    letter_rect . top = _logic_main_menu_layout_state . row_rect . top ;
    platform_math :: sub_fracts ( letter_rect . bottom , letter_rect . top , letter_size ) ;
    platform_math :: mul_fracts ( letter_rect . left , col_number , col_width ) ;
    platform_math :: add_to_fract ( letter_rect . left , _logic_main_menu_layout_state . row_rect . left ) ;
    platform_math :: add_fracts ( letter_rect . right , letter_rect . left , letter_size ) ;
    
    _logic_main_menu_layout_state . letter_rect = letter_rect ;
}

template < typename mediator >
void shy_logic_main_menu_layout < mediator > :: _compute_letter_position ( )
{
    num_fract letter_position_x ;
    num_fract letter_position_y ;
    num_fract letter_position_z ;
    _rect letter_rect ;
    
    letter_rect = _logic_main_menu_layout_state . letter_rect ;
    
    platform_math :: add_fracts ( letter_position_x , letter_rect . left , letter_rect . right ) ;
    platform_math :: add_fracts ( letter_position_y , letter_rect . bottom , letter_rect . top ) ;
    
    platform_math :: div_fract_by ( letter_position_x , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: div_fract_by ( letter_position_y , _platform_math_consts . get ( ) . fract_2 ) ;
    
    letter_position_z = _logic_main_menu_layout_consts . menu_position_z ;
    
    platform_vector :: xyz ( _logic_main_menu_layout_state . letter_position , letter_position_x , letter_position_y , letter_position_z ) ;
}
