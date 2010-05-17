template 
    < typename _platform
    , template < typename mediator > class _engine_camera
    , template < typename mediator > class _engine_math
    , template < typename mediator > class _engine_mesh
    , template < typename mediator > class _engine_rasterizer
    , template < typename mediator > class _engine_texture
    , template < typename mediator > class _logic 
    , template < typename mediator > class _logic_application
    , template < typename mediator > class _logic_camera
    , template < typename mediator > class _logic_entities
    , template < typename mediator > class _logic_fidget
    , template < typename mediator > class _logic_game
    , template < typename mediator > class _logic_image
    , template < typename mediator > class _logic_land
    , template < typename mediator > class _logic_sound
    , template < typename mediator > class _logic_text
    , template < typename mediator > class _logic_title
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
        typedef _engine_texture < mediator > engine_texture ;
        typedef _logic < mediator > logic ;
        typedef _logic_application < mediator > logic_application ;
        typedef _logic_camera < mediator > logic_camera ;
        typedef _logic_entities < mediator > logic_entities ;
        typedef _logic_fidget < mediator > logic_fidget ;
        typedef _logic_game < mediator > logic_game ;
        typedef _logic_image < mediator > logic_image ;
        typedef _logic_land < mediator > logic_land ;
        typedef _logic_sound < mediator > logic_sound ;
        typedef _logic_text < mediator > logic_text ;
        typedef _logic_title < mediator > logic_title ;
        typedef _logic_touch < mediator > logic_touch ;
    } ;
} ;

template < typename mediator_types >
class shy_mediator
{
public :
    typedef typename mediator_types :: platform platform ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_mesh :: mesh_id mesh_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_texture :: texture_id texture_id ;
    typedef typename platform :: float_32 float_32 ;
    typedef typename platform :: int_32 int_32 ;
    typedef typename platform :: index_data index_data ;
    typedef typename platform :: matrix_data matrix_data ;
    typedef typename platform :: texel_data texel_data ;
    typedef typename platform :: texture_resource_id texture_resource_id ;
    typedef typename platform :: vector_data vector_data ;
    typedef typename platform :: vertex_data vertex_data ;
public :
    shy_mediator ( ) ;
public :
    void application_render ( ) ;
    void application_update ( ) ;
    void camera_matrix_look_at ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up ) ;
    void camera_prepare_permit ( ) ;
    void camera_prepared ( ) ;
    void camera_update ( ) ;
    void done ( ) ;
    void entities_prepared ( ) ;
    void fidget_prepared ( ) ;
    void game_render ( ) ;
    void game_update ( ) ;
    float_32 get_entity_height ( ) ;
    vector_data get_entity_origin ( int_32 index ) ;
    float_32 get_near_plane_distance ( ) ;
    void image_prepared ( ) ;
    void init ( ) ;
    void land_prepared ( ) ;
    template < typename T > T math_abs ( T f ) ;
    vector_data math_catmull_rom_spline ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 ) ;
    template < typename T > T math_clamp ( T f , T from , T to ) ;
    float_32 math_lerp ( float_32 from_value , float_32 from_weight , float_32 to_value , float_32 to_weight , float_32 weight ) ;
    template < typename T > T math_max ( T f1 , T f2 ) ;
    template < typename T > T math_min ( T f1 , T f2 ) ;
    float_32 math_pi ( ) ;
    mesh_id mesh_create 
        ( vertex_data * vertices 
        , index_data * triangle_strip_indices 
        , index_data * triangle_fan_indices
        , int_32 vertices_count
        , int_32 triangle_strip_indices_count 
        , int_32 triangle_fan_indices_count
        ) ;
    void mesh_render ( mesh_id arg_mesh_id ) ;
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform ) ;
    void prepare_entities ( ) ;
    void prepare_fidget ( ) ;
    void prepare_image ( ) ;
    void prepare_land ( ) ;
    void prepare_sound ( ) ;
    void prepare_text ( ) ;
    void prepare_touch ( ) ;
    void rasterize_ellipse_in_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 ) ;
    void rasterize_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 ) ;
    void rasterize_triangle ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 , int_32 x3 , int_32 y3 ) ;
    void rasterize_use_texture ( texture_id arg_texture_id , int_32 origin_x , int_32 origin_y ) ;
    void rasterize_use_texel ( const texel_data & texel ) ;
    void render ( ) ;
    void render_entities ( ) ;
    void render_fidget ( ) ;
    void render_image ( ) ;
    void render_land ( ) ;
    void render_text ( ) ;
    void render_touch ( ) ;
    void sound_prepared ( ) ;
    void text_prepared ( ) ;
    texture_id texture_create ( ) ;
    void texture_finalize ( texture_id arg_texture_id ) ;
    int_32 texture_height ( ) ;
    void texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id ) ;
    void texture_select ( texture_id arg_texture_id ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , const texel_data & texel ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a ) ;
    void texture_unselect ( ) ;
    int_32 texture_width ( ) ;
    void title_finished ( ) ;
    void title_launch_permit ( ) ;
    void title_render ( ) ;
    void title_update ( ) ;
    void touch_prepared ( ) ;
    void update ( ) ;
    void use_camera_matrix ( ) ;
    void use_ortho_projection ( ) ;
    void use_perspective_projection ( ) ;
    void video_mode_changed ( ) ;
