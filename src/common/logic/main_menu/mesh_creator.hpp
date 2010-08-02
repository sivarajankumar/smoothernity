template < typename mediator >
class shy_logic_main_menu_mesh_creator
{
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: logic_text_stateless logic_text_stateless ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_mesh_creator_consts_type
    {
    public :
        _logic_main_menu_mesh_creator_consts_type ( ) ;
    public :
        num_whole frames_between_creation ;
        num_whole meshes_per_frame ;
    } ;
    
    class _main_menu_rows_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole rows ;
    } ;
    
    class _main_menu_cols_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole replied ;
        num_whole cols ;
    } ;

    class _main_menu_letter_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        letter_id letter ;
    } ;

    class _render_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        mesh_id mesh ;
    } ;
    
    class _text_letter_big_tex_coords_state_type
    {
    public :
        num_whole requested ;
        letter_id requested_letter ;
        num_whole replied ;
        num_fract bottom ;
        num_fract left ;
        num_fract top ;
        num_fract right ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: main_menu_mesh_create ) ;
    void receive ( typename messages :: main_menu_update ) ;
    void receive ( typename messages :: main_menu_cols_reply ) ;
    void receive ( typename messages :: main_menu_rows_reply ) ;
    void receive ( typename messages :: main_menu_letter_reply ) ;
    void receive ( typename messages :: render_mesh_create_reply ) ;
    void receive ( typename messages :: text_letter_big_tex_coords_reply ) ;
private :
    void _proceed_with_creation ( ) ;
    void _move_to_next_row ( ) ;
    void _move_to_next_col ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_mesh_creator_consts_type _logic_main_menu_mesh_creator_consts ;
    
    num_whole _mesh_creation_permitted ;

    _main_menu_rows_state_type _main_menu_rows_state ;
    _main_menu_cols_state_type _main_menu_cols_state ;
    _main_menu_letter_state_type _main_menu_letter_state ;
    _render_mesh_create_state_type _render_mesh_create_state ;
    _text_letter_big_tex_coords_state_type _text_letter_big_tex_coords_state ;
    
    num_whole _current_row ;
    num_whole _current_col ;
} ;

template < typename mediator >
shy_logic_main_menu_mesh_creator < mediator > :: _logic_main_menu_mesh_creator_consts_type :: _logic_main_menu_mesh_creator_consts_type ( )
{
    platform_math :: make_num_whole ( frames_between_creation , 5 ) ;
    platform_math :: make_num_whole ( meshes_per_frame , 10 ) ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _current_row = _platform_math_consts . get ( ) . whole_0 ;
    _current_col = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_mesh_create )
{
    _mesh_creation_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_update )
{
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_cols_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _main_menu_cols_state . requested )
      && platform_conditions :: wholes_are_equal ( _main_menu_cols_state . requested_row , msg . row )
       )
    {
        _main_menu_cols_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_cols_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_cols_state . cols = msg . cols ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_rows_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _main_menu_rows_state . requested ) )
    {
        _main_menu_rows_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_rows_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_rows_state . rows = msg . rows ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_letter_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _main_menu_letter_state . requested )
      && platform_conditions :: wholes_are_equal ( _main_menu_letter_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _main_menu_letter_state . requested_col , msg . col )
       )
    {
        _main_menu_letter_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_letter_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_letter_state . letter = msg . letter ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _render_mesh_create_state . requested ) )
    {
        _render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _render_mesh_create_state . mesh = msg . mesh ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: text_letter_big_tex_coords_reply msg )
{
    num_whole letters_are_equal ;
    logic_text_stateless :: are_letters_equal ( letters_are_equal , _text_letter_big_tex_coords_state . requested_letter , msg . letter ) ;
    if ( platform_conditions :: whole_is_true ( _text_letter_big_tex_coords_state . requested )
      && platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        _text_letter_big_tex_coords_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _text_letter_big_tex_coords_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _text_letter_big_tex_coords_state . bottom = msg . bottom ;
        _text_letter_big_tex_coords_state . left = msg . left ;
        _text_letter_big_tex_coords_state . top = msg . top ;
        _text_letter_big_tex_coords_state . right = msg . right ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _mesh_creation_permitted ) )
    {
        _mesh_creation_permitted = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_rows_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: main_menu_rows_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _main_menu_rows_state . replied ) )
    {
        _main_menu_rows_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _current_row = _platform_math_consts . get ( ) . whole_minus_1 ;
        _move_to_next_row ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _main_menu_cols_state . replied ) )
    {
        _main_menu_cols_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _current_col = _platform_math_consts . get ( ) . whole_minus_1 ;
        _move_to_next_col ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _main_menu_letter_state . replied ) )
    {
        _main_menu_letter_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
        typename messages :: render_mesh_create_request msg ;
        msg . vertices = _platform_math_consts . get ( ) . whole_4 ;
        msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_4 ;
        msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
        _mediator . get ( ) . send ( msg ) ;
    }
    if ( platform_conditions :: whole_is_true ( _render_mesh_create_state . replied ) )
    {
        _render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _text_letter_big_tex_coords_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _text_letter_big_tex_coords_state . requested_letter = _main_menu_letter_state . letter ;
        typename messages :: text_letter_big_tex_coords_request msg ;
        msg . letter = _main_menu_letter_state . letter ;
        _mediator . get ( ) . send ( msg ) ;
    }
    if ( platform_conditions :: whole_is_true ( _text_letter_big_tex_coords_state . replied ) )
    {
        _text_letter_big_tex_coords_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _move_to_next_col ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: _move_to_next_row ( )
{
    platform_math :: inc_whole ( _current_row ) ;
    if ( platform_conditions :: whole_less_than_whole ( _current_row , _main_menu_rows_state . rows ) )
    {
        _main_menu_cols_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_cols_state . requested_row = _current_row ;
        typename messages :: main_menu_cols_request msg ;
        msg . row = _current_row ;
        _mediator . get ( ) . send ( msg ) ;
    }
    else
        _mediator . get ( ) . send ( typename messages :: main_menu_mesh_create_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: _move_to_next_col ( )
{
    platform_math :: inc_whole ( _current_col ) ;
    if ( platform_conditions :: whole_less_than_whole ( _current_col , _main_menu_cols_state . cols ) )
    {
        _main_menu_letter_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_letter_state . requested_row = _current_row ;
        _main_menu_letter_state . requested_col = _current_col ;
        typename messages :: main_menu_letter_request msg ;
        msg . row = _current_row ;
        msg . col = _current_col ;
        _mediator . get ( ) . send ( msg ) ;
    }
    else
        _move_to_next_row ( ) ;
}
