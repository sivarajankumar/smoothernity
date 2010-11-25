template < typename mediator >
class shy_logic_main_menu_animation_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

public :
    class logic_main_menu_animation_stateless_consts_type
    {
    public :
        logic_main_menu_animation_stateless_consts_type ( ) ;
    public :
        num_fract shake_time_to_begin ;
        num_fract shake_time_from_begin_to_end ;
        num_fract shake_shift_x_amplitude_begin ;
        num_fract shake_shift_x_amplitude_end ;
        num_fract shake_shift_x_period_in_seconds ;
    } ;

    class logic_main_menu_animation_messages
    {
    public :
        class logic_main_menu_animation_shake_transform_reply { public : num_fract shift_x ; } ;
        class logic_main_menu_animation_shake_transform_request { } ;
        class logic_main_menu_animation_transform_reply { public : matrix_data view ; } ;
        class logic_main_menu_animation_transform_request { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_shake_transform_reply ) ;
        void send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_shake_transform_request ) ;
        void send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_transform_reply ) ;
        void send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_animation_stateless ( ) ;
private :
    shy_logic_main_menu_animation_stateless < mediator > & operator= ( const shy_logic_main_menu_animation_stateless < mediator > & ) ;
public :
    const logic_main_menu_animation_stateless_consts_type logic_main_menu_animation_stateless_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_animation_stateless < mediator > :: logic_main_menu_animation_stateless_consts_type :: logic_main_menu_animation_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( shake_time_to_begin , 0 , 10 ) ;
    platform_math :: make_num_fract ( shake_time_from_begin_to_end , 6 , 10 ) ;
    platform_math :: make_num_fract ( shake_shift_x_amplitude_begin , 20 , 1000 ) ;
    platform_math :: make_num_fract ( shake_shift_x_amplitude_end , 5 , 1000 ) ;
    platform_math :: make_num_fract ( shake_shift_x_period_in_seconds , 2 , 10 ) ;
}

template < typename mediator >
shy_logic_main_menu_animation_stateless < mediator > :: shy_logic_main_menu_animation_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_animation_stateless < mediator > 
:: logic_main_menu_animation_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_animation_stateless < mediator > 
:: logic_main_menu_animation_sender < receivers > 
:: send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_shake_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_animation_stateless < mediator > 
:: logic_main_menu_animation_sender < receivers > 
:: send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_shake_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_animation_shake . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_animation_stateless < mediator > 
:: logic_main_menu_animation_sender < receivers > 
:: send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_animation_stateless < mediator > 
:: logic_main_menu_animation_sender < receivers > 
:: send ( typename logic_main_menu_animation_messages :: logic_main_menu_animation_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_animation . get ( ) . receive ( msg ) ;
}
