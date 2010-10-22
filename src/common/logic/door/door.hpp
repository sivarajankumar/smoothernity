template < typename mediator >
class shy_logic_door
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_creation_permit ) ;
    void receive ( typename messages :: logic_door_launch_permit ) ;
    void receive ( typename messages :: logic_door_mesh_creation_finished ) ;
    void receive ( typename messages :: logic_door_texture_creation_finished ) ;
    void receive ( typename messages :: logic_door_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    num_whole _launch_permitted ;
    num_whole _created ;
} ;

template < typename mediator >
void shy_logic_door < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door < mediator > :: receive ( typename messages :: logic_door_creation_permit )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_mesh_create ( ) ) ;
}

template < typename mediator >
void shy_logic_door < mediator > :: receive ( typename messages :: logic_door_launch_permit )
{
    _launch_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_door < mediator > :: receive ( typename messages :: logic_door_mesh_creation_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_texture_create ( ) ) ;
}

template < typename mediator >
void shy_logic_door < mediator > :: receive ( typename messages :: logic_door_texture_creation_finished )
{
    _created = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_door_creation_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_door < mediator > :: receive ( typename messages :: logic_door_update )
{
    if ( platform_conditions :: whole_is_true ( _launch_permitted )
      && platform_conditions :: whole_is_true ( _created )
       )
    {
        _mediator . get ( ) . send ( typename messages :: logic_door_place ( ) ) ;
    }
}

