template < typename mediator >
class shy_logic_main_menu_letters_animation_unselection_weight
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_letters_animation_unselection_weight_consts_type
    {
    public :
        _logic_main_menu_letters_animation_unselection_weight_consts_type ( ) ;
    public :
        num_fract time_to_begin ;
        num_fract time_from_begin_to_end ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_unselect_row ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_animation_unselection_weight < mediator > 
:: _logic_main_menu_letters_animation_unselection_weight_consts_type
:: _logic_main_menu_letters_animation_unselection_weight_consts_type ( )
{
    platform_math :: make_num_fract ( time_to_begin , 0 , 100 ) ;
    platform_math :: make_num_fract ( time_from_begin_to_end , 7 , 100 ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_request msg )
{
    typename messages :: logic_main_menu_letters_animation_unselection_weight_reply reply_msg ;
    reply_msg . row = msg . row ;
    reply_msg . col = msg . col ;
    reply_msg . weight = _platform_math_consts . get ( ) . fract_1 ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_unselect_row )
{
}
