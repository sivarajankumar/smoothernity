template < typename mediator >
class shy_logic_main_menu_mesh_creator
{
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_mesh_creator_consts_type
    {
    public :
        _logic_main_menu_mesh_creator_consts_type ( ) ;
        num_whole frames_between_creation ;
        num_whole meshes_per_frame ;
    } ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: main_menu_mesh_create ) ;
    void receive ( typename messages :: main_menu_update ) ;
    void receive ( typename messages :: main_menu_cols_reply ) ;
    void receive ( typename messages :: main_menu_rows_reply ) ;
    void receive ( typename messages :: main_menu_letter_reply ) ;
private :
    void _proceed_with_creation ( ) ;
    void _move_to_next_row ( ) ;
    void _move_to_next_col ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_mesh_creator_consts_type _logic_main_menu_mesh_creator_consts ;
    
    num_whole _mesh_creation_permitted ;
    
    num_whole _main_menu_rows_requested ;
    num_whole _main_menu_rows_replied ;
    num_whole _main_menu_rows ;
    
    num_whole _main_menu_cols_requested ;
    num_whole _main_menu_cols_requested_row ;
    num_whole _main_menu_cols_replied ;
    num_whole _main_menu_cols ;
    
    num_whole _main_menu_letter_requested ;
    num_whole _main_menu_letter_requested_row ;
    num_whole _main_menu_letter_requested_col ;
    num_whole _main_menu_letter_replied ;
    letter_id _main_menu_letter ;
    
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
    
    _mesh_creation_permitted = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_rows_requested = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_rows_replied = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_cols_requested = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_cols_replied = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_letter_requested = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_letter_replied = _platform_math_consts . get ( ) . whole_false ;
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
    if ( platform_conditions :: whole_is_true ( _main_menu_cols_requested )
      && platform_conditions :: wholes_are_equal ( _main_menu_cols_requested_row , msg . row )
       )
    {
        _main_menu_cols_requested = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_cols_replied = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_cols = msg . cols ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_rows_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _main_menu_rows_requested ) )
    {
        _main_menu_rows_requested = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_rows_replied = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_rows = msg . rows ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_letter_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _main_menu_letter_requested )
      && platform_conditions :: wholes_are_equal ( _main_menu_letter_requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _main_menu_letter_requested_col , msg . col )
       )
    {
        _main_menu_letter_requested = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_letter_replied = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_letter = msg . letter ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _mesh_creation_permitted ) )
    {
        _mesh_creation_permitted = _platform_math_consts . get ( ) . whole_false ;
        _main_menu_rows_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: main_menu_rows_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _main_menu_rows_replied ) )
    {
        _main_menu_rows_replied = _platform_math_consts . get ( ) . whole_false ;
        _current_row = _platform_math_consts . get ( ) . whole_minus_1 ;
        _move_to_next_row ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _main_menu_cols_replied ) )
    {
        _main_menu_cols_replied = _platform_math_consts . get ( ) . whole_false ;
        _current_col = _platform_math_consts . get ( ) . whole_minus_1 ;
        _move_to_next_col ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _main_menu_letter_replied ) )
    {
        _move_to_next_col ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: _move_to_next_row ( )
{
    platform_math :: inc_whole ( _current_row ) ;
    if ( platform_conditions :: whole_less_than_whole ( _current_row , _main_menu_rows ) )
    {
        _main_menu_cols_requested = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_cols_requested_row = _current_row ;
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
    if ( platform_conditions :: whole_less_than_whole ( _current_col , _main_menu_cols ) )
    {
        _main_menu_letter_requested = _platform_math_consts . get ( ) . whole_true ;
        _main_menu_letter_requested_row = _current_row ;
        _main_menu_letter_requested_col = _current_col ;
        typename messages :: main_menu_letter_request msg ;
        msg . row = _current_row ;
        msg . col = _current_col ;
        _mediator . get ( ) . send ( msg ) ;
    }
    else
        _move_to_next_row ( ) ;
}
