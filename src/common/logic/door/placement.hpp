template < typename mediator >
class shy_logic_door_placement
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_place ) ;
    void receive ( typename messages :: logic_door_animation_transform_reply ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
} ;

template < typename mediator >
void shy_logic_door_placement < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_placement < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door_placement < mediator > :: receive ( typename messages :: logic_door_place )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_animation_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_door_placement < mediator > :: receive ( typename messages :: logic_door_animation_transform_reply msg )
{
    typename messages :: logic_door_mesh_set_transform set_transform_msg ;
    set_transform_msg . transform = msg . transform ;
    _mediator . get ( ) . send ( set_transform_msg ) ;
}

