template < typename mediator >
class shy_logic_main_menu_letters_animation_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

public :
    class logic_main_menu_letters_animation_stateless_consts_type
    {
    public :
        logic_main_menu_letters_animation_stateless_consts_type ( ) ;
    public :
        num_fract appear_time_from_begin_to_middle_in_seconds ;
        num_fract appear_time_from_middle_to_end_in_seconds ;
        num_fract appear_delay_per_col_in_seconds ;
        num_fract appear_delay_per_row_in_seconds ;
        num_fract appear_scale_begin ;
        num_fract appear_scale_middle ;
        num_fract appear_scale_end ;
        num_fract disappear_animation_time_in_seconds ; 
        num_fract disappear_time_from_begin_to_end_in_seconds ;
        num_fract disappear_delay_per_row_in_seconds ;
        num_fract disappear_delay_per_col_in_seconds ;
        num_fract disappear_scale_begin ;
        num_fract disappear_scale_end ;
        num_fract idle_vertical_shift_period_in_seconds ;
        num_fract idle_vertical_shift_phase_per_col ;
        num_fract idle_vertical_shift_phase_per_row ;
        num_fract idle_vertical_shift_amplitude ;
        num_fract idle_horizontal_shift_period_in_seconds ;
        num_fract idle_horizontal_shift_phase_per_row ;
        num_fract idle_horizontal_shift_amplitude ;
    } ;

    class logic_main_menu_letters_animation_messages
    {
    public :
        class logic_main_menu_letters_animation_appear_transform_reply { public : num_whole row ; num_whole col ; num_fract scale ; } ;
        class logic_main_menu_letters_animation_appear_transform_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_disappear_finished { } ;
        class logic_main_menu_letters_animation_disappear_start { } ;
        class logic_main_menu_letters_animation_disappear_transform_reply { public : num_whole row ; num_whole col ; num_fract scale ; } ;
        class logic_main_menu_letters_animation_disappear_transform_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_idle_transform_reply { public : num_whole row ; num_whole col ; vector_data position ; num_fract scale ; } ;
        class logic_main_menu_letters_animation_idle_transform_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_selection_push_transform_reply { public : num_whole row ; num_whole col ; num_fract scale ; } ;
        class logic_main_menu_letters_animation_selection_push_transform_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_selection_transform_reply { public : num_whole row ; num_whole col ; num_fract scale ; } ;
        class logic_main_menu_letters_animation_selection_transform_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_selection_weight_reply { public : num_whole row ; num_whole col ; num_fract weight ; } ;
        class logic_main_menu_letters_animation_selection_weight_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_selection_weight_select_row { public : num_whole row ; } ;
        class logic_main_menu_letters_animation_selection_weight_unselect_row { public : num_whole row ; } ;
        class logic_main_menu_letters_animation_unselection_weight_reply { public : num_whole row ; num_whole col ; num_fract weight ; } ;
        class logic_main_menu_letters_animation_unselection_weight_request { public : num_whole row ; num_whole col ; } ;
        class logic_main_menu_letters_animation_unselection_weight_select_row { public : num_whole row ; } ;
        class logic_main_menu_letters_animation_unselection_weight_unselect_row { public : num_whole row ; } ;
        class logic_main_menu_letters_animation_transform_reply { public : num_whole row ; num_whole col ; matrix_data transform ; } ;
        class logic_main_menu_letters_animation_transform_request { public : num_whole row ; num_whole col ; } ;
    } ;

    template < typename receivers >
    class logic_main_menu_letters_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_appear_transform_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_appear_transform_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_finished ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_start ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_transform_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_transform_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_idle_transform_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_idle_transform_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_push_transform_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_push_transform_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_transform_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_transform_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_select_row ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_unselect_row ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_request ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_select_row ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_unselect_row ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_transform_reply ) ;
        void send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_letters_animation_stateless ( ) ;
private :
    shy_logic_main_menu_letters_animation_stateless < mediator > & operator= ( const shy_logic_main_menu_letters_animation_stateless < mediator > & ) ;

public :
    const logic_main_menu_letters_animation_stateless_consts_type logic_main_menu_letters_animation_stateless_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_animation_stateless < mediator > :: logic_main_menu_letters_animation_stateless_consts_type :: logic_main_menu_letters_animation_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( appear_time_from_begin_to_middle_in_seconds , 1 , 10 ) ;
    platform_math :: make_num_fract ( appear_time_from_middle_to_end_in_seconds , 7 , 10 ) ;
    platform_math :: make_num_fract ( appear_delay_per_col_in_seconds , 2 , 100 ) ;
    platform_math :: make_num_fract ( appear_delay_per_row_in_seconds , 5 , 100 ) ;
    platform_math :: make_num_fract ( appear_scale_begin , 0 , 1 ) ;
    platform_math :: make_num_fract ( appear_scale_middle , 3 , 2 ) ;
    platform_math :: make_num_fract ( appear_scale_end , 1 , 1 ) ;
    platform_math :: make_num_fract ( disappear_animation_time_in_seconds , 8 , 10 ) ;
    platform_math :: make_num_fract ( disappear_time_from_begin_to_end_in_seconds , 3 , 10 ) ;
    platform_math :: make_num_fract ( disappear_delay_per_col_in_seconds , 2 , 100 ) ;
    platform_math :: make_num_fract ( disappear_delay_per_row_in_seconds , 5 , 100 ) ;
    platform_math :: make_num_fract ( disappear_scale_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( disappear_scale_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( idle_vertical_shift_period_in_seconds , 1 , 1 ) ;
    platform_math :: make_num_fract ( idle_vertical_shift_phase_per_col , 1 , 3 ) ;
    platform_math :: make_num_fract ( idle_vertical_shift_phase_per_row , 1 , 5 ) ;
    platform_math :: make_num_fract ( idle_vertical_shift_amplitude , 1 , 30 ) ;
    platform_math :: make_num_fract ( idle_horizontal_shift_period_in_seconds , 2 , 1 ) ;
    platform_math :: make_num_fract ( idle_horizontal_shift_phase_per_row , 1 , 2 ) ;
    platform_math :: make_num_fract ( idle_horizontal_shift_amplitude , 1 , 20 ) ;
}

template < typename mediator >
shy_logic_main_menu_letters_animation_stateless < mediator > :: shy_logic_main_menu_letters_animation_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_appear_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_appear_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_appear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_start msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_disappear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_disappear_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_disappear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_idle_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_idle_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_push_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_push_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_push . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_selection . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_weight . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_select_row msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_weight . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_selection_weight_unselect_row msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_weight . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_unselection_weight . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_select_row msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_unselection_weight . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_unselection_weight_unselect_row msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation_unselection_weight . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_letters_meshes_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_letters_animation_stateless < mediator > 
:: logic_main_menu_letters_animation_sender < receivers > 
:: send ( typename logic_main_menu_letters_animation_messages :: logic_main_menu_letters_animation_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
}
