template < typename mediator >
class shy_engine_render_stateless
{
    friend class shy_engine_render < mediator > ;

    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    
public :    
    class engine_render_mesh_id 
    {
        friend class shy_engine_render < mediator > ;
    private :
        num_whole _mesh_id ;
    } ;
    
    class engine_render_texture_id 
    {
        friend class shy_engine_render < mediator > ;
    private :
        num_whole _texture_id ;
    } ;
    
    class engine_render_stateless_consts_type
    {
    public :
        engine_render_stateless_consts_type ( ) ;
    public :
        num_whole texture_width ;
        num_whole texture_height ;
        static const_int_32 texture_size_pow2_base_int = 8 ;
        static const_int_32 texture_size_int = 1 << texture_size_pow2_base_int ;
    } ;
    
    class engine_render_messages
    {
    public :
        class engine_render_aspect_reply { public : num_fract width ; num_fract height ; } ;
        class engine_render_aspect_request { } ;
        class engine_render_blend_disable { } ;
        class engine_render_blend_src_alpha_dst_one_minus_alpha { } ;
        class engine_render_clear_screen { public : num_fract r ; num_fract g ; num_fract b ; } ;
        class engine_render_disable_depth_test { } ;
        class engine_render_enable_depth_test { } ;
        class engine_render_enable_face_culling { } ;
        class engine_render_fog_disable { } ;
        class engine_render_fog_linear { public : num_fract znear ; num_fract zfar ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class engine_render_frame_loss_reply { public : num_whole frame_loss ; } ;
        class engine_render_frame_loss_request { } ;
        class engine_render_matrix_identity { } ;
        class engine_render_matrix_load { public : matrix_data matrix ; } ;
        class engine_render_mesh_create_reply { public : engine_render_mesh_id mesh ; } ;
        class engine_render_mesh_create_request { public : num_whole vertices ; num_whole triangle_strip_indices ; num_whole triangle_fan_indices ; } ;
        class engine_render_mesh_delete { public : engine_render_mesh_id mesh ; } ;
        class engine_render_mesh_finalize { public : engine_render_mesh_id mesh ; } ;
        class engine_render_mesh_render { public : engine_render_mesh_id mesh ; } ;
        class engine_render_mesh_set_transform { public : engine_render_mesh_id mesh ; matrix_data transform ; } ;
        class engine_render_mesh_set_triangle_fan_index_value { public : engine_render_mesh_id mesh ; num_whole offset ; num_whole index ; } ;
        class engine_render_mesh_set_triangle_strip_index_value { public : engine_render_mesh_id mesh ; num_whole offset ; num_whole index ; } ;
        class engine_render_mesh_set_vertex_color { public : engine_render_mesh_id mesh ; num_whole offset ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class engine_render_mesh_set_vertex_position { public : engine_render_mesh_id mesh ; num_whole offset ; num_fract x ; num_fract y ; num_fract z ; } ;
        class engine_render_mesh_set_vertex_tex_coord { public : engine_render_mesh_id mesh ; num_whole offset ; num_fract u ; num_fract v ; } ;
        class engine_render_projection_frustum { public : num_fract left ; num_fract right ; num_fract bottom ; num_fract top ; num_fract znear ; num_fract zfar ; } ;
        class engine_render_projection_ortho { public : num_fract left ; num_fract right ; num_fract bottom ; num_fract top ; num_fract znear ; num_fract zfar ; } ;
        class engine_render_texture_create_reply { public : engine_render_texture_id texture ; } ;
        class engine_render_texture_create_request { } ;
        class engine_render_texture_finalize { public : engine_render_texture_id texture ; } ;
        class engine_render_texture_load_from_resource { public : engine_render_texture_id texture ; texture_resource_id resource ; } ;
        class engine_render_texture_loader_ready_reply { public : num_whole ready ; } ;
        class engine_render_texture_loader_ready_request { } ;
        class engine_render_texture_mode_modulate { } ;
        class engine_render_texture_select { public : engine_render_texture_id texture ; } ;
        class engine_render_texture_set_texel { public : engine_render_texture_id texture ; num_whole x ; num_whole y ; texel_data texel ; } ;
        class engine_render_texture_set_texel_rgba { public : engine_render_texture_id texture ; num_whole x ; num_whole y ; num_fract r ; num_fract g ; num_fract b ; num_fract a ; } ;
        class engine_render_texture_set_texels_rect { public : engine_render_texture_id texture ; num_whole left ; num_whole bottom ; num_whole right ; num_whole top ; texel_data texel ; } ;
        class engine_render_texture_unselect { } ;
    } ;
    
