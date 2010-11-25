template < typename context >
class shy_reflection
{
    typedef typename context :: mediator mediator ;
    typedef typename context :: mediator :: logic_title_stateless :: logic_title_stateless_consts_type logic_title_stateless_consts_type ;
    typedef typename context :: mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename context :: reflection_binder reflection_binder ;
public :
    void bind_all 
        ( typename platform_pointer :: template pointer < mediator >
        , typename platform_pointer :: template pointer < reflection_binder > 
        ) ;
private :
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
    _bind_logic_title_stateless_consts ( ) ;
}

template < typename context >
void shy_reflection < context > :: _bind_logic_title_stateless_consts ( )
{
    typename platform_pointer :: template pointer < const logic_title_stateless_consts_type > consts ;
    _mediator . get ( ) . logic_title_stateless_consts ( consts ) ;
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

