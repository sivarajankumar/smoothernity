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
    class messages ;

    typedef typename mediator_types :: platform platform ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_camera engine_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_math engine_math ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_mesh :: mesh_id mesh_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_texture :: texture_id texture_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text :: letter_id letter_id ;
    
private :
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_mesh engine_mesh ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer engine_rasterizer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_texture engine_texture ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_texture :: texture_consts_type texture_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic logic ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application logic_application ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera logic_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities logic_entities ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget logic_fidget ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game logic_game ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image logic_image ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_land logic_land ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_sound logic_sound ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text logic_text ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text :: logic_text_consts_type logic_text_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title logic_title ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch logic_touch ;
    typedef typename platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
    typedef typename platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename platform :: platform_pointer platform_pointer ;
    typedef typename platform :: platform_render :: index_data index_data ;
    typedef typename platform :: platform_render :: texel_data texel_data ;
    typedef typename platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename platform :: platform_render :: vertex_data vertex_data ;
    typedef typename platform :: platform_vector :: vector_data vector_data ;
    
public :
    class messages
    {
    public :
        class application_render { } ;
        class application_update { } ;
        class camera_matrix_use { } ;
        class camera_prepare_permit { } ;
        class camera_prepared { } ;
        class camera_update { } ;
        class done { } ;
        class entities_done { } ;
        class entities_height_reply { public : num_fract height ; } ;
        class entities_height_request { } ;
        class entities_mesh_grid_reply { public : num_whole grid ; } ;
        class entities_mesh_grid_request { } ;
        class entities_origin_reply { public : vector_data origin ; num_whole index ; } ;
        class entities_origin_request { public : num_whole index ; } ;
        class entities_prepare_permit { } ;
        class entities_prepared { } ;
        class entities_render { } ;
        class entities_update { } ;
        class fidget_done { } ;
        class fidget_prepare_permit { } ;
        class fidget_prepared { } ;
        class fidget_render { } ;
        class fidget_update { } ;
        class game_launch_permit { } ;
        class game_render { } ;
        class game_update { } ;
        class image_done { } ;
        class image_prepare_permit { } ;
        class image_prepared { } ;
        class image_render { } ;
        class image_update { } ;
        class init { } ;
        class land_done { } ;
        class land_prepare_permit { } ;
        class land_prepared { } ;
        class land_render { } ;
        class land_update { } ;
        class mesh_delete { public : mesh_id mesh ; } ;
        class mesh_render { public : mesh_id mesh ; } ;
        class mesh_set_transform { public : mesh_id mesh ; matrix_data transform ; } ;
        class near_plane_distance_reply { public : num_fract distance ; } ;
        class near_plane_distance_request { } ;
        class rasterize_ellipse_in_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_triangle { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; num_whole x3 ; num_whole y3 ; } ;
        class rasterize_use_texel { public : texel_data texel ; } ;
        class rasterize_use_texture { public : texture_id texture ; num_whole origin_x ; num_whole origin_y ; } ;
        class render { } ;
        class sound_prepare_permit { } ;
        class sound_prepared { } ;
        class sound_update { } ;
        class text_done { } ;
        class text_letter_big_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; } ;
        class text_letter_big_tex_coords_request { public : letter_id letter ; } ;
        class text_letter_small_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; } ;
        class text_letter_small_tex_coords_request { public : letter_id letter ; } ;
        class text_prepare_permit { } ;
        class text_prepared { } ;
        class text_render { } ;
        class text_update { } ;
        class texture_create_reply { public : texture_id texture ; } ;
        class texture_create_request { } ;
        class texture_finalize { public : texture_id texture ; } ;
        class texture_load_from_resource { public : texture_id texture ; texture_resource_id resource ; } ;
        class texture_select { public : texture_id texture ; } ;
        class texture_set_texel { public : texture_id texture ; num_whole x ; num_whole y ; texel_data texel ; } ;
        class texture_set_texel_rgba { public : texture_id texture ; num_whole x ; num_whole y ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class texture_set_texels_rect { public : texture_id texture ; num_whole left ; num_whole bottom ; num_whole right ; num_whole top ; texel_data texel ; } ;
        class texture_unselect { } ;
        class title_done { } ;
        class title_finished { } ;
        class title_launch_permit { } ;
        class title_render { } ;
        class title_update { } ;
        class touch_done { } ;
        class touch_prepare_permit { } ;
        class touch_prepared { } ;
        class touch_render { } ;
        class touch_update { } ;
        class update { } ;
        class use_ortho_projection { } ;
        class use_perspective_projection { } ;
        class use_text_texture { } ;
        class video_mode_changed { } ;
    } ;
    
