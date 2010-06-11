template < typename mediator >
class shy_logic_title
{
    typedef typename mediator :: alphabet_english alphabet_english ;
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
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
    void set_mediator ( mediator * arg_mediator ) ;
    void receive ( typename messages :: title_done msg ) ;
    void title_render ( ) ;
    void title_update ( ) ;
    void title_launch_permit ( ) ;
private :
    void _title_create ( ) ;
    void _title_render ( ) ;
    void _title_update ( ) ;
    void _add_letter ( letter_id letter ) ;
    void _bake_letters ( ) ;
private :
    mediator * _mediator ;
    num_whole _title_launch_permitted ;
    num_whole _title_created ;
    num_whole _title_finished ;
    num_whole _title_frames ;
    num_whole _title_appeared ;
    num_whole _letters_count ;
    num_whole _disappear_at_frames ;
    num_fract _desired_pos_radius_coeff ;
    num_fract _desired_pos_angle ;
    num_fract _desired_rot_angle ;
    num_fract _desired_scale ;
    num_fract _scene_scale ;
    num_fract _scene_scale_frames ;
    num_fract _rubber_first ;
    num_fract _rubber_last ;
    typename platform :: template static_array < _letter_state , _max_letters > _letters ;
} ;

template < typename mediator >
shy_logic_title < mediator > :: shy_logic_title ( )
: _mediator ( 0 )
{
    platform :: math_make_num_whole ( _title_launch_permitted , false ) ;
    platform :: math_make_num_whole ( _title_finished , false ) ;
    platform :: math_make_num_whole ( _title_created , false ) ;
    platform :: math_make_num_whole ( _title_appeared , false ) ;
    platform :: math_make_num_whole ( _disappear_at_frames , 0 ) ;
    platform :: math_make_num_fract ( _scene_scale , 1 , 1 ) ;
    platform :: math_make_num_fract ( _scene_scale_frames , 0 , 1 ) ;
    _letters_count = platform :: whole_0 ;
    _title_frames = platform :: whole_0 ;
}

