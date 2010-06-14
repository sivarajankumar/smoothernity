template < typename mediator >
class shy_logic_entities
{
    typedef typename mediator :: engine_math engine_math ;
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
    
    static const_int_32 _grid_step = 5 ;
    static const_int_32 _scale_in_frames = 120 ;
    static const_int_32 _scale_wave = 2 ;
    static const_int_32 _entity_mesh_spans = 50 ;
    static const_int_32 _entity_mesh_grid = 5 ;
    static const_int_32 _entity_mesh_height = 2 ;
    static const_int_32 _entity_color_roof_r = 255 ;
    static const_int_32 _entity_color_roof_g = 255 ;
    static const_int_32 _entity_color_roof_b = 255 ;

public :
    shy_logic_entities ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void receive ( typename messages :: entities_done msg ) ;
    void receive ( typename messages :: entities_render msg ) ;
    void receive ( typename messages :: entities_prepare_permit msg ) ;
    void receive ( typename messages :: entities_update msg ) ;
    void get_entity_origin ( vector_data & result , num_whole index ) ;
    void get_entity_height ( num_fract & result ) ;
    void get_entity_mesh_grid ( num_whole & result ) ;
private :
    void _entities_render ( ) ;
    void _entity_color ( num_fract & r , num_fract & g , num_fract & b , num_fract & a , num_whole i ) ;
    void _create_entity_mesh ( ) ;
    void _get_entity_origin ( vector_data & result , num_whole index ) ;
    void _update_entity_grid ( ) ;
private :
    mediator * _mediator ;
    num_whole _entity_created ;
    num_whole _entities_prepare_permitted ;
    num_whole _grid_scale ;
    num_whole _current_strip_mesh_span ;
    num_whole _current_fan_mesh_span ;
    num_whole _strip_indices_count ;
    num_whole _fan_indices_count ;
    num_whole _vertices_count ;
    mesh_id _entity_mesh_id ;
    typename platform :: template static_array < matrix_data , _entity_mesh_grid * _entity_mesh_grid > _entities_grid_matrices ;
    typename platform :: template static_array < vertex_data , ( _entity_mesh_spans + 1 ) * 2 + 1 > _vertices ;
    typename platform :: template static_array < index_data , ( _entity_mesh_spans + 1 ) * 2 > _strip_indices ;
    typename platform :: template static_array < index_data , _entity_mesh_spans + 2 > _fan_indices ;
} ;

