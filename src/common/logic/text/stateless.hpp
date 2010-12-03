template < typename mediator >
class shy_logic_text ;

template < typename mediator >
class shy_logic_text_stateless
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
public :
    class logic_text_letter_id 
    {
        friend class shy_logic_text < mediator > ;
        friend class shy_logic_text_stateless ;
        friend class shy_logic_text_stateless :: logic_text_stateless_consts_type ;
    private :
        num_whole _letter_id ;
    } ;

    class logic_text_alphabet_english_type 
    {
    public :
        logic_text_letter_id A ;
        logic_text_letter_id B ;
        logic_text_letter_id C ;
        logic_text_letter_id D ;
        logic_text_letter_id E ;
        logic_text_letter_id F ;
        logic_text_letter_id G ;
        logic_text_letter_id H ;
        logic_text_letter_id I ;
        logic_text_letter_id J ;
        logic_text_letter_id K ;
        logic_text_letter_id L ;
        logic_text_letter_id M ;
        logic_text_letter_id N ;
        logic_text_letter_id O ;
        logic_text_letter_id P ;
        logic_text_letter_id Q ;
        logic_text_letter_id R ;
        logic_text_letter_id S ;
        logic_text_letter_id T ;
        logic_text_letter_id U ;
        logic_text_letter_id V ;
        logic_text_letter_id W ;
        logic_text_letter_id X ;
        logic_text_letter_id Y ;
        logic_text_letter_id Z ;
    } ;
    
    class logic_text_stateless_consts_type
    {
    public :
        logic_text_stateless_consts_type ( ) ;
    public :
        logic_text_letter_id whitespace ;
        logic_text_alphabet_english_type alphabet_english ;
    } ;
    
    class logic_text_messages
    {
    public :
        class logic_text_letter_big_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; logic_text_letter_id letter ; } ;
        class logic_text_letter_big_tex_coords_request { public : logic_text_letter_id letter ; } ;
        class logic_text_letter_small_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; logic_text_letter_id letter ; } ;
        class logic_text_letter_small_tex_coords_request { public : logic_text_letter_id letter ; } ;
        class logic_text_prepare_permit { } ;
        class logic_text_prepared { } ;
        class logic_text_render_reply { } ;
        class logic_text_render_request { } ;
        class logic_text_update { } ;
        class logic_text_use_text_texture_reply { } ;
        class logic_text_use_text_texture_request { } ;
    } ;
    
    template < typename receivers >
    class logic_text_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_text_messages :: logic_text_letter_big_tex_coords_reply ) ;
        void send ( typename logic_text_messages :: logic_text_letter_big_tex_coords_request ) ;
        void send ( typename logic_text_messages :: logic_text_letter_small_tex_coords_reply ) ;
        void send ( typename logic_text_messages :: logic_text_letter_small_tex_coords_request ) ;
        void send ( typename logic_text_messages :: logic_text_prepare_permit ) ;
        void send ( typename logic_text_messages :: logic_text_prepared ) ;
        void send ( typename logic_text_messages :: logic_text_render_reply ) ;
        void send ( typename logic_text_messages :: logic_text_render_request ) ;
        void send ( typename logic_text_messages :: logic_text_update ) ;
        void send ( typename logic_text_messages :: logic_text_use_text_texture_reply ) ;
        void send ( typename logic_text_messages :: logic_text_use_text_texture_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
    
public :
    shy_logic_text_stateless ( ) ;
    shy_logic_text_stateless & operator= ( const shy_logic_text_stateless & ) ;
    static void are_letters_equal ( num_whole & result , logic_text_letter_id a , logic_text_letter_id b ) ;
public :
    const logic_text_stateless_consts_type logic_text_stateless_consts ;
} ;

template < typename mediator >
shy_logic_text_stateless < mediator > :: shy_logic_text_stateless ( )
{
}

template < typename mediator >
shy_logic_text_stateless < mediator > :: logic_text_stateless_consts_type :: logic_text_stateless_consts_type ( )
{
    num_whole index ;
    typename platform_pointer :: template pointer < logic_text_alphabet_english_type > eng ;
    platform_pointer :: bind ( eng , alphabet_english ) ;
    platform_math :: make_num_whole ( index , 0 ) ;
    whitespace . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . A . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . B . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . C . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . D . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . E . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . F . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . G . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . H . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . I . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . J . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . K . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . L . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . M . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . N . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . O . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . P . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . Q . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . R . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . S . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . T . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . U . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . V . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . W . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . X . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . Y . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    eng . get ( ) . Z . _letter_id = index ; platform_math :: inc_whole ( index ) ;
}

template < typename mediator >
void shy_logic_text_stateless < mediator > :: are_letters_equal ( num_whole & result , logic_text_letter_id a , logic_text_letter_id b )
{
    platform_math :: make_num_whole ( result , platform_conditions :: wholes_are_equal ( a . _letter_id , b . _letter_id ) ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_prepare_permit msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_render_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_prepared msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_application_fsm . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_update msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_letter_big_tex_coords_reply msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_letter_big_tex_coords_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_letter_small_tex_coords_reply msg )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_letter_small_tex_coords_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_use_text_texture_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: logic_text_use_text_texture_reply msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}
