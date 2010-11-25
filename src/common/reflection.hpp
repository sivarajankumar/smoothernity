template < typename context >
class shy_reflection
{
    typedef typename context :: mediator mediator ;
    typedef typename context :: mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename context :: reflection_binder reflection_binder ;
public :
    void bind_all 
        ( typename platform_pointer :: template pointer < mediator >
        , typename platform_pointer :: template pointer < reflection_binder > 
        ) ;
private :
    void _bind_logic_amusement_stateless_consts ( ) ;
    void _bind_logic_blanket_animation_stateless_consts ( ) ;
    void _bind_logic_blanket_stateless_consts ( ) ;
    void _bind_logic_door_animation_stateless_consts ( ) ;
    void _bind_logic_door_stateless_consts ( ) ;
    void _bind_logic_fidget_stateless_consts ( ) ;
    void _bind_logic_main_menu_animation_stateless_consts ( ) ;
    void _bind_logic_main_menu_letters_animation_stateless_consts ( ) ;
    void _bind_logic_main_menu_letters_layout_stateless_consts ( ) ;
    void _bind_logic_main_menu_letters_meshes_stateless_consts ( ) ;
    void _bind_logic_main_menu_selection_animation_stateless_consts ( ) ;
    void _bind_logic_main_menu_selection_stateless_consts ( ) ;
    void _bind_logic_title_stateless_consts ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < reflection_binder > _binder ;
} ;

