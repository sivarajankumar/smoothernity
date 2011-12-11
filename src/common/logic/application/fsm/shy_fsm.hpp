namespace shy_guts
{
    static void make_inputs_from_value
        ( so_called_platform_math_num_whole_type & enabled
        , so_called_platform_math_num_whole_type & disabled
        , so_called_platform_math_num_whole_type value
        ) ;
    static void run_fsm ( ) ;
    static void run_fsm_event ( so_called_platform_math_num_whole_type so_called_common_logic_application_fsm_inputs_type :: * ) ;

    static so_called_platform_math_num_whole_type stabilized ;
    static so_called_common_logic_application_fsm_inputs_type inputs_current ;
    static so_called_common_logic_application_fsm_inputs_type inputs_fixed ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: make_inputs_from_value
    ( so_called_platform_math_num_whole_type & enabled
    , so_called_platform_math_num_whole_type & disabled
    , so_called_platform_math_num_whole_type value
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( value ) )
    {
        enabled = so_called_platform_math_consts :: whole_true ;
        disabled = so_called_platform_math_consts :: whole_false ;
    }
    else
    {
        enabled = so_called_platform_math_consts :: whole_false ;
        disabled = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: run_fsm_event ( so_called_platform_math_num_whole_type so_called_common_logic_application_fsm_inputs_type :: * input )
{
    if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: stabilized ) )
    {
        shy_guts :: stabilized = so_called_platform_math_consts :: whole_true ;
        shy_guts :: run_fsm ( ) ;
    }
    shy_guts :: inputs_current .* input = so_called_platform_math_consts :: whole_true ;
    shy_guts :: run_fsm ( ) ;
}