private :
    typename mediator_types :: template modules < shy_mediator > :: engine_camera _engine_camera ;
    typename mediator_types :: template modules < shy_mediator > :: engine_math _engine_math ;
    typename mediator_types :: template modules < shy_mediator > :: engine_mesh _engine_mesh ;
    typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer _engine_rasterizer ;
    typename mediator_types :: template modules < shy_mediator > :: engine_texture _engine_texture ;
    typename mediator_types :: template modules < shy_mediator > :: logic _logic ;
    typename mediator_types :: template modules < shy_mediator > :: logic_application _logic_application ;
    typename mediator_types :: template modules < shy_mediator > :: logic_camera _logic_camera ;
    typename mediator_types :: template modules < shy_mediator > :: logic_entities _logic_entities ;
    typename mediator_types :: template modules < shy_mediator > :: logic_fidget _logic_fidget ;
    typename mediator_types :: template modules < shy_mediator > :: logic_game _logic_game ;
    typename mediator_types :: template modules < shy_mediator > :: logic_image _logic_image ;
    typename mediator_types :: template modules < shy_mediator > :: logic_land _logic_land ;
    typename mediator_types :: template modules < shy_mediator > :: logic_sound _logic_sound ;
    typename mediator_types :: template modules < shy_mediator > :: logic_text _logic_text ;
    typename mediator_types :: template modules < shy_mediator > :: logic_title _logic_title ;
    typename mediator_types :: template modules < shy_mediator > :: logic_touch _logic_touch ;
} ;

