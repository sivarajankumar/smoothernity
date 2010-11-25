template < typename mediator >
class shy_logic_title_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
	typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_title_stateless_consts_type
    {
    public :
        logic_title_stateless_consts_type ( ) ;
    public :
        num_fract appear_pos_angle_periods ;
        num_fract appear_rubber_first ;
        num_fract appear_rubber_last ;
        num_whole appear_duration_in_frames ;
        
        num_fract disappear_pos_angle_periods ;
        num_fract disappear_rubber_first ;
        num_fract disappear_rubber_last ;
        num_whole disappear_duration_in_frames ;

        num_fract scene_scale_min ;
        num_fract scene_scale_max ;
        
        num_fract spin_radius_in_letters ;
        num_whole frames_between_letters ;
    } ;
    
	class logic_title_messages
	{
	public :
        class logic_title_created { } ;
        class logic_title_finished { } ;
        class logic_title_launch_permit { } ;
        class logic_title_render { } ;
        class logic_title_update { } ;
	} ;

	template < typename receivers >
	class logic_title_sender
	{
	public :
		void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_title_messages :: logic_title_created ) ;
        void send ( typename logic_title_messages :: logic_title_finished ) ;
        void send ( typename logic_title_messages :: logic_title_launch_permit ) ;
        void send ( typename logic_title_messages :: logic_title_render ) ;
        void send ( typename logic_title_messages :: logic_title_update ) ;
	private :
		typename platform_pointer :: template pointer < const receivers > _receivers ;
	} ;

public :
    const logic_title_stateless_consts_type logic_title_stateless_consts ;
} ;

template < typename mediator >
shy_logic_title_stateless < mediator > :: logic_title_stateless_consts_type :: logic_title_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( appear_pos_angle_periods , 11 , 2 ) ;
    platform_math :: make_num_fract ( appear_rubber_first , 19 , 20 ) ;
    platform_math :: make_num_fract ( appear_rubber_last , 19 , 20 ) ;
    platform_math :: make_num_whole ( appear_duration_in_frames , 250 ) ;

    platform_math :: make_num_fract ( disappear_pos_angle_periods , 22 , 2 ) ;
    platform_math :: make_num_fract ( disappear_rubber_first , 59 , 60 ) ;
    platform_math :: make_num_fract ( disappear_rubber_last , 29 , 30 ) ;
    platform_math :: make_num_whole ( disappear_duration_in_frames , 150 ) ;

    platform_math :: make_num_fract ( scene_scale_min , 7 , 10 ) ;
    platform_math :: make_num_fract ( scene_scale_max , 9 , 10 ) ;
    
    platform_math :: make_num_fract ( spin_radius_in_letters , 2 , 1 ) ;
    platform_math :: make_num_whole ( frames_between_letters , 5 ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
	_receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_created msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_launch_permit msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_render msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_update msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}
