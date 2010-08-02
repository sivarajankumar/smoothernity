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
    class letter_id
    {
        friend class shy_logic_text < mediator > ;
        friend class shy_logic_text_stateless ;
        friend class shy_logic_text_stateless :: logic_text_stateless_consts_type ;
    private :
        num_whole _letter_id ;
    } ;

    class alphabet_english_type
    {
    public :
        letter_id A ;
        letter_id B ;
        letter_id C ;
        letter_id D ;
        letter_id E ;
        letter_id F ;
        letter_id G ;
        letter_id H ;
        letter_id I ;
        letter_id J ;
        letter_id K ;
        letter_id L ;
        letter_id M ;
        letter_id N ;
        letter_id O ;
        letter_id P ;
        letter_id Q ;
        letter_id R ;
        letter_id S ;
        letter_id T ;
        letter_id U ;
        letter_id V ;
        letter_id W ;
        letter_id X ;
        letter_id Y ;
        letter_id Z ;
    } ;
    
    class logic_text_stateless_consts_type
    {
    public :
        logic_text_stateless_consts_type ( ) ;
    public :
        letter_id whitespace ;
        alphabet_english_type alphabet_english ;
    } ;
    
    class logic_text_messages
    {
    public :
        class text_letter_big_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; letter_id letter ; } ;
        class text_letter_big_tex_coords_request { public : letter_id letter ; } ;
        class text_letter_small_tex_coords_reply { public : num_fract left ; num_fract bottom ; num_fract right ; num_fract top ; letter_id letter ; } ;
        class text_letter_small_tex_coords_request { public : letter_id letter ; } ;
        class text_prepare_permit { } ;
        class text_prepared { } ;
        class text_render_reply { } ;
        class text_render_request { } ;
        class text_update { } ;
        class use_text_texture_reply { } ;
        class use_text_texture_request { } ;
    } ;
    
    template < typename receivers >
    class logic_text_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_text_messages :: text_letter_big_tex_coords_reply ) ;
        void send ( typename logic_text_messages :: text_letter_big_tex_coords_request ) ;
        void send ( typename logic_text_messages :: text_letter_small_tex_coords_reply ) ;
        void send ( typename logic_text_messages :: text_letter_small_tex_coords_request ) ;
        void send ( typename logic_text_messages :: text_prepare_permit ) ;
        void send ( typename logic_text_messages :: text_prepared ) ;
        void send ( typename logic_text_messages :: text_render_reply ) ;
        void send ( typename logic_text_messages :: text_render_request ) ;
        void send ( typename logic_text_messages :: text_update ) ;
        void send ( typename logic_text_messages :: use_text_texture_reply ) ;
        void send ( typename logic_text_messages :: use_text_texture_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
    
public :
    shy_logic_text_stateless ( ) ;
    shy_logic_text_stateless & operator= ( const shy_logic_text_stateless & ) ;
    static void are_letters_equal ( num_whole & result , letter_id a , letter_id b ) ;
public :
    const logic_text_stateless_consts_type logic_text_stateless_consts ;
} ;

template < typename mediator >
shy_logic_text_stateless < mediator > :: shy_logic_text_stateless ( )
{
}

template < typename mediator >
shy_logic_text_stateless < mediator > &
shy_logic_text_stateless < mediator > :: operator= ( const shy_logic_text_stateless < mediator > & )
{
    return * this ;
}

template < typename mediator >
shy_logic_text_stateless < mediator > :: logic_text_stateless_consts_type :: logic_text_stateless_consts_type ( )
{
    num_whole index ;
    typename platform_pointer :: template pointer < alphabet_english_type > eng = alphabet_english ;
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
void shy_logic_text_stateless < mediator > :: are_letters_equal ( num_whole & result , letter_id a , letter_id b )
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
:: send ( typename logic_text_messages :: text_prepare_permit msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_render_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_prepared msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_update msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_letter_big_tex_coords_reply msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_letter_big_tex_coords_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_letter_small_tex_coords_reply msg )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: text_letter_small_tex_coords_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: use_text_texture_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_text_stateless < mediator > 
:: logic_text_sender < receivers > 
:: send ( typename logic_text_messages :: use_text_texture_reply msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}