    template < typename receivers >
    class engine_render_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename engine_render_messages :: engine_render_aspect_reply ) ;
        void send ( typename engine_render_messages :: engine_render_aspect_request ) ;
        void send ( typename engine_render_messages :: engine_render_blend_disable ) ;
        void send ( typename engine_render_messages :: engine_render_blend_src_alpha_dst_one_minus_alpha ) ;
        void send ( typename engine_render_messages :: engine_render_clear_screen ) ;
        void send ( typename engine_render_messages :: engine_render_disable_depth_test ) ;
        void send ( typename engine_render_messages :: engine_render_enable_depth_test ) ;
        void send ( typename engine_render_messages :: engine_render_enable_face_culling ) ;
        void send ( typename engine_render_messages :: engine_render_fog_disable ) ;
        void send ( typename engine_render_messages :: engine_render_fog_linear ) ;
        void send ( typename engine_render_messages :: engine_render_frame_loss_reply ) ;
        void send ( typename engine_render_messages :: engine_render_frame_loss_request ) ;
        void send ( typename engine_render_messages :: engine_render_matrix_identity ) ;
        void send ( typename engine_render_messages :: engine_render_matrix_load ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_create_reply ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_create_request ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_delete ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_finalize ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_render ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_set_transform ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_set_triangle_fan_index_value ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_set_triangle_strip_index_value ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_set_vertex_color ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_set_vertex_position ) ;
        void send ( typename engine_render_messages :: engine_render_mesh_set_vertex_tex_coord ) ;
        void send ( typename engine_render_messages :: engine_render_projection_frustum ) ;
        void send ( typename engine_render_messages :: engine_render_projection_ortho ) ;
        void send ( typename engine_render_messages :: engine_render_texture_create_reply ) ;
        void send ( typename engine_render_messages :: engine_render_texture_create_request ) ;
        void send ( typename engine_render_messages :: engine_render_texture_finalize ) ;
        void send ( typename engine_render_messages :: engine_render_texture_load_from_resource ) ;
        void send ( typename engine_render_messages :: engine_render_texture_loader_ready_reply ) ;
        void send ( typename engine_render_messages :: engine_render_texture_loader_ready_request ) ;
        void send ( typename engine_render_messages :: engine_render_texture_mode_modulate ) ;
        void send ( typename engine_render_messages :: engine_render_texture_select ) ;
        void send ( typename engine_render_messages :: engine_render_texture_set_texel ) ;
        void send ( typename engine_render_messages :: engine_render_texture_set_texel_rgba ) ;
        void send ( typename engine_render_messages :: engine_render_texture_set_texels_rect ) ;
        void send ( typename engine_render_messages :: engine_render_texture_unselect ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
    
public :
    shy_engine_render_stateless ( ) ;
    shy_engine_render_stateless & operator= ( const shy_engine_render_stateless & ) ;
    
    static void set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
    
public :
    const engine_render_stateless_consts_type engine_render_stateless_consts ;
} ;

template < typename mediator >
shy_engine_render_stateless < mediator > :: shy_engine_render_stateless ( )
{
}

template < typename mediator >
shy_engine_render_stateless < mediator > :: engine_render_stateless_consts_type :: engine_render_stateless_consts_type ( )
{
    platform_math :: make_num_whole ( texture_width , texture_size_int ) ;
    platform_math :: make_num_whole ( texture_height , texture_size_int ) ;
}

template < typename mediator >
void shy_engine_render_stateless < mediator > :: set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
    platform_render :: set_texel_color ( texel , r , g , b , a ) ;
}

template < typename mediator >
void shy_engine_render_stateless < mediator > :: create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
    platform_render :: create_texture_resource_id ( resource_id , resource_index ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_blend_disable msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_blend_src_alpha_dst_one_minus_alpha msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_clear_screen msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_disable_depth_test msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_enable_face_culling msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_enable_depth_test msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_fog_disable msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_fog_linear msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_matrix_load msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_matrix_identity msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_projection_frustum msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_projection_ortho msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_mode_modulate msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_set_vertex_position msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_set_vertex_tex_coord msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_set_vertex_color msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_set_triangle_strip_index_value msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_set_triangle_fan_index_value msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_create_request msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_create_reply msg )
{
    _receivers . get ( ) . logic_door_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_finalize msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_delete msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_render msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_mesh_set_transform msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_aspect_reply msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout_position . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout_row_rect . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_aspect_request msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_create_reply msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_create_request msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_finalize msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_load_from_resource msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_loader_ready_reply msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_loader_ready_request msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_select msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_set_texel msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_set_texel_rgba msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_set_texels_rect msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_texture_unselect msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_frame_loss_request msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_render_stateless < mediator > 
:: engine_render_sender < receivers > 
:: send ( typename engine_render_messages :: engine_render_frame_loss_reply msg )
{
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
}
