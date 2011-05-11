namespace shy_guts
{
    class type_machine_amusement_generator_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_amusement_generator_state_generating
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_amusement_generator_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_amusement_performer_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_amusement_performer_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_amusement_performer_state_performing
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_game_performer_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_game_performer_state_performing
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
    } ;

    class type_machine_generator_state_amusement
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_generator_state_game
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_generator_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_generator_state_main_menu
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_generator_state_text
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_generator_state_title
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_main_menu_generator_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_main_menu_generator_state_generating
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_main_menu_generator_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_main_menu_performer_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_main_menu_performer_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_main_menu_performer_state_performing
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_performer_state_amusement
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_performer_state_game
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
    } ;

    class type_machine_performer_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_performer_state_main_menu
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_performer_state_title
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_text_generator_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_text_generator_state_generating
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_text_generator_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_title_generator_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_title_generator_state_generating
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_title_generator_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_title_performer_state_finished
    : public so_called_type_common_engine_fsm_state
    {
    } ;

    class type_machine_title_performer_state_initial
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_machine_title_performer_state_performing
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_behaviour_inputs
    {
    public :
        so_called_type_platform_math_num_whole machine_amusement_generator_command_start ;
        so_called_type_platform_math_num_whole machine_amusement_generator_state_is_finished ;
        so_called_type_platform_math_num_whole machine_amusement_performer_command_start ;
        so_called_type_platform_math_num_whole machine_amusement_performer_state_is_finished ;
        so_called_type_platform_math_num_whole machine_game_performer_command_start ;
        so_called_type_platform_math_num_whole machine_main_menu_generator_command_start ;
        so_called_type_platform_math_num_whole machine_main_menu_generator_state_is_finished ;
        so_called_type_platform_math_num_whole machine_main_menu_performer_command_start ;
        so_called_type_platform_math_num_whole machine_main_menu_performer_state_is_finished ;
        so_called_type_platform_math_num_whole machine_text_generator_command_start ;
        so_called_type_platform_math_num_whole machine_text_generator_state_is_finished ;
        so_called_type_platform_math_num_whole machine_title_generator_command_start ;
        so_called_type_platform_math_num_whole machine_title_generator_state_is_finished ;
        so_called_type_platform_math_num_whole machine_title_performer_command_start ;
        so_called_type_platform_math_num_whole machine_title_performer_state_is_finished ;
    } ;

    namespace states
    {
       static type_machine_amusement_generator_state_finished amusement_generator_state_finished ;
       static type_machine_amusement_generator_state_generating amusement_generator_state_generating ;
       static type_machine_amusement_generator_state_initial amusement_generator_state_initial ;
       static type_machine_amusement_performer_state_finished amusement_performer_state_finished ;
       static type_machine_amusement_performer_state_initial amusement_performer_state_initial ;
       static type_machine_amusement_performer_state_performing amusement_performer_state_performing ;
       static type_machine_game_performer_state_initial game_performer_state_initial ;
       static type_machine_game_performer_state_performing game_performer_state_performing ;
       static type_machine_generator_state_amusement generator_state_amusement ;
       static type_machine_generator_state_game generator_state_game ;
       static type_machine_generator_state_initial generator_state_initial ;
       static type_machine_generator_state_main_menu generator_state_main_menu ;
       static type_machine_generator_state_text generator_state_text ;
       static type_machine_generator_state_title generator_state_title ;
       static type_machine_main_menu_generator_state_finished main_menu_generator_state_finished ;
       static type_machine_main_menu_generator_state_generating main_menu_generator_state_generating ;
       static type_machine_main_menu_generator_state_initial main_menu_generator_state_initial ;
       static type_machine_main_menu_performer_state_finished main_menu_performer_state_finished ;
       static type_machine_main_menu_performer_state_initial main_menu_performer_state_initial ;
       static type_machine_main_menu_performer_state_performing main_menu_performer_state_performing ;
       static type_machine_performer_state_amusement performer_state_amusement ;
       static type_machine_performer_state_game performer_state_game ;
       static type_machine_performer_state_initial performer_state_initial ;
       static type_machine_performer_state_main_menu performer_state_main_menu ;
       static type_machine_performer_state_title performer_state_title ;
       static type_machine_text_generator_state_finished text_generator_state_finished ;
       static type_machine_text_generator_state_generating text_generator_state_generating ;
       static type_machine_text_generator_state_initial text_generator_state_initial ;
       static type_machine_title_generator_state_finished title_generator_state_finished ;
       static type_machine_title_generator_state_generating title_generator_state_generating ;
       static type_machine_title_generator_state_initial title_generator_state_initial ;
       static type_machine_title_performer_state_finished title_performer_state_finished ;
       static type_machine_title_performer_state_initial title_performer_state_initial ;
       static type_machine_title_performer_state_performing title_performer_state_performing ;
    }

    namespace behaviour_actions
    {
        static void amusement_generator_command_start ( ) ;
        static void amusement_performer_command_start ( ) ;
        static void game_performer_command_start ( ) ;
        static void main_menu_generator_command_start ( ) ;
        static void main_menu_performer_command_start ( ) ;
        static void text_generator_command_start ( ) ;
        static void title_generator_command_start ( ) ;
        static void title_performer_command_start ( ) ;
    }

    namespace state_environment
    {
        static so_called_type_platform_pointer_data < shy_guts :: type_behaviour_inputs > behaviour_inputs ;
        static so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > inputs ;
    }

    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_amusement_generator_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_amusement_performer_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_game_performer_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_generator_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_main_menu_generator_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_main_menu_performer_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_performer_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_text_generator_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_title_generator_state ;
    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_title_performer_state ;

    static so_called_type_platform_math_num_whole fsm_running ;
    static type_behaviour_inputs current_behaviour_inputs ;
    static type_behaviour_inputs fixed_behaviour_inputs ;
}

