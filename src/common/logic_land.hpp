template < typename mediator >
class shy_logic_land
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    
    static const int_32 _scale_in_frames = 60 ;
    static const int_32 _land_r = 255 ;
    static const int_32 _land_g = 255 ;
    static const int_32 _land_b = 255 ;
    static const int_32 _land_grid = 10 ;
    static const int_32 _land_radius = 10 ;
    static const int_32 _create_rows_per_frame = 8 ;
public :
    shy_logic_land ( mediator * arg_mediator ) ;
    void land_prepare_permit ( ) ;
    void land_render ( ) ;
    void land_update ( ) ;
private :
    void _render_land ( ) ;
    void _create_land_mesh ( ) ;
    void _create_land_texture ( ) ;
private :
    mediator * _mediator ;
    int_32 _land_mesh_created ;
    int_32 _land_texture_created ;
    int_32 _land_prepare_permitted ;
    int_32 _land_texture_creation_row ;
    float_32 _land_scale ;
    mesh_id _land_mesh_id ;
    texture_id _land_texture_id ;
} ;

template < typename mediator >
shy_logic_land < mediator > :: shy_logic_land ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _land_mesh_created ( false )
, _land_texture_created ( false )
, _land_prepare_permitted ( false )
, _land_texture_creation_row ( 0 )
, _land_scale ( 0 )
{
}

