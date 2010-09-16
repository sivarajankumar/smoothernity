template < typename mediator >
class shy_logic_main_menu_selection_animation_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

public :
    class logic_main_menu_selection_animation_messages
    {
    public :
        class logic_main_menu_selection_animation_appear_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_appear_transform_request { } ;
        class logic_main_menu_selection_animation_disappear_start { } ;
        class logic_main_menu_selection_animation_disappear_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_disappear_transform_request { } ;
        class logic_main_menu_selection_animation_idle_transform_reply { public : vector_data position ; num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_idle_transform_request { } ;
        class logic_main_menu_selection_animation_transform_reply { public : matrix_data transform ; } ;
        class logic_main_menu_selection_animation_transform_request { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_selection_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_start ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_appear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_start msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_disappear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_disappear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}