public :
    shy_mediator ( ) ;
    void register_modules 
        ( typename platform_pointer :: template pointer < engine_mesh > arg_engine_mesh
        , typename platform_pointer :: template pointer < engine_rasterizer > arg_engine_rasterizer
        , typename platform_pointer :: template pointer < engine_texture > arg_engine_texture
        , typename platform_pointer :: template pointer < logic > arg_logic
        , typename platform_pointer :: template pointer < logic_application > arg_logic_application
        , typename platform_pointer :: template pointer < logic_camera > arg_logic_camera
        , typename platform_pointer :: template pointer < logic_entities > arg_logic_entities
        , typename platform_pointer :: template pointer < logic_fidget > arg_logic_fidget
        , typename platform_pointer :: template pointer < logic_game > arg_logic_game
        , typename platform_pointer :: template pointer < logic_image > arg_logic_image
        , typename platform_pointer :: template pointer < logic_land > arg_logic_land
        , typename platform_pointer :: template pointer < logic_sound > arg_logic_sound
        , typename platform_pointer :: template pointer < logic_text > arg_logic_text
        , typename platform_pointer :: template pointer < logic_title > arg_logic_title
        , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
        ) ;
public :
    void send ( typename messages :: application_render msg ) ;
    void send ( typename messages :: application_update msg ) ;
    void send ( typename messages :: camera_matrix_use msg ) ;
    void send ( typename messages :: camera_prepare_permit msg ) ;
    void send ( typename messages :: camera_prepared msg ) ;
    void send ( typename messages :: camera_update msg ) ;
    void send ( typename messages :: done msg ) ;
    void send ( typename messages :: entities_done msg ) ;
    void send ( typename messages :: entities_height_reply msg ) ;
    void send ( typename messages :: entities_height_request msg ) ;
    void send ( typename messages :: entities_mesh_grid_reply msg ) ;
    void send ( typename messages :: entities_mesh_grid_request msg ) ;
    void send ( typename messages :: entities_origin_reply msg ) ;
    void send ( typename messages :: entities_origin_request msg ) ;
    void send ( typename messages :: entities_prepare_permit msg ) ;
    void send ( typename messages :: entities_prepared msg ) ;
    void send ( typename messages :: entities_render msg ) ;
    void send ( typename messages :: entities_update msg ) ;
    void send ( typename messages :: fidget_done msg ) ;
    void send ( typename messages :: fidget_prepare_permit msg ) ;
    void send ( typename messages :: fidget_prepared msg ) ;
    void send ( typename messages :: fidget_render msg ) ;
    void send ( typename messages :: fidget_update msg ) ;
    void send ( typename messages :: game_launch_permit msg ) ;
    void send ( typename messages :: game_render msg ) ;
    void send ( typename messages :: game_update msg ) ;
    void send ( typename messages :: image_done msg ) ;
    void send ( typename messages :: image_prepare_permit msg ) ;
    void send ( typename messages :: image_prepared msg ) ;
    void send ( typename messages :: image_render msg ) ;
    void send ( typename messages :: image_update msg ) ;
    void send ( typename messages :: init msg ) ;
    void send ( typename messages :: land_done msg ) ;
    void send ( typename messages :: land_prepare_permit msg ) ;
    void send ( typename messages :: land_prepared msg ) ;
    void send ( typename messages :: land_render msg ) ;
    void send ( typename messages :: land_update msg ) ;
    void send ( typename messages :: mesh_delete msg ) ;
    void send ( typename messages :: mesh_render msg ) ;
    void send ( typename messages :: mesh_set_transform msg ) ;
    void send ( typename messages :: near_plane_distance_reply msg ) ;
    void send ( typename messages :: near_plane_distance_request msg ) ;
    void send ( typename messages :: rasterize_ellipse_in_rect msg ) ;
    void send ( typename messages :: rasterize_rect msg ) ;
    void send ( typename messages :: rasterize_triangle msg ) ;
    void send ( typename messages :: rasterize_use_texel msg ) ;
    void send ( typename messages :: rasterize_use_texture msg ) ;
    void send ( typename messages :: render msg ) ;
    void send ( typename messages :: sound_prepare_permit msg ) ;
    void send ( typename messages :: sound_prepared msg ) ;
    void send ( typename messages :: sound_update msg ) ;
    void send ( typename messages :: text_done msg ) ;
    void send ( typename messages :: text_letter_big_tex_coords_reply msg ) ;
    void send ( typename messages :: text_letter_big_tex_coords_request msg ) ;
    void send ( typename messages :: text_letter_small_tex_coords_reply msg ) ;
    void send ( typename messages :: text_letter_small_tex_coords_request msg ) ;
    void send ( typename messages :: text_prepare_permit msg ) ;
    void send ( typename messages :: text_prepared msg ) ;
    void send ( typename messages :: text_render msg ) ;
    void send ( typename messages :: text_update msg ) ;
    void send ( typename messages :: texture_create_reply msg ) ;
    void send ( typename messages :: texture_create_request msg ) ;
    void send ( typename messages :: texture_finalize msg ) ;
    void send ( typename messages :: texture_load_from_resource msg ) ;
    void send ( typename messages :: texture_select msg ) ;
    void send ( typename messages :: texture_set_texel msg ) ;
    void send ( typename messages :: texture_set_texel_rgba msg ) ;
    void send ( typename messages :: texture_set_texels_rect msg ) ;
    void send ( typename messages :: texture_unselect msg ) ;
    void send ( typename messages :: title_done msg ) ;
    void send ( typename messages :: title_finished msg ) ;
    void send ( typename messages :: title_launch_permit msg ) ;
    void send ( typename messages :: title_render msg ) ;
    void send ( typename messages :: title_update msg ) ;
    void send ( typename messages :: touch_done msg ) ;
    void send ( typename messages :: touch_prepare_permit msg ) ;
    void send ( typename messages :: touch_prepared msg ) ;
    void send ( typename messages :: touch_render msg ) ;
    void send ( typename messages :: touch_update msg ) ;
    void send ( typename messages :: update msg ) ;
    void send ( typename messages :: use_ortho_projection msg ) ;
    void send ( typename messages :: use_perspective_projection msg ) ;
    void send ( typename messages :: use_text_texture msg ) ;
    void send ( typename messages :: video_mode_changed msg ) ;
