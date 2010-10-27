template < typename mediator >
class shy_logic_blanket
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_creation_permit ) ;
    void receive ( typename messages :: logic_blanket_mesh_creation_finished ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
} ;

template < typename mediator >
void shy_logic_blanket < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_blanket < mediator > :: receive ( typename messages :: logic_blanket_creation_permit )
{
    _mediator . get ( ) . send ( typename messages :: logic_blanket_mesh_create ( ) ) ;
}

template < typename mediator >
void shy_logic_blanket < mediator > :: receive ( typename messages :: logic_blanket_mesh_creation_finished )
{
    _mediator . get ( ) . send ( typename messages :: logic_blanket_creation_finished ( ) ) ;
}

