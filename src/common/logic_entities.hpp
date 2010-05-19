template < typename mediator >
class shy_logic_entities
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 _grid_step = 5 ;
    static const int_32 _scale_in_frames = 120 ;
    static const int_32 _scale_wave = 2 ;
    static const int_32 _entity_mesh_spans = 50 ;
    static const int_32 _entity_mesh_grid = 5 ;
    static const int_32 _entity_mesh_height = 2 ;
    static const int_32 _entity_color_roof_r = 255 ;
    static const int_32 _entity_color_roof_g = 255 ;
    static const int_32 _entity_color_roof_b = 255 ;
    static const int_32 * _entity_colors_r ( ) { static const int_32 c [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ; return c ; }
    static const int_32 * _entity_colors_g ( ) { static const int_32 c [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ; return c ; }
    static const int_32 * _entity_colors_b ( ) { static const int_32 c [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ; return c ; }

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
    int_32 _entity_created ;
    int_32 _entities_prepare_permitted ;
    int_32 _grid_scale ;
    mesh_id _entity_mesh_id ;
    matrix_data _entities_grid_matrices [ _entity_mesh_grid * _entity_mesh_grid ] ;
} ;

template < typename mediator >
shy_logic_entities < mediator > :: shy_logic_entities ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _entity_created ( false )
, _entities_prepare_permitted ( false )
, _grid_scale ( 0 )
{
}

template < typename mediator >
void shy_logic_entities < mediator > :: entities_render ( )
{
    if ( _entity_created )
        _entities_render ( ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: entities_prepare_permit ( )
{
    _entities_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: entities_update ( )
{
    if ( _entities_prepare_permitted )
    {
        if ( ! _entity_created )
        {
            _create_entity_mesh ( ) ;
            _update_entity_grid ( ) ;
            _entity_created = true ;
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
    _mediator -> texture_unselect ( ) ;
    for ( int_32 i = 0 ; i < _entity_mesh_grid * _entity_mesh_grid ; i ++ )
    {
        _mediator -> mesh_set_transform ( _entity_mesh_id , _entities_grid_matrices [ i ] ) ;
        _mediator -> mesh_render ( _entity_mesh_id ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: _create_entity_mesh ( )
{
    vertex_data vertices [ ( _entity_mesh_spans + 1 ) * 2 + 1 ] ;
    index_data strip_indices [ ( _entity_mesh_spans + 1 ) * 2 ] ;
    index_data fan_indices [ _entity_mesh_spans + 2 ] ;
    int_32 strip_indices_count = 0 ;
    int_32 fan_indices_count = 0 ;
    int_32 vertices_count = 0 ;
    num_fract vertex_x ;
    num_fract vertex_y ;
    num_fract vertex_z ;
    num_whole vertex_r ;
    num_whole vertex_g ;
    num_whole vertex_b ;
    num_whole vertex_a ;
    for ( int_32 i = 0; i < _entity_mesh_spans + 1 ; i ++ )
    {
        float_32 pi ;
        _mediator -> math_pi ( pi ) ;
        float_32 angle = float_32 ( i ) * pi * 2.0f / float_32 ( _entity_mesh_spans ) ;
        float_32 x ;
        float_32 z ;
        platform :: math_sin ( x , angle ) ;
        platform :: math_cos ( z , angle ) ;
        int_32 color = ( i * 21 / ( _entity_mesh_spans + 1 ) ) % 7;
        int_32 color1 = color;
        int_32 color2 = ( color + 1 ) % 7;
        platform :: math_make_num_fract ( vertex_x , int_32 ( x * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_fract ( vertex_y , int_32 ( 0.5f * float_32 ( _entity_mesh_height ) * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_fract ( vertex_z , int_32 ( z * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_whole ( vertex_r , _entity_colors_r ( ) [ color1 ] ) ;
        platform :: math_make_num_whole ( vertex_g , _entity_colors_g ( ) [ color1 ] ) ;
        platform :: math_make_num_whole ( vertex_b , _entity_colors_b ( ) [ color1 ] ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        platform :: render_set_vertex_position ( vertices [ vertices_count ] , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( vertices [ vertices_count ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        platform :: render_set_index_value ( strip_indices [ strip_indices_count ] , vertices_count ) ;
        ++ strip_indices_count ;
        ++ vertices_count ;
        platform :: math_make_num_fract ( vertex_y , int_32 ( - 0.5f * float_32 ( _entity_mesh_height ) * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_whole ( vertex_r , _entity_colors_r ( ) [ color2 ] ) ;
        platform :: math_make_num_whole ( vertex_g , _entity_colors_g ( ) [ color2 ] ) ;
        platform :: math_make_num_whole ( vertex_b , _entity_colors_b ( ) [ color2 ] ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        platform :: render_set_vertex_position ( vertices [ vertices_count ] , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( vertices [ vertices_count ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        platform :: render_set_index_value ( strip_indices [ strip_indices_count ] , vertices_count ) ;
        ++ strip_indices_count ;
        ++ vertices_count ;
    }
    platform :: math_make_num_fract ( vertex_x , 0 , 1 ) ;
    platform :: math_make_num_fract ( vertex_y , int_32 ( 0.5f * float_32 ( _entity_mesh_height ) * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
    platform :: math_make_num_whole ( vertex_r , _entity_color_roof_r ) ;
    platform :: math_make_num_whole ( vertex_g , _entity_color_roof_g ) ;
    platform :: math_make_num_whole ( vertex_b , _entity_color_roof_b ) ;
    platform :: math_make_num_whole ( vertex_a , 255 ) ;
    platform :: render_set_vertex_position ( vertices [ vertices_count ] , vertex_x , vertex_y , vertex_z ) ;
    platform :: render_set_vertex_color ( vertices [ vertices_count ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
    platform :: render_set_index_value ( fan_indices [ fan_indices_count ] , vertices_count ) ;
    ++ fan_indices_count ;
    ++ vertices_count ;
    for ( int_32 i = 0 ; i < _entity_mesh_spans + 1 ; ++ i )
    {
        platform :: render_set_index_value ( fan_indices [ fan_indices_count ] , i * 2 ) ;
        ++ fan_indices_count ;
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
    int_32 x = index % _entity_mesh_grid ;
    int_32 z = index / _entity_mesh_grid ;
    platform :: vector_xyz
        ( result
        , ( float_32 ) ( _grid_step * ( x - ( _entity_mesh_grid / 2 ) ) )
        , 0.5f * _entity_mesh_height
        , ( float_32 ) ( _grid_step * ( z - ( _entity_mesh_grid / 2 ) ) )
        ) ;
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
                platform :: matrix_set_axis_x ( matrix , scale , 0 , 0 ) ;
                platform :: matrix_set_axis_y ( matrix , 0 , scale , 0 ) ;
                platform :: matrix_set_axis_z ( matrix , 0 , 0 , scale ) ;
                platform :: matrix_set_origin ( matrix , origin ) ;
            }
        }
        _grid_scale ++ ;
    }
}
