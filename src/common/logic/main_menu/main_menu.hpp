template < typename mediator >
class shy_logic_main_menu
{
    typedef typename mediator :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    typedef typename mediator :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_render ) ;
    void receive ( typename messages :: main_menu_update ) ;
    void receive ( typename messages :: main_menu_text_create_finished ) ;
    void receive ( typename messages :: logic_main_menu_mesh_create_finished ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    num_whole _launch_permitted ;
    num_whole _main_menu_finished ;
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
    
    _launch_permitted = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_finished = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _launch_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_render )
{
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _launch_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _main_menu_finished ) )
        {
            _main_menu_finished = _platform_math_consts . get ( ) . whole_true ;
            _mediator . get ( ) . send ( typename messages :: main_menu_text_create ( ) ) ;
        }
    }
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: main_menu_text_create_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_mesh_create ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: logic_main_menu_mesh_create_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_finished ( ) ) ;
}
