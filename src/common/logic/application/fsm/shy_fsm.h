class _shy_common_logic_application_fsm
{
public :
    static void reset_input_events ( ) ;
    static void recalc_current_inputs ( ) ;
    static void determine_inputs_change ( so_called_platform_math_num_whole_type & ) ;
    static void update_fixed_inputs ( ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_amusement_created_message ) ;
    static void receive ( so_called_common_logic_amusement_finished_message ) ;
    static void receive ( so_called_common_logic_application_render_message ) ;
    static void receive ( so_called_common_logic_application_update_message ) ;
    static void receive ( so_called_common_logic_fader_finished_message ) ;
    static void receive ( so_called_common_logic_font_mesh_generator_generate_finished_message ) ;
    static void receive ( so_called_common_logic_font_texture_generator_generate_finished_message ) ;
    static void receive ( so_called_common_logic_main_menu_created_message ) ;
    static void receive ( so_called_common_logic_main_menu_finished_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_cleaner_clean_finished_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_generator_generate_finished_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_cleaner_clean_finished_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_generator_generate_finished_message ) ;
    static void receive ( so_called_common_logic_salutation_timer_appear_finished_message ) ;
    static void receive ( so_called_common_logic_salutation_timer_disappear_finished_message ) ;
    static void receive ( so_called_common_logic_text_prepared_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > :: module shy_common_logic_application_fsm_scheduled ;
