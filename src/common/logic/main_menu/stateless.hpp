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
        num_fract letter_mesh_size ;
        static const_int_32 max_rows = 5 ;
        static const_int_32 max_cols = 16 ;
    } ;
    
    class logic_main_menu_messages
    {
    public :
        class logic_main_menu_creation_permit { } ;
        class logic_main_menu_finished { } ;
        class logic_main_menu_launch_permit { } ;
        class logic_main_menu_letter_add { public : logic_text_letter_id letter ; } ;
        class logic_main_menu_letter_reply { public : num_whole row ; num_whole col ; logic_text_letter_id letter ; } ;
        class logic_main_menu_letter_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_cols_reply { public : num_whole row ; num_whole cols ; } ;
        class logic_main_menu_letters_cols_request { public : num_whole row ; } ;
        class logic_main_menu_letters_create { } ;
        class logic_main_menu_letters_create_finished { } ;
        class logic_main_menu_letters_layout_position_reply { public : num_whole row ; num_whole col ; vector_data position ; num_fract scale ; } ;
        class logic_main_menu_letters_layout_position_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_mesh_create_next { } ;
        class logic_main_menu_letters_mesh_has_been_created { public : num_whole row ; num_whole col ; engine_render_mesh_id mesh ; } ;
        class logic_main_menu_letters_mesh_id_reply { public : num_whole index ; engine_render_mesh_id mesh ; } ;
        class logic_main_menu_letters_mesh_id_request { public : num_whole index ; } ;
        class logic_main_menu_letters_mesh_row_col_reply { public : num_whole index ; num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_mesh_row_col_request { public : num_whole index ; } ;
        class logic_main_menu_letters_meshes_count_reply { public : num_whole meshes ; } ;
        class logic_main_menu_letters_meshes_count_request { } ;
        class logic_main_menu_letters_meshes_create { } ;
        class logic_main_menu_letters_meshes_creation_finished { } ;
        class logic_main_menu_letters_meshes_destroy_reply { } ;
        class logic_main_menu_letters_meshes_destroy_request { } ;
        class logic_main_menu_letters_meshes_iterate_finished { } ;
        class logic_main_menu_letters_meshes_iterate_start { } ;
        class logic_main_menu_letters_meshes_iteration { public : num_whole row ; num_whole col ; engine_render_mesh_id mesh ; } ;
        class logic_main_menu_letters_meshes_place { } ;
        class logic_main_menu_letters_meshes_render_reply { } ;
        class logic_main_menu_letters_meshes_render_request { } ;
        class logic_main_menu_letters_next_row { } ;
        class logic_main_menu_letters_rows_reply { public : num_whole rows ; } ;
        class logic_main_menu_letters_rows_request { } ;
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
        void send ( typename logic_main_menu_messages :: logic_main_menu_letter_add ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letter_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letter_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_cols_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_cols_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_create ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_create_finished ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_layout_position_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_layout_position_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_create_next ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_has_been_created ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_id_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_id_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_row_col_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_row_col_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_count_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_count_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_create ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_creation_finished ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_destroy_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_destroy_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_iterate_finished ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_iterate_start ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_iteration ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_place ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_render_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_render_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_next_row ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_rows_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_letters_rows_request ) ;
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
    platform_math :: make_num_fract ( letter_mesh_size , 1 , 1 ) ;
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
:: send ( typename logic_main_menu_messages :: logic_main_menu_letter_add msg )
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
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
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_layout_position_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_layout_position_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
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
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_create msg )
{
    _receivers . get ( ) . logic_main_menu_letters_creation_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_create_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_next_row msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_create_next msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_id_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_id_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_row_col_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_row_col_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_count_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_count_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_create msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creation_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_creation_finished msg ) 
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_creation_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_destroy_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_destroy_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_destroyer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_iterate_finished msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_destroyer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_iterate_start msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_iteration msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_destroyer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_place msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_render_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_meshes_render_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator >
:: logic_main_menu_sender < receivers >
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_mesh_has_been_created msg )
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_cols_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_cols_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_creation_permit msg ) 
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letter_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letter_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_rows_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_letters_rows_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

