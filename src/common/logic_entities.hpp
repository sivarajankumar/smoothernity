template < typename mediator >
class shy_logic_entities
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
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
    static const_int_32 * _entity_colors_r ( ) { static const_int_32 c [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ; return c ; }
    static const_int_32 * _entity_colors_g ( ) { static const_int_32 c [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ; return c ; }
    static const_int_32 * _entity_colors_b ( ) { static const_int_32 c [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ; return c ; }

public :
    shy_logic_entities ( mediator * arg_mediator ) ;
    void entities_render ( ) ;
    void entities_prepare_permit ( ) ;
    void entities_update ( ) ;
    void get_entity_origin ( vector_data & result , int_32 index ) ;
    void get_entity_height ( float_32 & result ) ;
    void get_entity_mesh_grid ( int_32 & result ) ;
private :
    void _entities_render ( ) ;
    void _create_entity_mesh ( ) ;
    void _get_entity_origin ( vector_data & result , int_32 index ) ;
    void _update_entity_grid ( ) ;
private :
    mediator * _mediator ;
    num_whole _entity_created ;
    num_whole _entities_prepare_permitted ;
    int_32 _grid_scale ;
    mesh_id _entity_mesh_id ;
    matrix_data _entities_grid_matrices [ _entity_mesh_grid * _entity_mesh_grid ] ;
} ;

template < typename mediator >
shy_logic_entities < mediator > :: shy_logic_entities ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _grid_scale ( 0 )
{
    platform :: math_make_num_whole ( _entity_created , false ) ;
    platform :: math_make_num_whole ( _entities_prepare_permitted , false ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: entities_render ( )
{
    if ( platform :: condition_true ( _entity_created ) )
        _entities_render ( ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: entities_prepare_permit ( )
{
    platform :: math_make_num_whole ( _entities_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: entities_update ( )
{
    if ( platform :: condition_true ( _entities_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _entity_created ) )
        {
            _create_entity_mesh ( ) ;
            _update_entity_grid ( ) ;
            platform :: math_make_num_whole ( _entity_created , true ) ;
            _mediator -> entities_prepared ( ) ;
        }
        else
            _update_entity_grid ( ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: get_entity_origin ( vector_data & result , int_32 index )
{
    _get_entity_origin ( result , index ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: get_entity_mesh_grid ( int_32 & result )
{
    result = _entity_mesh_grid ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: get_entity_height ( float_32 & result )
{
    result = _entity_mesh_height ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _entities_render ( )
{
    num_whole i_max ;
    num_whole whole_entity_mesh_grid ;
    platform :: math_make_num_whole ( whole_entity_mesh_grid , _entity_mesh_grid ) ;
    platform :: math_mul_wholes ( i_max , whole_entity_mesh_grid , whole_entity_mesh_grid ) ;
    _mediator -> texture_unselect ( ) ;
    for ( num_whole i = platform :: whole_0 
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
        matrix_data * matrix_ptr = 0 ;
        platform :: memory_pointer_offset ( matrix_ptr , _entities_grid_matrices , i ) ;
        _mediator -> mesh_set_transform ( _entity_mesh_id , * matrix_ptr ) ;
        _mediator -> mesh_render ( _entity_mesh_id ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: _create_entity_mesh ( )
{
    vertex_data vertices [ ( _entity_mesh_spans + 1 ) * 2 + 1 ] ;
    index_data strip_indices [ ( _entity_mesh_spans + 1 ) * 2 ] ;
    index_data fan_indices [ _entity_mesh_spans + 2 ] ;
    num_fract vertex_x ;
    num_fract vertex_y ;
    num_fract vertex_z ;
    num_whole vertex_r ;
    num_whole vertex_g ;
    num_whole vertex_b ;
    num_whole vertex_a ;
    num_whole color_bias ;
    num_whole colors_max ;
    num_whole strip_indices_count ;
    num_whole fan_indices_count ;
    num_whole vertices_count ;
    num_fract fract_entity_mesh_height ;
    num_fract fract_entity_mesh_spans ;
    num_whole whole_entity_mesh_spans ;
    num_whole whole_entity_mesh_spans_plus_1 ;
    platform :: math_make_num_whole ( color_bias , 21 ) ;
    platform :: math_make_num_whole ( colors_max , 7 ) ;
    platform :: math_make_num_whole ( strip_indices_count , 0 ) ;
    platform :: math_make_num_whole ( fan_indices_count , 0 ) ;
    platform :: math_make_num_whole ( vertices_count , 0 ) ;
    platform :: math_make_num_whole ( whole_entity_mesh_spans , _entity_mesh_spans ) ;
    platform :: math_make_num_fract ( fract_entity_mesh_spans , _entity_mesh_spans , 1 ) ;
    platform :: math_add_wholes ( whole_entity_mesh_spans_plus_1 , whole_entity_mesh_spans , platform :: whole_1 ) ;
    platform :: math_make_num_fract ( fract_entity_mesh_height , int_32 ( _entity_mesh_height * 1000.0f ) , 1000 ) ;
    for ( num_whole i = platform :: whole_0 
        ; platform :: condition_whole_less_or_equal_to_whole ( i , whole_entity_mesh_spans ) 
        ; platform :: math_inc_whole ( i )
        )
    {
        num_fract angle ;
        num_whole color1 ;
        num_whole color2 ;
        const_int_32 * entity_color_r_ptr = 0 ;
        const_int_32 * entity_color_g_ptr = 0 ;
        const_int_32 * entity_color_b_ptr = 0 ;
        vertex_data * vertex_ptr = 0 ;
        index_data * index_ptr = 0 ;
                
        platform :: math_make_fract_from_whole ( angle , i ) ;
        platform :: math_mul_fract_by ( angle , platform :: fract_2pi ) ;
        platform :: math_div_fract_by ( angle , fract_entity_mesh_spans ) ;
        
        platform :: math_mul_wholes ( color1 , i , color_bias ) ;
        platform :: math_div_whole_by ( color1 , whole_entity_mesh_spans_plus_1 ) ;
        platform :: math_mod_whole_by ( color1 , colors_max ) ;
        platform :: math_add_wholes ( color2 , color1 , platform :: whole_1 ) ;
        platform :: math_mod_whole_by ( color2 , colors_max ) ;
        
        platform :: math_sin ( vertex_x , angle ) ;
        platform :: math_div_fracts ( vertex_y , fract_entity_mesh_height , platform :: fract_2 ) ;
        platform :: math_cos ( vertex_z , angle ) ;
        
        platform :: memory_pointer_offset ( entity_color_r_ptr , _entity_colors_r ( ) , color1 ) ;
        platform :: memory_pointer_offset ( entity_color_g_ptr , _entity_colors_g ( ) , color1 ) ;
        platform :: memory_pointer_offset ( entity_color_b_ptr , _entity_colors_b ( ) , color1 ) ;
        platform :: math_make_num_whole ( vertex_r , * entity_color_r_ptr ) ;
        platform :: math_make_num_whole ( vertex_g , * entity_color_g_ptr ) ;
        platform :: math_make_num_whole ( vertex_b , * entity_color_b_ptr ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        
        platform :: memory_pointer_offset ( vertex_ptr , vertices , vertices_count ) ;
        platform :: render_set_vertex_position ( * vertex_ptr , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( * vertex_ptr , vertex_r , vertex_g , vertex_b , vertex_a ) ;

        platform :: memory_pointer_offset ( index_ptr , strip_indices , strip_indices_count ) ;
        platform :: render_set_index_value ( * index_ptr , vertices_count ) ;

        platform :: math_inc_whole ( strip_indices_count ) ;
        platform :: math_inc_whole ( vertices_count ) ;
        
        platform :: math_neg_fract ( vertex_y ) ;
        
        platform :: memory_pointer_offset ( entity_color_r_ptr , _entity_colors_r ( ) , color2 ) ;
        platform :: memory_pointer_offset ( entity_color_g_ptr , _entity_colors_g ( ) , color2 ) ;
        platform :: memory_pointer_offset ( entity_color_b_ptr , _entity_colors_b ( ) , color2 ) ;
        platform :: math_make_num_whole ( vertex_r , * entity_color_r_ptr ) ;
        platform :: math_make_num_whole ( vertex_g , * entity_color_g_ptr ) ;
        platform :: math_make_num_whole ( vertex_b , * entity_color_b_ptr ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        
        platform :: memory_pointer_offset ( vertex_ptr , vertices , vertices_count ) ;
        platform :: render_set_vertex_position ( * vertex_ptr , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( * vertex_ptr , vertex_r , vertex_g , vertex_b , vertex_a ) ;

        platform :: memory_pointer_offset ( index_ptr , strip_indices , strip_indices_count ) ;
        platform :: render_set_index_value ( * index_ptr , vertices_count ) ;

        platform :: math_inc_whole ( strip_indices_count ) ;
        platform :: math_inc_whole ( vertices_count ) ;
    }
    platform :: math_make_num_fract ( vertex_x , 0 , 1 ) ;
    platform :: math_make_num_fract ( vertex_y , int_32 ( 0.5f * float_32 ( _entity_mesh_height ) * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
    platform :: math_make_num_whole ( vertex_r , _entity_color_roof_r ) ;
    platform :: math_make_num_whole ( vertex_g , _entity_color_roof_g ) ;
    platform :: math_make_num_whole ( vertex_b , _entity_color_roof_b ) ;
    platform :: math_make_num_whole ( vertex_a , 255 ) ;
    platform :: render_set_vertex_position ( vertices [ vertices_count . debug_to_int_32 ( ) ] , vertex_x , vertex_y , vertex_z ) ;
    platform :: render_set_vertex_color ( vertices [ vertices_count . debug_to_int_32 ( ) ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
    platform :: render_set_index_value ( fan_indices [ fan_indices_count . debug_to_int_32 ( ) ] , vertices_count ) ;
    platform :: math_inc_whole ( fan_indices_count ) ;
    platform :: math_inc_whole ( vertices_count ) ;
    for ( int_32 i = 0 ; i <= _entity_mesh_spans ; ++ i )
    {
        num_whole index ;
        platform :: math_make_num_whole ( index , i * 2 ) ;
        platform :: render_set_index_value ( fan_indices [ fan_indices_count . debug_to_int_32 ( ) ] , index ) ;
        platform :: math_inc_whole ( fan_indices_count ) ;
    }
    
    _mediator -> mesh_create 
        ( _entity_mesh_id
        , vertices 
        , strip_indices 
        , fan_indices 
        , vertices_count 
        , strip_indices_count 
        , fan_indices_count
        ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _get_entity_origin ( vector_data & result , int_32 index )
{
    num_fract entity_x ;
    num_fract entity_y ;
    num_fract entity_z ;
    int_32 x = index % _entity_mesh_grid ;
    int_32 z = index / _entity_mesh_grid ;
    
    platform :: math_make_num_fract ( entity_x , ( _grid_step * ( x - ( _entity_mesh_grid / 2 ) ) ) , 1 ) ;
    platform :: math_make_num_fract ( entity_y , int_32 ( 0.5f * _entity_mesh_height * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( entity_z , ( _grid_step * ( z - ( _entity_mesh_grid / 2 ) ) ) , 1 ) ;
    platform :: vector_xyz ( result , entity_x , entity_y , entity_z ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _update_entity_grid ( )
{
    if ( _grid_scale <= _scale_in_frames )
    {
        for ( int_32 x = 0 ; x < _entity_mesh_grid ; x ++ )
        {
            for ( int_32 z = 0 ; z < _entity_mesh_grid ; z ++ )
            {
                int_32 index = x + _entity_mesh_grid * z ;
                matrix_data & matrix = _entities_grid_matrices [ index ] ;
                float_32 scale = float_32 ( _scale_wave * ( x + z ) ) / float_32 ( _entity_mesh_grid * 2 ) ;
                scale = scale - float_32 ( _scale_wave ) + float_32 ( 1 + _scale_wave ) * float_32 ( _grid_scale ) / float_32 ( _scale_in_frames ) ;
                if ( scale < 0.0f )
                    scale = 0.0f ;
                else if ( scale > 1.0f )
                    scale = 1.0f ;
                vector_data origin ;
                _get_entity_origin ( origin , index ) ;
                num_fract num_zero ;
                num_fract num_scale ;
                platform :: math_make_num_fract ( num_zero , 0 , 1 ) ;
                platform :: math_make_num_fract ( num_scale , int_32 ( scale * 1000.0f ) , 1000 ) ;
                platform :: matrix_set_axis_x ( matrix , num_scale , num_zero , num_zero ) ;
                platform :: matrix_set_axis_y ( matrix , num_zero , num_scale , num_zero ) ;
                platform :: matrix_set_axis_z ( matrix , num_zero , num_zero , num_scale ) ;
                platform :: matrix_set_origin ( matrix , origin ) ;
            }
        }
        _grid_scale ++ ;
    }
}
