template 
    < typename _platform
    , template < typename mediator > class engine_camera
    , template < typename mediator > class engine_math
    , template < typename mediator > class engine_mesh
    , template < typename mediator > class engine_rasterizer
    , template < typename mediator > class logic 
    , template < typename mediator > class logic_camera
    , template < typename mediator > class logic_entities
    , template < typename mediator > class logic_fidget
    , template < typename mediator > class logic_land
    , template < typename mediator > class logic_sound
    , template < typename mediator > class logic_text
    , template < typename mediator > class logic_touch
    >
class shy_mediator
{
public :
    typedef _platform platform ;
    typedef typename engine_mesh < shy_mediator > :: mesh_id mesh_id ;
    typedef typename platform :: float_32 float_32 ;
    typedef typename platform :: int_32 int_32 ;
    typedef typename platform :: index_data index_data ;
    typedef typename platform :: matrix_data matrix_data ;
    typedef typename platform :: texel_data texel_data ;
    typedef typename platform :: vector_data vector_data ;
    typedef typename platform :: vertex_data vertex_data ;
public :
    shy_mediator ( )
    : _engine_rasterizer ( this )
    , _logic ( this )
    , _logic_camera ( this )
    , _logic_entities ( this )
    , _logic_fidget ( this )
    , _logic_land ( this )
    , _logic_sound ( this )
    , _logic_text ( this )
    , _logic_touch ( this )
    {
    }
public :
    void camera_matrix_look_at ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up )
    {
        _engine_camera . camera_matrix_look_at ( matrix , from , to , norm_up ) ;
    }
    void done ( )
    {
        _logic . done ( ) ;
    }
    float_32 get_entity_height ( )
    {
        return _logic_entities . get_entity_height ( ) ;
    }
    vector_data get_entity_origin ( int_32 index )
    {
        return _logic_entities . get_entity_origin ( index ) ;
    }
    float_32 get_near_plane_distance ( )
    {
        return _logic . get_near_plane_distance ( ) ;
    }
    void init ( )
    {
        _logic . init ( ) ;
        _logic_sound . init ( ) ;
    }
    template < typename T >
    T math_abs ( T f )
    {
        return _engine_math . math_abs < T > ( f ) ;
    }
    vector_data math_catmull_rom_spline ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
    {
        return _engine_math . math_catmull_rom_spline ( t , p0 , p1 , p2 , p3 ) ;
    }
    template < typename T >
    T math_clamp ( T f , T from , T to )
    {
        return _engine_math . math_clamp < T > ( f , from , to ) ;
    }
    template < typename T >
    T math_max ( T f1 , T f2 )
    {
        return _engine_math . math_max < T > ( f1 , f2 ) ;
    }
    template < typename T >
    T math_min ( T f1 , T f2 )
    {
        return _engine_math . math_min < T > ( f1 , f2 ) ;
    }
    mesh_id mesh_create 
        ( vertex_data * vertices 
        , index_data * triangle_strip_indices 
        , index_data * triangle_fan_indices
        , int_32 vertices_count
        , int_32 triangle_strip_indices_count 
        , int_32 triangle_fan_indices_count
        )
    {
        return _engine_mesh . mesh_create 
            ( vertices
            , triangle_strip_indices
            , triangle_fan_indices
            , vertices_count
            , triangle_strip_indices_count
            , triangle_fan_indices_count
            ) ;
    }
    void mesh_render ( mesh_id arg_mesh_id )
    {
        _engine_mesh . mesh_render ( arg_mesh_id ) ;
    }
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform )
    {
        _engine_mesh . mesh_set_transform ( arg_mesh_id , transform ) ;
    }
    void rasterize_ellipse_in_rect 
        ( texel_data * starting_texel
        , const texel_data & filler 
        , int_32 texels_in_row 
        , int_32 x1
        , int_32 y1 
        , int_32 x2
        , int_32 y2
        )
    {
        _engine_rasterizer . rasterize_ellipse_in_rect ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 ) ;
    }
    void rasterize_use_context ( texel_data * starting_texel , int_32 texels_in_row )
    {
        _engine_rasterizer . rasterize_use_context ( starting_texel , texels_in_row ) ;
    }
    void rasterize_use_texel ( const texel_data & texel )
    {
        _engine_rasterizer . rasterize_use_texel ( texel ) ;
    }
    void rasterize_triangle
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x1
        , int_32 y1
        , int_32 x2
        , int_32 y2
        , int_32 x3
        , int_32 y3
        )
    {
        _engine_rasterizer . rasterize_triangle ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 , x3 , y3 ) ;
    }
    void render ( )
    {
        _logic . render ( ) ;
    }
    void render_entities ( )
    {
        _logic_entities . render_entities ( ) ;
    }
    void render_fidget ( )
    {
        _logic_fidget . render_fidget ( ) ;
    }
    void render_land ( )
    {
        _logic_land . render_land ( ) ;
    }
    void render_text ( )
    {
        _logic_text . render_text ( ) ;
    }
    void render_touch ( )
    {
        _logic_touch . render_touch ( ) ;
    }
    void update ( )
    {
        _logic . update ( ) ;
        _logic_camera . update ( ) ;
        _logic_entities . update ( ) ;
        _logic_fidget . update ( ) ;
        _logic_land . update ( ) ;
        _logic_sound . update ( ) ;
        _logic_text . update ( ) ;
        _logic_touch . update ( ) ;
    }
    void use_camera_matrix ( )
    {
        _logic_camera . use_camera_matrix ( ) ;
    }
private :
    engine_camera < shy_mediator > _engine_camera ;
    engine_math < shy_mediator > _engine_math ;
    engine_mesh < shy_mediator > _engine_mesh ;
    engine_rasterizer < shy_mediator > _engine_rasterizer ;
    logic < shy_mediator > _logic ;
    logic_camera < shy_mediator > _logic_camera ;
    logic_entities < shy_mediator > _logic_entities ;
    logic_fidget < shy_mediator > _logic_fidget ;
    logic_land < shy_mediator > _logic_land ;
    logic_sound < shy_mediator > _logic_sound ;
    logic_text < shy_mediator > _logic_text ;
    logic_touch < shy_mediator > _logic_touch ;
} ;
