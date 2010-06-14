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
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_mesh engine_mesh ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_mesh :: mesh_id mesh_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer engine_rasterizer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_texture engine_texture ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_texture :: texture_id texture_id ;
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
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text :: alphabet_english alphabet_english ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text :: letter_id letter_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title logic_title ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch logic_touch ;
    typedef typename platform :: const_int_32 const_int_32 ;
    typedef typename platform :: index_data index_data ;
    typedef typename platform :: matrix_data matrix_data ;
    typedef typename platform :: num_fract num_fract ;
    typedef typename platform :: num_whole num_whole ;
    typedef typename platform :: texel_data texel_data ;
    typedef typename platform :: texture_resource_id texture_resource_id ;
    typedef typename platform :: vector_data vector_data ;
    typedef typename platform :: vertex_data vertex_data ;
    
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
        class render { } ;
        class sound_prepare_permit { } ;
        class sound_prepared { } ;
        class sound_update { } ;
        class text_done { } ;
        class text_prepare_permit { } ;
        class text_prepared { } ;
        class text_render { } ;
        class text_update { } ;
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
        class video_mode_changed { } ;
    } ;
    
public :
    shy_mediator ( ) ;
    void register_modules 
        ( typename platform :: template pointer < engine_mesh > arg_engine_mesh
        , typename platform :: template pointer < engine_rasterizer > arg_engine_rasterizer
        , typename platform :: template pointer < engine_texture > arg_engine_texture
        , typename platform :: template pointer < logic > arg_logic
        , typename platform :: template pointer < logic_application > arg_logic_application
        , typename platform :: template pointer < logic_camera > arg_logic_camera
        , typename platform :: template pointer < logic_entities > arg_logic_entities
        , typename platform :: template pointer < logic_fidget > arg_logic_fidget
        , typename platform :: template pointer < logic_game > arg_logic_game
        , typename platform :: template pointer < logic_image > arg_logic_image
        , typename platform :: template pointer < logic_land > arg_logic_land
        , typename platform :: template pointer < logic_sound > arg_logic_sound
        , typename platform :: template pointer < logic_text > arg_logic_text
        , typename platform :: template pointer < logic_title > arg_logic_title
        , typename platform :: template pointer < logic_touch > arg_logic_touch
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
    void send ( typename messages :: render msg ) ;
    void send ( typename messages :: sound_prepare_permit msg ) ;
    void send ( typename messages :: sound_prepared msg ) ;
    void send ( typename messages :: sound_update msg ) ;
    void send ( typename messages :: text_done msg ) ;
    void send ( typename messages :: text_prepare_permit msg ) ;
    void send ( typename messages :: text_prepared msg ) ;
    void send ( typename messages :: text_render msg ) ;
    void send ( typename messages :: text_update msg ) ;
    void send ( typename messages :: texture_unselect msg ) ;
    void send ( typename messages :: title_done msg ) ;
    void send ( typename messages :: title_finished msg ) ;
    void send ( typename messages :: title_launch_permit msg ) ;
    void send ( typename messages :: title_render msg ) ;
    void send ( typename messages :: title_update msg ) ;
    void send ( typename messages :: touch_done msg ) ;
    void send ( typename messages :: touch_prepare_permit msg ) ;
    void send ( typename messages :: touch_render msg ) ;
    void send ( typename messages :: touch_update msg ) ;
    void send ( typename messages :: update msg ) ;
    void send ( typename messages :: video_mode_changed msg ) ;
    void send ( typename messages :: touch_prepared msg ) ;
public :
    void get_big_letter_tex_coords ( num_fract & left , num_fract & bottom , num_fract & right , num_fract & top , letter_id letter ) ;
    void get_small_letter_tex_coords ( num_fract & left , num_fract & bottom , num_fract & right , num_fract & top , letter_id letter ) ;
    void get_entity_height ( num_fract & result ) ;
    void get_entity_mesh_grid ( num_whole & result ) ;
    void get_entity_origin ( vector_data & result , num_whole index ) ;
    void get_near_plane_distance ( num_fract & result ) ;
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
    void mesh_delete ( mesh_id arg_mesh_id ) ;
    void mesh_render ( mesh_id arg_mesh_id ) ;
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform ) ;
    void rasterize_ellipse_in_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void rasterize_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void rasterize_triangle ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 , num_whole x3 , num_whole y3 ) ;
    void rasterize_use_texture ( texture_id arg_texture_id , num_whole origin_x , num_whole origin_y ) ;
    void rasterize_use_texel ( const texel_data & texel ) ;
    const alphabet_english & text_alphabet_english ( ) ;
    void texture_create ( texture_id & result ) ;
    void texture_finalize ( texture_id arg_texture_id ) ;
    void texture_height ( num_whole & result ) ;
    void texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id ) ;
    void texture_select ( texture_id arg_texture_id ) ;
    void texture_set_texel ( texture_id arg_texture_id , num_whole x , num_whole y , const texel_data & texel ) ;
    void texture_set_texel ( texture_id arg_texture_id , num_whole x , num_whole y , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void texture_width ( num_whole & result ) ;
    void use_ortho_projection ( ) ;
    void use_perspective_projection ( ) ;
    void use_text_texture ( ) ;
private :
    typename platform :: template pointer < engine_mesh > _engine_mesh ;
    typename platform :: template pointer < engine_rasterizer > _engine_rasterizer ;
    typename platform :: template pointer < engine_texture > _engine_texture ;
    typename platform :: template pointer < logic > _logic ;
    typename platform :: template pointer < logic_application > _logic_application ;
    typename platform :: template pointer < logic_camera > _logic_camera ;
    typename platform :: template pointer < logic_entities > _logic_entities ;
    typename platform :: template pointer < logic_fidget > _logic_fidget ;
    typename platform :: template pointer < logic_game > _logic_game ;
    typename platform :: template pointer < logic_image > _logic_image ;
    typename platform :: template pointer < logic_land > _logic_land ;
    typename platform :: template pointer < logic_sound > _logic_sound ;
    typename platform :: template pointer < logic_text > _logic_text ;
    typename platform :: template pointer < logic_title > _logic_title ;
    typename platform :: template pointer < logic_touch > _logic_touch ;
} ;

