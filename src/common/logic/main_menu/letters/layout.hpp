template < typename mediator >
class shy_logic_main_menu_letters_layout
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: engine_math :: rect rect ;
    typedef typename mediator :: logic_main_menu_letters_meshes_stateless :: logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts_type ;
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

    class _logic_main_menu_letters_layout_consts_type
    {
    public :
        _logic_main_menu_letters_layout_consts_type ( ) ;
    public :
        num_fract letter_size_fract_horizontal_spacing ;
        num_fract letter_size_fract_vertical_spacing ;
        num_fract letter_size_fract_horizontal_border ;
        num_fract letter_size_fract_vertical_border ;
        num_fract menu_position_z ;
    } ;

    class _logic_main_menu_letters_layout_state_type
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
        rect menu_rect ;
        rect row_rect ;
        rect decorated_row_rect ;
        rect letter_rect ;
        vector_data letter_position ;
    } ;
    
    class _logic_main_menu_letters_rows_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole rows ;
    } ;
    
    class _logic_main_menu_letters_cols_state_type
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
    shy_logic_main_menu_letters_layout ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_position_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_rows_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_cols_reply ) ;
    void receive ( typename messages :: logic_main_menu_letter_add ) ;
    void receive ( typename messages :: logic_main_menu_letters_next_row ) ;
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    shy_logic_main_menu_letters_layout < mediator > & operator= ( const shy_logic_main_menu_letters_layout < mediator > & ) ;
    void _proceed_with_layout ( ) ;
    void _obtain_rows_count ( ) ;
    void _obtain_cols_count ( ) ;
    void _obtain_aspect_ratio ( ) ;
    void _reply_layout ( ) ;
    void _reply_computed_layout ( ) ;
    void _compute_layout ( ) ;
    static void _compute_unscaled_menu_size 
        ( num_fract & unscaled_menu_width
        , num_fract & unscaled_menu_height
        , num_whole max_cols
        , num_whole max_rows
        ) ;
    static void _compute_menu_scale 
        ( num_fract & menu_scale
        , num_fract aspect_width
        , num_fract aspect_height
        , num_fract unscaled_menu_width
        , num_fract unscaled_menu_height
        ) ;
    static void _compute_menu_rect 
        ( rect & menu_rect
        , num_fract menu_scale
        , num_fract unscaled_menu_width
        , num_fract unscaled_menu_height
        ) ;
    static void _compute_row_rect
        ( rect & row_rect
        , num_whole row
        , num_whole cols
        , num_fract menu_scale
        , rect menu_rect
        ) ;
    static void _compute_letter_rect 
        ( rect & letter_rect
        , num_whole col
        , num_fract menu_scale
        , rect row_rect
        ) ;
    static void _compute_letter_position 
        ( vector_data & letter_position
        , rect letter_rect
        ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_letters_meshes_stateless_consts_type > _logic_main_menu_letters_meshes_stateless_consts ;
    const _logic_main_menu_letters_layout_consts_type _logic_main_menu_letters_layout_consts ;
    
    _logic_main_menu_letters_layout_state_type _logic_main_menu_letters_layout_state ;
    _logic_main_menu_letters_rows_state_type _logic_main_menu_letters_rows_state ;
    _logic_main_menu_letters_cols_state_type _logic_main_menu_letters_cols_state ;
    _engine_render_aspect_state_type _engine_render_aspect_state ;    
} ;

template < typename mediator >
shy_logic_main_menu_letters_layout < mediator > :: shy_logic_main_menu_letters_layout ( )
{
}