template < typename mediator_types >
shy_mediator < mediator_types > :: shy_mediator ( )
: _engine_rasterizer ( this )
, _logic ( this )
, _logic_application ( this )
, _logic_camera ( this )
, _logic_entities ( this )
, _logic_fidget ( this )
, _logic_game ( this )
, _logic_image ( this )
, _logic_land ( this )
, _logic_sound ( this )
, _logic_text ( this )
, _logic_title ( this )
, _logic_touch ( this )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: application_render ( )
{
    _logic_application . application_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: application_update ( )
{
    _logic_application . application_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: camera_matrix_look_at
    ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up )
{
    _engine_camera . camera_matrix_look_at ( matrix , from , to , norm_up ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: camera_prepared ( )
{
    _logic . camera_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: camera_update ( )
{
    _logic_camera . camera_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: done ( )
{
    _logic . done ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: entities_prepared ( )
{
    _logic . entities_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: fidget_prepared ( )
{
    _logic . fidget_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: game_render ( )
{
    _logic_game . render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: game_update ( )
{
    _logic_game . update ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: float_32
shy_mediator < mediator_types > :: get_entity_height ( )
{
    return _logic_entities . get_entity_height ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: vector_data
shy_mediator < mediator_types > :: get_entity_origin ( int_32 index )
{
    return _logic_entities . get_entity_origin ( index ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: float_32
shy_mediator < mediator_types > :: get_near_plane_distance ( )
{
    return _logic . get_near_plane_distance ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: image_prepared ( )
{
    _logic . image_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: init ( )
{
    _logic . init ( ) ;
    _logic_sound . init ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: land_prepared ( )
{
    _logic . land_prepared ( ) ;
}

template < typename mediator_types >
template < typename T >
T shy_mediator < mediator_types > :: math_abs ( T f )
{
    return _engine_math . math_abs < T > ( f ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: vector_data
shy_mediator < mediator_types > :: math_catmull_rom_spline
    ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
{
    return _engine_math . math_catmull_rom_spline ( t , p0 , p1 , p2 , p3 ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: float_32 
shy_mediator < mediator_types > :: math_lerp 
    ( float_32 from_value , float_32 from_weight , float_32 to_value , float_32 to_weight , float_32 weight )
{
    return _engine_math . math_lerp ( from_value , from_weight , to_value , to_weight , weight ) ;
}

template < typename mediator_types >
template < typename T >
T shy_mediator < mediator_types > :: math_clamp ( T f , T from , T to )
{
    return _engine_math . math_clamp < T > ( f , from , to ) ;
}

template < typename mediator_types >
template < typename T >
T shy_mediator < mediator_types > :: math_max ( T f1 , T f2 )
{
    return _engine_math . math_max < T > ( f1 , f2 ) ;
}

template < typename mediator_types >
template < typename T >
T shy_mediator < mediator_types > :: math_min ( T f1 , T f2 )
{
    return _engine_math . math_min < T > ( f1 , f2 ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: float_32
shy_mediator < mediator_types > :: math_pi ( )
{
    return _engine_math . math_pi ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: mesh_id
shy_mediator < mediator_types > :: mesh_create 
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

template < typename mediator_types >
void shy_mediator < mediator_types > :: mesh_render ( mesh_id arg_mesh_id )
{
    _engine_mesh . mesh_render ( arg_mesh_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: mesh_set_transform
    ( mesh_id arg_mesh_id , const matrix_data & transform )
{
    _engine_mesh . mesh_set_transform ( arg_mesh_id , transform ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: camera_prepare_permit ( )
{
    _logic_camera . camera_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_entities ( )
{
    _logic_entities . prepare_entities ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_fidget ( )
{
    _logic_fidget . prepare_fidget ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_image ( )
{
    _logic_image . prepare_image ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_land ( )
{
    _logic_land . prepare_land ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_sound ( )
{
    _logic_sound . prepare_sound ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_text ( )
{
    _logic_text . prepare_text ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: prepare_touch ( )
{
    _logic_touch . prepare_touch ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_ellipse_in_rect
    ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 )
{
    _engine_rasterizer . rasterize_ellipse_in_rect ( x1 , y1 , x2 , y2 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_rect
    ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 )
{
    _engine_rasterizer . rasterize_rect ( x1 , y1 , x2 , y2 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_use_texture 
    ( texture_id arg_texture_id , int_32 origin_x , int_32 origin_y )
{
    _engine_rasterizer . rasterize_use_texture ( arg_texture_id , origin_x , origin_y ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_use_texel
    ( const texel_data & texel )
{
    _engine_rasterizer . rasterize_use_texel ( texel ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_triangle
    ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 , int_32 x3 , int_32 y3 )
{
    _engine_rasterizer . rasterize_triangle ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render ( )
{
    _logic . render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render_entities ( )
{
    _logic_entities . render_entities ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render_fidget ( )
{
    _logic_fidget . render_fidget ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render_image ( )
{
    _logic_image . render_image ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render_land ( )
{
    _logic_land . render_land ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render_text ( )
{
    _logic_text . render_text ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: render_touch ( )
{
    _logic_touch . render_touch ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sound_prepared ( )
{
    _logic . sound_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: text_prepared ( )
{
    _logic . text_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: update ( )
{
    _logic . update ( ) ;
    _logic_camera . update ( ) ;
    _logic_entities . update ( ) ;
    _logic_fidget . update ( ) ;
    _logic_image . update ( ) ;
    _logic_land . update ( ) ;
    _logic_sound . update ( ) ;
    _logic_text . update ( ) ;
    _logic_touch . update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: use_camera_matrix ( )
{
    _logic_camera . use_camera_matrix ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: texture_id 
shy_mediator < mediator_types > :: texture_create ( )
{
    return _engine_texture . texture_create ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_finalize ( texture_id arg_texture_id )
{
    _engine_texture . texture_finalize ( arg_texture_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_load_from_resource 
    ( texture_id arg_texture_id 
    , texture_resource_id arg_resource_id 
    )
{
    _engine_texture . texture_load_from_resource ( arg_texture_id , arg_resource_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_select ( texture_id arg_texture_id )
{
    _engine_texture . texture_select ( arg_texture_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_set_texel 
    ( texture_id arg_texture_id , int_32 x , int_32 y , const texel_data & texel )
{
    _engine_texture . texture_set_texel ( arg_texture_id , x , y , texel ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_set_texel 
    ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a )
{
    _engine_texture . texture_set_texel ( arg_texture_id , x , y , r , g , b , a ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_unselect ( )
{
    _engine_texture . texture_unselect ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: int_32
shy_mediator < mediator_types > :: texture_height ( )
{
    return _engine_texture . texture_height ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: int_32
shy_mediator < mediator_types > :: texture_width ( )
{
    return _engine_texture . texture_width ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: title_finished ( )
{
    _logic . title_finished ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: title_launch_permit ( )
{
    _logic_title . title_launch_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: title_render ( )
{
    _logic_title . title_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: title_update ( )
{
    _logic_title . title_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: touch_prepared ( )
{
    _logic . touch_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: video_mode_changed ( )
{
    _logic . video_mode_changed ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: use_perspective_projection ( )
{
    _logic . use_perspective_projection ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: use_ortho_projection ( )
{
    _logic . use_ortho_projection ( ) ;
}
