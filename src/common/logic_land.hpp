#define LAND_TEXTURE_SIZE_POW2_BASE 8
#define LAND_TEXTURE_SIZE ( 1 << LAND_TEXTURE_SIZE_POW2_BASE )

template < typename mediator >
class shy_logic_land
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    
public :
    shy_logic_land ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _land_created ( false )
    , _frames_left_to_create ( 0 )
    {
    }
    void render_land ( )
    {
        if ( _land_created )
            _render_land ( ) ;
    }
    void update ( )
    {
        if ( _frames_left_to_create > 0 )
            _frames_left_to_create -- ;
        else
        {
            if ( ! _land_created )
            {
                _create_land_mesh ( ) ;
                _create_land_texture ( ) ;
                _land_created = true ;
            }
        }
    }
private :
    void _render_land ( )
    {
        platform :: render_enable_texturing ( ) ;
        platform :: render_use_texture ( _land_texture_id ) ;
        _mediator -> mesh_render ( _land_mesh_id ) ;
    }
    void _create_land_mesh ( )
    {
        static const int_32 LAND_R = 255 ;
        static const int_32 LAND_G = 255 ;
        static const int_32 LAND_B = 255 ;
        static const int_32 LAND_GRID = 10 ;
        static const float_32 LAND_RADIUS = 10 ;
        
        vertex_data vertices [ ( LAND_GRID + 1 ) * ( LAND_GRID + 1 ) ] ;
        index_data indices [ ( LAND_GRID + 1 ) * 2 * LAND_GRID ] ;
        int_32 vertices_count = 0 ;
        int_32 indices_count = 0 ;
        
        const float_32 grid_step = LAND_RADIUS * 2.0f / ( float_32 ) LAND_GRID ;
        const float_32 grid_origin_x = - LAND_RADIUS ;
        const float_32 grid_origin_z = - LAND_RADIUS ;
        
        for ( int_32 iz = 0 ; iz < LAND_GRID + 1 ; iz ++ )
        {
            for ( int_32 ix = 0 ; ix < LAND_GRID + 1 ; ix ++ )
            {
                float_32 x = grid_origin_x + grid_step * ( float_32 ) ix ;
                float_32 z = grid_origin_z + grid_step * ( float_32 ) iz ;
                platform :: render_set_vertex_position 
                    ( vertices [ vertices_count ]
                    , x
                    , 0.0f
                    , z
                    ) ;
                platform :: render_set_vertex_color
                    ( vertices [ vertices_count ]
                    , LAND_R
                    , LAND_G
                    , LAND_B
                    , 255
                    ) ;
                platform :: render_set_vertex_tex_coord
                    ( vertices [ vertices_count ]
                    , float_32 ( iz ) / float_32 ( LAND_GRID )
                    , float_32 ( ix ) / float_32 ( LAND_GRID )
                    ) ;
                ++ vertices_count ;
            }
        }
        
        for ( int_32 iz = 0 ; iz < LAND_GRID ; iz ++ )
        {
            for ( int_32 ix = 0 ; ix < LAND_GRID + 1 ; ix ++ )
            {
                int_32 index = 0 ;
                if ( iz % 2 == 0 )
                {
                    index = ix + ( LAND_GRID + 1 ) * iz ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                    ++ indices_count ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index + LAND_GRID + 1 ) ;
                    ++ indices_count ;
                }
                else
                {
                    index = LAND_GRID - ix + ( LAND_GRID + 1 ) * iz ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index + LAND_GRID + 1 ) ;
                    ++ indices_count ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                    ++ indices_count ;
                }
            }
        }
        _land_mesh_id = _mediator -> mesh_create ( vertices , indices , 0 , vertices_count , indices_count , 0 ) ;
    }
    void _create_land_texture ( )
    {
        for ( int_32 x = 0 ; x < LAND_TEXTURE_SIZE ; x ++ )
        {
            for ( int_32 y = 0 ; y < LAND_TEXTURE_SIZE ; y ++ )
            {
                platform :: render_set_texel_color
                    ( _land_texture_data [ x + LAND_TEXTURE_SIZE * y ]
                    , ( ( x % 16 ) + ( y % 16 ) ) * 8
                    , ( ( x % 32 ) + ( y % 32 ) ) * 4
                    , ( ( x % 64 ) + ( y % 64 ) ) * 2
                    , 255
                    ) ;
            }
        }
        platform :: render_create_texture_id ( _land_texture_id ) ;
        platform :: render_load_texture_data ( _land_texture_id , LAND_TEXTURE_SIZE_POW2_BASE , _land_texture_data ) ;
    }
private :
    mediator * _mediator ;
    int_32 _land_created ;
    int_32 _frames_left_to_create ;
    mesh_id _land_mesh_id ;
    render_texture_id _land_texture_id ;
    texel_data _land_texture_data [ LAND_TEXTURE_SIZE * LAND_TEXTURE_SIZE ] ;
} ;
