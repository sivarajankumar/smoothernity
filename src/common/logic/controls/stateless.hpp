template < typename mediator >
class shy_logic_controls_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_controls_messages
    {
    public :
        class logic_controls_state_request { } ;
        class logic_controls_state_reply { public : num_whole primary_button_down ; num_fract cursor_x ; num_fract cursor_y ; } ;
    } ;

    template < typename receivers >
    class logic_controls_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_controls_messages :: logic_controls_state_reply ) ;
        void send ( typename logic_controls_messages :: logic_controls_state_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_controls_stateless < mediator > 
:: logic_controls_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_controls_stateless < mediator >
:: logic_controls_sender < receivers >
:: send ( typename logic_controls_messages :: logic_controls_state_reply msg )
{
    _receivers . get ( ) . logic_main_menu_choice . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_push . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_push . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_controls_stateless < mediator >
:: logic_controls_sender < receivers >
:: send ( typename logic_controls_messages :: logic_controls_state_request msg )
{
    _receivers . get ( ) . logic_controls . get ( ) . receive ( msg ) ;
}

