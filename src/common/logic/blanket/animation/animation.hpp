template < typename mediator >
class shy_logic_blanket_animation
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_blanket_animation_consts_type
    {
    public :
        _logic_blanket_animation_consts_type ( ) ;
    public :
        num_fract origin_x ;
        num_fract origin_y ;
        num_fract origin_z ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_animation_transform_request ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_blanket_animation_consts_type _logic_blanket_animation_consts ;
} ;

template < typename mediator >
shy_logic_blanket_animation < mediator > :: _logic_blanket_animation_consts_type :: _logic_blanket_animation_consts_type ( )
{
    platform_math :: make_num_fract ( origin_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_z , - 3 , 1 ) ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: receive ( typename messages :: logic_blanket_animation_transform_request )
{
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    matrix_data transform ;

    origin_x = _logic_blanket_animation_consts . origin_x ;
    origin_y = _logic_blanket_animation_consts . origin_y ;
    origin_z = _logic_blanket_animation_consts . origin_z ;

    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    typename messages :: logic_blanket_animation_transform_reply msg ;
    msg . transform = transform ;
    _mediator . get ( ) . send ( msg ) ;
}

