template < typename mediator >
class shy_logic_door_mesh
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_door_mesh_consts_type
    {
    public :
        _logic_door_mesh_consts_type ( ) ;
    public :
        num_fract color_r ;
        num_fract color_g ;
        num_fract color_b ;
        num_fract color_a ;
        num_fract mesh_x_left ;
        num_fract mesh_x_right ;
        num_fract mesh_y_bottom ;
        num_fract mesh_y_top ;
        num_fract mesh_z ;
        num_fract mesh_u_left ;
        num_fract mesh_u_right ;
        num_fract mesh_v_bottom ;
        num_fract mesh_v_top ;
        num_fract position_x ;
        num_fract position_y ;
        num_fract position_z ;
    } ;

    class _engine_render_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        engine_render_mesh_id mesh ;
    } ;

    class _logic_door_mesh_create_state_type
    {
    public :
        num_whole requested ;
    } ;

public :
    shy_logic_door_mesh ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_mesh_create ) ;
private :
    shy_logic_door_mesh < mediator > & operator= ( const shy_logic_door_mesh < mediator > & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_door_mesh_consts_type _logic_door_mesh_consts ;

    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
    _logic_door_mesh_create_state_type _logic_door_mesh_create_state ;
} ;

template < typename mediator >
shy_logic_door_mesh < mediator > :: _logic_door_mesh_consts_type :: _logic_door_mesh_consts_type ( )
{
    platform_math :: make_num_fract ( color_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_x_left , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_x_right , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_y_bottom , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_y_top , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_z , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_v_bottom , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_v_top , 1 , 1 ) ;

    platform_math :: make_num_fract ( position_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( position_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
}

template < typename mediator >
shy_logic_door_mesh < mediator > :: shy_logic_door_mesh ( )
{
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: logic_door_mesh_create )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_mesh_creation_finished ( ) ) ;
}

