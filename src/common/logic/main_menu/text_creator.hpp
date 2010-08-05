template < typename mediator >
class shy_logic_main_menu_text_creator
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
    void receive ( typename messages :: main_menu_text_create ) ;
public :
    void _add_letter ( letter_id ) ;
    void _next_row ( ) ;
    void _text_create_finished ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
} ;

template < typename mediator >
void shy_logic_main_menu_text_creator < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_text_creator < mediator > :: receive ( typename messages :: main_menu_text_create )
{
    typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > logic_text_stateless_consts ;
    _mediator . get ( ) . logic_text_stateless_consts ( logic_text_stateless_consts ) ;
    const alphabet_english_type & eng = logic_text_stateless_consts . get ( ) . alphabet_english ;
    letter_id whitespace = logic_text_stateless_consts . get ( ) . whitespace ;

    _add_letter ( eng . N ) ;
    _add_letter ( eng . E ) ;
    _add_letter ( eng . W ) ;
    _add_letter ( whitespace ) ;
    _add_letter ( eng . G ) ;
    _add_letter ( eng . A ) ;
    _add_letter ( eng . M ) ;
    _add_letter ( eng . E ) ;
    
    _next_row ( ) ;
    _add_letter ( eng . L ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . A ) ;
    _add_letter ( eng . D ) ;
    _add_letter ( whitespace ) ;
    _add_letter ( eng . G ) ;
    _add_letter ( eng . A ) ;
    _add_letter ( eng . M ) ;
    _add_letter ( eng . E ) ;

    _next_row ( ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . P ) ;
    _add_letter ( eng . T ) ;
    _add_letter ( eng . I ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . N ) ;
    _add_letter ( eng . S ) ;

    _next_row ( ) ;
    _add_letter ( eng . E ) ;
    _add_letter ( eng . X ) ;
    _add_letter ( eng . I ) ;
    _add_letter ( eng . T ) ;
    
    _text_create_finished ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_text_creator < mediator > :: _add_letter ( letter_id letter )
{
    typename messages :: logic_main_menu_add_letter msg ;
    msg . letter = letter ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_text_creator < mediator > :: _next_row ( )
{
    _mediator . get ( ) . send ( typename messages :: main_menu_next_row ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_text_creator < mediator > :: _text_create_finished ( )
{
    _mediator . get ( ) . send ( typename messages :: main_menu_text_create_finished ( ) ) ;
}