template < typename context >
void shy_reflection < context > :: bind_all 
    ( typename platform_pointer :: template pointer < mediator > arg_mediator
    , typename platform_pointer :: template pointer < reflection_binder > arg_binder 
    )
{
    _mediator = arg_mediator ;
    _binder = arg_binder ;
    _bind_logic_amusement_stateless_consts ( ) ;
    _bind_logic_blanket_animation_stateless_consts ( ) ;
    _bind_logic_blanket_stateless_consts ( ) ;
    _bind_logic_door_animation_stateless_consts ( ) ;
    _bind_logic_door_stateless_consts ( ) ;
    _bind_logic_fidget_stateless_consts ( ) ;
    _bind_logic_main_menu_animation_stateless_consts ( ) ;
    _bind_logic_main_menu_letters_animation_stateless_consts ( ) ;
    _bind_logic_main_menu_letters_layout_stateless_consts ( ) ;
    _bind_logic_main_menu_letters_meshes_stateless_consts ( ) ;
    _bind_logic_main_menu_selection_animation_stateless_consts ( ) ;
    _bind_logic_main_menu_selection_stateless_consts ( ) ;
    _bind_logic_title_stateless_consts ( ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_amusement_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_amusement_stateless :: logic_amusement_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_amusement_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_amusement_stateless" ) ;
    _binder . get ( ) . bind ( "renderer_clear_color_r" , consts . get ( ) . renderer_clear_color_r ) ;
    _binder . get ( ) . bind ( "renderer_clear_color_g" , consts . get ( ) . renderer_clear_color_g ) ;
    _binder . get ( ) . bind ( "renderer_clear_color_b" , consts . get ( ) . renderer_clear_color_b ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_blanket_animation_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_blanket_animation_stateless :: logic_blanket_animation_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_blanket_animation_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_blanket_animation_stateless" ) ;
    _binder . get ( ) . bind ( "animation_origin_x" , consts . get ( ) . animation_origin_x ) ;
    _binder . get ( ) . bind ( "animation_origin_y" , consts . get ( ) . animation_origin_y ) ;
    _binder . get ( ) . bind ( "animation_origin_z" , consts . get ( ) . animation_origin_z ) ;
    _binder . get ( ) . bind ( "appear_scale_begin" , consts . get ( ) . appear_scale_begin ) ;
    _binder . get ( ) . bind ( "appear_scale_end" , consts . get ( ) . appear_scale_end ) ;
    _binder . get ( ) . bind ( "appear_rotation_begin" , consts . get ( ) . appear_rotation_begin ) ;
    _binder . get ( ) . bind ( "appear_rotation_end" , consts . get ( ) . appear_rotation_end ) ;
    _binder . get ( ) . bind ( "appear_time_from_begin_to_end" , consts . get ( ) . appear_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "disappear_scale_begin" , consts . get ( ) . disappear_scale_begin ) ;
    _binder . get ( ) . bind ( "disappear_scale_end" , consts . get ( ) . disappear_scale_end ) ;
    _binder . get ( ) . bind ( "disappear_rotation_begin" , consts . get ( ) . disappear_rotation_begin ) ;
    _binder . get ( ) . bind ( "disappear_rotation_end" , consts . get ( ) . disappear_rotation_end ) ;
    _binder . get ( ) . bind ( "disappear_time_from_begin_to_end" , consts . get ( ) . disappear_time_from_begin_to_end ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_blanket_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_blanket_stateless :: logic_blanket_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_blanket_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_blanket_stateless" ) ;
    _binder . get ( ) . bind ( "mesh_vertex_x_left" , consts . get ( ) . mesh_vertex_x_left ) ;
    _binder . get ( ) . bind ( "mesh_vertex_x_right" , consts . get ( ) . mesh_vertex_x_right ) ;
    _binder . get ( ) . bind ( "mesh_vertex_y_bottom" , consts . get ( ) . mesh_vertex_y_bottom ) ;
    _binder . get ( ) . bind ( "mesh_vertex_y_top" , consts . get ( ) . mesh_vertex_y_top ) ;
    _binder . get ( ) . bind ( "mesh_vertex_z" , consts . get ( ) . mesh_vertex_z ) ;
    _binder . get ( ) . bind ( "mesh_color_r" , consts . get ( ) . mesh_color_r ) ;
    _binder . get ( ) . bind ( "mesh_color_g" , consts . get ( ) . mesh_color_g ) ;
    _binder . get ( ) . bind ( "mesh_color_b" , consts . get ( ) . mesh_color_b ) ;
    _binder . get ( ) . bind ( "mesh_color_a" , consts . get ( ) . mesh_color_a ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_door_animation_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_door_animation_stateless :: logic_door_animation_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_door_animation_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_door_animation_stateless" ) ;
    _binder . get ( ) . bind ( "animation_origin_x" , consts . get ( ) . animation_origin_x ) ;
    _binder . get ( ) . bind ( "animation_origin_y" , consts . get ( ) . animation_origin_y ) ;
    _binder . get ( ) . bind ( "animation_origin_z" , consts . get ( ) . animation_origin_z ) ;
    _binder . get ( ) . bind ( "appear_scale_begin" , consts . get ( ) . appear_scale_begin ) ;
    _binder . get ( ) . bind ( "appear_scale_end" , consts . get ( ) . appear_scale_end ) ;
    _binder . get ( ) . bind ( "appear_time_from_begin_to_end" , consts . get ( ) . appear_time_from_begin_to_end ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_door_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_door_stateless :: logic_door_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_door_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_door_stateless" ) ;
    _binder . get ( ) . bind ( "mesh_color_r" , consts . get ( ) . mesh_color_r ) ;
    _binder . get ( ) . bind ( "mesh_color_g" , consts . get ( ) . mesh_color_g ) ;
    _binder . get ( ) . bind ( "mesh_color_b" , consts . get ( ) . mesh_color_b ) ;
    _binder . get ( ) . bind ( "mesh_color_a" , consts . get ( ) . mesh_color_a ) ;
    _binder . get ( ) . bind ( "mesh_x_left" , consts . get ( ) . mesh_x_left ) ;
    _binder . get ( ) . bind ( "mesh_x_right" , consts . get ( ) . mesh_x_right ) ;
    _binder . get ( ) . bind ( "mesh_y_bottom" , consts . get ( ) . mesh_y_bottom ) ;
    _binder . get ( ) . bind ( "mesh_y_top" , consts . get ( ) . mesh_y_top ) ;
    _binder . get ( ) . bind ( "mesh_z" , consts . get ( ) . mesh_z ) ;
    _binder . get ( ) . bind ( "mesh_u_top_left" , consts . get ( ) . mesh_u_top_left ) ;
    _binder . get ( ) . bind ( "mesh_v_top_left" , consts . get ( ) . mesh_v_top_left ) ;
    _binder . get ( ) . bind ( "mesh_u_top_right" , consts . get ( ) . mesh_u_top_right ) ;
    _binder . get ( ) . bind ( "mesh_v_top_right" , consts . get ( ) . mesh_v_top_right ) ;
    _binder . get ( ) . bind ( "mesh_u_bottom_left" , consts . get ( ) . mesh_u_bottom_left ) ;
    _binder . get ( ) . bind ( "mesh_v_bottom_left" , consts . get ( ) . mesh_v_bottom_left ) ;
    _binder . get ( ) . bind ( "mesh_u_bottom_right" , consts . get ( ) . mesh_u_bottom_right ) ;
    _binder . get ( ) . bind ( "mesh_v_bottom_right" , consts . get ( ) . mesh_v_bottom_right ) ;
    _binder . get ( ) . bind ( "texture_pen_r" , consts . get ( ) . texture_pen_r ) ;
    _binder . get ( ) . bind ( "texture_pen_g" , consts . get ( ) . texture_pen_g ) ;
    _binder . get ( ) . bind ( "texture_pen_b" , consts . get ( ) . texture_pen_b ) ;
    _binder . get ( ) . bind ( "texture_pen_a" , consts . get ( ) . texture_pen_a ) ;
    _binder . get ( ) . bind ( "texture_paper_r" , consts . get ( ) . texture_paper_r ) ;
    _binder . get ( ) . bind ( "texture_paper_g" , consts . get ( ) . texture_paper_g ) ;
    _binder . get ( ) . bind ( "texture_paper_b" , consts . get ( ) . texture_paper_b ) ;
    _binder . get ( ) . bind ( "texture_paper_a" , consts . get ( ) . texture_paper_a ) ;
    _binder . get ( ) . bind ( "texture_stripes" , consts . get ( ) . texture_stripes ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_fidget_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_fidget_stateless :: logic_fidget_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_fidget_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_fidget_stateless" ) ;
    _binder . get ( ) . bind ( "fidget_size" , consts . get ( ) . fidget_size ) ;
    _binder . get ( ) . bind ( "fidget_r" , consts . get ( ) . fidget_r ) ;
    _binder . get ( ) . bind ( "fidget_g" , consts . get ( ) . fidget_g ) ;
    _binder . get ( ) . bind ( "fidget_b" , consts . get ( ) . fidget_b ) ;
    _binder . get ( ) . bind ( "mesh_x" , consts . get ( ) . mesh_x ) ;
    _binder . get ( ) . bind ( "mesh_y_from_top" , consts . get ( ) . mesh_y_from_top ) ;
    _binder . get ( ) . bind ( "mesh_z" , consts . get ( ) . mesh_z ) ;
    _binder . get ( ) . bind ( "angle_delta" , consts . get ( ) . angle_delta ) ;
    _binder . get ( ) . bind ( "fidget_edges" , consts . get ( ) . fidget_edges ) ;
    _binder . get ( ) . bind ( "scale_in_frames" , consts . get ( ) . scale_in_frames ) ;
    _binder . get ( ) . bind ( "should_render_fidget" , consts . get ( ) . should_render_fidget ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_main_menu_animation_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_main_menu_animation_stateless :: logic_main_menu_animation_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_main_menu_animation_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_main_menu_animation_stateless" ) ;
    _binder . get ( ) . bind ( "shake_time_to_begin" , consts . get ( ) . shake_time_to_begin ) ;
    _binder . get ( ) . bind ( "shake_time_from_begin_to_end" , consts . get ( ) . shake_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "shake_shift_x_amplitude_begin" , consts . get ( ) . shake_shift_x_amplitude_begin ) ;
    _binder . get ( ) . bind ( "shake_shift_x_amplitude_end" , consts . get ( ) . shake_shift_x_amplitude_end ) ;
    _binder . get ( ) . bind ( "shake_shift_x_period_in_seconds" , consts . get ( ) . shake_shift_x_period_in_seconds ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_main_menu_letters_animation_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_main_menu_letters_animation_stateless :: logic_main_menu_letters_animation_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_main_menu_letters_animation_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_main_menu_letters_animation_stateless" ) ;
    _binder . get ( ) . bind ( "appear_time_from_begin_to_middle_in_seconds" , consts . get ( ) . appear_time_from_begin_to_middle_in_seconds ) ;
    _binder . get ( ) . bind ( "appear_time_from_middle_to_end_in_seconds" , consts . get ( ) . appear_time_from_middle_to_end_in_seconds ) ;
    _binder . get ( ) . bind ( "appear_delay_per_col_in_seconds" , consts . get ( ) . appear_delay_per_col_in_seconds ) ;
    _binder . get ( ) . bind ( "appear_delay_per_row_in_seconds" , consts . get ( ) . appear_delay_per_row_in_seconds ) ;
    _binder . get ( ) . bind ( "appear_scale_begin" , consts . get ( ) . appear_scale_begin ) ;
    _binder . get ( ) . bind ( "appear_scale_middle" , consts . get ( ) . appear_scale_middle ) ;
    _binder . get ( ) . bind ( "appear_scale_end" , consts . get ( ) . appear_scale_end ) ;
    _binder . get ( ) . bind ( "disappear_animation_time_in_seconds" , consts . get ( ) . disappear_animation_time_in_seconds ) ;
    _binder . get ( ) . bind ( "disappear_time_from_begin_to_end_in_seconds" , consts . get ( ) . disappear_time_from_begin_to_end_in_seconds ) ;
    _binder . get ( ) . bind ( "disappear_delay_per_row_in_seconds" , consts . get ( ) . disappear_delay_per_row_in_seconds ) ;
    _binder . get ( ) . bind ( "disappear_delay_per_col_in_seconds" , consts . get ( ) . disappear_delay_per_col_in_seconds ) ;
    _binder . get ( ) . bind ( "disappear_scale_begin" , consts . get ( ) . disappear_scale_begin ) ;
    _binder . get ( ) . bind ( "disappear_scale_end" , consts . get ( ) . disappear_scale_end ) ;
    _binder . get ( ) . bind ( "idle_vertical_shift_period_in_seconds" , consts . get ( ) . idle_vertical_shift_period_in_seconds ) ;
    _binder . get ( ) . bind ( "idle_vertical_shift_phase_per_col" , consts . get ( ) . idle_vertical_shift_phase_per_col ) ;
    _binder . get ( ) . bind ( "idle_vertical_shift_phase_per_row" , consts . get ( ) . idle_vertical_shift_phase_per_row ) ;
    _binder . get ( ) . bind ( "idle_vertical_shift_amplitude" , consts . get ( ) . idle_vertical_shift_amplitude ) ;
    _binder . get ( ) . bind ( "idle_horizontal_shift_period_in_seconds" , consts . get ( ) . idle_horizontal_shift_period_in_seconds ) ;
    _binder . get ( ) . bind ( "idle_horizontal_shift_phase_per_row" , consts . get ( ) . idle_horizontal_shift_phase_per_row ) ;
    _binder . get ( ) . bind ( "idle_horizontal_shift_amplitude" , consts . get ( ) . idle_horizontal_shift_amplitude ) ;
    _binder . get ( ) . bind ( "selection_time_stable" , consts . get ( ) . selection_time_stable ) ;
    _binder . get ( ) . bind ( "selection_time_transition" , consts . get ( ) . selection_time_transition ) ;
    _binder . get ( ) . bind ( "selection_scale_min" , consts . get ( ) . selection_scale_min ) ;
    _binder . get ( ) . bind ( "selection_scale_max" , consts . get ( ) . selection_scale_max ) ;
    _binder . get ( ) . bind ( "selection_push_time_from_begin_to_middle" , consts . get ( ) . selection_push_time_from_begin_to_middle ) ;
    _binder . get ( ) . bind ( "selection_push_time_from_middle_to_end" , consts . get ( ) . selection_push_time_from_middle_to_end ) ;
    _binder . get ( ) . bind ( "selection_push_scale_begin" , consts . get ( ) . selection_push_scale_begin ) ;
    _binder . get ( ) . bind ( "selection_push_scale_middle" , consts . get ( ) . selection_push_scale_middle ) ;
    _binder . get ( ) . bind ( "selection_push_scale_end" , consts . get ( ) . selection_push_scale_end ) ;
    _binder . get ( ) . bind ( "selection_weight_time_to_begin" , consts . get ( ) . selection_weight_time_to_begin ) ;
    _binder . get ( ) . bind ( "selection_weight_time_from_begin_to_end" , consts . get ( ) . selection_weight_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "unselection_weight_time_to_begin" , consts . get ( ) . unselection_weight_time_to_begin ) ;
    _binder . get ( ) . bind ( "unselection_weight_time_from_begin_to_end" , consts . get ( ) . unselection_weight_time_from_begin_to_end ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_main_menu_letters_layout_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_main_menu_letters_layout_stateless :: logic_main_menu_letters_layout_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_main_menu_letters_layout_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_main_menu_letters_layout_stateless" ) ;
    _binder . get ( ) . bind ( "letter_size_fract_horizontal_spacing" , consts . get ( ) . letter_size_fract_horizontal_spacing ) ;
    _binder . get ( ) . bind ( "letter_size_fract_vertical_spacing" , consts . get ( ) . letter_size_fract_vertical_spacing ) ;
    _binder . get ( ) . bind ( "letter_size_fract_horizontal_border" , consts . get ( ) . letter_size_fract_horizontal_border ) ;
    _binder . get ( ) . bind ( "letter_size_fract_vertical_border" , consts . get ( ) . letter_size_fract_vertical_border ) ;
    _binder . get ( ) . bind ( "menu_position_z" , consts . get ( ) . menu_position_z ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_main_menu_letters_meshes_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_main_menu_letters_meshes_stateless :: logic_main_menu_letters_meshes_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_main_menu_letters_meshes_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_main_menu_letters_meshes_stateless" ) ;
    _binder . get ( ) . bind ( "letter_mesh_size" , consts . get ( ) . letter_mesh_size ) ;
    _binder . get ( ) . bind ( "letter_mesh_color_r" , consts . get ( ) . letter_mesh_color_r ) ;
    _binder . get ( ) . bind ( "letter_mesh_color_g" , consts . get ( ) . letter_mesh_color_g ) ;
    _binder . get ( ) . bind ( "letter_mesh_color_b" , consts . get ( ) . letter_mesh_color_b ) ;
    _binder . get ( ) . bind ( "letter_mesh_color_a" , consts . get ( ) . letter_mesh_color_a ) ;
    _binder . get ( ) . bind ( "time_between_creation" , consts . get ( ) . time_between_creation ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_main_menu_selection_animation_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_main_menu_selection_animation_stateless :: logic_main_menu_selection_animation_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_main_menu_selection_animation_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_main_menu_selection_animation_stateless" ) ;
    _binder . get ( ) . bind ( "appear_horizontal_scale_time_to_begin" , consts . get ( ) . appear_horizontal_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "appear_horizontal_scale_time_from_begin_to_end" , consts . get ( ) . appear_horizontal_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "appear_horizontal_scale_value_begin" , consts . get ( ) . appear_horizontal_scale_value_begin ) ;
    _binder . get ( ) . bind ( "appear_horizontal_scale_value_end" , consts . get ( ) . appear_horizontal_scale_value_end ) ;
    _binder . get ( ) . bind ( "appear_vertical_scale_time_to_begin" , consts . get ( ) . appear_vertical_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "appear_vertical_scale_time_from_begin_to_middle" , consts . get ( ) . appear_vertical_scale_time_from_begin_to_middle ) ;
    _binder . get ( ) . bind ( "appear_vertical_scale_time_from_middle_to_end" , consts . get ( ) . appear_vertical_scale_time_from_middle_to_end ) ;
    _binder . get ( ) . bind ( "appear_vertical_scale_value_begin" , consts . get ( ) . appear_vertical_scale_value_begin ) ;
    _binder . get ( ) . bind ( "appear_vertical_scale_value_middle" , consts . get ( ) . appear_vertical_scale_value_middle ) ;
    _binder . get ( ) . bind ( "appear_vertical_scale_value_end" , consts . get ( ) . appear_vertical_scale_value_end ) ;
    _binder . get ( ) . bind ( "appear_total_animation_time" , consts . get ( ) . appear_total_animation_time ) ;
    _binder . get ( ) . bind ( "disappear_horizontal_scale_time_to_begin" , consts . get ( ) . disappear_horizontal_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "disappear_horizontal_scale_time_from_begin_to_end" , consts . get ( ) . disappear_horizontal_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "disappear_horizontal_scale_value_begin" , consts . get ( ) . disappear_horizontal_scale_value_begin ) ;
    _binder . get ( ) . bind ( "disappear_horizontal_scale_value_end" , consts . get ( ) . disappear_horizontal_scale_value_end ) ;
    _binder . get ( ) . bind ( "disappear_vertical_scale_time_to_begin" , consts . get ( ) . disappear_vertical_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "disappear_vertical_scale_time_from_begin_to_end" , consts . get ( ) . disappear_vertical_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "disappear_vertical_scale_value_begin" , consts . get ( ) . disappear_vertical_scale_value_begin ) ;
    _binder . get ( ) . bind ( "disappear_vertical_scale_value_end" , consts . get ( ) . disappear_vertical_scale_value_end ) ;
    _binder . get ( ) . bind ( "idle_position_z" , consts . get ( ) . idle_position_z ) ;
    _binder . get ( ) . bind ( "idle_attention_horizontal_scale_min" , consts . get ( ) . idle_attention_horizontal_scale_min ) ;
    _binder . get ( ) . bind ( "idle_attention_horizontal_scale_max" , consts . get ( ) . idle_attention_horizontal_scale_max ) ;
    _binder . get ( ) . bind ( "idle_attention_horizontal_scale_period_in_seconds" , consts . get ( ) . idle_attention_horizontal_scale_period_in_seconds ) ;
    _binder . get ( ) . bind ( "idle_attention_vertical_scale_min" , consts . get ( ) . idle_attention_vertical_scale_min ) ;
    _binder . get ( ) . bind ( "idle_attention_vertical_scale_max" , consts . get ( ) . idle_attention_vertical_scale_max ) ;
    _binder . get ( ) . bind ( "idle_attention_vertical_scale_period_in_seconds" , consts . get ( ) . idle_attention_vertical_scale_period_in_seconds ) ;
    _binder . get ( ) . bind ( "push_time_from_begin_to_middle" , consts . get ( ) . push_time_from_begin_to_middle ) ;
    _binder . get ( ) . bind ( "push_time_from_middle_to_end" , consts . get ( ) . push_time_from_middle_to_end ) ;
    _binder . get ( ) . bind ( "push_horizontal_scale_begin" , consts . get ( ) . push_horizontal_scale_begin ) ;
    _binder . get ( ) . bind ( "push_horizontal_scale_middle" , consts . get ( ) . push_horizontal_scale_middle ) ;
    _binder . get ( ) . bind ( "push_horizontal_scale_end" , consts . get ( ) . push_horizontal_scale_end ) ;
    _binder . get ( ) . bind ( "push_vertical_scale_begin" , consts . get ( ) . push_vertical_scale_begin ) ;
    _binder . get ( ) . bind ( "push_vertical_scale_middle" , consts . get ( ) . push_vertical_scale_middle ) ;
    _binder . get ( ) . bind ( "push_vertical_scale_end" , consts . get ( ) . push_vertical_scale_end ) ;
    _binder . get ( ) . bind ( "push_attention_horizontal_scale_min" , consts . get ( ) . push_attention_horizontal_scale_min ) ;
    _binder . get ( ) . bind ( "push_attention_horizontal_scale_max" , consts . get ( ) . push_attention_horizontal_scale_max ) ;
    _binder . get ( ) . bind ( "push_attention_vertical_scale_min" , consts . get ( ) . push_attention_vertical_scale_min ) ;
    _binder . get ( ) . bind ( "push_attention_vertical_scale_max" , consts . get ( ) . push_attention_vertical_scale_max ) ;
    _binder . get ( ) . bind ( "push_attention_period_in_seconds" , consts . get ( ) . push_attention_period_in_seconds ) ;
    _binder . get ( ) . bind ( "push_weight_time_to_begin" , consts . get ( ) . push_weight_time_to_begin ) ;
    _binder . get ( ) . bind ( "push_weight_time_from_begin_to_end" , consts . get ( ) . push_weight_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "push_weight_min" , consts . get ( ) . push_weight_min ) ;
    _binder . get ( ) . bind ( "push_weight_max" , consts . get ( ) . push_weight_max ) ;
    _binder . get ( ) . bind ( "select_horizontal_scale_time_to_begin" , consts . get ( ) . select_horizontal_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "select_horizontal_scale_time_from_begin_to_end" , consts . get ( ) . select_horizontal_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "select_horizontal_scale_value_begin" , consts . get ( ) . select_horizontal_scale_value_begin ) ;
    _binder . get ( ) . bind ( "select_horizontal_scale_value_end" , consts . get ( ) . select_horizontal_scale_value_end ) ;
    _binder . get ( ) . bind ( "select_vertical_scale_time_to_begin" , consts . get ( ) . select_vertical_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "select_vertical_scale_time_from_begin_to_end" , consts . get ( ) . select_vertical_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "select_vertical_scale_value_begin" , consts . get ( ) . select_vertical_scale_value_begin ) ;
    _binder . get ( ) . bind ( "select_vertical_scale_value_end" , consts . get ( ) . select_vertical_scale_value_end ) ;
    _binder . get ( ) . bind ( "select_total_animation_time" , consts . get ( ) . select_total_animation_time ) ;
    _binder . get ( ) . bind ( "unselect_horizontal_scale_time_to_begin" , consts . get ( ) . unselect_horizontal_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "unselect_horizontal_scale_time_from_begin_to_end" , consts . get ( ) . unselect_horizontal_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "unselect_horizontal_scale_value_begin" , consts . get ( ) . unselect_horizontal_scale_value_begin ) ;
    _binder . get ( ) . bind ( "unselect_horizontal_scale_value_end" , consts . get ( ) . unselect_horizontal_scale_value_end ) ;
    _binder . get ( ) . bind ( "unselect_vertical_scale_time_to_begin" , consts . get ( ) . unselect_vertical_scale_time_to_begin ) ;
    _binder . get ( ) . bind ( "unselect_vertical_scale_time_from_begin_to_end" , consts . get ( ) . unselect_vertical_scale_time_from_begin_to_end ) ;
    _binder . get ( ) . bind ( "unselect_vertical_scale_value_begin" , consts . get ( ) . unselect_vertical_scale_value_begin ) ;
    _binder . get ( ) . bind ( "unselect_vertical_scale_value_end" , consts . get ( ) . unselect_vertical_scale_value_end ) ;
    _binder . get ( ) . bind ( "unselect_total_animation_time" , consts . get ( ) . unselect_total_animation_time ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_main_menu_selection_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_main_menu_selection_stateless :: logic_main_menu_selection_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_main_menu_selection_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_main_menu_selection_stateless" ) ;
    _binder . get ( ) . bind ( "mesh_size" , consts . get ( ) . mesh_size ) ;
    _binder . get ( ) . bind ( "mesh_color_r" , consts . get ( ) . mesh_color_r ) ;
    _binder . get ( ) . bind ( "mesh_color_g" , consts . get ( ) . mesh_color_g ) ;
    _binder . get ( ) . bind ( "mesh_color_b" , consts . get ( ) . mesh_color_b ) ;
    _binder . get ( ) . bind ( "mesh_color_a" , consts . get ( ) . mesh_color_a ) ;
    _binder . get ( ) . bind ( "selected_rect_vertical_scale" , consts . get ( ) . selected_rect_vertical_scale ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_title_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const typename mediator :: logic_title_stateless :: logic_title_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_title_stateless_consts ( consts ) ;
    _binder . get ( ) . module ( "logic_title_stateless" ) ;
    _binder . get ( ) . bind ( "appear_pos_angle_periods" , consts . get ( ) . appear_pos_angle_periods ) ;
    _binder . get ( ) . bind ( "appear_rubber_first" , consts . get ( ) . appear_rubber_first ) ;
    _binder . get ( ) . bind ( "appear_rubber_last" , consts . get ( ) . appear_rubber_last ) ;
    _binder . get ( ) . bind ( "appear_duration_in_frames" , consts . get ( ) . appear_duration_in_frames ) ;
    _binder . get ( ) . bind ( "disappear_pos_angle_periods" , consts . get ( ) . disappear_pos_angle_periods ) ;
    _binder . get ( ) . bind ( "disappear_rubber_first" , consts . get ( ) . disappear_rubber_first ) ;
    _binder . get ( ) . bind ( "disappear_rubber_last" , consts . get ( ) . disappear_rubber_last ) ;
    _binder . get ( ) . bind ( "disappear_duration_in_frames" , consts . get ( ) . disappear_duration_in_frames ) ;
    _binder . get ( ) . bind ( "scene_scale_min" , consts . get ( ) . scene_scale_min ) ;
    _binder . get ( ) . bind ( "scene_scale_max" , consts . get ( ) . scene_scale_max ) ;
    _binder . get ( ) . bind ( "spin_radius_in_letters" , consts . get ( ) . spin_radius_in_letters ) ;
    _binder . get ( ) . bind ( "frames_between_letters" , consts . get ( ) . frames_between_letters ) ;
}

