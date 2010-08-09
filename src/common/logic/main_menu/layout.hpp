template < typename mediator >
class shy_logic_main_menu_layout
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_main_menu_layout_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        vector_data position ;
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
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    void _proceed_with_layout ( ) ;
    void _obtain_rows_count ( ) ;
    void _obtain_cols_count ( ) ;
    void _obtain_aspect_ratio ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    _logic_main_menu_layout_state_type _logic_main_menu_layout_state ;
    _logic_main_menu_rows_state_type _logic_main_menu_rows_state ;
    _logic_main_menu_cols_state_type _logic_main_menu_cols_state ;
    _engine_render_aspect_state_type _engine_render_aspect_state ;
} ;

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
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
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
