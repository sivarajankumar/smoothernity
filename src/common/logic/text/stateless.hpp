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
    
public :
    class letter_id
    {
        friend class shy_logic_text < mediator > ;
        friend class shy_logic_text_stateless ;
        friend class shy_logic_text_stateless :: alphabet_english_type ;
    private :
        num_whole _letter_id ;
    } ;

    class alphabet_english_type
    {
    public :
        alphabet_english_type ( ) ;
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
    } ;
    
public :
    shy_logic_text_stateless ( ) ;
    shy_logic_text_stateless & operator= ( const shy_logic_text_stateless & src ) ;
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
shy_logic_text_stateless < mediator > :: operator= ( const shy_logic_text_stateless < mediator > & src )
{
    return * this ;
}

template < typename mediator >
shy_logic_text_stateless < mediator > :: alphabet_english_type :: alphabet_english_type ( )
{
    num_whole index ;
    platform_math :: make_num_whole ( index , 0 ) ;
    A . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    B . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    C . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    D . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    E . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    F . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    G . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    H . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    I . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    J . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    K . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    L . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    M . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    N . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    O . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    P . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    Q . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    R . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    S . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    T . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    U . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    V . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    W . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    X . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    Y . _letter_id = index ; platform_math :: inc_whole ( index ) ;
    Z . _letter_id = index ; platform_math :: inc_whole ( index ) ;
}

template < typename mediator >
void shy_logic_text_stateless < mediator > :: are_letters_equal ( num_whole & result , letter_id a , letter_id b )
{
    platform_math :: make_num_whole ( result , platform_conditions :: wholes_are_equal ( a . _letter_id , b . _letter_id ) ) ;
}