void shy_guts :: type_machine_amusement_generator_state_generating :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_amusement_creation_permit ( ) ;
}

void shy_guts :: type_machine_amusement_generator_state_generating :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_amusement_update ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_amusement_generator_state_generating :: transition ( )
{
    if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_amusement_created )
    || so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_amusement_created )
    )
    {
        return shy_guts :: states :: amusement_generator_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_amusement_generator_state_initial :: transition ( )
{
    if
    (  (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_amusement_enabled )
       && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_generator_command_start )
       && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_generator_command_start )
       )
    || (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_amusement_enabled )
       && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_generator_command_start )
       )
    )
    {
        return shy_guts :: states :: amusement_generator_state_generating ;
    }
    else if 
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_amusement_disabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_generator_command_start )
    )
    {
        return shy_guts :: states :: amusement_generator_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_amusement_performer_state_initial :: transition ( )
{
    if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_amusement_enabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_performer_command_start )
    )
    {
        return shy_guts :: states :: amusement_performer_state_performing ;
    }
    else if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_amusement_disabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_performer_command_start )
    )
    {
        return shy_guts :: states :: amusement_performer_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_amusement_performer_state_performing :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_amusement_launch_permit ( ) ;
}

void shy_guts :: type_machine_amusement_performer_state_performing :: on_input ( )
{
    if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_render )
    || (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_render )
       && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_render )
       )
    )
    {
        so_called_common_logic_application_fsm_actions :: logic_amusement_render ( ) ;
        so_called_common_logic_application_fsm_actions :: logic_amusement_render ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
    {
        so_called_common_logic_application_fsm_actions :: logic_amusement_update ( ) ;
        so_called_common_logic_application_fsm_actions :: logic_amusement_update ( ) ;
    }
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_amusement_performer_state_performing :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_amusement_finished ) )
        return shy_guts :: states :: amusement_performer_state_finished ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_game_performer_state_initial :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_game_performer_command_start ) )
        return shy_guts :: states :: game_performer_state_performing ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_game_performer_state_performing :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_game_launch_permit ( ) ;
}

