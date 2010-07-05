template < typename mediator_types >
class shy_mediator
{
public :
    class messages ;

    typedef typename mediator_types :: platform platform ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_camera engine_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_math engine_math ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: mesh_id mesh_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: texture_id texture_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless logic_text_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: letter_id letter_id ;
    
private :
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer engine_rasterizer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render engine_render ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: engine_render_consts_type engine_render_consts_type ;
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
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: logic_text_consts_type logic_text_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title logic_title ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch logic_touch ;
    typedef typename mediator_types :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator_types :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator_types :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator_types :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator_types :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator_types :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator_types :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename mediator_types :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator_types :: platform :: platform_vector :: vector_data vector_data ;
    
public :
    class messages
    {
    public :
        class application_render { } ;
        class application_update { } ;
        class camera_matrix_reply { public : matrix_data matrix ; } ;
        class camera_matrix_request { } ;
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
        class entities_render_reply { } ;
        class entities_render_request { } ;
        class entities_update { } ;
        class fidget_done { } ;
        class fidget_prepare_permit { } ;
        class fidget_prepared { } ;
        class fidget_render_reply { } ;
        class fidget_render_request { } ;
        class fidget_update { } ;
        class game_launch_permit { } ;
        class game_render { } ;
        class game_update { } ;
        class image_done { } ;
        class image_prepare_permit { } ;
        class image_prepared { } ;
        class image_render_reply { } ;
        class image_render_request { } ;
        class image_update { } ;
        class init { } ;
        class land_done { } ;
        class land_prepare_permit { } ;
        class land_prepared { } ;
        class land_render_reply { } ;
        class land_render_request { } ;
        class land_update { } ;
        class near_plane_distance_reply { public : num_fract distance ; } ;
        class near_plane_distance_request { } ;
        class rasterize_ellipse_in_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_finalize_reply { } ;
        class rasterize_finalize_request { } ;
        class rasterize_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_triangle { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; num_whole x3 ; num_whole y3 ; } ;
        class rasterize_use_texel { public : texel_data texel ; } ;
        class rasterize_use_texture { public : texture_id texture ; num_whole origin_x ; num_whole origin_y ; } ;
        class render { } ;
        class render_blend_disable { } ;
        class render_blend_src_alpha_dst_one_minus_alpha { } ;
        class render_clear_screen { public : num_fract r ; num_fract g ; num_fract b ; } ;
        class render_disable_depth_test { } ;
        class render_enable_depth_test { } ;
        class render_enable_face_culling { } ;
        class render_fog_disable { } ;
        class render_fog_linear { public : num_fract znear ; num_fract zfar ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class render_matrix_identity { } ;
        class render_matrix_load { public : matrix_data matrix ; } ;
        class render_mesh_create_reply { public : mesh_id mesh ; } ;
        class render_mesh_create_request { public : num_whole vertices ; num_whole triangle_strip_indices ; num_whole triangle_fan_indices ; } ;
        class render_mesh_delete { public : mesh_id mesh ; } ;
        class render_mesh_finalize { public : mesh_id mesh ; } ;
        class render_mesh_render { public : mesh_id mesh ; } ;
        class render_mesh_set_transform { public : mesh_id mesh ; matrix_data transform ; } ;
        class render_mesh_set_triangle_fan_index_value { public : mesh_id mesh ; num_whole offset ; num_whole index ; } ;
        class render_mesh_set_triangle_strip_index_value { public : mesh_id mesh ; num_whole offset ; num_whole index ; } ;
        class render_mesh_set_vertex_color { public : mesh_id mesh ; num_whole offset ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class render_mesh_set_vertex_position { public : mesh_id mesh ; num_whole offset ; num_fract x ; num_fract y ; num_fract z ; } ;
        class render_mesh_set_vertex_tex_coord { public : mesh_id mesh ; num_whole offset ; num_fract u ; num_fract v ; } ;
        class render_projection_frustum { public : num_fract left ; num_fract right ; num_fract bottom ; num_fract top ; num_fract znear ; num_fract zfar ; } ;
        class render_projection_ortho { public : num_fract left ; num_fract right ; num_fract bottom ; num_fract top ; num_fract znear ; num_fract zfar ; } ;
        class render_texture_create_reply { public : texture_id texture ; } ;
        class render_texture_create_request { } ;
        class render_texture_finalize { public : texture_id texture ; } ;
        class render_texture_load_from_resource { public : texture_id texture ; texture_resource_id resource ; } ;
        class render_texture_loader_ready_reply { public : num_whole ready ; } ;
        class render_texture_loader_ready_request { } ;
        class render_texture_mode_modulate { } ;
        class render_texture_select { public : texture_id texture ; } ;
        class render_texture_set_texel { public : texture_id texture ; num_whole x ; num_whole y ; texel_data texel ; } ;
        class render_texture_set_texel_rgba { public : texture_id texture ; num_whole x ; num_whole y ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class render_texture_set_texels_rect { public : texture_id texture ; num_whole left ; num_whole bottom ; num_whole right ; num_whole top ; texel_data texel ; } ;
        class render_texture_unselect { } ;
        class sound_prepare_permit { } ;
        class sound_prepared { } ;
        class sound_update { } ;
        class text_done { } ;
        class text_letter_big_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; letter_id letter ; } ;
        class text_letter_big_tex_coords_request { public : letter_id letter ; } ;
        class text_letter_small_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; letter_id letter ; } ;
        class text_letter_small_tex_coords_request { public : letter_id letter ; } ;
        class text_prepare_permit { } ;
        class text_prepared { } ;
        class text_render_reply { } ;
        class text_render_request { } ;
        class text_update { } ;
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
        class use_ortho_projection_reply { } ;
        class use_ortho_projection_request { } ;
        class use_perspective_projection_reply { } ;
        class use_perspective_projection_request { } ;
        class use_text_texture_reply { } ;
        class use_text_texture_request { } ;
        class video_mode_changed { } ;
    } ;
    
public :
    shy_mediator ( ) ;
    void set_platform ( typename platform_pointer :: template pointer < platform > arg_platform ) ;
    void register_modules 
        ( typename platform_pointer :: template pointer < engine_rasterizer > arg_engine_rasterizer
        , typename platform_pointer :: template pointer < engine_render > arg_engine_render
        , typename platform_pointer :: template pointer < engine_render_stateless > arg_engine_render_stateless
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
        , typename platform_pointer :: template pointer < logic_text_stateless > arg_logic_text_stateless
        , typename platform_pointer :: template pointer < logic_title > arg_logic_title
        , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
        ) ;
public :
    void send ( typename messages :: application_render msg ) ;
    void send ( typename messages :: application_update msg ) ;
    void send ( typename messages :: camera_matrix_reply msg ) ;
    void send ( typename messages :: camera_matrix_request msg ) ;
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
    void send ( typename messages :: entities_render_reply msg ) ;
    void send ( typename messages :: entities_render_request msg ) ;
    void send ( typename messages :: entities_update msg ) ;
    void send ( typename messages :: fidget_done msg ) ;
    void send ( typename messages :: fidget_prepare_permit msg ) ;
    void send ( typename messages :: fidget_prepared msg ) ;
    void send ( typename messages :: fidget_render_reply msg ) ;
    void send ( typename messages :: fidget_render_request msg ) ;
    void send ( typename messages :: fidget_update msg ) ;
    void send ( typename messages :: game_launch_permit msg ) ;
    void send ( typename messages :: game_render msg ) ;
    void send ( typename messages :: game_update msg ) ;
    void send ( typename messages :: image_done msg ) ;
    void send ( typename messages :: image_prepare_permit msg ) ;
    void send ( typename messages :: image_prepared msg ) ;
    void send ( typename messages :: image_render_reply msg ) ;
    void send ( typename messages :: image_render_request msg ) ;
    void send ( typename messages :: image_update msg ) ;
    void send ( typename messages :: init msg ) ;
    void send ( typename messages :: land_done msg ) ;
    void send ( typename messages :: land_prepare_permit msg ) ;
    void send ( typename messages :: land_prepared msg ) ;
    void send ( typename messages :: land_render_reply msg ) ;
    void send ( typename messages :: land_render_request msg ) ;
    void send ( typename messages :: land_update msg ) ;
    void send ( typename messages :: near_plane_distance_reply msg ) ;
    void send ( typename messages :: near_plane_distance_request msg ) ;
    void send ( typename messages :: rasterize_ellipse_in_rect msg ) ;
    void send ( typename messages :: rasterize_finalize_reply msg ) ;
    void send ( typename messages :: rasterize_finalize_request msg ) ;
    void send ( typename messages :: rasterize_rect msg ) ;
    void send ( typename messages :: rasterize_triangle msg ) ;
    void send ( typename messages :: rasterize_use_texel msg ) ;
    void send ( typename messages :: rasterize_use_texture msg ) ;
    void send ( typename messages :: render msg ) ;
    void send ( typename messages :: render_blend_disable msg ) ;
    void send ( typename messages :: render_blend_src_alpha_dst_one_minus_alpha msg ) ;
    void send ( typename messages :: render_clear_screen msg ) ;
    void send ( typename messages :: render_disable_depth_test msg ) ;
    void send ( typename messages :: render_enable_depth_test msg ) ;
    void send ( typename messages :: render_enable_face_culling msg ) ;
    void send ( typename messages :: render_fog_disable msg ) ;
    void send ( typename messages :: render_fog_linear msg ) ;
    void send ( typename messages :: render_matrix_identity msg ) ;
    void send ( typename messages :: render_matrix_load msg ) ;
    void send ( typename messages :: render_mesh_create_reply msg ) ;
    void send ( typename messages :: render_mesh_create_request msg ) ;
    void send ( typename messages :: render_mesh_delete msg ) ;
    void send ( typename messages :: render_mesh_finalize msg ) ;
    void send ( typename messages :: render_mesh_render msg ) ;
    void send ( typename messages :: render_mesh_set_transform msg ) ;
    void send ( typename messages :: render_mesh_set_triangle_fan_index_value msg ) ;
    void send ( typename messages :: render_mesh_set_triangle_strip_index_value msg ) ;
    void send ( typename messages :: render_mesh_set_vertex_color msg ) ;
    void send ( typename messages :: render_mesh_set_vertex_position msg ) ;
    void send ( typename messages :: render_mesh_set_vertex_tex_coord msg ) ;
    void send ( typename messages :: render_projection_frustum msg ) ;
    void send ( typename messages :: render_projection_ortho msg ) ;
    void send ( typename messages :: render_texture_create_reply msg ) ;
    void send ( typename messages :: render_texture_create_request msg ) ;
    void send ( typename messages :: render_texture_finalize msg ) ;
    void send ( typename messages :: render_texture_load_from_resource msg ) ;
    void send ( typename messages :: render_texture_loader_ready_reply msg ) ;
    void send ( typename messages :: render_texture_loader_ready_request msg ) ;
    void send ( typename messages :: render_texture_mode_modulate msg ) ;
    void send ( typename messages :: render_texture_select msg ) ;
    void send ( typename messages :: render_texture_set_texel msg ) ;
    void send ( typename messages :: render_texture_set_texel_rgba msg ) ;
    void send ( typename messages :: render_texture_set_texels_rect msg ) ;
    void send ( typename messages :: render_texture_unselect msg ) ;
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
    void send ( typename messages :: text_render_reply msg ) ;
    void send ( typename messages :: text_render_request msg ) ;
    void send ( typename messages :: text_update msg ) ;
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
    void send ( typename messages :: use_ortho_projection_reply msg ) ;
    void send ( typename messages :: use_ortho_projection_request msg ) ;
    void send ( typename messages :: use_perspective_projection_reply msg ) ;
    void send ( typename messages :: use_perspective_projection_request msg ) ;
    void send ( typename messages :: use_text_texture_reply msg ) ;
    void send ( typename messages :: use_text_texture_request msg ) ;
    void send ( typename messages :: video_mode_changed msg ) ;
public :
    const engine_render_consts_type & engine_render_consts ( ) ;
    const logic_text_consts_type & logic_text_consts ( ) ;
    engine_render_stateless & engine_render_stateless_obj ( ) ;
    platform & platform_obj ( ) ;
private :
    typename platform_pointer :: template pointer < engine_rasterizer > _engine_rasterizer ;
    typename platform_pointer :: template pointer < engine_render > _engine_render ;
    typename platform_pointer :: template pointer < engine_render_stateless > _engine_render_stateless ;
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
    typename platform_pointer :: template pointer < logic_text_stateless > _logic_text_stateless ;
    typename platform_pointer :: template pointer < logic_title > _logic_title ;
    typename platform_pointer :: template pointer < logic_touch > _logic_touch ;
    typename platform_pointer :: template pointer < platform > _platform ;
} ;

template < typename mediator_types >
shy_mediator < mediator_types > :: shy_mediator ( )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: set_platform ( typename platform_pointer :: template pointer < platform > arg_platform )
{
    _platform = arg_platform ;
    _engine_render_stateless . get ( ) . set_platform_render ( _platform . get ( ) . render ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: register_modules 
    ( typename platform_pointer :: template pointer < engine_rasterizer > arg_engine_rasterizer
    , typename platform_pointer :: template pointer < engine_render > arg_engine_render
    , typename platform_pointer :: template pointer < engine_render_stateless > arg_engine_render_stateless
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
    , typename platform_pointer :: template pointer < logic_text_stateless > arg_logic_text_stateless
    , typename platform_pointer :: template pointer < logic_title > arg_logic_title
    , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
    )
{
    _engine_rasterizer = arg_engine_rasterizer ;
    _engine_render = arg_engine_render ;
    _engine_render_stateless = arg_engine_render_stateless ;
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
    _logic_text_stateless = arg_logic_text_stateless ;
    _logic_title = arg_logic_title ;
    _logic_touch = arg_logic_touch ;

    _engine_rasterizer . get ( ) . set_mediator ( * this ) ;
    _engine_render . get ( ) . set_mediator ( * this ) ;
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
typename shy_mediator < mediator_types > :: platform & shy_mediator < mediator_types > :: platform_obj ( )
{
    return _platform . get ( ) ;
}

template < typename mediator_types >
typename shy_mediator < mediator_types > :: engine_render_stateless & shy_mediator < mediator_types > :: engine_render_stateless_obj ( )
{
    return _engine_render_stateless . get ( ) ;
}

template < typename mediator_types >
const typename shy_mediator < mediator_types > :: engine_render_consts_type &
shy_mediator < mediator_types > :: engine_render_consts ( )
{
    return _engine_render_stateless . get ( ) . engine_render_consts ;
}

template < typename mediator_types >
const typename shy_mediator < mediator_types > :: logic_text_consts_type &
shy_mediator < mediator_types > :: logic_text_consts ( )
{
    return _logic_text_stateless . get ( ) . logic_text_consts ;
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
    _engine_rasterizer . get ( ) . receive ( msg ) ;
    _engine_render . get ( ) . receive ( msg ) ;
    _logic . get ( ) . receive ( msg ) ;
    _logic_application . get ( ) . receive ( msg ) ;
    _logic_camera . get ( ) . receive ( msg ) ;
    _logic_entities . get ( ) . receive ( msg ) ;
    _logic_fidget . get ( ) . receive ( msg ) ;
    _logic_game . get ( ) . receive ( msg ) ;
    _logic_image . get ( ) . receive ( msg ) ;
    _logic_land . get ( ) . receive ( msg ) ;
    _logic_sound . get ( ) . receive ( msg ) ;
    _logic_text . get ( ) . receive ( msg ) ;
    _logic_title . get ( ) . receive ( msg ) ;
    _logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_prepared msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_blend_disable msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_blend_src_alpha_dst_one_minus_alpha msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_clear_screen msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_disable_depth_test msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_enable_face_culling msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_enable_depth_test msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_fog_disable msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_fog_linear msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_matrix_load msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_matrix_identity msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_projection_frustum msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_projection_ortho msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_mode_modulate msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_set_vertex_position msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_set_vertex_tex_coord msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_set_vertex_color msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_set_triangle_strip_index_value msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_set_triangle_fan_index_value msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_create_request msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_create_reply msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
    _logic_fidget . get ( ) . receive ( msg ) ;
    _logic_image . get ( ) . receive ( msg ) ;
    _logic_land . get ( ) . receive ( msg ) ;
    _logic_text . get ( ) . receive ( msg ) ;
    _logic_title . get ( ) . receive ( msg ) ;
    _logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_finalize msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_delete msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_render msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_mesh_set_transform msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
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
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_finalize_reply msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: rasterize_finalize_request msg )
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
void shy_mediator < mediator_types > :: send ( typename messages :: entities_render_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: entities_render_request msg )
{
    _logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_done msg )
{
    _logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_render_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: fidget_render_request msg )
{
    _logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_done msg )
{
    _logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_render_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: image_render_request msg )
{
    _logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_done msg )
{
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_render_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: land_render_request msg )
{
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_done msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_render_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_render_request msg )
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
void shy_mediator < mediator_types > :: send ( typename messages :: camera_matrix_request msg )
{
    _logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: camera_matrix_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_create_reply msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
    _logic_image . get ( ) . receive ( msg ) ;
    _logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_create_request msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_finalize msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_load_from_resource msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_loader_ready_reply msg )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_loader_ready_request msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_select msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_set_texel msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_set_texel_rgba msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_set_texels_rect msg ) 
{
    _engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: render_texture_unselect msg )
{
    _engine_render . get ( ) . receive ( msg ) ;
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
void shy_mediator < mediator_types > :: send ( typename messages :: use_perspective_projection_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_perspective_projection_request msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_ortho_projection_request msg )
{
    _logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_ortho_projection_reply msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: game_launch_permit msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_text_texture_request msg )
{
    _logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: use_text_texture_reply msg )
{
    _logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: text_letter_big_tex_coords_reply msg )
{
    _logic_title . get ( ) . receive ( msg ) ;
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
