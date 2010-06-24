template < typename mediator >
class shy_logic_title
{
    typedef typename mediator :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: logic_text logic_text ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
    
    static const_int_32 _max_letters = 32 ;
    static const_int_32 _spin_radius_in_letters = 2 ;
    static const_int_32 _appear_duration_in_frames = 250 ;
    static const_int_32 _disappear_duration_in_frames = 150 ;
    
    class _letter_state
    {
    public :
        num_fract pos_radius ;
        num_fract pos_angle ;
        num_fract rot_angle ;
        num_fract scale ;
        mesh_id mesh ;
        letter_id letter ;
    } ;
    
public :
    shy_logic_title ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: title_done msg ) ;
    void receive ( typename messages :: title_render msg ) ;
    void receive ( typename messages :: title_update msg ) ;
    void receive ( typename messages :: title_launch_permit msg ) ;
    void receive ( typename messages :: text_letter_big_tex_coords_reply msg ) ;
private :
    void _title_create ( ) ;
    void _title_render ( ) ;
    void _title_update ( ) ;
    void _add_letter ( letter_id letter ) ;
    void _prepare_to_appear ( ) ;
    void _prepare_to_disappear ( ) ;
    void _animate_appear ( ) ;
    void _animate_disappear ( ) ;
    void _animate_lifecycle ( ) ;
    void _bake_next_letter ( ) ;
    void _mesh_set_vertex_position ( mesh_id mesh , num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( mesh_id mesh , num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( mesh_id mesh , num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_static_array :: template static_array < _letter_state , _max_letters > _letters ;
    num_whole _title_launch_permitted ;
    num_whole _title_created ;
    num_whole _title_finished ;
    num_whole _title_frames ;
    num_whole _title_appeared ;
    num_whole _letters_count ;
    num_whole _disappear_at_frames ;
    num_whole _bake_letter_index ;
    num_whole _text_letter_big_tex_coords_requested ;
    letter_id _text_letter_big_tex_coords_letter ;
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
    platform_math :: make_num_whole ( _title_launch_permitted , false ) ;
    platform_math :: make_num_whole ( _title_finished , false ) ;
    platform_math :: make_num_whole ( _title_created , false ) ;
    platform_math :: make_num_whole ( _title_appeared , false ) ;
    platform_math :: make_num_whole ( _disappear_at_frames , 0 ) ;
    platform_math :: make_num_fract ( _scene_scale , 1 , 1 ) ;
    platform_math :: make_num_fract ( _scene_scale_frames , 0 , 1 ) ;
    _letters_count = platform :: math_consts . whole_0 ;
    _title_frames = platform :: math_consts . whole_0 ;
    _bake_letter_index = platform :: math_consts . whole_0 ;
    _text_letter_big_tex_coords_requested = platform :: math_consts . whole_false ;
}

template < typename mediator >
void shy_logic_title < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: title_done msg ) 
{
    if ( platform_conditions :: whole_is_true ( _title_created ) )
    {
        for ( num_whole i = platform :: math_consts . whole_0
            ; platform_conditions :: whole_less_than_whole ( i , _letters_count )
            ; platform_math :: inc_whole ( i )
            )
        {
            _letter_state & letter = platform_static_array :: element ( _letters , i ) ;
            typename messages :: mesh_delete mesh_delete_msg ;
            mesh_delete_msg . mesh = letter . mesh ;
            _mediator . get ( ) . send ( mesh_delete_msg ) ;
        }
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: title_render msg )
{
    platform_render :: clear_screen ( platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    platform_render :: disable_depth_test ( ) ;
    platform_render :: fog_disable ( ) ;
    _mediator . get ( ) . send ( typename messages :: use_ortho_projection ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_render ( ) ) ;
    if ( platform_conditions :: whole_is_true ( _title_created ) && platform_conditions :: whole_is_false ( _title_finished ) )
        _title_render ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: title_launch_permit msg )
{
    platform_math :: make_num_whole ( _title_launch_permitted , true ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: title_update msg )
{
    if ( platform_conditions :: whole_is_true ( _title_launch_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _title_created ) )
            _title_create ( ) ;
        else if ( platform_conditions :: whole_is_false ( _title_finished ) )
            _animate_lifecycle ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: text_letter_big_tex_coords_reply msg )
{
    num_whole letters_are_equal ;
    logic_text :: are_letters_equal ( letters_are_equal , _text_letter_big_tex_coords_letter , msg . letter ) ;
    if ( platform_conditions :: whole_is_true ( _text_letter_big_tex_coords_requested ) 
      && platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        _text_letter_big_tex_coords_requested = platform :: math_consts . whole_false ;
        _letter_state & letter = platform_static_array :: element ( _letters , _bake_letter_index ) ;
        
        num_fract title_r = platform :: math_consts . fract_0 ;
        num_fract title_g = platform :: math_consts . fract_1 ;
        num_fract title_b = platform :: math_consts . fract_0 ;
        num_fract title_a = platform :: math_consts . fract_1 ;
        num_fract x_left = platform :: math_consts . fract_minus_1 ;
        num_fract x_right = platform :: math_consts . fract_1 ;
        num_fract y_bottom = platform :: math_consts . fract_minus_1 ;
        num_fract y_top = platform :: math_consts . fract_1 ;
        num_fract z = platform :: math_consts . fract_0 ;
        num_whole total_vertices = platform :: math_consts . whole_4 ;
        
        _mediator . get ( ) . mesh_create ( letter . mesh , total_vertices , total_vertices , platform :: math_consts . whole_0 ) ;

        _mesh_set_triangle_strip_index_value ( letter . mesh , platform :: math_consts . whole_0 , platform :: math_consts . whole_0 ) ;
        _mesh_set_vertex_color               ( letter . mesh , platform :: math_consts . whole_0 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . mesh , platform :: math_consts . whole_0 , msg . left , msg . top ) ;
        _mesh_set_vertex_position            ( letter . mesh , platform :: math_consts . whole_0 , x_left , y_top , z ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . mesh , platform :: math_consts . whole_1 , platform :: math_consts . whole_1 ) ;
        _mesh_set_vertex_color               ( letter . mesh , platform :: math_consts . whole_1 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . mesh , platform :: math_consts . whole_1 , msg . left , msg . bottom ) ;
        _mesh_set_vertex_position            ( letter . mesh , platform :: math_consts . whole_1 , x_left , y_bottom , z ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . mesh , platform :: math_consts . whole_2 , platform :: math_consts . whole_2 ) ;
        _mesh_set_vertex_color               ( letter . mesh , platform :: math_consts . whole_2 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . mesh , platform :: math_consts . whole_2 , msg . right , msg . top ) ;
        _mesh_set_vertex_position            ( letter . mesh , platform :: math_consts . whole_2 , x_right , y_top , z ) ;
        
        _mesh_set_triangle_strip_index_value ( letter . mesh , platform :: math_consts . whole_3 , platform :: math_consts . whole_3 ) ;
        _mesh_set_vertex_color               ( letter . mesh , platform :: math_consts . whole_3 , title_r , title_g , title_b , title_a ) ;
        _mesh_set_vertex_tex_coord           ( letter . mesh , platform :: math_consts . whole_3 , msg . right , msg . bottom ) ;
        _mesh_set_vertex_position            ( letter . mesh , platform :: math_consts . whole_3 , x_right , y_bottom , z ) ;
        
        typename messages :: mesh_finalize mesh_finalize_msg ;
        mesh_finalize_msg . mesh = letter . mesh ;
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
    num_whole whole_appear_duration_in_frames ;
    platform_math :: make_num_whole ( whole_appear_duration_in_frames , _appear_duration_in_frames ) ;
    platform_math :: inc_whole ( _title_frames ) ;
    if ( platform_conditions :: whole_greater_than_whole ( _title_frames , whole_appear_duration_in_frames ) )
    {
        _title_frames = platform :: math_consts . whole_0 ;
        _prepare_to_disappear ( ) ;
    }
    else
        _title_update ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _animate_disappear ( )
{
    num_whole whole_disappear_duration_in_frames ;
    platform_math :: make_num_whole ( whole_disappear_duration_in_frames , _disappear_duration_in_frames ) ;
    platform_math :: inc_whole ( _title_frames ) ;
    if ( platform_conditions :: whole_greater_than_whole ( _title_frames , whole_disappear_duration_in_frames ) )
    {
        platform_math :: make_num_whole ( _title_finished , true ) ;
        _mediator . get ( ) . send ( typename messages :: title_finished ( ) ) ;
    }
    else
        _title_update ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _prepare_to_appear ( )
{
    platform_math :: make_num_fract ( _desired_pos_radius_coeff , _spin_radius_in_letters , 1 ) ;
    platform_math :: make_num_fract ( _desired_pos_angle , 11 , 2 ) ;
    platform_math :: mul_fract_by ( _desired_pos_angle , platform :: math_consts . fract_pi ) ;
    platform_math :: mul_fracts ( _desired_rot_angle , platform :: math_consts . fract_2pi , platform :: math_consts . fract_3 ) ;
    platform_math :: make_num_fract ( _desired_scale , 1 , 1 ) ;    
    platform_math :: make_num_fract ( _rubber_first , 19 , 20 ) ;
    platform_math :: make_num_fract ( _rubber_last , 19 , 20 ) ;
    platform_math :: make_num_whole ( _disappear_at_frames , 9999 ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _prepare_to_disappear ( )
{
    platform_math :: make_num_fract ( _desired_pos_radius_coeff , 0 , 1 ) ;
    platform_math :: make_num_fract ( _desired_pos_angle , 22 , 2 ) ;
    platform_math :: mul_fract_by ( _desired_pos_angle , platform :: math_consts . fract_pi ) ;
    platform_math :: mul_fracts ( _desired_rot_angle , platform :: math_consts . fract_2pi , platform :: math_consts . fract_6 ) ;
    platform_math :: make_num_fract ( _desired_scale , 0 , 1 ) ;    
    platform_math :: make_num_whole ( _title_appeared , true ) ;
    platform_math :: make_num_fract ( _rubber_first , 59 , 60 ) ;
    platform_math :: make_num_fract ( _rubber_last , 29 , 30 ) ;
    platform_math :: make_num_whole ( _disappear_at_frames , _disappear_duration_in_frames ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_create ( )
{
    const alphabet_english_type & eng = _mediator . get ( ) . logic_text_consts ( ) . alphabet_english ;
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

    platform_matrix :: set_axis_x ( scene_tm , _scene_scale , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_y ( scene_tm , platform :: math_consts . fract_0 , _scene_scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_z ( scene_tm , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_1 ) ;
    platform_matrix :: set_origin ( scene_tm , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    
    platform_render :: blend_src_alpha_dst_one_minus_alpha ( ) ;
    _mediator . get ( ) . send ( typename messages :: use_text_texture ( ) ) ;
    platform_render :: matrix_load ( scene_tm ) ;
    
    for ( num_whole i = platform :: math_consts . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _letters_count )
        ; platform_math :: inc_whole ( i )
        )
    {
        _letter_state & letter = platform_static_array :: element ( _letters , i ) ;
        typename messages :: mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = letter . mesh ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
    platform_render :: blend_disable ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_update ( )
{
    num_fract fract_letters_count ;
    num_fract letter_size ;
    num_fract aspect_width ;
    num_fract desired_pos_radius ;
    num_fract offset_y ;
    num_fract fract_appear_duration_in_frames ;
    num_fract scale_min ;
    num_fract scale_max ;
    num_whole frames_between_letters ;
    
    platform_render :: get_aspect_width ( aspect_width ) ;
    platform_math :: make_fract_from_whole ( fract_letters_count , _letters_count ) ;
    platform_math :: div_fracts ( letter_size , aspect_width , fract_letters_count ) ;    
    platform_math :: mul_fracts ( desired_pos_radius , letter_size , _desired_pos_radius_coeff ) ;
    platform_math :: make_num_whole ( frames_between_letters , 5 ) ;
    platform_math :: make_num_fract ( offset_y , _spin_radius_in_letters , 1 ) ;
    platform_math :: mul_fract_by ( offset_y , letter_size ) ;
    platform_math :: make_num_fract ( fract_appear_duration_in_frames , _appear_duration_in_frames , 1 ) ;
    platform_math :: make_num_fract ( scale_min , 7 , 10 ) ;
    platform_math :: make_num_fract ( scale_max , 9 , 10 ) ;
    
    engine_math :: math_lerp 
        ( _scene_scale 
        , scale_min
        , platform :: math_consts . fract_0 
        , scale_max 
        , fract_appear_duration_in_frames
        , _scene_scale_frames
        ) ;
    platform_math :: add_to_fract ( _scene_scale_frames , platform :: math_consts . fract_1 ) ;
                    
    for ( num_whole i = platform :: math_consts . whole_0
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
        _letter_state & letter = platform_static_array :: element ( _letters , i ) ;
        
        platform_math :: make_fract_from_whole ( fract_i , i ) ;
        platform_math :: mul_fracts ( offset_x , aspect_width , platform :: math_consts . fract_2 ) ;
        platform_math :: mul_fract_by ( offset_x , fract_i ) ;
        platform_math :: div_fract_by ( offset_x , fract_letters_count ) ;
        platform_math :: sub_from_fract ( offset_x , aspect_width ) ;
        platform_math :: add_to_fract ( offset_x , letter_size ) ;
        platform_vector :: xyz ( offset , offset_x , offset_y , platform :: math_consts . fract_minus_3 ) ;        
        
        platform_math :: mul_wholes ( starting_frame , frames_between_letters , i ) ;
        platform_math :: sub_wholes ( finishing_frame , _disappear_at_frames , starting_frame ) ;
        if ( platform_conditions :: whole_greater_than_whole ( _title_frames , starting_frame ) )
        {
            engine_math :: math_lerp ( rubber , _rubber_first , platform :: math_consts . fract_0 , _rubber_last , fract_letters_count , fract_i ) ;
            
            platform_math :: mul_fracts ( pos_angle_old_part , letter . pos_angle , rubber ) ;
            platform_math :: sub_fracts ( pos_angle_new_part , platform :: math_consts . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( pos_angle_new_part , _desired_pos_angle ) ;
            platform_math :: add_fracts ( letter . pos_angle , pos_angle_old_part , pos_angle_new_part ) ;
            
            platform_math :: mul_fracts ( pos_radius_old_part , letter . pos_radius , rubber ) ;
            platform_math :: sub_fracts ( pos_radius_new_part , platform :: math_consts . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( pos_radius_new_part , desired_pos_radius ) ;
            platform_math :: add_fracts ( letter . pos_radius , pos_radius_old_part , pos_radius_new_part ) ;
            
            platform_math :: mul_fracts ( rot_angle_old_part , letter . rot_angle , rubber ) ;
            platform_math :: sub_fracts ( rot_angle_new_part , platform :: math_consts . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( rot_angle_new_part , _desired_rot_angle ) ;
            platform_math :: add_fracts ( letter . rot_angle , rot_angle_old_part , rot_angle_new_part ) ;
            
            platform_math :: mul_fracts ( scale_old_part , letter . scale , rubber ) ;
            platform_math :: sub_fracts ( scale_new_part , platform :: math_consts . fract_1 , rubber ) ;
            platform_math :: mul_fract_by ( scale_new_part , _desired_scale ) ;
            platform_math :: add_fracts ( letter . scale , scale_old_part , scale_new_part ) ;
        }
        
        platform_math :: sin ( rot_sin , letter . rot_angle ) ;
        platform_math :: cos ( rot_cos , letter . rot_angle ) ;
        platform_math :: neg_fract ( rot_neg_sin , rot_sin ) ;
        
        platform_math :: sin ( pos_sin , letter . pos_angle ) ;
        platform_math :: cos ( pos_cos , letter . pos_angle ) ;
        platform_math :: neg_fract ( pos_neg_sin , pos_sin ) ;
        
        platform_vector :: xyz ( pos , pos_cos , pos_sin , platform :: math_consts . fract_0 ) ;
        platform_vector :: mul_by ( pos , letter . pos_radius ) ;
        
        if ( platform_conditions :: whole_less_than_whole ( _title_frames , finishing_frame ) )
        {
            platform_vector :: xyz ( axis_x , rot_cos , rot_sin , platform :: math_consts . fract_0 ) ;
            platform_vector :: xyz ( axis_y , rot_neg_sin , rot_cos , platform :: math_consts . fract_0 ) ;
            platform_vector :: mul_by ( axis_x , letter . scale ) ;
            platform_vector :: mul_by ( axis_y , letter . scale ) ;
            platform_vector :: mul_by ( axis_x , letter_size ) ;
            platform_vector :: mul_by ( axis_y , letter_size ) ;
        }
        else
        {
            platform_vector :: xyz ( axis_x , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
            platform_vector :: xyz ( axis_y , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
        }
        
        platform_vector :: add ( origin , pos , offset ) ;
        
        platform_matrix :: set_axis_x ( tm , axis_x ) ;
        platform_matrix :: set_axis_y ( tm , axis_y ) ;
        platform_matrix :: set_axis_z ( tm , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_1 ) ;
        platform_matrix :: set_origin ( tm , origin ) ;
        
        {
            typename messages :: mesh_set_transform mesh_set_transform_msg ;
            mesh_set_transform_msg . mesh = letter . mesh ;
            mesh_set_transform_msg . transform = tm ;
            _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
        }
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _add_letter ( letter_id letter )
{
    platform_static_array :: element ( _letters , _letters_count ) . letter = letter ;
    platform_math :: inc_whole ( _letters_count ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _bake_next_letter ( )
{
    if ( platform_conditions :: whole_less_than_whole ( _bake_letter_index , _letters_count ) )
    {
        _letter_state & letter = platform_static_array :: element ( _letters , _bake_letter_index ) ;
        letter . scale = platform :: math_consts . fract_0 ;
        letter . pos_radius = platform :: math_consts . fract_0 ;
        letter . pos_angle = platform :: math_consts . fract_0 ;
        letter . rot_angle = platform :: math_consts . fract_0 ;
        _text_letter_big_tex_coords_requested = platform :: math_consts . whole_true ;
        _text_letter_big_tex_coords_letter = letter . letter ;
        typename messages :: text_letter_big_tex_coords_request text_letter_big_tex_coords_request_msg ;
        text_letter_big_tex_coords_request_msg . letter = letter . letter ;
        _mediator . get ( ) . send ( text_letter_big_tex_coords_request_msg  ) ;        
    }
    else
    {
        _title_created = platform :: math_consts . whole_true ;
        _prepare_to_appear ( ) ;
        _animate_lifecycle ( ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _mesh_set_vertex_position ( mesh_id mesh , num_whole offset , num_fract x , num_fract y , num_fract z )
{
    typename messages :: mesh_set_vertex_position msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _mesh_set_vertex_tex_coord ( mesh_id mesh , num_whole offset , num_fract u , num_fract v )
{
    typename messages :: mesh_set_vertex_tex_coord msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _mesh_set_vertex_color ( mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    _mediator . get ( ) . mesh_set_vertex_color ( mesh , offset , r , g , b , a ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _mesh_set_triangle_strip_index_value ( mesh_id mesh , num_whole offset , num_whole index )
{
    typename messages :: mesh_set_triangle_strip_index_value msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}