void shy_guts :: type_machine_game_performer_state_performing :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_render ) )
        so_called_common_logic_application_fsm_actions :: logic_game_render ( ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_game_update ( ) ;
}

void shy_guts :: type_machine_generator_state_amusement :: on_entry ( )
{
    shy_guts :: behaviour_actions :: amusement_generator_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_generator_state_amusement :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_generator_state_is_finished ) )
        return shy_guts :: states :: generator_state_game ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_generator_state_initial :: transition ( )
{
    return shy_guts :: states :: generator_state_text ;
}

void shy_guts :: type_machine_generator_state_main_menu :: on_entry ( )
{
    shy_guts :: behaviour_actions :: main_menu_generator_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_generator_state_main_menu :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_main_menu_generator_state_is_finished ) )
        return shy_guts :: states :: generator_state_amusement ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_generator_state_text :: on_entry ( )
{
    shy_guts :: behaviour_actions :: text_generator_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_generator_state_text :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_text_generator_state_is_finished ) )
        return shy_guts :: states :: generator_state_title ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_generator_state_title :: on_entry ( )
{
    shy_guts :: behaviour_actions :: title_generator_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_generator_state_title :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_title_generator_state_is_finished ) )
        return shy_guts :: states :: generator_state_main_menu ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_main_menu_generator_state_generating :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_main_menu_creation_permit ( ) ;
}

void shy_guts :: type_machine_main_menu_generator_state_generating :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_main_menu_update ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_main_menu_generator_state_generating :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_main_menu_created ) )
        return shy_guts :: states :: main_menu_generator_state_finished ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_main_menu_generator_state_initial :: transition ( )
{
    if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_main_menu_enabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_main_menu_generator_command_start )
    )
    {
        return shy_guts :: states :: main_menu_generator_state_generating ;
    }
    else if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_main_menu_disabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_main_menu_generator_command_start )
    )
    {
        return shy_guts :: states :: main_menu_generator_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_main_menu_performer_state_initial :: transition ( )
{
    if 
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_main_menu_enabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_main_menu_performer_command_start )
    )
    {
        return shy_guts :: states :: main_menu_performer_state_performing ;
    }
    else if 
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_main_menu_disabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_main_menu_performer_command_start )
    )
    {
        return shy_guts :: states :: main_menu_performer_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_main_menu_performer_state_performing :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_main_menu_launch_permit ( ) ;
}

void shy_guts :: type_machine_main_menu_performer_state_performing :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_render ) )
        so_called_common_logic_application_fsm_actions :: logic_main_menu_render ( ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_main_menu_update ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_main_menu_performer_state_performing :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_main_menu_finished ) )
        return shy_guts :: states :: main_menu_performer_state_finished ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_performer_state_amusement :: on_entry ( )
{
    shy_guts :: behaviour_actions :: amusement_performer_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_performer_state_amusement :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_amusement_performer_state_is_finished ) )
        return shy_guts :: states :: performer_state_game ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_performer_state_game :: on_entry ( )
{
    shy_guts :: behaviour_actions :: game_performer_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_performer_state_initial :: transition ( )
{
    return shy_guts :: states :: performer_state_title ;
}

void shy_guts :: type_machine_performer_state_main_menu :: on_entry ( )
{
    shy_guts :: behaviour_actions :: main_menu_performer_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_performer_state_main_menu :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_main_menu_performer_state_is_finished ) )
        return shy_guts :: states :: performer_state_amusement ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_performer_state_title :: on_entry ( )
{
    shy_guts :: behaviour_actions :: title_performer_command_start ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_performer_state_title :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_title_performer_state_is_finished ) )
        return shy_guts :: states :: performer_state_main_menu ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_text_generator_state_generating :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_text_prepare_permit ( ) ;
}

