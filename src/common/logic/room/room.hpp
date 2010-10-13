template < typename mediator >
class shy_logic_room
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_room_consts_type
    {
    public :
        _logic_room_consts_type ( ) ;
    public :
        num_fract show_time ;
    } ;

    class _logic_room_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;

public :
    shy_logic_room ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_room_creation_permit ) ;
    void receive ( typename messages :: logic_room_launch_permit ) ;
    void receive ( typename messages :: logic_room_mesh_creation_finished ) ;
    void receive ( typename messages :: logic_room_update ) ;
private :
    shy_logic_room < mediator > & operator= ( const shy_logic_room < mediator > & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_room_consts_type _logic_room_consts ;

    _logic_room_update_state_type _logic_room_update_state ;
} ;

template < typename mediator >
shy_logic_room < mediator > :: _logic_room_consts_type :: _logic_room_consts_type ( )
{
    platform_math :: make_num_fract ( show_time , 10 , 1 ) ;
}

template < typename mediator >
shy_logic_room < mediator > :: shy_logic_room ( )
{
}

template < typename mediator >
void shy_logic_room < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_room < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_room < mediator > :: receive ( typename messages :: logic_room_creation_permit )
{
    _mediator . get ( ) . send ( typename messages :: logic_room_mesh_create ( ) ) ;
}

template < typename mediator >
void shy_logic_room < mediator > :: receive ( typename messages :: logic_room_launch_permit )
{
    _logic_room_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_room_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_room < mediator > :: receive ( typename messages :: logic_room_mesh_creation_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_room_render_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_room < mediator > :: receive ( typename messages :: logic_room_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_update_state . launch_permitted ) )
    {
        num_fract time ;
        num_fract time_step ;
        num_fract show_time ;

        time = _logic_room_update_state . time ;
        show_time = _logic_room_consts . show_time ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;

        platform_math :: add_to_fract ( time , time_step ) ;
        if ( platform_conditions :: fract_greater_than_fract ( time , show_time ) )
        {
            _logic_room_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_false ;
            _mediator . get ( ) . send ( typename messages :: logic_room_finished ( ) ) ;
        }

        _logic_room_update_state . time = time ;
    }
}

