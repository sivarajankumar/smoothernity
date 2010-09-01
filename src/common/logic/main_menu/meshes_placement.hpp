template < typename mediator >
class shy_logic_main_menu_letters_meshes_placement
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_main_menu_letters_meshes_place_state_type
    {
    public :
        num_whole requested ;
        num_whole current_mesh_index ;
    } ;
    
    class _logic_main_menu_meshes_count_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole meshes ;
    } ;

    class _logic_main_menu_mesh_row_col_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_index ;
        num_whole replied ;
        num_whole row ;
        num_whole col ;
    } ;

    class _logic_main_menu_mesh_id_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_index ;
        num_whole replied ;
        engine_render_mesh_id mesh ;
    } ;

    class _logic_main_menu_letters_animation_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        matrix_data transform ;
    } ;
    
public :
    shy_logic_main_menu_letters_meshes_placement ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_place ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_count_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_mesh_row_col_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_mesh_id_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_transform_reply ) ;
private :
    shy_logic_main_menu_letters_meshes_placement < mediator > & operator= ( const shy_logic_main_menu_letters_meshes_placement < mediator > & ) ;
    void _proceed_with_placement ( ) ;
    void _obtain_meshes_count ( ) ;
    void _obtain_first_mesh_row_col ( ) ;
    void _obtain_current_mesh_row_col ( ) ;
    void _obtain_current_mesh_id ( ) ;
    void _obtain_animated_transform ( ) ;
    void _animated_transform_received ( ) ;
    void _place_current_mesh ( ) ;
    void _move_to_next_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_main_menu_letters_meshes_place_state_type _logic_main_menu_letters_meshes_place_state ;
    _logic_main_menu_meshes_count_state_type _logic_main_menu_meshes_count_state ;
    _logic_main_menu_mesh_row_col_state_type _logic_main_menu_mesh_row_col_state ;
    _logic_main_menu_mesh_id_state_type _logic_main_menu_mesh_id_state ;
    _logic_main_menu_letters_animation_transform_state_type _logic_main_menu_letters_animation_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_meshes_placement < mediator > :: shy_logic_main_menu_letters_meshes_placement ( )
{
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_place )
{
    _logic_main_menu_letters_meshes_place_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_placement ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_count_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_count_state . requested ) )
    {
        _logic_main_menu_meshes_count_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_meshes_count_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_meshes_count_state . meshes = msg . meshes ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_letters_mesh_row_col_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_row_col_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_mesh_row_col_state . requested_index , msg . index )
       )
    {
        _logic_main_menu_mesh_row_col_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_mesh_row_col_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_mesh_row_col_state . row = msg . row ;
        _logic_main_menu_mesh_row_col_state . col = msg . col ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_letters_mesh_id_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_id_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_mesh_id_state . requested_index , msg . index )
       )
    {
        _logic_main_menu_mesh_id_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_mesh_id_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_mesh_id_state . mesh = msg . mesh ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_animation_transform_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letters_animation_transform_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letters_animation_transform_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_letters_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_animation_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_animation_transform_state . transform = msg . transform ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _proceed_with_placement ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_meshes_place_state . requested ) )
    {
        _logic_main_menu_letters_meshes_place_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_meshes_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_count_state . replied ) )
    {
        _logic_main_menu_meshes_count_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_first_mesh_row_col ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_row_col_state . replied ) )
    {
        _logic_main_menu_mesh_row_col_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_current_mesh_id ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_id_state . replied ) )
    {
        _logic_main_menu_mesh_id_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_animated_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_animation_transform_state . replied ) )
    {
        _logic_main_menu_letters_animation_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _animated_transform_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _obtain_meshes_count ( )
{
    _logic_main_menu_meshes_count_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_count_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _obtain_first_mesh_row_col ( )
{
    _logic_main_menu_letters_meshes_place_state . current_mesh_index = _platform_math_consts . get ( ) . whole_0 ;
    _obtain_current_mesh_row_col ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _obtain_current_mesh_row_col ( )
{
    _logic_main_menu_mesh_row_col_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_mesh_row_col_state . requested_index = _logic_main_menu_letters_meshes_place_state . current_mesh_index ;
    typename messages :: logic_main_menu_letters_mesh_row_col_request msg ;
    msg . index = _logic_main_menu_letters_meshes_place_state . current_mesh_index ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _obtain_current_mesh_id ( )
{
    _logic_main_menu_mesh_id_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_mesh_id_state . requested_index = _logic_main_menu_letters_meshes_place_state . current_mesh_index ;
    typename messages :: logic_main_menu_letters_mesh_id_request msg ;
    msg . index = _logic_main_menu_letters_meshes_place_state . current_mesh_index ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _obtain_animated_transform ( )
{
    _logic_main_menu_letters_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_animation_transform_state . requested_row = _logic_main_menu_mesh_row_col_state . row ;
    _logic_main_menu_letters_animation_transform_state . requested_col = _logic_main_menu_mesh_row_col_state . col ;
    typename messages :: logic_main_menu_letters_animation_transform_request msg ;
    msg . row = _logic_main_menu_mesh_row_col_state . row ;
    msg . col = _logic_main_menu_mesh_row_col_state . col ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _animated_transform_received ( )
{
    _place_current_mesh ( ) ;
    _move_to_next_mesh ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _place_current_mesh ( )
{
    typename messages :: engine_render_mesh_set_transform msg ;
    msg . transform = _logic_main_menu_letters_animation_transform_state . transform ;
    msg . mesh = _logic_main_menu_mesh_id_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_placement < mediator > :: _move_to_next_mesh ( )
{
    platform_math :: inc_whole ( _logic_main_menu_letters_meshes_place_state . current_mesh_index ) ;
    if ( platform_conditions :: whole_less_than_whole ( _logic_main_menu_letters_meshes_place_state . current_mesh_index , _logic_main_menu_meshes_count_state . meshes ) )
        _obtain_current_mesh_row_col ( ) ;
}
