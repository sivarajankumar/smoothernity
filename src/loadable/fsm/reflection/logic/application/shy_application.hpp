#define shy_guts_bind_action(action) so_called_loadable_fsm_binder_helper_action ( logic_application , action )
#define shy_guts_bind_input(input) so_called_loadable_fsm_binder_helper_input ( logic_application , input )
#define shy_guts_bind_system(system) so_called_loadable_fsm_binder_helper_system ( system )

void shy_loadable_fsm_reflection_logic_application :: prepare ( )
{
    shy_guts_bind_system ( logic_application ) ;

    shy_guts_bind_action ( logic_amusement_creation_permit ) ;
    shy_guts_bind_action ( logic_amusement_launch_permit ) ;
    shy_guts_bind_action ( logic_amusement_render ) ;
    shy_guts_bind_action ( logic_amusement_update ) ;
    shy_guts_bind_action ( logic_game_launch_permit ) ;
    shy_guts_bind_action ( logic_game_render ) ;
    shy_guts_bind_action ( logic_game_update ) ;
    shy_guts_bind_action ( logic_main_menu_creation_permit ) ;
    shy_guts_bind_action ( logic_main_menu_launch_permit ) ;
    shy_guts_bind_action ( logic_main_menu_render ) ;
    shy_guts_bind_action ( logic_main_menu_update ) ;
    shy_guts_bind_action ( logic_salutation_animation_zoom_rewind ) ;
    shy_guts_bind_action ( logic_salutation_animation_zoom_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_appear_rewind ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_appear_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_disappear_rewind ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_disappear_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_roll_in_rewind ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_roll_in_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_roll_out_rewind ) ;
    shy_guts_bind_action ( logic_salutation_letters_animation_roll_out_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_meshes_cleaner_clean ) ;
    shy_guts_bind_action ( logic_salutation_letters_meshes_cleaner_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_meshes_generator_generate ) ;
    shy_guts_bind_action ( logic_salutation_letters_meshes_generator_update ) ;
    shy_guts_bind_action ( logic_salutation_letters_text_cleaner_clean ) ;
    shy_guts_bind_action ( logic_salutation_letters_text_generator_generate ) ;
    shy_guts_bind_action ( logic_salutation_renderer_render ) ;
    shy_guts_bind_action ( logic_salutation_timer_appear_run ) ;
    shy_guts_bind_action ( logic_salutation_timer_appear_update ) ;
    shy_guts_bind_action ( logic_salutation_timer_disappear_run ) ;
    shy_guts_bind_action ( logic_salutation_timer_disappear_update ) ;
    shy_guts_bind_action ( logic_text_prepare_permit ) ;
    shy_guts_bind_action ( logic_text_update ) ;
    shy_guts_bind_action ( logic_title_launch_permit ) ;
    shy_guts_bind_action ( logic_title_render ) ;
    shy_guts_bind_action ( logic_title_update ) ;
    shy_guts_bind_action ( logic_vacuum_render ) ;
    shy_guts_bind_action ( logic_vacuum_update ) ;

    shy_guts_bind_input ( logic_amusement_created ) ;
    shy_guts_bind_input ( logic_amusement_finished ) ;
    shy_guts_bind_input ( logic_application_render ) ;
    shy_guts_bind_input ( logic_application_update ) ;
    shy_guts_bind_input ( logic_text_prepared ) ;
    shy_guts_bind_input ( logic_title_created ) ;
    shy_guts_bind_input ( logic_title_finished ) ;
    shy_guts_bind_input ( logic_main_menu_created ) ;
    shy_guts_bind_input ( logic_main_menu_finished ) ;
    shy_guts_bind_input ( logic_salutation_letters_meshes_cleaner_clean_finished ) ;
    shy_guts_bind_input ( logic_salutation_letters_meshes_generator_generate_finished ) ;
    shy_guts_bind_input ( logic_salutation_letters_text_cleaner_clean_finished ) ;
    shy_guts_bind_input ( logic_salutation_letters_text_generator_generate_finished ) ;
    shy_guts_bind_input ( logic_salutation_timer_appear_run_finished ) ;
    shy_guts_bind_input ( logic_salutation_timer_disappear_run_finished ) ;
    shy_guts_bind_input ( stage_amusement_disabled ) ;
    shy_guts_bind_input ( stage_amusement_enabled ) ;
    shy_guts_bind_input ( stage_main_menu_disabled ) ;
    shy_guts_bind_input ( stage_main_menu_enabled ) ;
    shy_guts_bind_input ( stage_salutation_disabled ) ;
    shy_guts_bind_input ( stage_salutation_enabled ) ;
    shy_guts_bind_input ( stage_title_disabled ) ;
    shy_guts_bind_input ( stage_title_enabled ) ;
}
