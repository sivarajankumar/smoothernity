template < typename mediator >
class shy_logic_main_menu_meshes_creator
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator :: logic_text_stateless logic_text_stateless ;
    typedef typename mediator :: logic_text_stateless :: logic_text_alphabet_english_type logic_text_alphabet_english_type ;
    typedef typename mediator :: logic_text_stateless :: logic_text_letter_id logic_text_letter_id ;
    typedef typename mediator :: logic_text_stateless :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    class _logic_main_menu_meshes_creator_consts_type
    {
    public :
        _logic_main_menu_meshes_creator_consts_type ( ) ;
    public :
        num_fract color_r ;
        num_fract color_g ;
        num_fract color_b ;
        num_fract color_a ;
    } ;
    
    class _logic_main_menu_letters_rows_state_type
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

    class _logic_main_menu_letter_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        logic_text_letter_id letter ;
    } ;

    class _engine_render_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        engine_render_mesh_id mesh ;
    } ;
    
    class _logic_text_letter_big_tex_coords_state_type
    {
    public :
        num_whole requested ;
        logic_text_letter_id requested_letter ;
        num_whole replied ;
        num_fract bottom ;
        num_fract left ;
        num_fract top ;
        num_fract right ;
    } ;
    
public :
	shy_logic_main_menu_meshes_creator ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_mesh_create_next ) ;
    void receive ( typename messages :: logic_main_menu_letters_cols_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_rows_reply ) ;
    void receive ( typename messages :: logic_main_menu_letter_reply ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
    void receive ( typename messages :: logic_text_letter_big_tex_coords_reply ) ;
private :
	shy_logic_main_menu_meshes_creator < mediator > & operator= ( const shy_logic_main_menu_meshes_creator < mediator > & ) ;
    void _proceed_with_creation ( ) ;
    void _obtain_rows_count ( ) ;
    void _start_first_row ( ) ;
    void _start_first_col ( ) ;
    void _move_to_next_row ( ) ;
    void _move_to_next_col ( ) ;
    void _letter_state_received ( ) ;
    void _create_mesh ( ) ;
    void _obtain_tex_coords ( ) ;
    void _letter_tex_coords_received ( ) ;
    void _fill_mesh_content ( ) ;
    void _send_mesh_created_notification ( ) ;
    void _mesh_set_vertex_position ( engine_render_mesh_id mesh , num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( engine_render_mesh_id mesh , num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( engine_render_mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( engine_render_mesh_id mesh , num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > _logic_main_menu_stateless_consts ;
    const _logic_main_menu_meshes_creator_consts_type _logic_main_menu_meshes_creator_consts ;
    
    _logic_main_menu_letters_rows_state_type _logic_main_menu_letters_rows_state ;
    _logic_main_menu_cols_state_type _logic_main_menu_cols_state ;
    _logic_main_menu_letter_state_type _logic_main_menu_letter_state ;
    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
    _logic_text_letter_big_tex_coords_state_type _logic_text_letter_big_tex_coords_state ;
    
    num_whole _first_mesh ;
    num_whole _current_row ;
    num_whole _current_col ;
} ;

template < typename mediator >
shy_logic_main_menu_meshes_creator < mediator > :: _logic_main_menu_meshes_creator_consts_type :: _logic_main_menu_meshes_creator_consts_type ( )
{
    platform_math :: make_num_fract ( color_r , 0 , 255 ) ;
    platform_math :: make_num_fract ( color_g , 255 , 255 ) ;
    platform_math :: make_num_fract ( color_b , 0 , 255 ) ;
    platform_math :: make_num_fract ( color_a , 255 , 255 ) ;
}

template < typename mediator >
shy_logic_main_menu_meshes_creator < mediator > :: shy_logic_main_menu_meshes_creator ( )
{
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_stateless_consts ( _logic_main_menu_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _current_row = _platform_math_consts . get ( ) . whole_0 ;
    _current_col = _platform_math_consts . get ( ) . whole_0 ;
    _first_mesh = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: logic_main_menu_letters_mesh_create_next )
{
    if ( platform_conditions :: whole_is_true ( _first_mesh ) )
    {
        _first_mesh = _platform_math_consts . get ( ) . whole_false ;
        _obtain_rows_count ( ) ;
    }
    else
        _move_to_next_col ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: logic_main_menu_letters_cols_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_cols_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_cols_state . requested_row , msg . row )
       )
    {
        _logic_main_menu_cols_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_cols_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_cols_state . cols = msg . cols ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: logic_main_menu_letters_rows_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_rows_state . requested ) )
    {
        _logic_main_menu_letters_rows_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_rows_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_rows_state . rows = msg . rows ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: logic_main_menu_letter_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letter_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letter_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letter_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_letter_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letter_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letter_state . letter = msg . letter ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . requested ) )
    {
        _engine_render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_mesh_create_state . mesh = msg . mesh ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: receive ( typename messages :: logic_text_letter_big_tex_coords_reply msg )
{
    num_whole letters_are_equal ;
    logic_text_stateless :: are_letters_equal ( letters_are_equal , _logic_text_letter_big_tex_coords_state . requested_letter , msg . letter ) ;
    if ( platform_conditions :: whole_is_true ( _logic_text_letter_big_tex_coords_state . requested )
      && platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        _logic_text_letter_big_tex_coords_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_text_letter_big_tex_coords_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_text_letter_big_tex_coords_state . bottom = msg . bottom ;
        _logic_text_letter_big_tex_coords_state . left = msg . left ;
        _logic_text_letter_big_tex_coords_state . top = msg . top ;
        _logic_text_letter_big_tex_coords_state . right = msg . right ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_rows_state . replied ) )
    {
        _logic_main_menu_letters_rows_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _start_first_row ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_cols_state . replied ) )
    {
        _logic_main_menu_cols_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _start_first_col ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letter_state . replied ) )
    {
        _logic_main_menu_letter_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _letter_state_received ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . replied ) )
    {
        _engine_render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_tex_coords ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_text_letter_big_tex_coords_state . replied ) )
    {
        _logic_text_letter_big_tex_coords_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _letter_tex_coords_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _obtain_rows_count ( )
{
    _logic_main_menu_letters_rows_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_rows_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _start_first_row ( )
{
    _current_row = _platform_math_consts . get ( ) . whole_minus_1 ;
    _move_to_next_row ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _start_first_col ( )
{
    _current_col = _platform_math_consts . get ( ) . whole_minus_1 ;
    _move_to_next_col ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _move_to_next_row ( )
{
    platform_math :: inc_whole ( _current_row ) ;
    if ( platform_conditions :: whole_less_than_whole ( _current_row , _logic_main_menu_letters_rows_state . rows ) )
    {
        _logic_main_menu_cols_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_cols_state . requested_row = _current_row ;
        typename messages :: logic_main_menu_letters_cols_request msg ;
        msg . row = _current_row ;
        _mediator . get ( ) . send ( msg ) ;
    }
    else
    {
        _logic_main_menu_cols_state . cols = _platform_math_consts . get ( ) . whole_0 ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_creation_finished ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _move_to_next_col ( )
{
    platform_math :: inc_whole ( _current_col ) ;
    if ( platform_conditions :: whole_less_than_whole ( _current_col , _logic_main_menu_cols_state . cols ) )
    {
        _logic_main_menu_letter_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letter_state . requested_row = _current_row ;
        _logic_main_menu_letter_state . requested_col = _current_col ;
        typename messages :: logic_main_menu_letter_request msg ;
        msg . row = _current_row ;
        msg . col = _current_col ;
        _mediator . get ( ) . send ( msg ) ;
    }
    else
        _move_to_next_row ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _letter_state_received ( )
{
    num_whole letter_is_whitespace ;
    logic_text_letter_id whitespace ;
    typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > logic_text_stateless_consts ;
    
    _mediator . get ( ) . logic_text_stateless_consts ( logic_text_stateless_consts ) ;
    whitespace = logic_text_stateless_consts . get ( ) . whitespace ;
    
    logic_text_stateless :: are_letters_equal ( letter_is_whitespace , _logic_main_menu_letter_state . letter , whitespace ) ;
    if ( platform_conditions :: whole_is_false ( letter_is_whitespace ) )
        _create_mesh ( ) ;
    else
        _move_to_next_col ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _create_mesh ( )
{
    _engine_render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_create_request msg ;
    msg . vertices = _platform_math_consts . get ( ) . whole_4 ;
    msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_4 ;
    msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _obtain_tex_coords ( )
{
    _logic_text_letter_big_tex_coords_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_text_letter_big_tex_coords_state . requested_letter = _logic_main_menu_letter_state . letter ;
    typename messages :: logic_text_letter_big_tex_coords_request msg ;
    msg . letter = _logic_main_menu_letter_state . letter ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _letter_tex_coords_received ( )
{
    _fill_mesh_content ( ) ;
    _send_mesh_created_notification ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _send_mesh_created_notification ( )
{
    typename messages :: logic_main_menu_letters_mesh_has_been_created msg ;
    msg . row = _current_row ;
    msg . col = _current_col ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _fill_mesh_content ( )
{
    engine_render_mesh_id mesh ;
    num_fract half_size ;
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_bottom ;
    num_fract y_top ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_bottom ;
    num_fract v_top ;
    num_fract z ;
    num_fract color_r ;
    num_fract color_g ;
    num_fract color_b ;
    num_fract color_a ;
    num_whole index_left_top ;
    num_whole index_left_bottom ;
    num_whole index_right_top ;
    num_whole index_right_bottom ;
    
    mesh = _engine_render_mesh_create_state . mesh ;
    
    platform_math :: div_fracts ( half_size , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: mul_fracts ( x_left , half_size , _platform_math_consts . get ( ) . fract_minus_1 ) ;
    platform_math :: mul_fracts ( y_bottom , half_size , _platform_math_consts . get ( ) . fract_minus_1 ) ;
    platform_math :: mul_fracts ( x_right , half_size , _platform_math_consts . get ( ) . fract_1 ) ;
    platform_math :: mul_fracts ( y_top , half_size , _platform_math_consts . get ( ) . fract_1 ) ;
    z = _platform_math_consts . get ( ) . fract_0 ;
    
    u_left = _logic_text_letter_big_tex_coords_state . left ;
    u_right = _logic_text_letter_big_tex_coords_state . right ;
    v_bottom = _logic_text_letter_big_tex_coords_state . bottom ;
    v_top = _logic_text_letter_big_tex_coords_state . top ;
    
    color_r = _logic_main_menu_meshes_creator_consts . color_r ;
    color_g = _logic_main_menu_meshes_creator_consts . color_g ;
    color_b = _logic_main_menu_meshes_creator_consts . color_b ;
    color_a = _logic_main_menu_meshes_creator_consts . color_a ;

    index_left_top = _platform_math_consts . get ( ) . whole_0 ;
    index_left_bottom = _platform_math_consts . get ( ) . whole_1 ;
    index_right_top = _platform_math_consts . get ( ) . whole_2 ;
    index_right_bottom = _platform_math_consts . get ( ) . whole_3 ;
    
    _mesh_set_triangle_strip_index_value ( mesh , index_left_top , index_left_top ) ;
    _mesh_set_vertex_color               ( mesh , index_left_top , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( mesh , index_left_top , u_left , v_top ) ;
    _mesh_set_vertex_position            ( mesh , index_left_top , x_left , y_top , z ) ;

    _mesh_set_triangle_strip_index_value ( mesh , index_left_bottom , index_left_bottom ) ;
    _mesh_set_vertex_color               ( mesh , index_left_bottom , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( mesh , index_left_bottom , u_left , v_bottom ) ;
    _mesh_set_vertex_position            ( mesh , index_left_bottom , x_left , y_bottom , z ) ;

    _mesh_set_triangle_strip_index_value ( mesh , index_right_top , index_right_top ) ;
    _mesh_set_vertex_color               ( mesh , index_right_top , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( mesh , index_right_top , u_right , v_top ) ;
    _mesh_set_vertex_position            ( mesh , index_right_top , x_right , y_top , z ) ;

    _mesh_set_triangle_strip_index_value ( mesh , index_right_bottom , index_right_bottom ) ;
    _mesh_set_vertex_color               ( mesh , index_right_bottom , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( mesh , index_right_bottom , u_right , v_bottom ) ;
    _mesh_set_vertex_position            ( mesh , index_right_bottom , x_right , y_bottom , z ) ;
    
    typename messages :: engine_render_mesh_finalize finalize_msg ;
    finalize_msg . mesh = mesh ;
    _mediator . get ( ) . send ( finalize_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _mesh_set_vertex_position ( engine_render_mesh_id mesh , num_whole offset , num_fract x , num_fract y , num_fract z )
{
    typename messages :: engine_render_mesh_set_vertex_position msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _mesh_set_vertex_tex_coord ( engine_render_mesh_id mesh , num_whole offset , num_fract u , num_fract v )
{
    typename messages :: engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _mesh_set_vertex_color ( engine_render_mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    typename messages :: engine_render_mesh_set_vertex_color msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_creator < mediator > :: _mesh_set_triangle_strip_index_value ( engine_render_mesh_id mesh , num_whole offset , num_whole index )
{
    typename messages :: engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}