public :
    const texture_consts_type & texture_consts ( ) ;
    const logic_text_consts_type & logic_text_consts ( ) ;
public :
    void get_big_letter_tex_coords ( num_fract & left , num_fract & bottom , num_fract & right , num_fract & top , letter_id letter ) ;
    void get_small_letter_tex_coords ( num_fract & left , num_fract & bottom , num_fract & right , num_fract & top , letter_id letter ) ;
    template 
        < typename vertex_array 
        , typename strip_index_array
        , typename fan_index_array
        >
    void mesh_create 
        ( mesh_id & result
        , const vertex_array & vertices 
        , const strip_index_array & triangle_strip_indices 
        , const fan_index_array & triangle_fan_indices
        , num_whole vertices_count
        , num_whole triangle_strip_indices_count 
        , num_whole triangle_fan_indices_count
        ) ;
private :
    typename platform_pointer :: template pointer < engine_mesh > _engine_mesh ;
    typename platform_pointer :: template pointer < engine_rasterizer > _engine_rasterizer ;
    typename platform_pointer :: template pointer < engine_texture > _engine_texture ;
    typename platform_pointer :: template pointer < logic > _logic ;
    typename platform_pointer :: template pointer < logic_application > _logic_application ;
    typename platform_pointer :: template pointer < logic_camera > _logic_camera ;
    typename platform_pointer :: template pointer < logic_entities > _logic_entities ;
    typename platform_pointer :: template pointer < logic_fidget > _logic_fidget ;
    typename platform_pointer :: template pointer < logic_game > _logic_game ;
    typename platform_pointer :: template pointer < logic_image > _logic_image ;
    typename platform_pointer :: template pointer < logic_land > _logic_land ;
    typename platform_pointer :: template pointer < logic_sound > _logic_sound ;
    typename platform_pointer :: template pointer < logic_text > _logic_text ;
    typename platform_pointer :: template pointer < logic_title > _logic_title ;
    typename platform_pointer :: template pointer < logic_touch > _logic_touch ;
} ;

