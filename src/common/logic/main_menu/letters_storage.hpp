template < typename mediator >
class shy_logic_main_menu_letters_storage
{
    typedef typename mediator :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_mesh_id logic_main_menu_mesh_id ;
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
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
    
    class _col_state_type
    {
    public :
        letter_id letter ;
        logic_main_menu_mesh_id mesh ;
    } ;
    
    class _row_state_type
    {
    public :
        typename platform_static_array :: template static_array < _col_state_type , logic_main_menu_stateless_consts_type :: max_cols > cols ;
        num_whole cols_count ;
    } ;
    
    class _rows_state_type
    {
    public :
        typename platform_static_array :: template static_array < _row_state_type , logic_main_menu_stateless_consts_type :: max_rows > rows ;
        num_whole rows_count ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_add_letter ) ;
    void receive ( typename messages :: logic_main_menu_next_row ) ;
    void receive ( typename messages :: logic_main_menu_cols_request ) ;
    void receive ( typename messages :: logic_main_menu_rows_request ) ;
    void receive ( typename messages :: logic_main_menu_letter_request ) ;
    void receive ( typename messages :: logic_main_menu_mesh_has_been_created ) ;
public :
    void _next_row ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    _rows_state_type _rows_state ;
} ;

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _rows_state . rows_count = _platform_math_consts . get ( ) . whole_minus_1 ;
    _next_row ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: logic_main_menu_add_letter msg )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    typename platform_pointer :: template pointer < _col_state_type > col_state ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , _rows_state . rows_count ) ;
    platform_static_array :: element_ptr ( col_state , row_state . get ( ) . cols , row_state . get ( ) . cols_count ) ;
    col_state . get ( ) . letter = msg . letter ;
    platform_math :: inc_whole ( row_state . get ( ) . cols_count ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: logic_main_menu_mesh_has_been_created msg )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    typename platform_pointer :: template pointer < _col_state_type > col_state ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , msg . row ) ;
    platform_static_array :: element_ptr ( col_state , row_state . get ( ) . cols , msg . col ) ;
    col_state . get ( ) . mesh = msg . mesh ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: logic_main_menu_next_row )
{
    _next_row ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: logic_main_menu_cols_request msg )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , msg . row ) ;
    
    typename messages :: logic_main_menu_cols_reply reply_msg ;
    reply_msg . row = msg . row ;
    reply_msg . cols = row_state . get ( ) . cols_count ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: logic_main_menu_rows_request )
{
    typename messages :: logic_main_menu_rows_reply reply_msg ;
    reply_msg . rows = _rows_state . rows_count ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: receive ( typename messages :: logic_main_menu_letter_request msg )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    typename platform_pointer :: template pointer < _col_state_type > col_state ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , msg . row ) ;
    platform_static_array :: element_ptr ( col_state , row_state . get ( ) . cols , msg . col ) ;

    typename messages :: logic_main_menu_letter_reply reply_msg ;
    reply_msg . row = msg . row ;
    reply_msg . col = msg . col ;
    reply_msg . letter = col_state . get ( ) . letter ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_storage < mediator > :: _next_row ( )
{
    typename platform_pointer :: template pointer < _row_state_type > row_state ;
    platform_math :: inc_whole ( _rows_state . rows_count ) ;
    platform_static_array :: element_ptr ( row_state , _rows_state . rows , _rows_state . rows_count ) ;
    row_state . get ( ) . cols_count = _platform_math_consts . get ( ) . whole_0 ;
}
