template 
    < typename _platform
    , template < typename mediator > class _engine_camera
    , template < typename mediator > class _engine_math
    , template < typename mediator > class _engine_mesh
    , template < typename mediator > class _engine_rasterizer
    , template < typename mediator > class _logic 
    , template < typename mediator > class _logic_camera
    , template < typename mediator > class _logic_entities
    , template < typename mediator > class _logic_fidget
    , template < typename mediator > class _logic_land
    , template < typename mediator > class _logic_sound
    , template < typename mediator > class _logic_text
    , template < typename mediator > class _logic_touch
    >
class shy_mediator_types
{
public :
    typedef _platform platform ;
    template < typename mediator >
    class modules
    {
    public :
        typedef _engine_camera < mediator > engine_camera ;
        typedef _engine_math < mediator > engine_math ;
        typedef _engine_mesh < mediator > engine_mesh ;
        typedef _engine_rasterizer < mediator > engine_rasterizer ;
        typedef _logic < mediator > logic ;
        typedef _logic_camera < mediator > logic_camera ;
        typedef _logic_entities < mediator > logic_entities ;
        typedef _logic_fidget < mediator > logic_fidget ;
        typedef _logic_land < mediator > logic_land ;
        typedef _logic_sound < mediator > logic_sound ;
        typedef _logic_text < mediator > logic_text ;
        typedef _logic_touch < mediator > logic_touch ;
    } ;
} ;

template < typename mediator_types >
class shy_mediator
{
public :
    typedef typename mediator_types :: platform platform ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_mesh :: mesh_id mesh_id ;
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
    float_32 math_pi ( )
    {
        return _engine_math . math_pi ( ) ;
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
    void rasterize_ellipse_in_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 )
    {
        _engine_rasterizer . rasterize_ellipse_in_rect ( x1 , y1 , x2 , y2 ) ;
    }
    void rasterize_use_context ( texel_data * starting_texel , int_32 texels_in_row )
    {
        _engine_rasterizer . rasterize_use_context ( starting_texel , texels_in_row ) ;
    }
    void rasterize_use_texel ( const texel_data & texel )
    {
        _engine_rasterizer . rasterize_use_texel ( texel ) ;
    }
    void rasterize_triangle ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 , int_32 x3 , int_32 y3 )
    {
        _engine_rasterizer . rasterize_triangle ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
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
    typename mediator_types :: template modules < shy_mediator > :: engine_camera _engine_camera ;
    typename mediator_types :: template modules < shy_mediator > :: engine_math _engine_math ;
    typename mediator_types :: template modules < shy_mediator > :: engine_mesh _engine_mesh ;
    typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer _engine_rasterizer ;
    typename mediator_types :: template modules < shy_mediator > :: logic _logic ;
    typename mediator_types :: template modules < shy_mediator > :: logic_camera _logic_camera ;
    typename mediator_types :: template modules < shy_mediator > :: logic_entities _logic_entities ;
    typename mediator_types :: template modules < shy_mediator > :: logic_fidget _logic_fidget ;
    typename mediator_types :: template modules < shy_mediator > :: logic_land _logic_land ;
    typename mediator_types :: template modules < shy_mediator > :: logic_sound _logic_sound ;
    typename mediator_types :: template modules < shy_mediator > :: logic_text _logic_text ;
    typename mediator_types :: template modules < shy_mediator > :: logic_touch _logic_touch ;
} ;