template < typename mediator_types >
shy_mediator < mediator_types > :: shy_mediator ( )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: register_modules 
    ( typename platform_pointer :: template pointer < engine_mesh > arg_engine_mesh
    , typename platform_pointer :: template pointer < engine_rasterizer > arg_engine_rasterizer
    , typename platform_pointer :: template pointer < engine_texture > arg_engine_texture
    , typename platform_pointer :: template pointer < logic > arg_logic
    , typename platform_pointer :: template pointer < logic_application > arg_logic_application
    , typename platform_pointer :: template pointer < logic_camera > arg_logic_camera
    , typename platform_pointer :: template pointer < logic_entities > arg_logic_entities
    , typename platform_pointer :: template pointer < logic_fidget > arg_logic_fidget
    , typename platform_pointer :: template pointer < logic_game > arg_logic_game
    , typename platform_pointer :: template pointer < logic_image > arg_logic_image
    , typename platform_pointer :: template pointer < logic_land > arg_logic_land
    , typename platform_pointer :: template pointer < logic_sound > arg_logic_sound
    , typename platform_pointer :: template pointer < logic_text > arg_logic_text
    , typename platform_pointer :: template pointer < logic_title > arg_logic_title
    , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
    )
{
    _engine_mesh = arg_engine_mesh ;
    _engine_rasterizer = arg_engine_rasterizer ;
    _engine_texture = arg_engine_texture ;
    _logic = arg_logic ;
    _logic_application = arg_logic_application ;
    _logic_camera = arg_logic_camera ;
    _logic_entities = arg_logic_entities ;
    _logic_fidget = arg_logic_fidget ;
    _logic_game = arg_logic_game ;
    _logic_image = arg_logic_image ;
    _logic_land = arg_logic_land ;
    _logic_sound = arg_logic_sound ;
    _logic_text = arg_logic_text ;
    _logic_title = arg_logic_title ;
    _logic_touch = arg_logic_touch ;

    _engine_rasterizer . get ( ) . set_mediator ( * this ) ;
    _engine_texture . get ( ) . set_mediator ( * this ) ;
    _logic . get ( ) . set_mediator ( * this ) ;
    _logic_application . get ( ) . set_mediator ( * this ) ;
    _logic_camera . get ( ) . set_mediator ( * this ) ;
    _logic_entities . get ( ) . set_mediator ( * this ) ;
    _logic_fidget . get ( ) . set_mediator ( * this ) ;
    _logic_game . get ( ) . set_mediator ( * this ) ;
    _logic_image . get ( ) . set_mediator ( * this ) ;
    _logic_land . get ( ) . set_mediator ( * this ) ;
    _logic_sound . get ( ) . set_mediator ( * this ) ;
    _logic_text . get ( ) . set_mediator ( * this ) ;
    _logic_title . get ( ) . set_mediator ( * this ) ;
    _logic_touch . get ( ) . set_mediator ( * this ) ;
}