template < typename mediator >
shy_logic_main_menu_letters_layout < mediator > :: _logic_main_menu_letters_layout_consts_type :: _logic_main_menu_letters_layout_consts_type ( )
{
    platform_math :: make_num_fract ( letter_size_fract_horizontal_spacing , 0 , 10 ) ;
    platform_math :: make_num_fract ( letter_size_fract_vertical_spacing , 10 , 10 ) ;
    platform_math :: make_num_fract ( letter_size_fract_horizontal_border , 1 , 1 ) ;
    platform_math :: make_num_fract ( letter_size_fract_vertical_border , 1 , 1 ) ;
    platform_math :: make_num_fract ( menu_position_z , - 3 , 1 ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_letters_meshes_stateless_consts ( _logic_main_menu_letters_meshes_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _logic_main_menu_letters_layout_state . max_cols = _platform_math_consts . get ( ) . whole_0 ;
    _logic_main_menu_letters_layout_state . max_rows = _platform_math_consts . get ( ) . whole_1 ;
    _logic_main_menu_letters_layout_state . current_cols = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: logic_main_menu_letters_layout_position_request msg )
{
    _logic_main_menu_letters_layout_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_layout_state . requested_col = msg . col ;
    _logic_main_menu_letters_layout_state . requested_row = msg . row ;
    _proceed_with_layout ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: logic_main_menu_letters_rows_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_rows_state . requested ) )
    {
        _logic_main_menu_letters_rows_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_rows_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_rows_state . rows = msg . rows ;
        _proceed_with_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: logic_main_menu_letters_cols_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_cols_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letters_cols_state . requested_row , msg . row )
       )
    {
        _logic_main_menu_letters_cols_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_cols_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_cols_state . cols = msg . cols ;
        _proceed_with_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: engine_render_aspect_reply msg )
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
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: logic_main_menu_letter_add )
{
    platform_math :: inc_whole ( _logic_main_menu_letters_layout_state . current_cols ) ;
    engine_math :: max_whole 
        ( _logic_main_menu_letters_layout_state . max_cols 
        , _logic_main_menu_letters_layout_state . max_cols 
        , _logic_main_menu_letters_layout_state . current_cols 
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: receive ( typename messages :: logic_main_menu_letters_next_row )
{
    platform_math :: inc_whole ( _logic_main_menu_letters_layout_state . max_rows ) ;
    _logic_main_menu_letters_layout_state . current_cols = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _proceed_with_layout ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_state . requested ) )
    {
        _logic_main_menu_letters_layout_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_rows_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_rows_state . replied ) )
    {
        _logic_main_menu_letters_rows_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_cols_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_cols_state . replied ) )
    {
        _logic_main_menu_letters_cols_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_aspect_ratio ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . replied ) )
    {
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_layout ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _obtain_cols_count ( )
{
    _logic_main_menu_letters_cols_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_cols_state . requested_row = _logic_main_menu_letters_layout_state . requested_row ;
    typename messages :: logic_main_menu_letters_cols_request msg ;
    msg . row = _logic_main_menu_letters_layout_state . requested_row ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _obtain_rows_count ( )
{
    _logic_main_menu_letters_rows_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_rows_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _obtain_aspect_ratio ( )
{
    _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _reply_layout ( )
{
    _compute_layout ( ) ;
    _reply_computed_layout ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _reply_computed_layout ( )
{
    typename messages :: logic_main_menu_letters_layout_position_reply msg ;
    msg . row = _logic_main_menu_letters_layout_state . requested_row ;
    msg . col = _logic_main_menu_letters_layout_state . requested_col ;
    msg . position = _logic_main_menu_letters_layout_state . letter_position ;
    msg . scale = _logic_main_menu_letters_layout_state . menu_scale ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _compute_layout ( )
{
    _compute_unscaled_menu_size 
        ( _logic_main_menu_letters_layout_state . unscaled_menu_width
        , _logic_main_menu_letters_layout_state . unscaled_menu_height
        , _logic_main_menu_letters_layout_state . max_cols
        , _logic_main_menu_letters_layout_state . max_rows
        ) ;
    _compute_menu_scale 
        ( _logic_main_menu_letters_layout_state . menu_scale
        , _engine_render_aspect_state . width
        , _engine_render_aspect_state . height
        , _logic_main_menu_letters_layout_state . unscaled_menu_width
        , _logic_main_menu_letters_layout_state . unscaled_menu_height
        ) ;
    _compute_menu_rect 
        ( _logic_main_menu_letters_layout_state . menu_rect
        , _logic_main_menu_letters_layout_state . menu_scale
        , _logic_main_menu_letters_layout_state . unscaled_menu_width
        , _logic_main_menu_letters_layout_state . unscaled_menu_height
        ) ;
    _compute_row_rect 
        ( _logic_main_menu_letters_layout_state . row_rect
        , _logic_main_menu_letters_layout_state . requested_row
        , _logic_main_menu_letters_cols_state . cols
        , _logic_main_menu_letters_layout_state . menu_scale
        , _logic_main_menu_letters_layout_state . menu_rect
        ) ;
    _compute_letter_rect 
        ( _logic_main_menu_letters_layout_state . letter_rect
        , _logic_main_menu_letters_layout_state . requested_col
        , _logic_main_menu_letters_layout_state . menu_scale
        , _logic_main_menu_letters_layout_state . row_rect
        ) ;
    _compute_letter_position 
        ( _logic_main_menu_letters_layout_state . letter_position
        , _logic_main_menu_letters_layout_state . letter_rect
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _compute_unscaled_menu_size 
    ( num_fract & unscaled_menu_width
    , num_fract & unscaled_menu_height
    , num_whole max_cols
    , num_whole max_rows
    )
{
    static const _logic_main_menu_letters_layout_consts_type logic_main_menu_letters_layout_consts ;
    static const logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts ;
    
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

    platform_math :: mul_fracts ( spacings_width , logic_main_menu_letters_layout_consts . letter_size_fract_horizontal_spacing , spacings_in_row ) ;
    platform_math :: mul_fracts ( spacings_height , logic_main_menu_letters_layout_consts . letter_size_fract_vertical_spacing , spacings_in_col ) ;
    
    platform_math :: mul_fracts ( borders_width , logic_main_menu_letters_layout_consts . letter_size_fract_horizontal_border , fract_2 ) ;
    platform_math :: mul_fracts ( borders_height , logic_main_menu_letters_layout_consts . letter_size_fract_vertical_border , fract_2 ) ;
    
    platform_math :: add_fracts ( menu_width , letters_width , spacings_width ) ;
    platform_math :: add_fracts ( menu_height , letters_height , spacings_height ) ;
    
    platform_math :: add_to_fract ( menu_width , borders_width ) ;
    platform_math :: add_to_fract ( menu_height , borders_height ) ;

    platform_math :: mul_fracts ( unscaled_menu_width , menu_width , logic_main_menu_letters_meshes_stateless_consts . letter_mesh_size ) ;
    platform_math :: mul_fracts ( unscaled_menu_height , menu_height , logic_main_menu_letters_meshes_stateless_consts . letter_mesh_size ) ;    
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _compute_menu_scale 
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
void shy_logic_main_menu_letters_layout < mediator > :: _compute_menu_rect 
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
void shy_logic_main_menu_letters_layout < mediator > :: _compute_row_rect 
    ( rect & row_rect
    , num_whole row
    , num_whole cols
    , num_fract menu_scale
    , rect menu_rect
    )
{
    static const _logic_main_menu_letters_layout_consts_type logic_main_menu_letters_layout_consts ;
    static const logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts ;

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
    border_height = logic_main_menu_letters_layout_consts . letter_size_fract_vertical_border ;
    platform_math :: mul_fracts ( spacings_width , spacings_in_row , logic_main_menu_letters_layout_consts . letter_size_fract_horizontal_spacing ) ;
    
    platform_math :: add_fracts ( row_width , letters_width , spacings_width ) ;
    platform_math :: add_fracts ( row_height , fract_1 , logic_main_menu_letters_layout_consts . letter_size_fract_vertical_spacing ) ;
    
    platform_math :: mul_fracts ( letter_size , logic_main_menu_letters_meshes_stateless_consts . letter_mesh_size , menu_scale ) ;
    
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
void shy_logic_main_menu_letters_layout < mediator > :: _compute_letter_rect 
    ( rect & letter_rect
    , num_whole col
    , num_fract menu_scale
    , rect row_rect
    )
{
    static const _logic_main_menu_letters_layout_consts_type logic_main_menu_letters_layout_consts ;
    static const logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts ;

    num_fract col_number ;
    num_fract col_width ;
    num_fract letter_size ;
    num_fract fract_1 ;
    
    platform_math :: make_num_fract ( fract_1 , 1 , 1 ) ;
    
    platform_math :: make_fract_from_whole ( col_number , col ) ;
    platform_math :: mul_fracts ( letter_size , logic_main_menu_letters_meshes_stateless_consts . letter_mesh_size , menu_scale ) ;
    
    platform_math :: add_fracts ( col_width , fract_1 , logic_main_menu_letters_layout_consts . letter_size_fract_horizontal_spacing ) ;
    platform_math :: mul_fract_by ( col_width , letter_size ) ;
    
    letter_rect . top = row_rect . top ;
    platform_math :: sub_fracts ( letter_rect . bottom , letter_rect . top , letter_size ) ;
    platform_math :: mul_fracts ( letter_rect . left , col_number , col_width ) ;
    platform_math :: add_to_fract ( letter_rect . left , row_rect . left ) ;
    platform_math :: add_fracts ( letter_rect . right , letter_rect . left , letter_size ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout < mediator > :: _compute_letter_position 
    ( vector_data & letter_position
    , rect letter_rect
    )
{
    static const _logic_main_menu_letters_layout_consts_type logic_main_menu_letters_layout_consts ;

    num_fract letter_position_x ;
    num_fract letter_position_y ;
    num_fract letter_position_z ;
    num_fract fract_2 ;
    
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    
    platform_math :: add_fracts ( letter_position_x , letter_rect . left , letter_rect . right ) ;
    platform_math :: add_fracts ( letter_position_y , letter_rect . bottom , letter_rect . top ) ;
    
    platform_math :: div_fract_by ( letter_position_x , fract_2 ) ;
    platform_math :: div_fract_by ( letter_position_y , fract_2 ) ;
    
    letter_position_z = logic_main_menu_letters_layout_consts . menu_position_z ;
    
    platform_vector :: xyz ( letter_position , letter_position_x , letter_position_y , letter_position_z ) ;
}
