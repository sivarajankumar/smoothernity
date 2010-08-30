template < typename mediator >
class shy_logic_title
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
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
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
    
    class _logic_title_consts_type
    {
    public :
        _logic_title_consts_type ( ) ;
        
        num_fract appear_pos_angle_periods ;
        num_fract appear_rubber_first ;
        num_fract appear_rubber_last ;
        num_whole appear_duration_in_frames ;
        
        num_fract disappear_pos_angle_periods ;
        num_fract disappear_rubber_first ;
        num_fract disappear_rubber_last ;
        num_whole disappear_duration_in_frames ;

        num_fract scene_scale_min ;
        num_fract scene_scale_max ;
        
        num_fract spin_radius_in_letters ;
        num_whole frames_between_letters ;
        num_whole never ;
        static const_int_32 max_letters = 32 ;
    } ;
    
    class _letter_state
    {
    public :
        num_fract pos_radius ;
        num_fract pos_angle ;
        num_fract rot_angle ;
        num_fract scale ;
        engine_render_mesh_id mesh ;
        logic_text_letter_id letter ;
    } ;
    
public :
    shy_logic_title ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_title_render ) ;
    void receive ( typename messages :: logic_title_update ) ;
    void receive ( typename messages :: logic_title_launch_permit ) ;
    void receive ( typename messages :: logic_text_letter_big_tex_coords_reply ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
    void receive ( typename messages :: logic_core_use_ortho_projection_reply ) ;
    void receive ( typename messages :: logic_fidget_render_reply ) ;
    void receive ( typename messages :: logic_text_use_text_texture_reply ) ;
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    shy_logic_title < mediator > & operator= ( const shy_logic_title < mediator > & ) ;
    void _title_create ( ) ;
    void _title_render ( ) ;
    void _title_update ( ) ;
    void _delete_all_meshes ( ) ;
    void _add_letter ( logic_text_letter_id ) ;
    void _prepare_to_appear ( ) ;
    void _prepare_to_disappear ( ) ;
    void _animate_appear ( ) ;
    void _animate_disappear ( ) ;
    void _animate_lifecycle ( ) ;
    void _bake_next_letter ( ) ;
    void _proceed_with_render ( ) ;
    void _proceed_with_letter_creation ( ) ;
    void _mesh_set_vertex_position ( engine_render_mesh_id mesh , num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( engine_render_mesh_id mesh , num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( engine_render_mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( engine_render_mesh_id mesh , num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_static_array :: template static_array < _letter_state , _logic_title_consts_type :: max_letters > _letters ;
    const _logic_title_consts_type _logic_title_consts ;
    num_whole _title_launch_permitted ;
    num_whole _title_created ;
    num_whole _title_finished ;
    num_whole _title_frames ;
    num_whole _title_appeared ;
    num_whole _letters_count ;
    num_whole _disappear_at_frames ;
    num_whole _bake_letter_index ;

    num_whole _render_started ;
    
    num_whole _mesh_create_requested ;
    num_whole _mesh_create_replied ;
    
    num_whole _use_ortho_projection_requested ;
    num_whole _use_ortho_projection_replied ;
    
    num_whole _fidget_render_requested ;
    num_whole _fidget_render_replied ;

    num_whole _use_text_texture_requested ;
    num_whole _use_text_texture_replied ;
    
    num_whole _text_letter_big_tex_coords_requested ;
    num_whole _text_letter_big_tex_coords_replied ;
    logic_text_letter_id _text_letter_big_tex_coords_letter ;
    
    num_whole _render_aspect_requested ;
    num_fract _render_aspect_width ;
    
    num_fract _tex_coords_left ;
    num_fract _tex_coords_right ;
    num_fract _tex_coords_bottom ;
    num_fract _tex_coords_top ;
    
    num_fract _desired_pos_radius_coeff ;
    num_fract _desired_pos_angle ;
    num_fract _desired_rot_angle ;
    num_fract _desired_scale ;
    num_fract _scene_scale ;
    num_fract _scene_scale_frames ;
    num_fract _rubber_first ;
    num_fract _rubber_last ;
} ;

template < typename mediator >
shy_logic_title < mediator > :: shy_logic_title ( )
{
}

template < typename mediator >
shy_logic_title < mediator > :: _logic_title_consts_type :: _logic_title_consts_type ( )
{
    platform_math :: make_num_fract ( appear_pos_angle_periods , 11 , 2 ) ;
    platform_math :: make_num_fract ( appear_rubber_first , 19 , 20 ) ;
    platform_math :: make_num_fract ( appear_rubber_last , 19 , 20 ) ;
    platform_math :: make_num_whole ( appear_duration_in_frames , 250 ) ;

    platform_math :: make_num_fract ( disappear_pos_angle_periods , 22 , 2 ) ;
    platform_math :: make_num_fract ( disappear_rubber_first , 59 , 60 ) ;
    platform_math :: make_num_fract ( disappear_rubber_last , 29 , 30 ) ;
    platform_math :: make_num_whole ( disappear_duration_in_frames , 150 ) ;

    platform_math :: make_num_fract ( scene_scale_min , 7 , 10 ) ;
    platform_math :: make_num_fract ( scene_scale_max , 9 , 10 ) ;
    
    platform_math :: make_num_fract ( spin_radius_in_letters , 2 , 1 ) ;
    platform_math :: make_num_whole ( frames_between_letters , 5 ) ;
    platform_math :: make_num_whole ( never , 9999 ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: init ) 
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _title_launch_permitted = _platform_math_consts . get ( ) . whole_false ;
    _title_finished = _platform_math_consts . get ( ) . whole_false ;
    _title_created = _platform_math_consts . get ( ) . whole_false ;
    _title_appeared = _platform_math_consts . get ( ) . whole_false ;
    _disappear_at_frames = _platform_math_consts . get ( ) . whole_0 ;
    _scene_scale = _platform_math_consts . get ( ) . fract_1 ;
    _scene_scale_frames = _platform_math_consts . get ( ) . fract_0 ;
    _letters_count = _platform_math_consts . get ( ) . whole_0 ;
    _title_frames = _platform_math_consts . get ( ) . whole_0 ;
    _bake_letter_index = _platform_math_consts . get ( ) . whole_0 ;
    _text_letter_big_tex_coords_requested = _platform_math_consts . get ( ) . whole_false ;
    _text_letter_big_tex_coords_replied = _platform_math_consts . get ( ) . whole_false ;
    _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
    _mesh_create_replied = _platform_math_consts . get ( ) . whole_false ;
    _use_ortho_projection_requested = _platform_math_consts . get ( ) . whole_false ;
    _use_ortho_projection_replied = _platform_math_consts . get ( ) . whole_false;
    _fidget_render_requested = _platform_math_consts . get ( ) . whole_false ;
    _fidget_render_replied = _platform_math_consts . get ( ) . whole_false ;
    _use_text_texture_requested = _platform_math_consts . get ( ) . whole_false ;
    _use_text_texture_replied = _platform_math_consts . get ( ) . whole_false ;
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
    _render_started = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_title < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_title_render )
{
    _render_started = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_render ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_core_use_ortho_projection_reply )
{
    if ( platform_conditions :: whole_is_true ( _use_ortho_projection_requested ) )
    {
        _use_ortho_projection_requested = _platform_math_consts . get ( ) . whole_false ;
        _use_ortho_projection_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_title_launch_permit )
{
    _title_launch_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_title_update )
{
    if ( platform_conditions :: whole_is_true ( _title_launch_permitted ) )
    {
        _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: engine_render_aspect_request ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: engine_render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _render_aspect_requested ) )
    {
        _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
        _render_aspect_width = msg . width ;
        if ( platform_conditions :: whole_is_false ( _title_created ) )
            _title_create ( ) ;
        else if ( platform_conditions :: whole_is_false ( _title_finished ) )
            _animate_lifecycle ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
        _mesh_create_replied = _platform_math_consts . get ( ) . whole_true ;
        typename platform_pointer :: template pointer < _letter_state > letter ;
        platform_static_array :: element_ptr ( letter , _letters , _bake_letter_index ) ;
        letter . get ( ) . mesh = msg . mesh ;
        _proceed_with_letter_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_text_letter_big_tex_coords_reply msg )
{
    num_whole letters_are_equal ;
    logic_text_stateless :: are_letters_equal ( letters_are_equal , _text_letter_big_tex_coords_letter , msg . letter ) ;
    if ( platform_conditions :: whole_is_true ( _text_letter_big_tex_coords_requested ) 
      && platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        _text_letter_big_tex_coords_requested = _platform_math_consts . get ( ) . whole_false ;
        _text_letter_big_tex_coords_replied = _platform_math_consts . get ( ) . whole_true ;
        _tex_coords_left = msg . left ;
        _tex_coords_right = msg . right ;
        _tex_coords_bottom = msg . bottom ;
        _tex_coords_top = msg . top ;
        _proceed_with_letter_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_fidget_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _fidget_render_requested ) )
    {
        _fidget_render_requested = _platform_math_consts . get ( ) . whole_false ;
        _fidget_render_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: logic_text_use_text_texture_reply )
{
    if ( platform_conditions :: whole_is_true ( _use_text_texture_requested ) )
    {
        _use_text_texture_requested = _platform_math_consts . get ( ) . whole_false ;
        _use_text_texture_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _render_started ) )
    {
        _render_started = _platform_math_consts . get ( ) . whole_false ;
        _use_ortho_projection_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_core_use_ortho_projection_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _use_ortho_projection_replied ) )
    {
        _use_ortho_projection_replied = _platform_math_consts . get ( ) . whole_false ;
        typename messages :: engine_render_clear_screen clear_screen_msg ;
        clear_screen_msg . r = _platform_math_consts . get ( ) . fract_0 ;
        clear_screen_msg . g = _platform_math_consts . get ( ) . fract_0 ;
        clear_screen_msg . b = _platform_math_consts . get ( ) . fract_0 ;
        _mediator . get ( ) . send ( clear_screen_msg ) ;
        _mediator . get ( ) . send ( typename messages :: engine_render_disable_depth_test ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: engine_render_fog_disable ( ) ) ;

        _fidget_render_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_fidget_render_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _fidget_render_replied ) )
    {
        _fidget_render_replied = _platform_math_consts . get ( ) . whole_false ;
        if ( platform_conditions :: whole_is_true ( _title_created ) && platform_conditions :: whole_is_false ( _title_finished ) )
        {
            _use_text_texture_requested = _platform_math_consts . get ( ) . whole_true ;
            _mediator . get ( ) . send ( typename messages :: logic_text_use_text_texture_request ( ) ) ;
        }
    }
    if ( platform_conditions :: whole_is_true ( _use_text_texture_replied ) )
    {
        _use_text_texture_replied = _platform_math_consts . get ( ) . whole_false ;
        _title_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _proceed_with_letter_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_replied )
      && platform_conditions :: whole_is_true ( _text_letter_big_tex_coords_replied )
       )
    {
        _mesh_create_replied = _platform_math_consts . get ( ) . whole_false ;
        _text_letter_big_tex_coords_replied = _platform_math_consts . get ( ) . whole_false ;
                
        num_fract title_r = _platform_math_consts . get ( ) . fract_0 ;
        num_fract title_g = _platform_math_consts . get ( ) . fract_1 ;
        num_fract title_b = _platform_math_consts . get ( ) . fract_0 ;
        num_fract title_a = _platform_math_consts . get ( ) . fract_1 ;
        num_fract x_left = _platform_math_consts . get ( ) . fract_minus_1 ;
        num_fract x_right = _platform_math_consts . get ( ) . fract_1 ;
        num_fract y_bottom = _platform_math_consts . get ( ) . fract_minus_1 ;
        num_fract y_top = _platform_math_consts . get ( ) . fract_1 ;
        num_fract z = _platform_math_consts . get ( ) . fract_0 ;
        
        typename platform_pointer :: template pointer < _letter_state > letter ;
        platform_static_array :: element_ptr ( letter , _letters , _bake_letter_index ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 ) ;
        _mesh_set_vertex_color               ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_0 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_0 , _tex_coords_left , _tex_coords_top ) ;
        _mesh_set_vertex_position            ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_0 , x_left , y_top , z ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_1 , _platform_math_consts . get ( ) . whole_1 ) ;
        _mesh_set_vertex_color               ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_1 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_1 , _tex_coords_left , _tex_coords_bottom ) ;
        _mesh_set_vertex_position            ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_1 , x_left , y_bottom , z ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_2 , _platform_math_consts . get ( ) . whole_2 ) ;
        _mesh_set_vertex_color               ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_2 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_2 , _tex_coords_right , _tex_coords_top ) ;
        _mesh_set_vertex_position            ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_2 , x_right , y_top , z ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_3 , _platform_math_consts . get ( ) . whole_3 ) ;
        _mesh_set_vertex_color               ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_3 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_3 , _tex_coords_right , _tex_coords_bottom ) ;
        _mesh_set_vertex_position            ( letter . get ( ) . mesh , _platform_math_consts . get ( ) . whole_3 , x_right , y_bottom , z ) ;
        
        typename messages :: engine_render_mesh_finalize mesh_finalize_msg ;
        mesh_finalize_msg . mesh = letter . get ( ) . mesh ;
        _mediator . get ( ) . send ( mesh_finalize_msg ) ;
        
        platform_math :: inc_whole ( _bake_letter_index ) ;
        _bake_next_letter ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _animate_lifecycle ( )
{
    if ( platform_conditions :: whole_is_false ( _title_appeared ) )
        _animate_appear ( ) ;
    if ( platform_conditions :: whole_is_true ( _title_appeared ) )
        _animate_disappear ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _animate_appear ( )
{
    platform_math :: inc_whole ( _title_frames ) ;
    if ( platform_conditions :: whole_greater_than_whole ( _title_frames , _logic_title_consts . appear_duration_in_frames ) )
    {
        _title_frames = _platform_math_consts . get ( ) . whole_0 ;
        _prepare_to_disappear ( ) ;
    }
    else
        _title_update ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _animate_disappear ( )
{
    platform_math :: inc_whole ( _title_frames ) ;
    if ( platform_conditions :: whole_greater_than_whole ( _title_frames , _logic_title_consts . disappear_duration_in_frames ) )
    {
        _title_finished = _platform_math_consts . get ( ) . whole_true ;
        _delete_all_meshes ( ) ;
        _mediator . get ( ) . send ( typename messages :: logic_title_finished ( ) ) ;
    }
    else
        _title_update ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _prepare_to_appear ( )
{
    _desired_pos_angle = _logic_title_consts . appear_pos_angle_periods ;
    platform_math :: mul_fract_by ( _desired_pos_angle , _platform_math_consts . get ( ) . fract_pi ) ;
    platform_math :: mul_fracts ( _desired_rot_angle , _platform_math_consts . get ( ) . fract_2pi , _platform_math_consts . get ( ) . fract_3 ) ;
    _rubber_first = _logic_title_consts . appear_rubber_first ;
    _rubber_last = _logic_title_consts . appear_rubber_last ;
    _disappear_at_frames = _logic_title_consts . never ;
    _desired_scale = _platform_math_consts . get ( ) . fract_1 ;    
    _desired_pos_radius_coeff = _logic_title_consts . spin_radius_in_letters ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _prepare_to_disappear ( )
{
    _desired_pos_radius_coeff = _platform_math_consts . get ( ) . fract_0 ;
    _desired_pos_angle = _logic_title_consts . disappear_pos_angle_periods ;
    platform_math :: mul_fract_by ( _desired_pos_angle , _platform_math_consts . get ( ) . fract_pi ) ;
    platform_math :: mul_fracts ( _desired_rot_angle , _platform_math_consts . get ( ) . fract_2pi , _platform_math_consts . get ( ) . fract_6 ) ;
    _rubber_first = _logic_title_consts . disappear_rubber_first ;
    _rubber_last = _logic_title_consts . disappear_rubber_last ;
    _desired_scale = _platform_math_consts . get ( ) . fract_0 ;    
    _title_appeared = _platform_math_consts . get ( ) . whole_true ;
    _disappear_at_frames = _logic_title_consts . disappear_duration_in_frames ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_create ( )
{
    typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > logic_text_stateless_consts ;
    _mediator . get ( ) . logic_text_stateless_consts ( logic_text_stateless_consts ) ;
    const logic_text_alphabet_english_type & eng = logic_text_stateless_consts . get ( ) . alphabet_english ;
    _add_letter ( eng . S ) ;
    _add_letter ( eng . M ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . T ) ;
    _add_letter ( eng . H ) ;
    _add_letter ( eng . E ) ;
    _add_letter ( eng . R ) ;
    _add_letter ( eng . N ) ;
    _add_letter ( eng . I ) ;
    _add_letter ( eng . T ) ;
    _add_letter ( eng . Y ) ;
    _bake_next_letter ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_render ( )
{
    matrix_data scene_tm ;

    platform_matrix :: set_axis_x ( scene_tm , _scene_scale , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 ) ;
    platform_matrix :: set_axis_y ( scene_tm , _platform_math_consts . get ( ) . fract_0 , _scene_scale , _platform_math_consts . get ( ) . fract_0 ) ;
    platform_matrix :: set_axis_z ( scene_tm , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_1 ) ;
    platform_matrix :: set_origin ( scene_tm , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 ) ;
    
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    
    typename messages :: engine_render_matrix_load matrix_load_msg ;
    matrix_load_msg . matrix = scene_tm ;
    _mediator . get ( ) . send ( matrix_load_msg ) ;
    
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _letters_count )
        ; platform_math :: inc_whole ( i )
        )
    {
        typename platform_pointer :: template pointer < _letter_state > letter ;
        platform_static_array :: element_ptr ( letter , _letters , i ) ;
        typename messages :: engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = letter . get ( ) . mesh ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_disable ( ) ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_update ( )
{
    num_fract fract_letters_count ;
    num_fract letter_size ;
    num_fract desired_pos_radius ;
    num_fract offset_y ;
    num_fract fract_appear_duration_in_frames ;
    
    platform_math :: make_fract_from_whole ( fract_letters_count , _letters_count ) ;
    platform_math :: div_fracts ( letter_size , _render_aspect_width , fract_letters_count ) ;    
    platform_math :: mul_fracts ( desired_pos_radius , letter_size , _desired_pos_radius_coeff ) ;
    offset_y = _logic_title_consts . spin_radius_in_letters ;
    platform_math :: mul_fract_by ( offset_y , letter_size ) ;
    platform_math :: make_fract_from_whole ( fract_appear_duration_in_frames , _logic_title_consts . appear_duration_in_frames ) ;
    
    engine_math :: lerp 
        ( _scene_scale 
        , _logic_title_consts . scene_scale_min
        , _platform_math_consts . get ( ) . fract_0 
        , _logic_title_consts . scene_scale_max 
        , fract_appear_duration_in_frames
        , _scene_scale_frames
        ) ;
    platform_math :: add_to_fract ( _scene_scale_frames , _platform_math_consts . get ( ) . fract_1 ) ;
                    
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _letters_count )
        ; platform_math :: inc_whole ( i )
        )
    {
        num_fract offset_x ;
        num_fract fract_i ;
        num_fract rot_cos ;
        num_fract rot_sin ;
        num_fract rot_neg_sin ;
        num_fract pos_cos ;
        num_fract pos_sin ;
        num_fract pos_neg_sin ;
        num_fract rubber ;
        num_fract pos_radius_old_part ;
        num_fract pos_radius_new_part ;
        num_fract pos_angle_old_part ;
        num_fract pos_angle_new_part ;
        num_fract rot_angle_old_part ;
        num_fract rot_angle_new_part ;
        num_fract scale_old_part ;
        num_fract scale_new_part ;
        num_whole starting_frame ;
        num_whole finishing_frame ;
        vector_data axis_x ;
        vector_data axis_y ;
        vector_data origin ;
        vector_data offset ;
        vector_data pos ;
        matrix_data tm ;
        typename platform_pointer :: template pointer < _letter_state > letter ;
        
        platform_static_array :: element_ptr ( letter , _letters , i ) ;
        
        platform_math :: make_fract_from_whole ( fract_i , i ) ;
        platform_math :: mul_fracts ( offset_x , _render_aspect_width , _platform_math_consts . get ( ) . fract_2 ) ;
        platform_math :: mul_fract_by ( offset_x , fract_i ) ;
        platform_math :: div_fract_by ( offset_x , fract_letters_count ) ;
        platform_math :: sub_from_fract ( offset_x , _render_aspect_width ) ;
        platform_math :: add_to_fract ( offset_x , letter_size ) ;
        platform_vector :: xyz ( offset , offset_x , offset_y , _platform_math_consts . get ( ) . fract_minus_3 ) ;        
        
        platform_math :: mul_wholes ( starting_frame , _logic_title_consts . frames_between_letters , i ) ;
        platform_math :: sub_wholes ( finishing_frame , _disappear_at_frames , starting_frame ) ;
        if ( platform_conditions :: whole_greater_than_whole ( _title_frames , starting_frame ) )
        {
            engine_math :: lerp ( rubber , _rubber_first , _platform_math_consts . get ( ) . fract_0 , _rubber_last , fract_letters_count , fract_i ) ;
            
            platform_math :: mul_fracts ( pos_angle_old_part , letter . get ( ) . pos_angle , rubber ) ;
            platform_math :: sub_fracts ( pos_angle_new_part , _platform_math_consts . get ( ) . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( pos_angle_new_part , _desired_pos_angle ) ;
            platform_math :: add_fracts ( letter . get ( ) . pos_angle , pos_angle_old_part , pos_angle_new_part ) ;
            
            platform_math :: mul_fracts ( pos_radius_old_part , letter . get ( ) . pos_radius , rubber ) ;
            platform_math :: sub_fracts ( pos_radius_new_part , _platform_math_consts . get ( ) . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( pos_radius_new_part , desired_pos_radius ) ;
            platform_math :: add_fracts ( letter . get ( ) . pos_radius , pos_radius_old_part , pos_radius_new_part ) ;
            
            platform_math :: mul_fracts ( rot_angle_old_part , letter . get ( ) . rot_angle , rubber ) ;
            platform_math :: sub_fracts ( rot_angle_new_part , _platform_math_consts . get ( ) . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( rot_angle_new_part , _desired_rot_angle ) ;
            platform_math :: add_fracts ( letter . get ( ) . rot_angle , rot_angle_old_part , rot_angle_new_part ) ;
            
            platform_math :: mul_fracts ( scale_old_part , letter . get ( ) . scale , rubber ) ;
            platform_math :: sub_fracts ( scale_new_part , _platform_math_consts . get ( ) . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( scale_new_part , _desired_scale ) ;
            platform_math :: add_fracts ( letter . get ( ) . scale , scale_old_part , scale_new_part ) ;
        }
        
        platform_math :: sin ( rot_sin , letter . get ( ) . rot_angle ) ;
        platform_math :: cos ( rot_cos , letter . get ( ) . rot_angle ) ;
        platform_math :: neg_fract ( rot_neg_sin , rot_sin ) ;
        
        platform_math :: sin ( pos_sin , letter . get ( ) . pos_angle ) ;
        platform_math :: cos ( pos_cos , letter . get ( ) . pos_angle ) ;
        platform_math :: neg_fract ( pos_neg_sin , pos_sin ) ;
        
        platform_vector :: xyz ( pos , pos_cos , pos_sin , _platform_math_consts . get ( ) . fract_0 ) ;
        platform_vector :: mul_by ( pos , letter . get ( ) . pos_radius ) ;
        
        if ( platform_conditions :: whole_less_than_whole ( _title_frames , finishing_frame ) )
        {
            platform_vector :: xyz ( axis_x , rot_cos , rot_sin , _platform_math_consts . get ( ) . fract_0 ) ;
            platform_vector :: xyz ( axis_y , rot_neg_sin , rot_cos , _platform_math_consts . get ( ) . fract_0 ) ;
            platform_vector :: mul_by ( axis_x , letter . get ( ) . scale ) ;
            platform_vector :: mul_by ( axis_y , letter . get ( ) . scale ) ;
            platform_vector :: mul_by ( axis_x , letter_size ) ;
            platform_vector :: mul_by ( axis_y , letter_size ) ;
        }
        else
        {
            platform_vector :: xyz ( axis_x , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 ) ;
            platform_vector :: xyz ( axis_y , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 ) ;
        }
        
        platform_vector :: add ( origin , pos , offset ) ;
        
        platform_matrix :: set_axis_x ( tm , axis_x ) ;
        platform_matrix :: set_axis_y ( tm , axis_y ) ;
        platform_matrix :: set_axis_z ( tm , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_1 ) ;
        platform_matrix :: set_origin ( tm , origin ) ;
        
        {
            typename messages :: engine_render_mesh_set_transform mesh_set_transform_msg ;
            mesh_set_transform_msg . mesh = letter . get ( ) . mesh ;
            mesh_set_transform_msg . transform = tm ;
            _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
        }
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _delete_all_meshes ( )
{
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _letters_count )
        ; platform_math :: inc_whole ( i )
        )
    {
        typename platform_pointer :: template pointer < _letter_state > letter ;
        platform_static_array :: element_ptr ( letter , _letters , i ) ;
        typename messages :: engine_render_mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = letter . get ( ) . mesh ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _add_letter ( logic_text_letter_id letter )
{
    typename platform_pointer :: template pointer < _letter_state > letter_state ;
    platform_static_array :: element_ptr ( letter_state , _letters , _letters_count ) ;
    letter_state . get ( ) . letter = letter ;
    platform_math :: inc_whole ( _letters_count ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _bake_next_letter ( )
{
    if ( platform_conditions :: whole_less_than_whole ( _bake_letter_index , _letters_count ) )
    {
        typename platform_pointer :: template pointer < _letter_state > letter ;
        platform_static_array :: element_ptr ( letter , _letters , _bake_letter_index ) ;
        
        letter . get ( ) . scale = _platform_math_consts . get ( ) . fract_0 ;
        letter . get ( ) . pos_radius = _platform_math_consts . get ( ) . fract_0 ;
        letter . get ( ) . pos_angle = _platform_math_consts . get ( ) . fract_0 ;
        letter . get ( ) . rot_angle = _platform_math_consts . get ( ) . fract_0 ;
        
        _text_letter_big_tex_coords_requested = _platform_math_consts . get ( ) . whole_true ;
        _text_letter_big_tex_coords_letter = letter . get ( ) . letter ;
        
        _mesh_create_requested = _platform_math_consts . get ( ) . whole_true ;
        
        typename messages :: logic_text_letter_big_tex_coords_request text_letter_big_tex_coords_request_msg ;
        text_letter_big_tex_coords_request_msg . letter = letter . get ( ) . letter ;
        _mediator . get ( ) . send ( text_letter_big_tex_coords_request_msg  ) ;        
        
        typename messages :: engine_render_mesh_create_request mesh_create_msg ;
        mesh_create_msg . vertices = _platform_math_consts . get ( ) . whole_4 ;
        mesh_create_msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_4 ;
        mesh_create_msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
        _mediator . get ( ) . send ( mesh_create_msg ) ;
    }
    else
    {
        _title_created = _platform_math_consts . get ( ) . whole_true ;
        _prepare_to_appear ( ) ;
        _animate_lifecycle ( ) ;
        _mediator . get ( ) . send ( typename messages :: logic_title_created ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _mesh_set_vertex_position ( engine_render_mesh_id mesh , num_whole offset , num_fract x , num_fract y , num_fract z )
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
void shy_logic_title < mediator > :: _mesh_set_vertex_tex_coord ( engine_render_mesh_id mesh , num_whole offset , num_fract u , num_fract v )
{
    typename messages :: engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _mesh_set_vertex_color ( engine_render_mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
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
void shy_logic_title < mediator > :: _mesh_set_triangle_strip_index_value ( engine_render_mesh_id mesh , num_whole offset , num_whole index )
{
    typename messages :: engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}
