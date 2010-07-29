template < typename mediator >
class shy_logic_main_menu
{
    typedef typename mediator :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    class _logic_main_menu_consts_type
    {
    public :
        _logic_main_menu_consts_type ( ) ;
    public :
        static const_int_32 max_rows = 5 ;
        static const_int_32 max_letters = 16 ;
    } ;
    
    class _letter_state_type
    {
    public :
        letter_id letter ;
        mesh_id mesh ;
        num_whole is_whitespace ;
    } ;
    
    class _row_state_type
    {
    public :
        typename platform_static_array :: template static_array < _letter_state_type , _logic_main_menu_consts_type :: max_letters > letters ;
        num_whole letters_count ;
    } ;
    
    class _rows_state_type
    {
    public :
        typename platform_static_array :: template static_array < _row_state_type , _logic_main_menu_consts_type :: max_rows > rows ;
        num_whole rows_count ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: main_menu_launch_permit msg ) ;
    void receive ( typename messages :: main_menu_render msg ) ;
    void receive ( typename messages :: main_menu_update msg ) ;
public :
    void _create_menu_text ( ) ;
    void _add_letter ( letter_id letter ) ;
    void _add_whitespace ( ) ;
    void _next_row ( ) ;
    void _first_row ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_consts_type _logic_main_menu_consts ;
    _rows_state_type _rows_state ;
    num_whole _launch_permitted ;
    num_whole _main_menu_finished ;
} ;

template < typename mediator >
void shy_logic_main_menu < mediator > :: _add_letter ( letter_id letter )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    typename platform_pointer :: template pointer < _letter_state_type > letter_state ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , _rows_state . rows_count ) ;
    platform_static_array :: element_ptr ( letter_state , row_state . get ( ) . letters , row_state . get ( ) . letters_count ) ;
    letter_state . get ( ) . letter = letter ;
    letter_state . get ( ) . is_whitespace = _platform_math_consts . get ( ) . whole_false ;
    platform_math :: inc_whole ( row_state . get ( ) . letters_count ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: _add_whitespace ( )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    typename platform_pointer :: template pointer < _letter_state_type > letter_state ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , _rows_state . rows_count ) ;
    platform_static_array :: element_ptr ( letter_state , row_state . get ( ) . letters , row_state . get ( ) . letters_count ) ;
    letter_state . get ( ) . is_whitespace = _platform_math_consts . get ( ) . whole_true ;
    platform_math :: inc_whole ( row_state . get ( ) . letters_count ) ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: _next_row ( )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    platform_math :: inc_whole ( _rows_state . rows_count ) ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , _rows_state . rows_count ) ;
    row_state . get ( ) . letters_count = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: _first_row ( )
{
    _rows_state . rows_count = _platform_math_consts . get ( ) . whole_minus_1 ;
    _next_row ( ) ;
}

template < typename mediator >
shy_logic_main_menu < mediator > :: _logic_main_menu_consts_type :: _logic_main_menu_consts_type ( )
{
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: init msg )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _launch_permitted = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_finished = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: main_menu_launch_permit msg )
{
    _launch_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: main_menu_render msg )
{
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: receive ( typename messages :: main_menu_update msg )
{
    if ( platform_conditions :: whole_is_true ( _launch_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _main_menu_finished ) )
        {
            _create_menu_text ( ) ;
            _main_menu_finished = _platform_math_consts . get ( ) . whole_true ;
            _mediator . get ( ) . send ( typename messages :: main_menu_finished ( ) ) ;
        }
    }
}

template < typename mediator >
void shy_logic_main_menu < mediator > :: _create_menu_text ( )
{
    typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > logic_text_stateless_consts ;
    _mediator . get ( ) . logic_text_stateless_consts ( logic_text_stateless_consts ) ;
    const alphabet_english_type & eng = logic_text_stateless_consts . get ( ) . alphabet_english ;

    _first_row ( ) ;
    _add_letter ( eng . N ) ;
    _add_letter ( eng . E ) ;
    _add_letter ( eng . W ) ;
    _add_whitespace ( ) ;
    _add_letter ( eng . G ) ;
    _add_letter ( eng . A ) ;
    _add_letter ( eng . M ) ;
    _add_letter ( eng . E ) ;
    
    _next_row ( ) ;
    _add_letter ( eng . L ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . A ) ;
    _add_letter ( eng . D ) ;
    _add_whitespace ( ) ;
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
}
