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
    typedef typename platform :: num_fract num_fract ;
    typedef typename platform :: num_whole num_whole ;
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
    void camera_matrix_use ( ) ;
    void camera_prepare_permit ( ) ;
    void camera_prepared ( ) ;
    void camera_update ( ) ;
    void done ( ) ;
    void entities_prepare_permit ( ) ;
    void entities_prepared ( ) ;
    void entities_render ( ) ;
    void entities_update ( ) ;
    void fidget_prepare_permit ( ) ;
    void fidget_prepared ( ) ;
    void fidget_render ( ) ;
    void fidget_update ( ) ;
    void game_launch_permit ( ) ;
    void game_render ( ) ;
    void game_update ( ) ;
    void get_entity_height ( float_32 & result ) ;
    void get_entity_mesh_grid ( int_32 & result ) ;
    void get_entity_origin ( vector_data & result , int_32 index ) ;
    void get_near_plane_distance ( num_fract & result ) ;
    void image_prepare_permit ( ) ;
    void image_prepared ( ) ;
    void image_render ( ) ;
    void image_update ( ) ;
    void init ( ) ;
    void land_prepare_permit ( ) ;
    void land_prepared ( ) ;
    void land_render ( ) ;
    void land_update ( ) ;
    template < typename T > void math_abs ( T & result , T f ) ;
    void math_abs_whole ( num_whole & result , num_whole a ) ;
    void math_catmull_rom_spline ( vector_data & result , float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 ) ;
    template < typename T > void math_clamp ( T & result , T f , T from , T to ) ;
    void math_clamp_fract ( num_fract & result , num_fract num , num_fract from , num_fract to ) ;
    void math_lerp ( float_32 & result , float_32 from_value , float_32 from_weight , float_32 to_value , float_32 to_weight , float_32 weight ) ;
    void math_lerp ( num_fract & result , num_fract from_value , num_fract from_weight , num_fract to_value , num_fract to_weight , num_fract weight ) ;
    template < typename T > void math_max ( T & result , T f1 , T f2 ) ;
    void math_max_whole ( num_whole & result , num_whole a , num_whole b ) ;
    template < typename T > void math_min ( T & result , T f1 , T f2 ) ;
    void math_min_whole ( num_whole & result , num_whole a , num_whole b ) ;
    void mesh_create 
        ( mesh_id & result
        , vertex_data * vertices 
        , index_data * triangle_strip_indices 
        , index_data * triangle_fan_indices
        , num_whole vertices_count
        , num_whole triangle_strip_indices_count 
        , num_whole triangle_fan_indices_count
        ) ;
    void mesh_render ( mesh_id arg_mesh_id ) ;
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform ) ;
    void rasterize_ellipse_in_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 ) ;
    void rasterize_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 ) ;
    void rasterize_triangle ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 , int_32 x3 , int_32 y3 ) ;
    void rasterize_use_texture ( texture_id arg_texture_id , int_32 origin_x , int_32 origin_y ) ;
    void rasterize_use_texel ( const texel_data & texel ) ;
    void render ( ) ;
    void sound_prepare_permit ( ) ;
    void sound_prepared ( ) ;
    void sound_update ( ) ;
    void text_prepare_permit ( ) ;
    void text_prepared ( ) ;
    void text_render ( ) ;
    void text_update ( ) ;
    void texture_create ( texture_id & result ) ;
    void texture_finalize ( texture_id arg_texture_id ) ;
    void texture_height ( int_32 & result ) ;
    void texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id ) ;
    void texture_select ( texture_id arg_texture_id ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , const texel_data & texel ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a ) ;
    void texture_unselect ( ) ;
    void texture_width ( int_32 & result ) ;
    void title_finished ( ) ;
    void title_launch_permit ( ) ;
    void title_render ( ) ;
    void title_update ( ) ;
    void touch_prepare_permit ( ) ;
    void touch_prepared ( ) ;
    void touch_render ( ) ;
    void touch_update ( ) ;
    void update ( ) ;
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
    _logic_game . camera_prepared ( ) ;
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
    _logic_game . entities_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: fidget_prepared ( )
{
    _logic . fidget_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: game_render ( )
{
    _logic_game . game_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: game_update ( )
{
    _logic_game . game_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_entity_height ( float_32 & result )
{
    _logic_entities . get_entity_height ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_entity_mesh_grid ( int_32 & result )
{
    _logic_entities . get_entity_mesh_grid ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_entity_origin ( vector_data & result , int_32 index )
{
    _logic_entities . get_entity_origin ( result , index ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_near_plane_distance ( num_fract & result )
{
    _logic . get_near_plane_distance ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: image_prepared ( )
{
    _logic_game . image_prepared ( ) ;
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
    _logic_game . land_prepared ( ) ;
}

template < typename mediator_types >
template < typename T >
void shy_mediator < mediator_types > :: math_abs ( T & result , T f )
{
    _engine_math . math_abs < T > ( result , f ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_abs_whole ( num_whole & result , num_whole a )
{
    _engine_math . math_abs_whole ( result , a ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_catmull_rom_spline
    ( vector_data & result , float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
{
    _engine_math . math_catmull_rom_spline ( result , t , p0 , p1 , p2 , p3 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_lerp 
    ( float_32 & result , float_32 from_value , float_32 from_weight , float_32 to_value , float_32 to_weight , float_32 weight )
{
    _engine_math . math_lerp ( result , from_value , from_weight , to_value , to_weight , weight ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_clamp_fract ( num_fract & result , num_fract f , num_fract from , num_fract to )
{
    _engine_math . math_clamp_fract ( result , f , from , to ) ;
}

template < typename mediator_types >
template < typename T >
void shy_mediator < mediator_types > :: math_clamp ( T & result , T f , T from , T to )
{
    _engine_math . math_clamp < T > ( result , f , from , to ) ;
}

template < typename mediator_types >
template < typename T >
void shy_mediator < mediator_types > :: math_max ( T & result , T f1 , T f2 )
{
    _engine_math . math_max < T > ( result , f1 , f2 ) ;
}

template < typename mediator_types >
template < typename T >
void shy_mediator < mediator_types > :: math_min ( T & result , T f1 , T f2 )
{
    _engine_math . math_min < T > ( result , f1 , f2 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_max_whole ( num_whole & result , num_whole a , num_whole b )
{
    _engine_math . math_max_whole ( result , a , b ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_min_whole ( num_whole & result , num_whole a , num_whole b )
{
    _engine_math . math_min_whole ( result , a , b ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: mesh_create 
    ( mesh_id & result
    , vertex_data * vertices 
    , index_data * triangle_strip_indices 
    , index_data * triangle_fan_indices
    , num_whole vertices_count
    , num_whole triangle_strip_indices_count 
    , num_whole triangle_fan_indices_count
    )
{
    _engine_mesh . mesh_create 
        ( result
        , vertices
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
void shy_mediator < mediator_types > :: entities_prepare_permit ( )
{
    _logic_entities . entities_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: fidget_prepare_permit ( )
{
    _logic_fidget . fidget_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: image_prepare_permit ( )
{
    _logic_image . image_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: land_prepare_permit ( )
{
    _logic_land . land_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sound_prepare_permit ( )
{
    _logic_sound . sound_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: text_prepare_permit ( )
{
    _logic_text . text_prepare_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: touch_prepare_permit ( )
{
    _logic_touch . touch_prepare_permit ( ) ;
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
void shy_mediator < mediator_types > :: entities_render ( )
{
    _logic_entities . entities_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: fidget_render ( )
{
    _logic_fidget . fidget_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: image_render ( )
{
    _logic_image . image_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: land_render ( )
{
    _logic_land . land_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: text_render ( )
{
    _logic_text . text_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: touch_render ( )
{
    _logic_touch . touch_render ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sound_prepared ( )
{
    _logic_game . sound_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: text_prepared ( )
{
    _logic_game . text_prepared ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: update ( )
{
    _logic . update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: touch_update ( )
{
    _logic_touch . touch_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: text_update ( )
{
    _logic_text . text_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sound_update ( )
{
    _logic_sound . sound_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: land_update ( )
{
    _logic_land . land_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: image_update ( )
{
    _logic_image . image_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: fidget_update ( )
{
    _logic_fidget . fidget_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: entities_update ( )
{
    _logic_entities . entities_update ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: camera_matrix_use ( )
{
    _logic_camera . camera_matrix_use ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_create ( texture_id & result )
{
    _engine_texture . texture_create ( result ) ;
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
void shy_mediator < mediator_types > :: texture_height ( int_32 & result )
{
    _engine_texture . texture_height ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_width ( int_32 & result )
{
    _engine_texture . texture_width ( result ) ;
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
    _logic_game . touch_prepared ( ) ;
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

template < typename mediator_types >
void shy_mediator < mediator_types > :: game_launch_permit ( )
{
    _logic_game . game_launch_permit ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: math_lerp 
    ( num_fract & result , num_fract from_value , num_fract from_weight , num_fract to_value , num_fract to_weight , num_fract weight )
{
    _engine_math . math_lerp ( result , from_value , from_weight , to_value , to_weight , weight ) ;
}
