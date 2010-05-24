template < typename mediator >
class shy_logic_entities
{
    typedef typename mediator :: mesh_id mesh_id ;
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
    static const_int_32 * _entity_colors_r ( ) { static const_int_32 c [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ; return c ; }
    static const_int_32 * _entity_colors_g ( ) { static const_int_32 c [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ; return c ; }
    static const_int_32 * _entity_colors_b ( ) { static const_int_32 c [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ; return c ; }

public :
    shy_logic_entities ( mediator * arg_mediator ) ;
    void entities_render ( ) ;
    void entities_prepare_permit ( ) ;
    void entities_update ( ) ;
    void get_entity_origin ( vector_data & result , num_whole index ) ;
    void get_entity_height ( num_fract & result ) ;
    void get_entity_mesh_grid ( num_whole & result ) ;
private :
    void _entities_render ( ) ;
    void _create_entity_mesh ( ) ;
    void _get_entity_origin ( vector_data & result , num_whole index ) ;
    void _update_entity_grid ( ) ;
private :
    mediator * _mediator ;
    num_whole _entity_created ;
    num_whole _entities_prepare_permitted ;
    num_whole _grid_scale ;
    mesh_id _entity_mesh_id ;
    matrix_data _entities_grid_matrices [ _entity_mesh_grid * _entity_mesh_grid ] ;
} ;

template < typename mediator >
shy_logic_entities < mediator > :: shy_logic_entities ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _entity_created , false ) ;
    platform :: math_make_num_whole ( _entities_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _grid_scale , 0 ) ;
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
    num_whole i ;
    num_whole i_max ;
    matrix_data * matrix_ptr = 0 ;
    _mediator -> texture_unselect ( ) ;
    for ( platform :: math_make_num_whole ( i , 0 )
        , platform :: math_make_num_whole ( i_max , _entity_mesh_grid * _entity_mesh_grid ) 
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
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
    num_fract fract_entity_mesh_spans ;
    num_fract vertex_x ;
    num_fract vertex_y ;
    num_fract vertex_z ;
    num_whole vertex_r ;
    num_whole vertex_g ;
    num_whole vertex_b ;
    num_whole vertex_a ;
    num_whole color_const1 ;
    num_whole color_const2 ;
    num_whole color_delta ;
    num_whole strip_indices_count ;
    num_whole fan_indices_count ;
    num_whole vertices_count ;
    num_whole i ;
    num_whole i_max ;
    vertex_data * vertex_ptr = 0 ;
    index_data * index_ptr = 0 ;
    
    platform :: math_make_num_whole ( strip_indices_count , 0 ) ;
    platform :: math_make_num_whole ( fan_indices_count , 0 ) ;
    platform :: math_make_num_whole ( vertices_count , 0 ) ;
    platform :: math_make_num_fract ( fract_entity_mesh_spans , _entity_mesh_spans , 1 ) ;
    platform :: math_make_num_whole ( color_const1 , 21 ) ;
    platform :: math_make_num_whole ( color_const2 , 7 ) ;
    platform :: math_make_num_whole ( color_delta , 1 ) ;
    platform :: math_make_num_whole ( i , 0 ) ;
    platform :: math_make_num_whole ( i_max , _entity_mesh_spans + 1 ) ;
    for (
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
        num_fract angle ;
        num_fract i_fract ;
        num_whole color1 ;
        num_whole color2 ;
        const_int_32 * entity_color_r_ptr = 0 ;
        const_int_32 * entity_color_g_ptr = 0 ;
        const_int_32 * entity_color_b_ptr = 0 ;
        
        platform :: math_make_fract_from_whole ( i_fract , i ) ;
        platform :: math_mul_wholes ( color1 , i , color_const1 ) ;
        platform :: math_div_whole_by ( color1 , i_max ) ;
        platform :: math_mod_whole_by ( color1 , color_const2 ) ;
        platform :: math_add_wholes ( color2 , color1 , color_delta ) ;
        platform :: math_mod_whole_by ( color2 , color_const2 ) ;
        platform :: math_mul_fracts ( angle , i_fract , platform :: fract_2pi ) ;
        platform :: math_div_fract_by ( angle , fract_entity_mesh_spans );
        platform :: math_sin ( vertex_x , angle ) ;
        platform :: math_make_num_fract ( vertex_y , _entity_mesh_height , 2 ) ;
        platform :: math_cos ( vertex_z , angle ) ;
        platform :: memory_pointer_offset ( entity_color_r_ptr , _entity_colors_r ( ) , color1 ) ;
        platform :: memory_pointer_offset ( entity_color_g_ptr , _entity_colors_g ( ) , color1 ) ;
        platform :: memory_pointer_offset ( entity_color_b_ptr , _entity_colors_b ( ) , color1 ) ;
        platform :: math_make_num_whole ( vertex_r , * entity_color_r_ptr ) ;
        platform :: math_make_num_whole ( vertex_g , * entity_color_g_ptr ) ;
        platform :: math_make_num_whole ( vertex_b , * entity_color_b_ptr ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        platform :: memory_pointer_offset ( vertex_ptr , vertices , vertices_count ) ;
        platform :: memory_pointer_offset ( index_ptr , strip_indices , strip_indices_count ) ;
        platform :: render_set_vertex_position ( * vertex_ptr , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( * vertex_ptr , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        platform :: render_set_index_value ( * index_ptr , vertices_count ) ;        
        platform :: math_inc_whole ( strip_indices_count ) ;
        platform :: math_inc_whole ( vertices_count ) ;
        
        platform :: math_make_num_fract ( vertex_y , - _entity_mesh_height , 2 ) ;
        platform :: memory_pointer_offset ( entity_color_r_ptr , _entity_colors_r ( ) , color2 ) ;
        platform :: memory_pointer_offset ( entity_color_g_ptr , _entity_colors_g ( ) , color2 ) ;
        platform :: memory_pointer_offset ( entity_color_b_ptr , _entity_colors_b ( ) , color2 ) ;
        platform :: math_make_num_whole ( vertex_r , * entity_color_r_ptr ) ;
        platform :: math_make_num_whole ( vertex_g , * entity_color_g_ptr ) ;
        platform :: math_make_num_whole ( vertex_b , * entity_color_b_ptr ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        platform :: memory_pointer_offset ( vertex_ptr , vertices , vertices_count ) ;
        platform :: memory_pointer_offset ( index_ptr , strip_indices , strip_indices_count ) ;
        platform :: render_set_vertex_position ( * vertex_ptr , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( * vertex_ptr , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        platform :: render_set_index_value ( * index_ptr , vertices_count ) ;
        platform :: math_inc_whole ( strip_indices_count ) ;
        platform :: math_inc_whole ( vertices_count ) ;
    }
    platform :: math_make_num_fract ( vertex_x , 0 , 1 ) ;
    platform :: math_make_num_fract ( vertex_y , _entity_mesh_height , 2 ) ;
    platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
    platform :: math_make_num_whole ( vertex_r , _entity_color_roof_r ) ;
    platform :: math_make_num_whole ( vertex_g , _entity_color_roof_g ) ;
    platform :: math_make_num_whole ( vertex_b , _entity_color_roof_b ) ;
    platform :: math_make_num_whole ( vertex_a , 255 ) ;
    platform :: memory_pointer_offset ( vertex_ptr , vertices , vertices_count ) ;
    platform :: memory_pointer_offset ( index_ptr , fan_indices , fan_indices_count ) ;
    platform :: render_set_vertex_position ( * vertex_ptr , vertex_x , vertex_y , vertex_z ) ;
    platform :: render_set_vertex_color ( * vertex_ptr , vertex_r , vertex_g , vertex_b , vertex_a ) ;
    platform :: render_set_index_value ( * index_ptr , vertices_count ) ;
    platform :: math_inc_whole ( fan_indices_count ) ;
    platform :: math_inc_whole ( vertices_count ) ;
    platform :: math_make_num_whole ( i , 0 ) ;
    platform :: math_make_num_whole ( i_max , _entity_mesh_spans + 1 ) ;
    for (
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
        num_whole index ;
        platform :: math_add_wholes ( index , i , i ) ;
        platform :: memory_pointer_offset ( index_ptr , fan_indices , fan_indices_count ) ;
        platform :: render_set_index_value ( * index_ptr , index ) ;
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
void shy_logic_entities < mediator > :: _get_entity_origin ( vector_data & result , num_whole index )
{
    num_fract entity_x ;
    num_fract entity_y ;
    num_fract entity_z ;
    num_whole x ;
    num_whole z ;
    num_whole whole_entity_mesh_grid ;
    num_fract fract_half_entity_mesh_grid ;
    num_fract fract_grid_step ;
    num_fract fract_x ;
    num_fract fract_z ;
    
    platform :: math_make_num_whole ( whole_entity_mesh_grid , _entity_mesh_grid ) ;
    platform :: math_make_num_fract ( fract_half_entity_mesh_grid , _entity_mesh_grid , 2 ) ;
    platform :: math_make_num_fract ( fract_grid_step , _grid_step , 1 ) ;
    platform :: math_mod_wholes ( x , index , whole_entity_mesh_grid ) ;
    platform :: math_div_wholes ( z , index , whole_entity_mesh_grid ) ;
    platform :: math_make_fract_from_whole ( fract_x , x ) ;
    platform :: math_make_fract_from_whole ( fract_z , z ) ;
    platform :: math_sub_fracts ( entity_x , fract_x , fract_half_entity_mesh_grid ) ;
    platform :: math_sub_fracts ( entity_z , fract_z , fract_half_entity_mesh_grid ) ;
    platform :: math_mul_fract_by ( entity_x , fract_grid_step ) ;
    platform :: math_mul_fract_by ( entity_z , fract_grid_step ) ;
    platform :: math_make_num_fract ( entity_y , _entity_mesh_height , 2 ) ;
    platform :: vector_xyz ( result , entity_x , entity_y , entity_z ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _update_entity_grid ( )
{
    num_whole x ;
    num_whole z ;
    num_whole whole_entity_mesh_grid ;
    num_whole whole_scale_in_frames ;
    num_fract fract_scale_wave ;
    num_fract fract_doubled_entity_mesh_grid ;
    num_fract fract_grid_scale ;
    num_fract fract_scale_in_frames ;
    num_fract scale_delta ;
    
    platform :: math_make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform :: math_make_num_whole ( whole_entity_mesh_grid , _entity_mesh_grid ) ;
    platform :: math_make_num_fract ( fract_scale_wave , _scale_wave , 1 ) ;
    platform :: math_make_num_fract ( fract_doubled_entity_mesh_grid , _entity_mesh_grid * 2 , 1 ) ;
    platform :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform :: math_make_fract_from_whole ( fract_grid_scale , _grid_scale ) ;
    platform :: math_make_num_fract ( scale_delta , 1 + _scale_wave * ( 1 - _scale_in_frames ) , 1 ) ;
    platform :: math_add_to_fract ( scale_delta , fract_grid_scale ) ;
    platform :: math_div_fract_by ( scale_delta , fract_scale_in_frames ) ;
    
    if ( platform :: condition_whole_less_or_equal_to_whole ( _grid_scale , whole_scale_in_frames ) )
    {
        for ( platform :: math_make_num_whole ( x , 0 )
            ; platform :: condition_whole_less_than_whole ( x , whole_entity_mesh_grid )
            ; platform :: math_inc_whole ( x )
            )
        {
            for ( platform :: math_make_num_whole ( z , 0 )
                ; platform :: condition_whole_less_than_whole ( z , whole_entity_mesh_grid )
                ; platform :: math_inc_whole ( z )
                )
            {
                vector_data origin ;
                num_fract scale ;
                num_fract scale_clamped ;
                num_fract fract_x ;
                num_fract fract_z ;
                num_whole index ;
                matrix_data * matrix_ptr ;
                
                platform :: math_make_fract_from_whole ( fract_x , x ) ;
                platform :: math_make_fract_from_whole ( fract_z , z ) ;
                platform :: math_mul_wholes ( index , whole_entity_mesh_grid , z ) ;
                platform :: math_add_to_whole ( index , x ) ;
                platform :: memory_pointer_offset ( matrix_ptr , _entities_grid_matrices , index ) ;
                
                platform :: math_add_fracts ( scale , fract_x , fract_z ) ;
                platform :: math_mul_fract_by ( scale , fract_scale_wave ) ;
                platform :: math_div_fract_by ( scale , fract_doubled_entity_mesh_grid ) ;                
                platform :: math_add_to_fract ( scale , scale_delta ) ;
                _mediator -> math_clamp_fract ( scale , scale , platform :: fract_0 , platform :: fract_1 ) ;
                
                _get_entity_origin ( origin , index ) ;
                platform :: matrix_set_axis_x ( * matrix_ptr , scale , platform :: fract_0 , platform :: fract_0 ) ;
                platform :: matrix_set_axis_y ( * matrix_ptr , platform :: fract_0 , scale , platform :: fract_0 ) ;
                platform :: matrix_set_axis_z ( * matrix_ptr , platform :: fract_0 , platform :: fract_0 , scale ) ;
                platform :: matrix_set_origin ( * matrix_ptr , origin ) ;
            }
        }
        platform :: math_inc_whole ( _grid_scale ) ;
    }
}