template < typename mediator >
shy_logic_entities < mediator > :: shy_logic_entities ( )
: _mediator ( 0 )
{
    platform :: math_make_num_whole ( _entity_created , false ) ;
    platform :: math_make_num_whole ( _entities_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _grid_scale , 0 ) ;
    platform :: math_make_num_whole ( _current_strip_mesh_span , 0 ) ;
    platform :: math_make_num_whole ( _current_fan_mesh_span , 0 ) ;
    platform :: math_make_num_whole ( _strip_indices_count , 0 ) ;
    platform :: math_make_num_whole ( _fan_indices_count , 0 ) ;
    platform :: math_make_num_whole ( _vertices_count , 0 ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: receive ( typename messages :: entities_render msg )
{
    if ( platform :: condition_true ( _entity_created ) )
        _entities_render ( ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: receive ( typename messages :: entities_done msg )
{
    if ( platform :: condition_true ( _entity_created ) )
    {
        typename messages :: mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _entity_mesh_id ;
        _mediator -> send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: receive ( typename messages :: entities_prepare_permit msg )
{
    platform :: math_make_num_whole ( _entities_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: receive ( typename messages :: entities_update msg )
{
    if ( platform :: condition_true ( _entities_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _entity_created ) )
            _create_entity_mesh ( ) ;
        if ( platform :: condition_true ( _entity_created ) )
            _update_entity_grid ( ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: get_entity_origin ( vector_data & result , num_whole index )
{
    _get_entity_origin ( result , index ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: get_entity_mesh_grid ( num_whole & result )
{
    platform :: math_make_num_whole ( result , _entity_mesh_grid ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: get_entity_height ( num_fract & result )
{
    platform :: math_make_num_fract ( result , _entity_mesh_height , 1 ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _entities_render ( )
{
    num_whole i_max ;
    num_whole whole_entity_mesh_grid ;
    platform :: math_make_num_whole ( whole_entity_mesh_grid , _entity_mesh_grid ) ;
    platform :: math_mul_wholes ( i_max , whole_entity_mesh_grid , whole_entity_mesh_grid ) ;
    _mediator -> send ( typename messages :: texture_unselect ( ) ) ;
    for ( num_whole i = platform :: whole_0 
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
        matrix_data & matrix = platform :: array_element ( _entities_grid_matrices , i ) ;
        _mediator -> mesh_set_transform ( _entity_mesh_id , matrix ) ;
        {
            typename messages :: mesh_render mesh_render_msg ;
            mesh_render_msg . mesh = _entity_mesh_id ;
            _mediator -> send ( mesh_render_msg ) ;
        }
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: _entity_color ( num_fract & r , num_fract & g , num_fract & b , num_fract & a , num_whole i )
{
    if ( platform :: condition_wholes_are_equal ( i , platform :: whole_0 ) )
    {
        platform :: math_make_num_fract ( r , 1 , 1 ) ;
        platform :: math_make_num_fract ( g , 0 , 1 ) ;
        platform :: math_make_num_fract ( b , 0 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
    else if ( platform :: condition_wholes_are_equal ( i , platform :: whole_1 ) )
    {
        platform :: math_make_num_fract ( r , 1 , 1 ) ;
        platform :: math_make_num_fract ( g , 1 , 2 ) ;
        platform :: math_make_num_fract ( b , 0 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
    else if ( platform :: condition_wholes_are_equal ( i , platform :: whole_2 ) )
    {
        platform :: math_make_num_fract ( r , 1 , 1 ) ;
        platform :: math_make_num_fract ( g , 1 , 1 ) ;
        platform :: math_make_num_fract ( b , 0 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
    else if ( platform :: condition_wholes_are_equal ( i , platform :: whole_3 ) )
    {
        platform :: math_make_num_fract ( r , 0 , 1 ) ;
        platform :: math_make_num_fract ( g , 1 , 1 ) ;
        platform :: math_make_num_fract ( b , 0 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
    else if ( platform :: condition_wholes_are_equal ( i , platform :: whole_4 ) )
    {
        platform :: math_make_num_fract ( r , 0 , 1 ) ;
        platform :: math_make_num_fract ( g , 1 , 1 ) ;
        platform :: math_make_num_fract ( b , 1 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
    else if ( platform :: condition_wholes_are_equal ( i , platform :: whole_5 ) )
    {
        platform :: math_make_num_fract ( r , 0 , 1 ) ;
        platform :: math_make_num_fract ( g , 0 , 1 ) ;
        platform :: math_make_num_fract ( b , 1 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
    else if ( platform :: condition_wholes_are_equal ( i , platform :: whole_6 ) )
    {
        platform :: math_make_num_fract ( r , 1 , 1 ) ;
        platform :: math_make_num_fract ( g , 0 , 1 ) ;
        platform :: math_make_num_fract ( b , 1 , 1 ) ;
        platform :: math_make_num_fract ( a , 1 , 1 ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: _create_entity_mesh ( )
{
    num_fract vertex_x ;
    num_fract vertex_y ;
    num_fract vertex_z ;
    num_fract vertex_r ;
    num_fract vertex_g ;
    num_fract vertex_b ;
    num_fract vertex_a ;
    num_whole color_bias ;
    num_whole colors_max ;
    num_fract fract_entity_mesh_height ;
    num_fract fract_entity_mesh_spans ;
    num_whole whole_entity_mesh_spans ;
    num_whole whole_entity_mesh_spans_plus_1 ;
    
    platform :: math_make_num_whole ( color_bias , 21 ) ;
    platform :: math_make_num_whole ( colors_max , 7 ) ;
    platform :: math_make_num_whole ( whole_entity_mesh_spans , _entity_mesh_spans ) ;
    platform :: math_make_num_fract ( fract_entity_mesh_spans , _entity_mesh_spans , 1 ) ;
    platform :: math_add_wholes ( whole_entity_mesh_spans_plus_1 , whole_entity_mesh_spans , platform :: whole_1 ) ;
    platform :: math_make_num_fract ( fract_entity_mesh_height , _entity_mesh_height , 1 ) ;

    if ( platform :: condition_whole_less_or_equal_to_whole ( _current_strip_mesh_span , whole_entity_mesh_spans ) )
    {
        num_fract angle ;
        num_whole color1 ;
        num_whole color2 ;
                
        platform :: math_make_fract_from_whole ( angle , _current_strip_mesh_span ) ;
        platform :: math_mul_fract_by ( angle , platform :: fract_2pi ) ;
        platform :: math_div_fract_by ( angle , fract_entity_mesh_spans ) ;
        
        platform :: math_mul_wholes ( color1 , _current_strip_mesh_span , color_bias ) ;
        platform :: math_div_whole_by ( color1 , whole_entity_mesh_spans_plus_1 ) ;
        platform :: math_mod_whole_by ( color1 , colors_max ) ;
        platform :: math_add_wholes ( color2 , color1 , platform :: whole_1 ) ;
        platform :: math_mod_whole_by ( color2 , colors_max ) ;
        
        platform :: math_sin ( vertex_x , angle ) ;
        platform :: math_div_fracts ( vertex_y , fract_entity_mesh_height , platform :: fract_2 ) ;
        platform :: math_cos ( vertex_z , angle ) ;

        _entity_color ( vertex_r , vertex_g , vertex_b , vertex_a , color1 ) ;

        {
            vertex_data & vertex = platform :: array_element ( _vertices , _vertices_count ) ;
            platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
            platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        }
        {
            index_data & index = platform :: array_element ( _strip_indices , _strip_indices_count ) ;
            platform :: render_set_index_value ( index , _vertices_count ) ;
        }

        platform :: math_inc_whole ( _strip_indices_count ) ;
        platform :: math_inc_whole ( _vertices_count ) ;
        
        platform :: math_neg_fract ( vertex_y ) ;
        
        _entity_color ( vertex_r , vertex_g , vertex_b , vertex_a , color2 ) ;
        
        {
            vertex_data & vertex = platform :: array_element ( _vertices , _vertices_count ) ;
            platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
            platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        }
        {
            index_data & index = platform :: array_element ( _strip_indices , _strip_indices_count ) ;
            platform :: render_set_index_value ( index , _vertices_count ) ;
        }

        platform :: math_inc_whole ( _strip_indices_count ) ;
        platform :: math_inc_whole ( _vertices_count ) ;
        platform :: math_inc_whole ( _current_strip_mesh_span ) ;
    }
    else
    {
        if ( platform :: condition_whole_is_zero ( _current_fan_mesh_span ) )
        {
            vertex_x = platform :: fract_0 ;
            platform :: math_div_fracts ( vertex_y , fract_entity_mesh_height , platform :: fract_2 ) ;
            vertex_z = platform :: fract_0 ;
            
            platform :: math_make_num_fract ( vertex_r , _entity_color_roof_r , 255 ) ;
            platform :: math_make_num_fract ( vertex_g , _entity_color_roof_g , 255 ) ;
            platform :: math_make_num_fract ( vertex_b , _entity_color_roof_b , 255 ) ;
            platform :: math_make_num_fract ( vertex_a , 1 , 1 ) ;

            {
                vertex_data & vertex = platform :: array_element ( _vertices , _vertices_count ) ;
                platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
                platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
            }
            {
                index_data & index = platform :: array_element ( _fan_indices , _fan_indices_count ) ;
                platform :: render_set_index_value ( index , _vertices_count ) ;
            }
            
            platform :: math_inc_whole ( _fan_indices_count ) ;
            platform :: math_inc_whole ( _vertices_count ) ;
        }
        if ( platform :: condition_whole_less_or_equal_to_whole ( _current_fan_mesh_span , whole_entity_mesh_spans ) )
        {
            num_whole index ;
            platform :: math_mul_wholes ( index , _current_fan_mesh_span , platform :: whole_2 ) ;
            {
                index_data & index_ptr = platform :: array_element ( _fan_indices , _fan_indices_count ) ;
                platform :: render_set_index_value ( index_ptr , index ) ;
            }
            platform :: math_inc_whole ( _fan_indices_count ) ;
            platform :: math_inc_whole ( _current_fan_mesh_span ) ;
        }
        else
        {
            _mediator -> mesh_create
                ( _entity_mesh_id
                , _vertices 
                , _strip_indices 
                , _fan_indices 
                , _vertices_count 
                , _strip_indices_count 
                , _fan_indices_count
                ) ;                
            platform :: math_make_num_whole ( _entity_created , true ) ;
            _mediator -> send ( typename messages :: entities_prepared ( ) ) ;
        }
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: _get_entity_origin ( vector_data & result , num_whole index )
{
    num_whole x ;
    num_whole z ;
    num_whole whole_entity_mesh_grid ;
    num_whole half_entity_mesh_grid ;
    num_whole whole_grid_step ;
    num_fract fract_entity_mesh_height ;
    num_fract entity_x ;
    num_fract entity_y ;
    num_fract entity_z ;
    
    platform :: math_make_num_fract ( fract_entity_mesh_height , _entity_mesh_height , 1 ) ;
    platform :: math_make_num_whole ( whole_grid_step , _grid_step ) ;
    platform :: math_make_num_whole ( whole_entity_mesh_grid , _entity_mesh_grid ) ;
    platform :: math_div_wholes ( half_entity_mesh_grid , whole_entity_mesh_grid , platform :: whole_2 ) ;
    
    platform :: math_mod_wholes ( x , index , whole_entity_mesh_grid ) ;
    platform :: math_sub_from_whole ( x , half_entity_mesh_grid ) ;
    platform :: math_mul_whole_by ( x , whole_grid_step ) ;
    
    platform :: math_div_wholes ( z , index , whole_entity_mesh_grid ) ;
    platform :: math_sub_from_whole ( z , half_entity_mesh_grid ) ;
    platform :: math_mul_whole_by ( z , whole_grid_step ) ;
    
    platform :: math_make_fract_from_whole ( entity_x , x ) ;
    platform :: math_div_fracts ( entity_y , fract_entity_mesh_height , platform :: fract_2 ) ;
    platform :: math_make_fract_from_whole ( entity_z , z ) ;
    platform :: vector_xyz ( result , entity_x , entity_y , entity_z ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _update_entity_grid ( )
{
    num_whole whole_scale_in_frames ;
    num_whole whole_entity_mesh_grid ;
    num_fract fract_entity_mesh_grid ;
    num_fract fract_scale_wave ;
    num_fract fract_scale_in_frames ;
    num_fract fract_grid_scale ;
    
    platform :: math_make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform :: math_make_num_whole ( whole_entity_mesh_grid , _entity_mesh_grid ) ;
    platform :: math_make_num_fract ( fract_entity_mesh_grid , _entity_mesh_grid , 1 ) ;
    platform :: math_make_num_fract ( fract_scale_wave , _scale_wave , 1 ) ;
    platform :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform :: math_make_fract_from_whole ( fract_grid_scale , _grid_scale ) ;
    
    if ( platform :: condition_whole_less_or_equal_to_whole ( _grid_scale , whole_scale_in_frames ) )
    {
        for ( num_whole x = platform :: whole_0 
            ; platform :: condition_whole_less_than_whole ( x , whole_entity_mesh_grid ) 
            ; platform :: math_inc_whole ( x )
            )
        {
            for ( num_whole z = platform :: whole_0 
                ; platform :: condition_whole_less_than_whole ( z , whole_entity_mesh_grid )
                ; platform :: math_inc_whole ( z )
                )
            {
                num_fract fract_x ;
                num_fract fract_z ;
                num_fract scale ;
                num_fract scale_wave_part ;
                num_fract scale_frame_part ;
                num_whole index ;
                
                platform :: math_mul_wholes ( index , z , whole_entity_mesh_grid ) ;
                platform :: math_add_to_whole ( index , x ) ;
                
                platform :: math_make_fract_from_whole ( fract_x , x ) ;
                platform :: math_make_fract_from_whole ( fract_z , z ) ;
                
                platform :: math_add_fracts ( scale_wave_part , fract_x , fract_z ) ;
                platform :: math_mul_fract_by ( scale_wave_part , fract_scale_wave ) ;
                platform :: math_div_fract_by ( scale_wave_part , fract_entity_mesh_grid ) ;
                platform :: math_div_fract_by ( scale_wave_part , platform :: fract_2 ) ;
                
                platform :: math_add_fracts ( scale_frame_part , fract_scale_wave , platform :: fract_1 ) ;
                platform :: math_mul_fract_by ( scale_frame_part , fract_grid_scale ) ;
                platform :: math_div_fract_by ( scale_frame_part , fract_scale_in_frames ) ;
                platform :: math_sub_from_fract ( scale_frame_part , fract_scale_wave ) ;
                
                platform :: math_add_fracts ( scale , scale_wave_part , scale_frame_part ) ;
                engine_math :: math_clamp_fract ( scale , platform :: fract_0 , platform :: fract_1 ) ;
                
                vector_data origin ;
                _get_entity_origin ( origin , index ) ;
                
                matrix_data & matrix = platform :: array_element ( _entities_grid_matrices , index ) ;
                platform :: matrix_set_axis_x ( matrix , scale , platform :: fract_0 , platform :: fract_0 ) ;
                platform :: matrix_set_axis_y ( matrix , platform :: fract_0 , scale , platform :: fract_0 ) ;
                platform :: matrix_set_axis_z ( matrix , platform :: fract_0 , platform :: fract_0 , scale ) ;
                platform :: matrix_set_origin ( matrix , origin ) ;
            }
        }
        platform :: math_inc_whole ( _grid_scale ) ;
    }
}