template < typename mediator_types >
const typename shy_mediator < mediator_types > :: texture_consts_type &
shy_mediator < mediator_types > :: texture_consts ( )
{
    return _engine_texture . get ( ) . texture_consts ;
}

template < typename mediator_types >
const typename shy_mediator < mediator_types > :: logic_text_consts_type &
shy_mediator < mediator_types > :: logic_text_consts ( )
{
    return _logic_text . get ( ) . logic_text_consts ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: application_render msg )
{
    _logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: application_update msg )
{
    _logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: camera_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: camera_update msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: done msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_prepared msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: game_render msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: game_update msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_height_reply msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_height_request msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_mesh_grid_reply msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_mesh_grid_request msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_origin_reply msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_origin_request msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: near_plane_distance_request msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: near_plane_distance_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: init msg )
{
    _logic . get ( ) . receive ( msg ) ;
    _logic_sound . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
template 
    < typename vertex_array
    , typename strip_index_array
    , typename fan_index_array
    >
void shy_mediator < mediator_types > :: mesh_create 
    ( mesh_id & result
    , const vertex_array & vertices 
    , const strip_index_array & triangle_strip_indices 
    , const fan_index_array & triangle_fan_indices
    , num_whole vertices_count
    , num_whole triangle_strip_indices_count 
    , num_whole triangle_fan_indices_count
    )
{
    _engine_mesh . get ( ) . mesh_create
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
void shy_mediator < mediator_types > :: send ( typename messages :: mesh_delete msg )
{
    _engine_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: mesh_render msg )
{
    _engine_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: mesh_set_transform msg )
{
    _engine_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: camera_prepare_permit msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_prepare_permit msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_prepare_permit msg )
{
    _logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_prepare_permit msg )
{
    _logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_prepare_permit msg )
{
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: sound_prepare_permit msg )
{
    _logic_sound . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_prepare_permit msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: touch_prepare_permit msg )
{
    _logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_use_texel msg )
{
    _engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_ellipse_in_rect msg )
{
    _engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_rect msg )
{
    _engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_use_texture msg )
{
    _engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_triangle msg )
{
    _engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_done msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_render msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_done msg )
{
    _logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_render msg )
{
    _logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_done msg )
{
    _logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_render msg )
{
    _logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_done msg )
{
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_render msg )
{
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_done msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_render msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: touch_done msg )
{
    _logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: touch_render msg )
{
    _logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: sound_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_prepared msg )
{
    _logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: update msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: touch_update msg )
{
    _logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_update msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: sound_update msg )
{
    _logic_sound . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_update msg )
{
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_update msg )
{
    _logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_update msg )
{
    _logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_update msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: camera_matrix_use msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_create_reply msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
    _logic_image . get ( ) . receive ( msg ) ;
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_create_request msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_finalize msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_load_from_resource msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_select msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_set_texel msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_set_texel_rgba msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_set_texels_rect msg ) 
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_unselect msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: title_finished msg )
{
    _logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: title_launch_permit msg )
{
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: title_done msg )
{
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: title_render msg )
{
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: title_update msg )
{
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: touch_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: video_mode_changed msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_perspective_projection msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_ortho_projection msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: game_launch_permit msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_text_texture msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_letter_big_tex_coords_reply msg )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_letter_big_tex_coords_request msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_letter_small_tex_coords_reply msg )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_letter_small_tex_coords_request msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_big_letter_tex_coords 
    ( num_fract & left 
    , num_fract & bottom 
    , num_fract & right 
    , num_fract & top 
    , letter_id letter 
    )
{
    _logic_text . get ( ) . get_big_letter_tex_coords ( left , bottom , right , top , letter ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_small_letter_tex_coords 
    ( num_fract & left 
    , num_fract & bottom 
    , num_fract & right 
    , num_fract & top 
    , letter_id letter 
    )
{
    _logic_text . get ( ) . get_small_letter_tex_coords ( left , bottom , right , top , letter ) ;
}

