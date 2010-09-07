template < typename mediator >
class shy_logic_main_menu_stateless
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_text_stateless :: logic_text_letter_id logic_text_letter_id ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

public :
    class logic_main_menu_stateless_consts_type
    {
    public :
        logic_main_menu_stateless_consts_type ( ) ;
    public :
        static const_int_32 max_rows = 5 ;
        static const_int_32 max_cols = 16 ;
    } ;
    
    class logic_main_menu_messages
    {
    public :
        class logic_main_menu_creation_permit { } ;
        class logic_main_menu_finished { } ;
        class logic_main_menu_launch_permit { } ;
        class logic_main_menu_render { } ;
        class logic_main_menu_render_permit { } ;
        class logic_main_menu_selection_mesh_create { } ;
        class logic_main_menu_selection_mesh_create_finished { } ;
        class logic_main_menu_selection_mesh_destroy_reply { } ;
        class logic_main_menu_selection_mesh_destroy_request { } ;
        class logic_main_menu_selection_mesh_render_reply { } ;
        class logic_main_menu_selection_mesh_render_request { } ;
        class logic_main_menu_update { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_creation_permit ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_finished ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_launch_permit ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_render ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_render_permit ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_create ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_create_finished ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_destroy_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_destroy_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_render_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_render_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_stateless ( ) ;
private :
    shy_logic_main_menu_stateless < mediator > & operator= ( const shy_logic_main_menu_stateless < mediator > & ) ;
public :
    const logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_stateless < mediator > :: shy_logic_main_menu_stateless ( )
{
}

template < typename mediator >
shy_logic_main_menu_stateless < mediator > :: logic_main_menu_stateless_consts_type :: logic_main_menu_stateless_consts_type ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_launch_permit msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_disappear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_render msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_render_permit msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_create msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_create_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_destroy_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_destroy_reply msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_render_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_selection_mesh_render_reply msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_update msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_disappear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_creation_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_creation_permit msg ) 
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}
