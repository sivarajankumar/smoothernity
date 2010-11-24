template < typename mediator >
class shy_logic_main_menu_selection_animation_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

public :
    class logic_main_menu_selection_animation_stateless_consts_type
    {
    public :
        logic_main_menu_selection_animation_stateless_consts_type ( ) ;
    public :
        num_fract appear_horizontal_scale_time_to_begin ;
        num_fract appear_horizontal_scale_time_from_begin_to_end ;
        num_fract appear_horizontal_scale_value_begin ;
        num_fract appear_horizontal_scale_value_end ;
        num_fract appear_vertical_scale_time_to_begin ;
        num_fract appear_vertical_scale_time_from_begin_to_middle ;
        num_fract appear_vertical_scale_time_from_middle_to_end ;
        num_fract appear_vertical_scale_value_begin ;
        num_fract appear_vertical_scale_value_middle ;
        num_fract appear_vertical_scale_value_end ;
        num_fract appear_total_animation_time ;
        num_fract disappear_horizontal_scale_time_to_begin ;
        num_fract disappear_horizontal_scale_time_from_begin_to_end ;
        num_fract disappear_horizontal_scale_value_begin ;
        num_fract disappear_horizontal_scale_value_end ;
        num_fract disappear_vertical_scale_time_to_begin ;
        num_fract disappear_vertical_scale_time_from_begin_to_end ;
        num_fract disappear_vertical_scale_value_begin ;
        num_fract disappear_vertical_scale_value_end ;
        num_fract idle_position_z ;
        num_fract idle_attention_horizontal_scale_min ;
        num_fract idle_attention_horizontal_scale_max ;
        num_fract idle_attention_horizontal_scale_period_in_seconds ;
        num_fract idle_attention_vertical_scale_min ;
        num_fract idle_attention_vertical_scale_max ;
        num_fract idle_attention_vertical_scale_period_in_seconds ;
        num_fract push_time_from_begin_to_middle ;
        num_fract push_time_from_middle_to_end ;
        num_fract push_horizontal_scale_begin ;
        num_fract push_horizontal_scale_middle ;
        num_fract push_horizontal_scale_end ;
        num_fract push_vertical_scale_begin ;
        num_fract push_vertical_scale_middle ;
        num_fract push_vertical_scale_end ;
        num_fract push_attention_horizontal_scale_min ;
        num_fract push_attention_horizontal_scale_max ;
        num_fract push_attention_vertical_scale_min ;
        num_fract push_attention_vertical_scale_max ;
        num_fract push_attention_period_in_seconds ;
    } ;

    class logic_main_menu_selection_animation_messages
    {
    public :
        class logic_main_menu_selection_animation_appear_finished { } ;
        class logic_main_menu_selection_animation_appear_start { } ;
        class logic_main_menu_selection_animation_appear_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_appear_transform_request { } ;
        class logic_main_menu_selection_animation_disappear_start { } ;
        class logic_main_menu_selection_animation_disappear_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_disappear_transform_request { } ;
        class logic_main_menu_selection_animation_idle_attention_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_idle_attention_transform_request { } ;
        class logic_main_menu_selection_animation_idle_row_selected { public : num_whole row ; } ;
        class logic_main_menu_selection_animation_idle_transform_reply { public : vector_data position ; num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_idle_transform_request { } ;
        class logic_main_menu_selection_animation_idle_void_selected { } ;
        class logic_main_menu_selection_animation_push_attention_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_push_attention_transform_request { } ;
        class logic_main_menu_selection_animation_push_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_push_transform_request { } ;
        class logic_main_menu_selection_animation_push_weight_reply { public : num_fract weight ; } ;
        class logic_main_menu_selection_animation_push_weight_request { } ;
        class logic_main_menu_selection_animation_select_finished { } ;
        class logic_main_menu_selection_animation_select_start { } ;
        class logic_main_menu_selection_animation_select_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_select_transform_request { } ;
        class logic_main_menu_selection_animation_transform_reply { public : matrix_data transform ; } ;
        class logic_main_menu_selection_animation_transform_request { } ;
        class logic_main_menu_selection_animation_unselect_finished { } ;
        class logic_main_menu_selection_animation_unselect_start { } ;
        class logic_main_menu_selection_animation_unselect_transform_reply { public : num_fract scale_x ; num_fract scale_y ; } ;
        class logic_main_menu_selection_animation_unselect_transform_request { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_selection_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_finished ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_start ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_start ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_disappear_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_attention_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_attention_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_row_selected ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_void_selected ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_attention_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_attention_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_weight_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_weight_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_finished ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_start ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_transform_request ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_finished ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_start ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_transform_reply ) ;
        void send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    const logic_main_menu_selection_animation_stateless_consts_type logic_main_menu_selection_animation_stateless_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_stateless < mediator > :: logic_main_menu_selection_animation_stateless_consts_type :: logic_main_menu_selection_animation_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( appear_horizontal_scale_time_to_begin , 0 , 10 ) ;
    platform_math :: make_num_fract ( appear_horizontal_scale_time_from_begin_to_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( appear_horizontal_scale_value_begin , 8 , 10 ) ;
    platform_math :: make_num_fract ( appear_horizontal_scale_value_end , 1 , 1 ) ;
    platform_math :: make_num_fract ( appear_vertical_scale_time_to_begin , 2 , 10 ) ;
    platform_math :: make_num_fract ( appear_vertical_scale_time_from_begin_to_middle , 1 , 10 ) ;
    platform_math :: make_num_fract ( appear_vertical_scale_time_from_middle_to_end , 2 , 10 ) ;
    platform_math :: make_num_fract ( appear_vertical_scale_value_begin , 10 , 100 ) ;
    platform_math :: make_num_fract ( appear_vertical_scale_value_middle , 2 , 1 ) ;
    platform_math :: make_num_fract ( appear_vertical_scale_value_end , 1 , 1 ) ;
    platform_math :: make_num_fract ( appear_total_animation_time , 5 , 10 ) ;
    platform_math :: make_num_fract ( disappear_horizontal_scale_time_to_begin , 4 , 10 ) ;
    platform_math :: make_num_fract ( disappear_horizontal_scale_time_from_begin_to_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( disappear_horizontal_scale_value_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( disappear_horizontal_scale_value_end , 0 , 1 ) ;
    platform_math :: make_num_fract ( disappear_vertical_scale_time_to_begin , 0 , 10 ) ;
    platform_math :: make_num_fract ( disappear_vertical_scale_time_from_begin_to_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( disappear_vertical_scale_value_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( disappear_vertical_scale_value_end , 10 , 100 ) ;
    platform_math :: make_num_fract ( idle_position_z , - 3 , 1 ) ;
    platform_math :: make_num_fract ( idle_attention_horizontal_scale_min , 19 , 20 ) ;
    platform_math :: make_num_fract ( idle_attention_horizontal_scale_max , 20 , 20 ) ;
    platform_math :: make_num_fract ( idle_attention_horizontal_scale_period_in_seconds , 2 , 1 ) ;
    platform_math :: make_num_fract ( idle_attention_vertical_scale_min , 20 , 10 ) ;
    platform_math :: make_num_fract ( idle_attention_vertical_scale_max , 23 , 10 ) ;
    platform_math :: make_num_fract ( idle_attention_vertical_scale_period_in_seconds , 1 , 1 ) ;
    platform_math :: make_num_fract ( push_time_from_begin_to_middle , 10 , 100 ) ;
    platform_math :: make_num_fract ( push_time_from_middle_to_end , 20 , 100 ) ;
    platform_math :: make_num_fract ( push_horizontal_scale_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( push_horizontal_scale_middle , 90 , 100 ) ;
    platform_math :: make_num_fract ( push_horizontal_scale_end , 95 , 100 ) ;
    platform_math :: make_num_fract ( push_vertical_scale_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( push_vertical_scale_middle , 70 , 100 ) ;
    platform_math :: make_num_fract ( push_vertical_scale_end , 95 , 100 ) ;
    platform_math :: make_num_fract ( push_attention_horizontal_scale_min , 185 , 200 ) ;
    platform_math :: make_num_fract ( push_attention_horizontal_scale_max , 200 , 200 ) ;
    platform_math :: make_num_fract ( push_attention_vertical_scale_min , 200 , 100 ) ;
    platform_math :: make_num_fract ( push_attention_vertical_scale_max , 250 , 100 ) ;
    platform_math :: make_num_fract ( push_attention_period_in_seconds , 4 , 10 ) ;
}

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
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_finished msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_appear_start msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_appear . get ( ) . receive ( msg ) ;
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
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_attention_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_attention_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_idle_attention . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_row_selected msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_idle . get ( ) . receive ( msg ) ;
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
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_idle_void_selected msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_idle . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_attention_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_attention_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_push_attention . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_push . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_weight_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_push_weight_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_push_weight . get ( ) . receive ( msg ) ;
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

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_finished msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_start msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_select . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_select_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_select . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_finished msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_start msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_unselect . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_transform_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_animation_stateless < mediator > 
:: logic_main_menu_selection_animation_sender < receivers > 
:: send ( typename logic_main_menu_selection_animation_messages :: logic_main_menu_selection_animation_unselect_transform_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_animation_unselect . get ( ) . receive ( msg ) ;
}