template < typename mediator >
void shy_logic_land < mediator > :: land_prepare_permit ( )
{
    _land_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_land < mediator > :: land_render ( )
{
    if ( _land_mesh_created && _land_texture_created )
        _render_land ( ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: land_update ( )
{
    if ( _land_prepare_permitted )
    {
        if ( ! _land_texture_created )
            _create_land_texture ( ) ;
        else if ( ! _land_mesh_created )
        {
            _create_land_mesh ( ) ;
            if ( _land_mesh_created )
                _mediator -> land_prepared ( ) ;
        }
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: _render_land ( )
{
    _mediator -> texture_select ( _land_texture_id ) ;
    float_32 scale_step = 1.0f / float_32 ( _scale_in_frames ) ;
    if ( _land_scale + scale_step < 1.0f )
        _land_scale += scale_step ;
    else
        _land_scale = 1 ;
    matrix_data matrix ;
    num_fract num_scale ;
    num_fract num_zero ;
    platform :: math_make_num_fract ( num_scale , int_32 ( _land_scale * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( num_zero , 0 , 1 ) ;
    platform :: matrix_set_axis_x ( matrix , num_scale , num_zero , num_zero ) ;
    platform :: matrix_set_axis_y ( matrix , num_zero , num_scale , num_zero ) ;
    platform :: matrix_set_axis_z ( matrix , num_zero , num_zero , num_scale ) ;
    platform :: matrix_set_origin ( matrix , num_zero , num_zero , num_zero ) ;
    _mediator -> mesh_set_transform ( _land_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _land_mesh_id ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: _create_land_mesh ( )
{    
    vertex_data vertices [ ( _land_grid + 1 ) * ( _land_grid + 1 ) ] ;
    index_data indices [ ( _land_grid + 1 ) * 2 * _land_grid ] ;
    int_32 vertices_count = 0 ;
    int_32 indices_count = 0 ;
    
    float_32 grid_step = float_32 ( _land_radius ) * 2.0f / float_32 ( _land_grid ) ;
    float_32 grid_origin_x = - _land_radius ;
    float_32 grid_origin_z = - _land_radius ;
    
    for ( int_32 iz = 0 ; iz < _land_grid + 1 ; iz ++ )
    {
        for ( int_32 ix = 0 ; ix < _land_grid + 1 ; ix ++ )
        {
            float_32 x = grid_origin_x + grid_step * ( float_32 ) ix ;
            float_32 z = grid_origin_z + grid_step * ( float_32 ) iz ;
            num_fract vertex_x ;
            num_fract vertex_y ;
            num_fract vertex_z ;
            num_fract vertex_u ;
            num_fract vertex_v ;
            num_whole vertex_r ;
            num_whole vertex_g ;
            num_whole vertex_b ;
            num_whole vertex_a ;
            platform :: math_make_num_fract ( vertex_x , int_32 ( x * 1000.0f ) , 1000 ) ;
            platform :: math_make_num_fract ( vertex_y , 0 , 1 ) ;
            platform :: math_make_num_fract ( vertex_z , int_32 ( z * 1000.0f ) , 1000 ) ;
            platform :: math_make_num_fract ( vertex_u , int_32 ( float_32 ( iz * 1000.0f ) / float_32 ( _land_grid ) ) , 1000 ) ;
            platform :: math_make_num_fract ( vertex_v , int_32 ( float_32 ( ix * 1000.0f ) / float_32 ( _land_grid ) ) , 1000 ) ;
            platform :: math_make_num_whole ( vertex_r , _land_r ) ;
            platform :: math_make_num_whole ( vertex_g , _land_g ) ;
            platform :: math_make_num_whole ( vertex_b , _land_b ) ;
            platform :: math_make_num_whole ( vertex_a , 255 ) ;
            platform :: render_set_vertex_position ( vertices [ vertices_count ] , vertex_x , vertex_y , vertex_z ) ;
            platform :: render_set_vertex_color ( vertices [ vertices_count ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
            platform :: render_set_vertex_tex_coord ( vertices [ vertices_count ] , vertex_u , vertex_v ) ;
            ++ vertices_count ;
        }
    }
    
    for ( int_32 iz = 0 ; iz < _land_grid ; iz ++ )
    {
        for ( int_32 ix = 0 ; ix < _land_grid + 1 ; ix ++ )
        {
            if ( iz % 2 == 0 )
            {
                num_whole index ;
                int_32 index_int_32 = ix + ( _land_grid + 1 ) * iz ;
                platform :: math_make_num_whole ( index , index_int_32 ) ;
                platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                ++ indices_count ;
                platform :: math_make_num_whole ( index , index_int_32 + _land_grid + 1 ) ;
                platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                ++ indices_count ;
            }
            else
            {
                num_whole index ;
                int_32 index_int_32 = _land_grid - ix + ( _land_grid + 1 ) * iz ;
                platform :: math_make_num_whole ( index , index_int_32 + _land_grid + 1 ) ;
                platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                ++ indices_count ;
                platform :: math_make_num_whole ( index , index_int_32 ) ;
                platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                ++ indices_count ;
            }
        }
    }
    num_whole num_vertices_count ;
    num_whole num_indices_count ;
    platform :: math_make_num_whole ( num_vertices_count , vertices_count ) ;
    platform :: math_make_num_whole ( num_indices_count , indices_count ) ;
    _mediator -> mesh_create ( _land_mesh_id , vertices , indices , 0 , num_vertices_count , num_indices_count , platform :: whole_0 ) ;
    _land_mesh_created = true ;
}

template < typename mediator >
void shy_logic_land < mediator > :: _create_land_texture ( )
{
    if ( _land_texture_creation_row == 0 )
        _mediator -> texture_create ( _land_texture_id ) ;
    int_32 prev_creation_row = _land_texture_creation_row ;
    int_32 texture_width ;
    int_32 texture_height ;
    _mediator -> texture_width ( texture_width ) ;
    _mediator -> texture_height ( texture_height ) ;
    while ( _land_texture_creation_row < texture_height
         && ( _land_texture_creation_row - prev_creation_row ) <= _create_rows_per_frame
          )
    {
        int_32 y = _land_texture_creation_row ;
        for ( int_32 x = 0 ; x < texture_width ; x ++ )
        {
            int_32 c = x ^ y ;
            _mediator -> texture_set_texel
                ( _land_texture_id
                , x
                , y
                , ( c % 32 ) * 8
                , ( c % 64 ) * 4
                , ( c % 128 ) * 2
                , 255
                ) ;
        }
        _land_texture_creation_row ++ ;
    }
    if ( _land_texture_creation_row == texture_height )
    {
        _mediator -> texture_finalize ( _land_texture_id ) ;
        _land_texture_created = true ;
    }
}
