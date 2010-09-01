template < typename mediator >
class shy_logic_main_menu_renderer
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_render_state_type
    {
    public :
        num_whole requested ;
    } ;
    
    class _logic_core_use_ortho_projection_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

    class _logic_fidget_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;
    
    class _logic_text_use_text_texture_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;
    
    class _logic_main_menu_letters_meshes_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;
    
    class _logic_main_menu_selection_mesh_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_render ) ;
    void receive ( typename messages :: logic_main_menu_render_permit ) ;
    void receive ( typename messages :: logic_core_use_ortho_projection_reply ) ;
    void receive ( typename messages :: logic_fidget_render_reply ) ;
    void receive ( typename messages :: logic_text_use_text_texture_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_render_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_render_reply ) ;
private :
    void _proceed_with_render ( ) ;
    void _render_started ( ) ;
    void _prepare_render_state ( ) ;
    void _restore_render_state ( ) ;
    void _clear_screen ( ) ;
    void _blue_screen ( ) ;
    void _request_ortho_projection ( ) ;
    void _request_fidget_render ( ) ;
    void _select_text_texture ( ) ;
    void _render_selection_mesh ( ) ;
    void _render_letters_meshes ( ) ;
    void _render_finished ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;    
    
    _logic_main_menu_render_state_type _logic_main_menu_render_state ;
    _logic_core_use_ortho_projection_state_type _logic_core_use_ortho_projection_state ;
    _logic_fidget_render_state_type _logic_fidget_render_state ;
    _logic_text_use_text_texture_state_type _logic_text_use_text_texture_state ;
    _logic_main_menu_letters_meshes_render_state_type _logic_main_menu_letters_meshes_render_state ;
    _logic_main_menu_selection_mesh_render_state_type _logic_main_menu_selection_mesh_render_state ;
    
    num_whole _permitted ;
} ;

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_main_menu_render_permit )
{
    _permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_main_menu_render )
{
    if ( platform_conditions :: whole_is_true ( _permitted ) )
    {
        _logic_main_menu_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
    else
        _blue_screen ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_core_use_ortho_projection_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_core_use_ortho_projection_state . requested ) )
    {
        _logic_core_use_ortho_projection_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_core_use_ortho_projection_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_fidget_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_fidget_render_state . requested ) )
    {
        _logic_fidget_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_fidget_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_meshes_render_state . requested ) )
    {
        _logic_main_menu_letters_meshes_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_meshes_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_mesh_render_state . requested ) )
    {
        _logic_main_menu_selection_mesh_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_mesh_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: receive ( typename messages :: logic_text_use_text_texture_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_text_use_text_texture_state . requested ) )
    {
        _logic_text_use_text_texture_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_text_use_text_texture_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_render_state . requested ) )
    {
        _logic_main_menu_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _render_started ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_core_use_ortho_projection_state . replied ) )
    {
        _logic_core_use_ortho_projection_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _request_fidget_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_fidget_render_state . replied ) )
    {
        _logic_fidget_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _render_selection_mesh ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_mesh_render_state . replied ) )
    {
        _logic_main_menu_selection_mesh_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _select_text_texture ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_text_use_text_texture_state . replied ) )
    {
        _logic_text_use_text_texture_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _render_letters_meshes ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_meshes_render_state . replied ) )
    {
        _logic_main_menu_letters_meshes_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _render_finished ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _render_started ( )
{
    _prepare_render_state ( ) ;
    _clear_screen ( ) ;
    _request_ortho_projection ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _render_finished ( )
{
    _restore_render_state ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _prepare_render_state ( )
{
    _mediator . get ( ) . send ( typename messages :: engine_render_disable_depth_test ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: engine_render_fog_disable ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: engine_render_matrix_identity ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _restore_render_state ( )
{
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_disable ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _clear_screen ( )
{
    typename messages :: engine_render_clear_screen msg ;
    msg . r = _platform_math_consts . get ( ) . fract_0 ;
    msg . g = _platform_math_consts . get ( ) . fract_0 ;
    msg . b = _platform_math_consts . get ( ) . fract_0 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _blue_screen ( )
{
    typename messages :: engine_render_clear_screen msg ;
    msg . r = _platform_math_consts . get ( ) . fract_0 ;
    msg . g = _platform_math_consts . get ( ) . fract_0 ;
    msg . b = _platform_math_consts . get ( ) . fract_1 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _request_ortho_projection ( )
{
    _logic_core_use_ortho_projection_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_core_use_ortho_projection_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _request_fidget_render ( )
{
    _logic_fidget_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_fidget_render_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _select_text_texture ( )
{
    _logic_text_use_text_texture_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_text_use_text_texture_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _render_letters_meshes ( )
{
    _logic_main_menu_letters_meshes_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_render_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_renderer < mediator > :: _render_selection_mesh ( )
{
    _logic_main_menu_selection_mesh_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_render_request ( ) ) ;
}