void shy_guts :: run_fsm ( )
{
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: reset_input_events ( )
{
    shy_guts :: inputs_current . logic_amusement_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_amusement_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_application_render = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_application_update = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_fader_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_font_mesh_generator_generate_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_font_texture_generator_generate_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_main_menu_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_main_menu_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_meshes_cleaner_clean_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_meshes_generator_generate_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_text_cleaner_clean_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_text_generator_generate_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_timer_appear_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_timer_disappear_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_text_prepared = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_amusement_disabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_amusement_enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_fader_disabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_fader_enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_main_menu_disabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_main_menu_enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_salutation_disabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . stage_salutation_enabled = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_application_fsm :: recalc_current_inputs ( )
{
    shy_guts :: make_inputs_from_value 
        ( shy_guts :: inputs_current . stage_amusement_disabled
        , shy_guts :: inputs_current . stage_amusement_enabled
        , so_called_common_logic_application_consts :: skip_amusement 
        ) ;
    shy_guts :: make_inputs_from_value 
        ( shy_guts :: inputs_current . stage_fader_disabled
        , shy_guts :: inputs_current . stage_fader_enabled
        , so_called_common_logic_application_consts :: skip_fader 
        ) ;
    shy_guts :: make_inputs_from_value 
        ( shy_guts :: inputs_current . stage_main_menu_disabled
        , shy_guts :: inputs_current . stage_main_menu_enabled
        , so_called_common_logic_application_consts :: skip_main_menu 
        ) ;
    shy_guts :: make_inputs_from_value 
        ( shy_guts :: inputs_current . stage_salutation_disabled
        , shy_guts :: inputs_current . stage_salutation_enabled
        , so_called_common_logic_application_consts :: skip_salutation 
        ) ;
}

void _shy_common_logic_application_fsm :: determine_inputs_change ( so_called_platform_math_num_whole_type & inputs_changed )
{
    if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_amusement_created , shy_guts :: inputs_fixed . logic_amusement_created ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_amusement_finished , shy_guts :: inputs_fixed . logic_amusement_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_application_render , shy_guts :: inputs_fixed . logic_application_render ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_application_update , shy_guts :: inputs_fixed . logic_application_update ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_fader_finished , shy_guts :: inputs_fixed . logic_fader_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_font_mesh_generator_generate_finished , shy_guts :: inputs_fixed . logic_font_mesh_generator_generate_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_font_texture_generator_generate_finished , shy_guts :: inputs_fixed . logic_font_texture_generator_generate_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_main_menu_created , shy_guts :: inputs_fixed . logic_main_menu_created ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_main_menu_finished , shy_guts :: inputs_fixed . logic_main_menu_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_salutation_letters_meshes_cleaner_clean_finished , shy_guts :: inputs_fixed . logic_salutation_letters_meshes_cleaner_clean_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_salutation_letters_meshes_generator_generate_finished , shy_guts :: inputs_fixed . logic_salutation_letters_meshes_generator_generate_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_salutation_letters_text_cleaner_clean_finished , shy_guts :: inputs_fixed . logic_salutation_letters_text_cleaner_clean_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_salutation_letters_text_generator_generate_finished , shy_guts :: inputs_fixed . logic_salutation_letters_text_generator_generate_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_salutation_timer_appear_finished , shy_guts :: inputs_fixed . logic_salutation_timer_appear_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_salutation_timer_disappear_finished , shy_guts :: inputs_fixed . logic_salutation_timer_disappear_finished ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . logic_text_prepared , shy_guts :: inputs_fixed . logic_text_prepared ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_amusement_disabled , shy_guts :: inputs_fixed . stage_amusement_disabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_amusement_enabled , shy_guts :: inputs_fixed . stage_amusement_enabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_fader_disabled , shy_guts :: inputs_fixed . stage_fader_disabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_fader_enabled , shy_guts :: inputs_fixed . stage_fader_enabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_main_menu_disabled , shy_guts :: inputs_fixed . stage_main_menu_disabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_main_menu_enabled , shy_guts :: inputs_fixed . stage_main_menu_enabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_salutation_disabled , shy_guts :: inputs_fixed . stage_salutation_disabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else if ( ! so_called_platform_conditions :: wholes_are_equal ( shy_guts :: inputs_current . stage_salutation_enabled , shy_guts :: inputs_fixed . stage_salutation_enabled ) )
        inputs_changed = so_called_platform_math_consts :: whole_true ;
    else
        inputs_changed = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_application_fsm :: update_fixed_inputs ( )
{
    shy_guts :: inputs_fixed = shy_guts :: inputs_current ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_init_message )
{
    reset_input_events ( ) ;
    update_fixed_inputs ( ) ;

    shy_guts :: stabilized = so_called_platform_math_consts :: whole_false ;

    so_called_platform_pointer_data_type < so_called_common_logic_application_fsm_inputs_type > inputs_current ;
    so_called_platform_pointer_data_type < so_called_common_logic_application_fsm_inputs_type > inputs_fixed ;

    so_called_platform_pointer :: bind ( inputs_current , shy_guts :: inputs_current ) ;
    so_called_platform_pointer :: bind ( inputs_fixed , shy_guts :: inputs_fixed ) ;

    so_called_common_logic_application_fsm_behaviour :: set_inputs ( inputs_current , inputs_fixed ) ;
    so_called_common_logic_application_fsm_behaviour :: init ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_amusement_created_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_amusement_created ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_amusement_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_amusement_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_application_render_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_application_render ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_application_update_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_application_update ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_fader_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_fader_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_font_mesh_generator_generate_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_font_mesh_generator_generate_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_font_texture_generator_generate_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_font_texture_generator_generate_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_main_menu_created_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_main_menu_created ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_main_menu_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_main_menu_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_salutation_letters_meshes_cleaner_clean_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_salutation_letters_meshes_cleaner_clean_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_salutation_letters_meshes_generator_generate_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_salutation_letters_meshes_generator_generate_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_salutation_letters_text_cleaner_clean_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_salutation_letters_text_cleaner_clean_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_salutation_letters_text_generator_generate_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_salutation_letters_text_generator_generate_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_salutation_timer_appear_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_salutation_timer_appear_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_salutation_timer_disappear_finished_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_salutation_timer_disappear_finished ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_common_logic_text_prepared_message )
{
    shy_guts :: run_fsm_event ( & so_called_common_logic_application_fsm_inputs_type :: logic_text_prepared ) ;
}

void _shy_common_logic_application_fsm :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