void shy_guts :: type_machine_text_generator_state_generating :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_text_update ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_text_generator_state_generating :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_text_prepared ) )
        return shy_guts :: states :: text_generator_state_finished ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_text_generator_state_initial :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_text_generator_command_start ) )
        return shy_guts :: states :: text_generator_state_generating ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_title_generator_state_generating :: on_entry ( )
{
    so_called_common_logic_application_fsm_actions :: logic_title_launch_permit ( ) ;
}

void shy_guts :: type_machine_title_generator_state_generating :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_title_update ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_title_generator_state_generating :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_title_created ) )
        return shy_guts :: states :: title_generator_state_finished ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_title_generator_state_initial :: transition ( )
{
    if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_title_enabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_title_generator_command_start )
    )
    {
        return shy_guts :: states :: title_generator_state_generating ;
    }
    else if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_title_disabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_title_generator_command_start )
    )
    {
        return shy_guts :: states :: title_generator_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_title_performer_state_initial :: transition ( )
{
    if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_title_enabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_title_performer_command_start )
    )
    {
        return shy_guts :: states :: title_performer_state_performing ;
    }
    else if
    (  so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . stage_title_disabled )
    && so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: behaviour_inputs . get ( ) . machine_title_performer_command_start )
    )
    {
        return shy_guts :: states :: title_performer_state_finished ;
    }
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: type_machine_title_performer_state_performing :: on_input ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_render ) )
        so_called_common_logic_application_fsm_actions :: logic_title_render ( ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_application_update ) )
        so_called_common_logic_application_fsm_actions :: logic_title_update ( ) ;
}

so_called_type_common_engine_fsm_state & shy_guts :: type_machine_title_performer_state_performing :: transition ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: state_environment :: inputs . get ( ) . logic_title_finished ) )
        return shy_guts :: states :: title_performer_state_finished ;
    else
        return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

void shy_guts :: behaviour_actions :: amusement_generator_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_amusement_generator_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: amusement_performer_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_amusement_performer_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: game_performer_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_game_performer_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: main_menu_generator_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_main_menu_generator_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: main_menu_performer_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_main_menu_performer_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: text_generator_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_text_generator_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: title_generator_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_title_generator_command_start , true ) ;
}

void shy_guts :: behaviour_actions :: title_performer_command_start ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_title_performer_command_start , true ) ;
}

void so_called_common_logic_application_fsm_behaviour :: determine_behaviour_inputs_change ( so_called_type_platform_math_num_whole & inputs_changed )
{
    if ( so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_amusement_generator_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_amusement_generator_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_amusement_generator_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_amusement_generator_state_is_finished
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_amusement_performer_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_amusement_performer_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_amusement_performer_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_amusement_performer_state_is_finished
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_game_performer_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_game_performer_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_main_menu_generator_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_main_menu_generator_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_main_menu_generator_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_main_menu_generator_state_is_finished
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_main_menu_performer_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_main_menu_performer_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_main_menu_performer_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_main_menu_performer_state_is_finished
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_text_generator_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_text_generator_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_text_generator_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_text_generator_state_is_finished
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_title_generator_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_title_generator_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_title_generator_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_title_generator_state_is_finished
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_title_performer_command_start
            , shy_guts :: fixed_behaviour_inputs . machine_title_performer_command_start
            )
      && so_called_platform_conditions :: wholes_are_equal
            ( shy_guts :: current_behaviour_inputs . machine_title_performer_state_is_finished
            , shy_guts :: fixed_behaviour_inputs . machine_title_performer_state_is_finished
            )
       )
    {
        so_called_platform_math :: make_num_whole ( inputs_changed , false ) ;
    }
    else
        so_called_platform_math :: make_num_whole ( inputs_changed , true ) ;
}

