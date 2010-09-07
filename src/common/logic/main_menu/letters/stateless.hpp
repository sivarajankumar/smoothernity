template < typename mediator >
class shy_logic_main_menu_letters_stateless
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
    class logic_main_menu_letters_messages
    {
    public :
        class logic_main_menu_letter_add { public : logic_text_letter_id letter ; } ;
        class logic_main_menu_letter_reply { public : num_whole row ; num_whole col ; logic_text_letter_id letter ; } ;
        class logic_main_menu_letter_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_cols_reply { public : num_whole row ; num_whole cols ; } ;
        class logic_main_menu_letters_cols_request { public : num_whole row ; } ;
        class logic_main_menu_letters_create { } ;
        class logic_main_menu_letters_create_finished { } ;
        class logic_main_menu_letters_layout_position_reply { public : num_whole row ; num_whole col ; vector_data position ; num_fract scale ; } ;
        class logic_main_menu_letters_layout_position_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_next_row { } ;
        class logic_main_menu_letters_rows_reply { public : num_whole rows ; } ;
        class logic_main_menu_letters_rows_request { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_letters_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letter_add ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letter_reply ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letter_request ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_cols_reply ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_cols_request ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_create ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_create_finished ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_layout_position_reply ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_layout_position_request ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_next_row ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_rows_reply ) ;
        void send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_rows_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_letters_stateless ( ) ;
private :
    shy_logic_main_menu_letters_stateless < mediator > & operator= ( const shy_logic_main_menu_letters_stateless < mediator > & ) ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_stateless < mediator > :: shy_logic_main_menu_letters_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letter_add msg )
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_layout_position_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_layout_position_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_create msg )
{
    _receivers . get ( ) . logic_main_menu_letters_creation_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_create_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_next_row msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_cols_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_cols_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letter_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letter_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_rows_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_stateless < mediator > 
:: logic_main_menu_letters_sender < receivers > 
:: send ( typename logic_main_menu_letters_messages :: logic_main_menu_letters_rows_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}
