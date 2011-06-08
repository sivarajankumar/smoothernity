class _shy_common_logic_application_fsm
{
public :
    static void reset_input_events ( ) ;
    static void recalc_current_inputs ( ) ;
    static void determine_inputs_change ( so_called_type_platform_math_num_whole & ) ;
    static void update_fixed_inputs ( ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_amusement_created ) ;
    static void receive ( so_called_message_common_logic_amusement_finished ) ;
    static void receive ( so_called_message_common_logic_application_render ) ;
    static void receive ( so_called_message_common_logic_application_update ) ;
    static void receive ( so_called_message_common_logic_main_menu_created ) ;
    static void receive ( so_called_message_common_logic_main_menu_finished ) ;
    static void receive ( so_called_message_common_logic_salutation_created ) ;
    static void receive ( so_called_message_common_logic_salutation_finished ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_generator_generate_finished ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_text_generator_generate_finished ) ;
    static void receive ( so_called_message_common_logic_salutation_timer_disappear_run_finished ) ;
    static void receive ( so_called_message_common_logic_text_prepared ) ;
    static void receive ( so_called_message_common_logic_title_created ) ;
    static void receive ( so_called_message_common_logic_title_finished ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > :: module shy_common_logic_application_fsm_scheduled ;