template < typename mediator >
void shy_logic_title < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_title < mediator > :: receive ( typename messages :: title_done msg ) 
{
    if ( platform :: condition_true ( _title_created ) )
    {
        for ( num_whole i = platform :: whole_0
            ; platform :: condition_whole_less_than_whole ( i , _letters_count )
            ; platform :: math_inc_whole ( i )
            )
        {
            _letter_state & letter = platform :: array_element ( _letters , i ) ;
            _mediator -> mesh_delete ( letter . mesh ) ;
        }
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: title_render ( )
{
    platform :: render_clear_screen ( platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: render_disable_depth_test ( ) ;
    platform :: render_fog_disable ( ) ;
    _mediator -> use_ortho_projection ( ) ;
    _mediator -> send ( typename messages :: fidget_render ( ) ) ;
    if ( platform :: condition_true ( _title_created ) && platform :: condition_false ( _title_finished ) )
        _title_render ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: title_launch_permit ( )
{
    platform :: math_make_num_whole ( _title_launch_permitted , true ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: title_update ( )
{
    if ( platform :: condition_true ( _title_launch_permitted ) )
    {
        if ( platform :: condition_false ( _title_created ) )
        {
            _title_create ( ) ;
            platform :: math_make_num_whole ( _title_created , true ) ;
            
            platform :: math_make_num_fract ( _desired_pos_radius_coeff , _spin_radius_in_letters , 1 ) ;
            platform :: math_make_num_fract ( _desired_pos_angle , 11 , 2 ) ;
            platform :: math_mul_fract_by ( _desired_pos_angle , platform :: fract_pi ) ;
            platform :: math_mul_fracts ( _desired_rot_angle , platform :: fract_2pi , platform :: fract_3 ) ;
            platform :: math_make_num_fract ( _desired_scale , 1 , 1 ) ;    
            platform :: math_make_num_fract ( _rubber_first , 19 , 20 ) ;
            platform :: math_make_num_fract ( _rubber_last , 19 , 20 ) ;
            platform :: math_make_num_whole ( _disappear_at_frames , 9999 ) ;
        }
    }
    if ( platform :: condition_true ( _title_created ) && platform :: condition_false ( _title_finished ) )
    {
        if ( platform :: condition_false ( _title_appeared ) )
        {
            num_whole whole_appear_duration_in_frames ;
            platform :: math_make_num_whole ( whole_appear_duration_in_frames , _appear_duration_in_frames ) ;
            platform :: math_inc_whole ( _title_frames ) ;
            if ( platform :: condition_whole_greater_than_whole ( _title_frames , whole_appear_duration_in_frames ) )
            {
                _title_frames = platform :: whole_0 ;
                platform :: math_make_num_fract ( _desired_pos_radius_coeff , 0 , 1 ) ;
                platform :: math_make_num_fract ( _desired_pos_angle , 22 , 2 ) ;
                platform :: math_mul_fract_by ( _desired_pos_angle , platform :: fract_pi ) ;
                platform :: math_mul_fracts ( _desired_rot_angle , platform :: fract_2pi , platform :: fract_6 ) ;
                platform :: math_make_num_fract ( _desired_scale , 0 , 1 ) ;    
                platform :: math_make_num_whole ( _title_appeared , true ) ;
                platform :: math_make_num_fract ( _rubber_first , 59 , 60 ) ;
                platform :: math_make_num_fract ( _rubber_last , 29 , 30 ) ;
                platform :: math_make_num_whole ( _disappear_at_frames , _disappear_duration_in_frames ) ;
            }
            else
            {
                _title_update ( ) ;
            }
        }
        if ( platform :: condition_true ( _title_appeared ) )
        {
            num_whole whole_disappear_duration_in_frames ;
            platform :: math_make_num_whole ( whole_disappear_duration_in_frames , _disappear_duration_in_frames ) ;
            platform :: math_inc_whole ( _title_frames ) ;
            if ( platform :: condition_whole_greater_than_whole ( _title_frames , whole_disappear_duration_in_frames ) )
            {
                platform :: math_make_num_whole ( _title_finished , true ) ;
                _mediator -> send ( typename messages :: title_finished ( ) ) ;
            }
            else
            {
                _title_update ( ) ;
            }
        }
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_create ( )
{
    const alphabet_english & eng = _mediator -> text_alphabet_english ( ) ;
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
    _bake_letters ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_render ( )
{
    matrix_data scene_tm ;

    platform :: matrix_set_axis_x ( scene_tm , _scene_scale , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: matrix_set_axis_y ( scene_tm , platform :: fract_0 , _scene_scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_z ( scene_tm , platform :: fract_0 , platform :: fract_0 , platform :: fract_1 ) ;
    platform :: matrix_set_origin ( scene_tm , platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
    
    platform :: render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    _mediator -> use_text_texture ( ) ;
    platform :: render_matrix_load ( scene_tm ) ;
    
    for ( num_whole i = platform :: whole_0
        ; platform :: condition_whole_less_than_whole ( i , _letters_count )
        ; platform :: math_inc_whole ( i )
        )
    {
        _letter_state & letter = platform :: array_element ( _letters , i ) ;
        _mediator -> mesh_render ( letter . mesh ) ;
    }
    platform :: render_blend_disable ( ) ;
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
    
    platform :: render_get_aspect_width ( aspect_width ) ;
    platform :: math_make_fract_from_whole ( fract_letters_count , _letters_count ) ;
    platform :: math_div_fracts ( letter_size , aspect_width , fract_letters_count ) ;    
    platform :: math_mul_fracts ( desired_pos_radius , letter_size , _desired_pos_radius_coeff ) ;
    platform :: math_make_num_whole ( frames_between_letters , 5 ) ;
    platform :: math_make_num_fract ( offset_y , _spin_radius_in_letters , 1 ) ;
    platform :: math_mul_fract_by ( offset_y , letter_size ) ;
    platform :: math_make_num_fract ( fract_appear_duration_in_frames , _appear_duration_in_frames , 1 ) ;
    platform :: math_make_num_fract ( scale_min , 7 , 10 ) ;
    platform :: math_make_num_fract ( scale_max , 9 , 10 ) ;
    
    engine_math :: math_lerp 
        ( _scene_scale 
        , scale_min
        , platform :: fract_0 
        , scale_max 
        , fract_appear_duration_in_frames
        , _scene_scale_frames
        ) ;
    platform :: math_add_to_fract ( _scene_scale_frames , platform :: fract_1 ) ;
                    
    for ( num_whole i = platform :: whole_0
        ; platform :: condition_whole_less_than_whole ( i , _letters_count )
        ; platform :: math_inc_whole ( i )
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
        _letter_state & letter = platform :: array_element ( _letters , i ) ;
        
        platform :: math_make_fract_from_whole ( fract_i , i ) ;
        platform :: math_mul_fracts ( offset_x , aspect_width , platform :: fract_2 ) ;
        platform :: math_mul_fract_by ( offset_x , fract_i ) ;
        platform :: math_div_fract_by ( offset_x , fract_letters_count ) ;
        platform :: math_sub_from_fract ( offset_x , aspect_width ) ;
        platform :: math_add_to_fract ( offset_x , letter_size ) ;
        platform :: vector_xyz ( offset , offset_x , offset_y , platform :: fract_minus_3 ) ;        
        
        platform :: math_mul_wholes ( starting_frame , frames_between_letters , i ) ;
        platform :: math_sub_wholes ( finishing_frame , _disappear_at_frames , starting_frame ) ;
        if ( platform :: condition_whole_greater_than_whole ( _title_frames , starting_frame ) )
        {
            engine_math :: math_lerp ( rubber , _rubber_first , platform :: fract_0 , _rubber_last , fract_letters_count , fract_i ) ;
            
            platform :: math_mul_fracts ( pos_angle_old_part , letter . pos_angle , rubber ) ;
            platform :: math_sub_fracts ( pos_angle_new_part , platform :: fract_1 , rubber ) ;
            platform :: math_mul_fract_by ( pos_angle_new_part , _desired_pos_angle ) ;
            platform :: math_add_fracts ( letter . pos_angle , pos_angle_old_part , pos_angle_new_part ) ;
            
            platform :: math_mul_fracts ( pos_radius_old_part , letter . pos_radius , rubber ) ;
            platform :: math_sub_fracts ( pos_radius_new_part , platform :: fract_1 , rubber ) ;
            platform :: math_mul_fract_by ( pos_radius_new_part , desired_pos_radius ) ;
            platform :: math_add_fracts ( letter . pos_radius , pos_radius_old_part , pos_radius_new_part ) ;
            
            platform :: math_mul_fracts ( rot_angle_old_part , letter . rot_angle , rubber ) ;
            platform :: math_sub_fracts ( rot_angle_new_part , platform :: fract_1 , rubber ) ;
            platform :: math_mul_fract_by ( rot_angle_new_part , _desired_rot_angle ) ;
            platform :: math_add_fracts ( letter . rot_angle , rot_angle_old_part , rot_angle_new_part ) ;
            
            platform :: math_mul_fracts ( scale_old_part , letter . scale , rubber ) ;
            platform :: math_sub_fracts ( scale_new_part , platform :: fract_1 , rubber ) ;
            platform :: math_mul_fract_by ( scale_new_part , _desired_scale ) ;
            platform :: math_add_fracts ( letter . scale , scale_old_part , scale_new_part ) ;
        }
        
        platform :: math_sin ( rot_sin , letter . rot_angle ) ;
        platform :: math_cos ( rot_cos , letter . rot_angle ) ;
        platform :: math_neg_fract ( rot_neg_sin , rot_sin ) ;
        
        platform :: math_sin ( pos_sin , letter . pos_angle ) ;
        platform :: math_cos ( pos_cos , letter . pos_angle ) ;
        platform :: math_neg_fract ( pos_neg_sin , pos_sin ) ;
        
        platform :: vector_xyz ( pos , pos_cos , pos_sin , platform :: fract_0 ) ;
        platform :: vector_mul_by ( pos , letter . pos_radius ) ;
        
        if ( platform :: condition_whole_less_than_whole ( _title_frames , finishing_frame ) )
        {
            platform :: vector_xyz ( axis_x , rot_cos , rot_sin , platform :: fract_0 ) ;
            platform :: vector_xyz ( axis_y , rot_neg_sin , rot_cos , platform :: fract_0 ) ;
            platform :: vector_mul_by ( axis_x , letter . scale ) ;
            platform :: vector_mul_by ( axis_y , letter . scale ) ;
            platform :: vector_mul_by ( axis_x , letter_size ) ;
            platform :: vector_mul_by ( axis_y , letter_size ) ;
        }
        else
        {
            platform :: vector_xyz ( axis_x , platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
            platform :: vector_xyz ( axis_y , platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
        }
        
        platform :: vector_add ( origin , pos , offset ) ;
        
        platform :: matrix_set_axis_x ( tm , axis_x ) ;
        platform :: matrix_set_axis_y ( tm , axis_y ) ;
        platform :: matrix_set_axis_z ( tm , platform :: fract_0 , platform :: fract_0 , platform :: fract_1 ) ;
        platform :: matrix_set_origin ( tm , origin ) ;
        
        _mediator -> mesh_set_transform ( letter . mesh , tm ) ;
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _add_letter ( letter_id letter )
{
    platform :: array_element ( _letters , _letters_count ) . letter = letter ;
    platform :: math_inc_whole ( _letters_count ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _bake_letters ( )
{
    typename platform :: template static_array < vertex_data , 4 > vertices ;
    typename platform :: template static_array < index_data , 4 > indices ;
    
    num_fract title_r = platform :: fract_0 ;
    num_fract title_g = platform :: fract_1 ;
    num_fract title_b = platform :: fract_0 ;
    num_fract title_a = platform :: fract_1 ;
    
    {
        vertex_data & vertex = platform :: array_element ( vertices , platform :: whole_0 ) ;
        index_data & index = platform :: array_element ( indices , platform :: whole_0 ) ;
        platform :: render_set_index_value ( index , platform :: whole_0 ) ;
        platform :: render_set_vertex_color ( vertex , title_r , title_g , title_b , title_a ) ;
        platform :: render_set_vertex_position 
            ( vertex 
            , platform :: fract_minus_1 
            , platform :: fract_1 
            , platform :: fract_0 
            ) ;
    }
    
    {
        vertex_data & vertex = platform :: array_element ( vertices , platform :: whole_1 ) ;
        index_data & index = platform :: array_element ( indices , platform :: whole_1 ) ;
        platform :: render_set_index_value ( index , platform :: whole_1 ) ;
        platform :: render_set_vertex_color ( vertex , title_r , title_g , title_b , title_a ) ;
        platform :: render_set_vertex_position 
            ( vertex 
            , platform :: fract_minus_1 
            , platform :: fract_minus_1 
            , platform :: fract_0 
            ) ;
    }
    
    {
        vertex_data & vertex = platform :: array_element ( vertices , platform :: whole_2 ) ;
        index_data & index = platform :: array_element ( indices , platform :: whole_2 ) ;
        platform :: render_set_index_value ( index , platform :: whole_2 ) ;
        platform :: render_set_vertex_color ( vertex , title_r , title_g , title_b , title_a ) ;
        platform :: render_set_vertex_position 
            ( vertex 
            , platform :: fract_1 
            , platform :: fract_1 
            , platform :: fract_0 
            ) ;
    }
    
    {
        vertex_data & vertex = platform :: array_element ( vertices , platform :: whole_3 ) ;
        index_data & index = platform :: array_element ( indices , platform :: whole_3 ) ;
        platform :: render_set_index_value ( index , platform :: whole_3 ) ;
        platform :: render_set_vertex_color ( vertex , title_r , title_g , title_b , title_a ) ;
        platform :: render_set_vertex_position 
            ( vertex 
            , platform :: fract_1 
            , platform :: fract_minus_1 
            , platform :: fract_0 
            ) ;
    }
    
    for ( num_whole i = platform :: whole_0
        ; platform :: condition_whole_less_than_whole ( i , _letters_count )
        ; platform :: math_inc_whole ( i )
        )
    {
        num_fract tex_left ;
        num_fract tex_bottom ;
        num_fract tex_right ;
        num_fract tex_top ;
        _letter_state & letter = platform :: array_element ( _letters , i ) ;
        letter . scale = platform :: fract_0 ;
        letter . pos_radius = platform :: fract_0 ;
        letter . pos_angle = platform :: fract_0 ;
        letter . rot_angle = platform :: fract_0 ;
        _mediator -> get_big_letter_tex_coords ( tex_left , tex_bottom , tex_right , tex_top , letter . letter ) ;
        platform :: render_set_vertex_tex_coord 
            ( platform :: array_element ( vertices , platform :: whole_0 )
            , tex_left
            , tex_top
            ) ;
        platform :: render_set_vertex_tex_coord 
            ( platform :: array_element ( vertices , platform :: whole_1 )
            , tex_left
            , tex_bottom
            ) ;
        platform :: render_set_vertex_tex_coord 
            ( platform :: array_element ( vertices , platform :: whole_2 )
            , tex_right
            , tex_top
            ) ;
        platform :: render_set_vertex_tex_coord 
            ( platform :: array_element ( vertices , platform :: whole_3 )
            , tex_right
            , tex_bottom
            ) ;
        _mediator -> mesh_create
            ( letter . mesh
            , vertices 
            , indices 
            , indices
            , platform :: whole_4 
            , platform :: whole_4 
            , platform :: whole_0 
            ) ;
    }
}
