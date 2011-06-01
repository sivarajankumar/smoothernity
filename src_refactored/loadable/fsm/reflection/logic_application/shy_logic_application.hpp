#define shy_bind_system_helper(system) \
    so_called_loadable_fsm_binder :: bind_system \
        ( #system \
        , & so_called_common_##system##_fsm_binding \
        )

#define shy_bind_action_helper(action) \
    so_called_loadable_fsm_binder :: bind_action \
        ( #action \
        , & so_called_common_logic_application_fsm_actions :: action \
        )

#define shy_bind_input_helper(input) \
    so_called_loadable_fsm_binder :: bind_input \
        ( #input \
        , reinterpret_cast < so_called_type_loadable_fsm_content_input_binding > ( & so_called_type_common_logic_application_fsm_inputs :: input ) \
        )

void shy_loadable_fsm_reflection_logic_application :: prepare ( )
{
    shy_bind_system_helper ( logic_application ) ;

    shy_bind_action_helper ( logic_amusement_creation_permit ) ;
    shy_bind_action_helper ( logic_amusement_launch_permit ) ;
    shy_bind_action_helper ( logic_amusement_render ) ;
    shy_bind_action_helper ( logic_amusement_update ) ;
    shy_bind_action_helper ( logic_game_launch_permit ) ;
    shy_bind_action_helper ( logic_game_render ) ;
    shy_bind_action_helper ( logic_game_update ) ;
    shy_bind_action_helper ( logic_main_menu_creation_permit ) ;
    shy_bind_action_helper ( logic_main_menu_launch_permit ) ;
    shy_bind_action_helper ( logic_main_menu_render ) ;
    shy_bind_action_helper ( logic_main_menu_update ) ;
    shy_bind_action_helper ( logic_salutation_update ) ;
    shy_bind_action_helper ( logic_text_prepare_permit ) ;
    shy_bind_action_helper ( logic_text_update ) ;
    shy_bind_action_helper ( logic_title_launch_permit ) ;
    shy_bind_action_helper ( logic_title_render ) ;
    shy_bind_action_helper ( logic_title_update ) ;

    shy_bind_input_helper ( logic_amusement_created ) ;
    shy_bind_input_helper ( logic_amusement_finished ) ;
    shy_bind_input_helper ( logic_application_render ) ;
    shy_bind_input_helper ( logic_application_update ) ;
    shy_bind_input_helper ( logic_text_prepared ) ;
    shy_bind_input_helper ( logic_title_created ) ;
    shy_bind_input_helper ( logic_title_finished ) ;
    shy_bind_input_helper ( logic_main_menu_created ) ;
    shy_bind_input_helper ( logic_main_menu_finished ) ;
    shy_bind_input_helper ( logic_salutation_finished ) ;
    shy_bind_input_helper ( stage_amusement_disabled ) ;
    shy_bind_input_helper ( stage_amusement_enabled ) ;
    shy_bind_input_helper ( stage_main_menu_disabled ) ;
    shy_bind_input_helper ( stage_main_menu_enabled ) ;
    shy_bind_input_helper ( stage_title_disabled ) ;
    shy_bind_input_helper ( stage_title_enabled ) ;
}

#undef shy_bind_system_helper
#undef shy_bind_action_helper
#undef shy_bind_input_helper