void so_called_common_logic_application_fsm_behaviour :: init ( )
{
    so_called_platform_pointer :: bind
        ( shy_guts :: state_environment :: behaviour_inputs
        , shy_guts :: fixed_behaviour_inputs
        ) ;

    so_called_platform_math :: make_num_whole ( shy_guts :: fsm_running , false ) ;

    so_called_platform_pointer :: bind
        ( shy_guts :: machine_amusement_generator_state
        , shy_guts :: states :: amusement_generator_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_amusement_performer_state
        , shy_guts :: states :: amusement_performer_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_game_performer_state
        , shy_guts :: states :: game_performer_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_generator_state
        , shy_guts :: states :: generator_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_main_menu_generator_state
        , shy_guts :: states :: main_menu_generator_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_main_menu_performer_state
        , shy_guts :: states :: main_menu_performer_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_performer_state
        , shy_guts :: states :: performer_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_text_generator_state
        , shy_guts :: states :: text_generator_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_title_generator_state
        , shy_guts :: states :: title_generator_state_initial
        ) ;
    so_called_platform_pointer :: bind
        ( shy_guts :: machine_title_performer_state
        , shy_guts :: states :: title_performer_state_initial
        ) ;
}

void so_called_common_logic_application_fsm_behaviour :: is_fsm_running ( so_called_type_platform_math_num_whole & result )
{
    result = shy_guts :: fsm_running ;
}

void so_called_common_logic_application_fsm_behaviour :: recalc_current_behaviour_inputs ( )
{
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_amusement_generator_state_is_finished
        , shy_guts :: machine_amusement_generator_state
        , shy_guts :: states :: amusement_generator_state_finished
        ) ;
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_amusement_performer_state_is_finished
        , shy_guts :: machine_amusement_performer_state
        , shy_guts :: states :: amusement_performer_state_finished
        ) ;
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_main_menu_generator_state_is_finished
        , shy_guts :: machine_main_menu_generator_state
        , shy_guts :: states :: main_menu_generator_state_finished
        ) ;
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_main_menu_performer_state_is_finished
        , shy_guts :: machine_main_menu_performer_state
        , shy_guts :: states :: main_menu_performer_state_finished
        ) ;
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_text_generator_state_is_finished
        , shy_guts :: machine_text_generator_state
        , shy_guts :: states :: text_generator_state_finished
        ) ;
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_title_generator_state_is_finished
        , shy_guts :: machine_title_generator_state
        , shy_guts :: states :: title_generator_state_finished
        ) ;
    so_called_platform_pointer :: is_bound_to
        ( shy_guts :: current_behaviour_inputs . machine_title_performer_state_is_finished
        , shy_guts :: machine_title_performer_state
        , shy_guts :: states :: title_performer_state_finished
        ) ;
}

void so_called_common_logic_application_fsm_behaviour :: reset_behaviour_input_events ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_amusement_generator_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_amusement_performer_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_game_performer_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_main_menu_generator_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_main_menu_performer_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_text_generator_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_title_generator_command_start , false ) ;
    so_called_platform_math :: make_num_whole ( shy_guts :: current_behaviour_inputs . machine_title_performer_command_start , false ) ;
}

void so_called_common_logic_application_fsm_behaviour :: run_fsm_begin ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: fsm_running , true ) ;
}

void so_called_common_logic_application_fsm_behaviour :: run_fsm_end ( )
{
    so_called_platform_math :: make_num_whole ( shy_guts :: fsm_running , false ) ;
}

void so_called_common_logic_application_fsm_behaviour :: set_inputs ( so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > inputs )
{
    shy_guts :: state_environment :: inputs = inputs ;
}

void so_called_common_logic_application_fsm_behaviour :: tick_all_fsms ( )
{
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_amusement_generator_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_amusement_performer_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_game_performer_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_generator_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_main_menu_generator_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_main_menu_performer_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_performer_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_text_generator_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_title_generator_state ) ;
    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_title_performer_state ) ;
}

void so_called_common_logic_application_fsm_behaviour :: update_fixed_behaviour_inputs ( )
{
    shy_guts :: fixed_behaviour_inputs = shy_guts :: current_behaviour_inputs ;
}

