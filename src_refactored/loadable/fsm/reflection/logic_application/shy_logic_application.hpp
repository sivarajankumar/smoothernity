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
    shy_guts_bind_action ( logic_salutation_creation_permit ) ;
    shy_guts_bind_action ( logic_salutation_launch_permit ) ;
    shy_guts_bind_action ( logic_salutation_render ) ;
    shy_guts_bind_action ( logic_salutation_update ) ;
    shy_guts_bind_action ( logic_text_prepare_permit ) ;
    shy_guts_bind_action ( logic_text_update ) ;
    shy_guts_bind_action ( logic_title_launch_permit ) ;
    shy_guts_bind_action ( logic_title_render ) ;
    shy_guts_bind_action ( logic_title_update ) ;

    shy_guts_bind_input ( logic_amusement_created ) ;
    shy_guts_bind_input ( logic_amusement_finished ) ;
    shy_guts_bind_input ( logic_application_render ) ;
    shy_guts_bind_input ( logic_application_update ) ;
    shy_guts_bind_input ( logic_text_prepared ) ;
    shy_guts_bind_input ( logic_title_created ) ;
    shy_guts_bind_input ( logic_title_finished ) ;
    shy_guts_bind_input ( logic_main_menu_created ) ;
    shy_guts_bind_input ( logic_main_menu_finished ) ;
    shy_guts_bind_input ( logic_salutation_created ) ;
    shy_guts_bind_input ( logic_salutation_finished ) ;
    shy_guts_bind_input ( logic_salutation_letters_meshes_generate_finished ) ;
    shy_guts_bind_input ( stage_amusement_disabled ) ;
    shy_guts_bind_input ( stage_amusement_enabled ) ;
    shy_guts_bind_input ( stage_main_menu_disabled ) ;
    shy_guts_bind_input ( stage_main_menu_enabled ) ;
    shy_guts_bind_input ( stage_salutation_disabled ) ;
    shy_guts_bind_input ( stage_salutation_enabled ) ;
    shy_guts_bind_input ( stage_title_disabled ) ;
    shy_guts_bind_input ( stage_title_enabled ) ;
}
