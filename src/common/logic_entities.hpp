template < typename mediator >
class shy_logic_entities
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 ENTITY_MESH_SPANS = 50 ;
    static const int_32 ENTITY_MESH_GRID = 5 ;
    static const int_32 ENTITY_MESH_HEIGHT = 2 ;

public :
    shy_logic_entities ( mediator * arg_mediator ) ;
    void render_entities ( ) ;
    void update ( ) ;
    vector_data get_entity_origin ( int_32 index ) ;
    float_32 get_entity_height ( ) ;
private :
    void _render_entities ( ) ;
    void _create_entity_mesh ( ) ;
    vector_data _get_entity_origin ( int_32 index ) ;
    void _update_entity_grid ( ) ;
private :
    mediator * _mediator ;
    int_32 _entity_created ;
    int_32 _frames_left_to_create ;
    int_32 _grid_scale ;
    mesh_id _entity_mesh_id ;
    matrix_data _entities_grid_matrices [ ENTITY_MESH_GRID * ENTITY_MESH_GRID ] ;
} ;

template < typename mediator >
shy_logic_entities < mediator > :: shy_logic_entities ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _entity_created ( false )
, _frames_left_to_create ( 0 )
, _grid_scale ( 0 )
{
}

template < typename mediator >
void shy_logic_entities < mediator > :: render_entities ( )
{
    if ( _entity_created )
        _render_entities ( ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: update ( )
{
    if ( _frames_left_to_create > 0 )
        _frames_left_to_create -- ;
    else
    {
        if ( ! _entity_created )
        {
            _create_entity_mesh ( ) ;
            _update_entity_grid ( ) ;
            _entity_created = true ;
        }
        else
            _update_entity_grid ( ) ;
    }
}

template < typename mediator >
typename shy_logic_entities < mediator > :: vector_data 
shy_logic_entities < mediator > :: get_entity_origin ( int_32 index )
{
    return _get_entity_origin ( index ) ;
}

template < typename mediator >
typename shy_logic_entities < mediator > :: float_32
shy_logic_entities < mediator > :: get_entity_height ( )
{
    return ENTITY_MESH_HEIGHT ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _render_entities ( )
{
    platform :: render_disable_texturing ( ) ;
    for ( int_32 i = 0 ; i < ENTITY_MESH_GRID * ENTITY_MESH_GRID ; i ++ )
    {
        _mediator -> mesh_set_transform ( _entity_mesh_id , _entities_grid_matrices [ i ] ) ;
        _mediator -> mesh_render ( _entity_mesh_id ) ;
    }
}

template < typename mediator >
void shy_logic_entities < mediator > :: _create_entity_mesh ( )
{
    static const int_32 COLORS_R [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ;
    static const int_32 COLORS_G [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ;
    static const int_32 COLORS_B [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ;
    
    static const int_32 COLOR_ROOF_R = 255 ;
    static const int_32 COLOR_ROOF_G = 255 ;
    static const int_32 COLOR_ROOF_B = 255 ;

    vertex_data vertices [ ( ENTITY_MESH_SPANS + 1 ) * 2 + 1 ] ;
    index_data strip_indices [ ( ENTITY_MESH_SPANS + 1 ) * 2 ] ;
    index_data fan_indices [ ENTITY_MESH_SPANS + 2 ] ;
    int_32 strip_indices_count = 0 ;
    int_32 fan_indices_count = 0 ;
    int_32 vertices_count = 0 ;
    for ( int_32 i = 0; i < ENTITY_MESH_SPANS + 1 ; i ++ )
    {
        float_32 angle 
            = ( ( float_32 ) i ) 
            * _mediator -> math_pi ( )
            * 2.0f 
            / ( float_32 ) ENTITY_MESH_SPANS
            ;
        float_32 x = platform :: math_sin ( angle ) ;
        float_32 z = platform :: math_cos ( angle ) ;
        int_32 color = ( i * 21 / ( ENTITY_MESH_SPANS + 1 ) ) % 7;
        int_32 color1 = color;
        int_32 color2 = ( color + 1 ) % 7;
        platform :: render_set_vertex_position 
            ( vertices [ vertices_count ] 
            , x 
            , 0.5f * ENTITY_MESH_HEIGHT
            , z 
            ) ;
        platform :: render_set_vertex_color 
            ( vertices [ vertices_count ] 
            , COLORS_R [ color1 ]
            , COLORS_G [ color1 ]
            , COLORS_B [ color1 ]
            , 255
            ) ;
        platform :: render_set_index_value ( strip_indices [ strip_indices_count ] , vertices_count ) ;
        ++ strip_indices_count ;
        ++ vertices_count ;
        platform :: render_set_vertex_position 
            ( vertices [ vertices_count ] 
            , x 
            , - 0.5f * ENTITY_MESH_HEIGHT
            , z 
            ) ;
        platform :: render_set_vertex_color 
            ( vertices [ vertices_count ] 
            , COLORS_R [ color2 ]
            , COLORS_G [ color2 ]
            , COLORS_B [ color2 ]
            , 255
            ) ;
        platform :: render_set_index_value ( strip_indices [ strip_indices_count ] , vertices_count ) ;
        ++ strip_indices_count ;
        ++ vertices_count ;
    }
    platform :: render_set_vertex_position 
        ( vertices [ vertices_count ] 
        , 0.0f
        , 0.5f * ENTITY_MESH_HEIGHT
        , 0.0f 
        ) ;
    platform :: render_set_vertex_color 
        ( vertices [ vertices_count ] 
        , COLOR_ROOF_R
        , COLOR_ROOF_G
        , COLOR_ROOF_B
        , 255
        ) ;
    platform :: render_set_index_value ( fan_indices [ fan_indices_count ] , vertices_count ) ;
    ++ fan_indices_count ;
    ++ vertices_count ;
    for ( int_32 i = 0 ; i < ENTITY_MESH_SPANS + 1 ; ++ i )
    {
        platform :: render_set_index_value ( fan_indices [ fan_indices_count ] , i * 2 ) ;
        ++ fan_indices_count ;
    }
    _entity_mesh_id = _mediator -> mesh_create 
        ( vertices 
        , strip_indices 
        , fan_indices 
        , vertices_count 
        , strip_indices_count 
        , fan_indices_count
        ) ;
}

template < typename mediator >
typename shy_logic_entities < mediator > :: vector_data
shy_logic_entities < mediator > :: _get_entity_origin ( int_32 index )
{
    const float_32 GRID_STEP = 5.0f ;
    int_32 x = index % ENTITY_MESH_GRID ;
    int_32 z = index / ENTITY_MESH_GRID ;
    return platform :: vector_xyz
        ( GRID_STEP * ( float_32 ) ( x - ( ENTITY_MESH_GRID / 2 ) )
        , 0.5f * ENTITY_MESH_HEIGHT
        , GRID_STEP * ( float_32 ) ( z - ( ENTITY_MESH_GRID / 2 ) )
        ) ;
}

template < typename mediator >
void shy_logic_entities < mediator > :: _update_entity_grid ( )
{
    static const int_32 SCALE_IN_FRAMES = 120 ;
    static const float_32 SCALE_WAVE = 2 ;
    if ( _grid_scale <= SCALE_IN_FRAMES )
    {
        for ( int_32 x = 0 ; x < ENTITY_MESH_GRID ; x ++ )
        {
            for ( int_32 z = 0 ; z < ENTITY_MESH_GRID ; z ++ )
            {
                int_32 index = x + ENTITY_MESH_GRID * z ;
                matrix_data & matrix = _entities_grid_matrices [ index ] ;
                float_32 scale = SCALE_WAVE * float_32 ( x + z ) / float_32 ( ENTITY_MESH_GRID * 2 ) ;
                scale = scale - SCALE_WAVE + ( 1.0f + SCALE_WAVE ) * float_32 ( _grid_scale ) / float_32 ( SCALE_IN_FRAMES ) ;
                if ( scale < 0.0f )
                    scale = 0.0f ;
                else if ( scale > 1.0f )
                    scale = 1.0f ;
                platform :: matrix_set_axis_x ( matrix , scale , 0 , 0 ) ;
                platform :: matrix_set_axis_y ( matrix , 0 , scale , 0 ) ;
                platform :: matrix_set_axis_z ( matrix , 0 , 0 , scale ) ;
                platform :: matrix_set_origin ( matrix , _get_entity_origin ( index ) ) ;
            }
        }
        _grid_scale ++ ;
    }
}
