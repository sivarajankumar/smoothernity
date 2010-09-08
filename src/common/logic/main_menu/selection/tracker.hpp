template < typename mediator >
class shy_logic_main_menu_selection_tracker
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_main_menu_selection_tracker_consts_type
    {
    public :
        _logic_main_menu_selection_tracker_consts_type ( ) ;
    public :
        num_fract position_z ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_track ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_tracker_consts_type _logic_main_menu_selection_tracker_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_tracker < mediator > :: _logic_main_menu_selection_tracker_consts_type :: _logic_main_menu_selection_tracker_consts_type ( )
{
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: logic_main_menu_selection_track )
{
    matrix_data transform ;
    num_fract zero ;
    num_fract half ;
    num_fract shift ;
    
    platform_math :: make_num_fract ( zero , 0 , 1 ) ;
    platform_math :: make_num_fract ( half , 1 , 2 ) ;
    shift = _logic_main_menu_selection_tracker_consts . position_z ;
    
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , half , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , half , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , half ) ;
    platform_matrix :: set_origin ( transform , zero , zero , shift ) ;
    
    typename messages :: logic_main_menu_selection_mesh_set_transform transform_msg ;
    transform_msg . transform = transform ;
    _mediator . get ( ) . send ( transform_msg ) ;
}
