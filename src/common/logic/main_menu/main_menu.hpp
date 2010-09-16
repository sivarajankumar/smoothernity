template < typename mediator >
class shy_logic_main_menu
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_text_stateless :: logic_text_alphabet_english_type logic_text_alphabet_english_type ;
    typedef typename mediator :: logic_text_stateless :: logic_text_letter_id logic_text_letter_id ;
    typedef typename mediator :: logic_text_stateless :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: platform_touch platform_touch ;    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_disappear_finished ) ;
    void receive ( typename messages :: logic_main_menu_creation_permit ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_render ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_letters_create_finished ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_creation_finished ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_destroy_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_create_finished ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_destroy_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_reply ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < platform_touch > _platform_touch ;
    num_whole _creation_permitted ;
    num_whole _launch_permitted ;
    num_whole _created ;
    num_whole _launched ;
    num_whole _disappearing ;
} ;

template < typename mediator >
void shy_logic_main_menu < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _platform_mouse = platform_obj . get ( ) . mouse ;
    _platform_touch = platform_obj . get ( ) . touch ;
    
    _launch_permitted = _platform_math_consts . get ( ) . whole_false ;
    _creation_permitted = _platform_math_consts . get ( ) . whole_false ;
    _launched = _platform_math_consts . get ( ) . whole_false ;
    _created = _platform_math_consts . get ( ) . whole_false ;
    _disappearing = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_creation_permit )
{
    _creation_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _launch_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _creation_permitted ) )
    {
        _creation_permitted = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_create ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _created ) 
      && platform_conditions :: whole_is_true ( _launch_permitted )
       )
    {
        _launch_permitted = _platform_math_consts . get ( ) . whole_false ;
        _launched = _platform_math_consts . get ( ) . whole_true ;
    }
    if ( platform_conditions :: whole_is_true ( _created ) 
      && platform_conditions :: whole_is_true ( _launched )
       )
    {
        num_whole touch_occured ;
        num_whole mouse_button ;
        _platform_touch . get ( ) . occured ( touch_occured ) ;
        _platform_mouse . get ( ) . left_button_down ( mouse_button ) ;
        if ( platform_conditions :: whole_is_true ( touch_occured )
          || platform_conditions :: whole_is_true ( mouse_button )
           )
        {
            _launched = _platform_math_consts . get ( ) . whole_false ;
            _disappearing = _platform_math_consts . get ( ) . whole_true ;
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_animation_disappear_start ( ) ) ;
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_disappear_start ( ) ) ;
        }
        else
        {
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_place ( ) ) ;
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_track_request ( ) ) ;
        }
    }
    if ( platform_conditions :: whole_is_true ( _created )
      && platform_conditions :: whole_is_true ( _disappearing )
       )
    {
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_place ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_place ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_disappear_finished )
{
    _disappearing = _platform_math_consts . get ( ) . whole_false ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_destroy_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_destroy_reply )
{
    _created = _platform_math_consts . get ( ) . whole_false ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_destroy_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_destroy_reply )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_letters_create_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_create ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_creation_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_create ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_create_finished )
{
    _created = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_render_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_reply )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_place ( ) ) ;
}
