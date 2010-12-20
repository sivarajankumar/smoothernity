template < typename mediator >
class shy_logic_application_stateless
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_application_stateless_consts_type
    {
    public :
        logic_application_stateless_consts_type ( ) ;
    public :
        num_whole skip_title ;
        num_whole skip_main_menu ;
        num_whole skip_amusement ;
    } ;

    class logic_application_fsm_inputs_type
    {
    public :
        num_whole logic_amusement_created ;
        num_whole logic_amusement_finished ;
        num_whole logic_application_render ;
        num_whole logic_application_update ;
        num_whole logic_text_prepared ;
        num_whole logic_title_created ;
        num_whole logic_title_finished ;
        num_whole logic_main_menu_created ;
        num_whole logic_main_menu_finished ;
        num_whole stage_amusement_disabled ;
        num_whole stage_amusement_enabled ;
        num_whole stage_main_menu_disabled ;
        num_whole stage_main_menu_enabled ;
        num_whole stage_title_disabled ;
        num_whole stage_title_enabled ;
    } ;

    class logic_application_fsm_actions_type
    {
    public :
        void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;

        void logic_amusement_creation_permit ( ) ;
        void logic_amusement_launch_permit ( ) ;
        void logic_amusement_render ( ) ;
        void logic_amusement_update ( ) ;
        void logic_game_launch_permit ( ) ;
        void logic_game_render ( ) ;
        void logic_game_update ( ) ;
        void logic_main_menu_creation_permit ( ) ;
        void logic_main_menu_launch_permit ( ) ;
        void logic_main_menu_render ( ) ;
        void logic_main_menu_update ( ) ;
        void logic_text_prepare_permit ( ) ;
        void logic_text_update ( ) ;
        void logic_title_launch_permit ( ) ;
        void logic_title_render ( ) ;
        void logic_title_update ( ) ;
    private :
        typename platform_pointer :: template pointer < mediator > _mediator ;
    } ;

    class logic_application_messages
    {
    public :
        class logic_application_render { } ;
        class logic_application_update { } ;
    } ;
    
    template < typename receivers >
    class logic_application_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_application_messages :: logic_application_render ) ;
        void send ( typename logic_application_messages :: logic_application_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
public :
    shy_logic_application_stateless ( ) ;
private :
    shy_logic_application_stateless < mediator > & operator= ( const shy_logic_application_stateless < mediator > & ) ;
public :
    const logic_application_stateless_consts_type logic_application_stateless_consts ;
} ;

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_amusement_creation_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_amusement_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_amusement_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_amusement_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_game_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_game_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_game_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_game_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_game_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_game_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_creation_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_text_prepare_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_text_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_text_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_text_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_title_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_title_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_title_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_title_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_stateless < mediator > :: logic_application_fsm_actions_type :: logic_title_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_title_update ( ) ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
shy_logic_application_stateless < mediator > :: shy_logic_application_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_application_stateless < mediator > 
:: logic_application_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_application_stateless < mediator > 
:: logic_application_sender < receivers >
:: send ( typename logic_application_messages :: logic_application_render msg )
{
    _receivers . get ( ) . logic_application_fsm . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_application_stateless < mediator > 
:: logic_application_sender < receivers >
:: send ( typename logic_application_messages :: logic_application_update msg )
{
    _receivers . get ( ) . logic_application_fsm . get ( ) . receive ( msg ) ;
}