template < typename mediator_types >
shy_mediator < mediator_types > :: shy_mediator ( )
{
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: register_modules 
    ( typename platform :: template pointer < engine_mesh > arg_engine_mesh
    , typename platform :: template pointer < engine_rasterizer > arg_engine_rasterizer
    , typename platform :: template pointer < engine_texture > arg_engine_texture
    , typename platform :: template pointer < logic > arg_logic
    , typename platform :: template pointer < logic_application > arg_logic_application
    , typename platform :: template pointer < logic_camera > arg_logic_camera
    , typename platform :: template pointer < logic_entities > arg_logic_entities
    , typename platform :: template pointer < logic_fidget > arg_logic_fidget
    , typename platform :: template pointer < logic_game > arg_logic_game
    , typename platform :: template pointer < logic_image > arg_logic_image
    , typename platform :: template pointer < logic_land > arg_logic_land
    , typename platform :: template pointer < logic_sound > arg_logic_sound
    , typename platform :: template pointer < logic_text > arg_logic_text
    , typename platform :: template pointer < logic_title > arg_logic_title
    , typename platform :: template pointer < logic_touch > arg_logic_touch
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

    _engine_rasterizer . get ( ) . set_mediator ( this ) ;
    _logic . get ( ) . set_mediator ( this ) ;
    _logic_application . get ( ) . set_mediator ( this ) ;
    _logic_camera . get ( ) . set_mediator ( this ) ;
    _logic_entities . get ( ) . set_mediator ( this ) ;
    _logic_fidget . get ( ) . set_mediator ( this ) ;
    _logic_game . get ( ) . set_mediator ( this ) ;
    _logic_image . get ( ) . set_mediator ( this ) ;
    _logic_land . get ( ) . set_mediator ( this ) ;
    _logic_sound . get ( ) . set_mediator ( this ) ;
    _logic_text . get ( ) . set_mediator ( this ) ;
    _logic_title . get ( ) . set_mediator ( this ) ;
    _logic_touch . get ( ) . set_mediator ( this ) ;
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
void shy_mediator < mediator_types > :: get_entity_height ( num_fract & result )
{
    _logic_entities . get ( ) . get_entity_height ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_entity_mesh_grid ( num_whole & result )
{
    _logic_entities . get ( ) . get_entity_mesh_grid ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_entity_origin ( vector_data & result , num_whole index )
{
    _logic_entities . get ( ) . get_entity_origin ( result , index ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: get_near_plane_distance ( num_fract & result )
{
    _logic . get ( ) . get_near_plane_distance ( result ) ;
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
void shy_mediator < mediator_types > :: mesh_delete ( mesh_id arg_mesh_id )
{
    _engine_mesh . get ( ) . mesh_delete ( arg_mesh_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: mesh_render ( mesh_id arg_mesh_id )
{
    _engine_mesh . get ( ) . mesh_render ( arg_mesh_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: mesh_set_transform
    ( mesh_id arg_mesh_id , const matrix_data & transform )
{
    _engine_mesh . get ( ) . mesh_set_transform ( arg_mesh_id , transform ) ;
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
void shy_mediator < mediator_types > :: rasterize_use_texel
    ( const texel_data & texel )
{
    _engine_rasterizer . get ( ) . rasterize_use_texel ( texel ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_ellipse_in_rect
    ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    _engine_rasterizer . get ( ) . rasterize_ellipse_in_rect ( x1 , y1 , x2 , y2 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_rect
    ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    _engine_rasterizer . get ( ) . rasterize_rect ( x1 , y1 , x2 , y2 ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_use_texture 
    ( texture_id arg_texture_id , num_whole origin_x , num_whole origin_y )
{
    _engine_rasterizer . get ( ) . rasterize_use_texture ( arg_texture_id , origin_x , origin_y ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: rasterize_triangle
    ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 , num_whole x3 , num_whole y3 )
{
    _engine_rasterizer . get ( ) . rasterize_triangle ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
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
void shy_mediator < mediator_types > :: texture_create ( texture_id & result )
{
    _engine_texture . get ( ) . texture_create ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_finalize ( texture_id arg_texture_id )
{
    _engine_texture . get ( ) . texture_finalize ( arg_texture_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_load_from_resource 
    ( texture_id arg_texture_id 
    , texture_resource_id arg_resource_id 
    )
{
    _engine_texture . get ( ) . texture_load_from_resource ( arg_texture_id , arg_resource_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_select ( texture_id arg_texture_id )
{
    _engine_texture . get ( ) . texture_select ( arg_texture_id ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_set_texel 
    ( texture_id arg_texture_id , num_whole x , num_whole y , const texel_data & texel )
{
    _engine_texture . get ( ) . texture_set_texel ( arg_texture_id , x , y , texel ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_set_texel 
    ( texture_id arg_texture_id , num_whole x , num_whole y , num_fract r , num_fract g , num_fract b , num_fract a )
{
    _engine_texture . get ( ) . texture_set_texel ( arg_texture_id , x , y , r , g , b , a ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: texture_unselect msg )
{
    _engine_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_height ( num_whole & result )
{
    _engine_texture . get ( ) . texture_height ( result ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: texture_width ( num_whole & result )
{
    _engine_texture . get ( ) . texture_width ( result ) ;
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
void shy_mediator < mediator_types > :: use_perspective_projection ( )
{
    _logic . get ( ) . use_perspective_projection ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: use_ortho_projection ( )
{
    _logic . get ( ) . use_ortho_projection ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: send ( typename messages :: game_launch_permit msg )
{
    _logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
const typename shy_mediator < mediator_types > :: alphabet_english & 
shy_mediator < mediator_types > :: text_alphabet_english ( )
{
    return _logic_text . get ( ) . text_alphabet_english ( ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: use_text_texture ( )
{
    _logic_text . get ( ) . use_text_texture ( ) ;
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

