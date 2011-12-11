template < typename fsm_inputs_type >
class shy_loadable_fsm_behaviour
{
private :
    typedef so_called_platform_math_num_whole_type fsm_inputs_type :: * fsm_input_binding_type ;

    class fsm_state_type
    : public so_called_common_engine_fsm_state_type
    {
    public :
        fsm_state_type ( ) ;
        virtual void on_entry ( ) ;
        virtual void on_exit ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_common_engine_fsm_state_type & transition ( ) ;
    private :
        void _calculate_condition_commands 
            ( so_called_lib_std_bool & 
            , const so_called_loadable_fsm_content_condition_command_container_type &
            ) ;
        void _calculate_condition_groups 
            ( so_called_lib_std_bool & 
            , const so_called_loadable_fsm_content_condition_group_container_type & 
            ) ;
        void _calculate_condition_inputs 
            ( so_called_lib_std_bool & 
            , const so_called_loadable_fsm_content_condition_input_container_type &
            ) ;
        void _calculate_condition_states 
            ( so_called_lib_std_bool & 
            , const so_called_loadable_fsm_content_condition_state_container_type &
            ) ;
        void _execute_action_command ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator ) ;
        void _execute_action_discard ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator ) ;
        void _execute_action_do ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator ) ;
        void _execute_actions ( const so_called_loadable_fsm_content_actions_type & ) ;
        void _execute_actions_commands ( const so_called_loadable_fsm_content_action_command_container_type & ) ;
        void _execute_actions_discard ( const so_called_loadable_fsm_content_action_discard_container_type & ) ;
        void _execute_actions_do ( const so_called_loadable_fsm_content_action_do_container_type & ) ;
    public :
        shy_loadable_fsm_behaviour < fsm_inputs_type > * _behaviour ;
        so_called_loadable_fsm_content_machine_container_type :: const_iterator _machine_i ;
        so_called_loadable_fsm_content_state_container_type :: const_iterator _state_i ;
        so_called_loadable_fsm_content_system_container_type :: const_iterator _system_i ;
    } ;

    typedef so_called_lib_std_map < so_called_lib_std_string , fsm_state_type > fsm_state_container_type ;

    class fsm_machine_type
    {
    public :
        fsm_state_container_type states ;
        so_called_platform_pointer_data_type < so_called_common_engine_fsm_state_type > state_current ;
    } ;

    typedef so_called_lib_std_map < so_called_lib_std_string , fsm_machine_type > fsm_machine_container_type ;

    class fsm_behaviour_input_command_type
    {
    public :
        fsm_behaviour_input_command_type ( ) ;
        so_called_lib_std_bool active ;
    } ;

    typedef so_called_lib_std_map < so_called_lib_std_string , fsm_behaviour_input_command_type > fsm_behaviour_input_command_container_type ;

    class fsm_behaviour_input_state_type
    {
    public :
        fsm_behaviour_input_state_type ( ) ;
        so_called_lib_std_bool active ;
    } ;

    typedef so_called_lib_std_map < so_called_lib_std_string , fsm_behaviour_input_state_type > fsm_behaviour_input_state_container_type ;

    class fsm_behaviour_input_machine_type
    {
    public :
        fsm_behaviour_input_command_container_type commands ;
        fsm_behaviour_input_state_container_type states ;
    } ;

    typedef so_called_lib_std_map < so_called_lib_std_string , fsm_behaviour_input_machine_type > fsm_behaviour_input_machine_container_type ;

    class fsm_behaviour_inputs_type
    {
    public :
        fsm_behaviour_input_machine_container_type machines ;
    } ;

public :
    shy_loadable_fsm_behaviour ( ) ;
    void determine_behaviour_inputs_change ( so_called_platform_math_num_whole_type & ) ;
    void init ( ) ;
    void is_fsm_running ( so_called_platform_math_num_whole_type & ) ;
    void recalc_current_behaviour_inputs ( ) ;
    void reset_behaviour_input_events ( ) ;
    void run_fsm_begin ( ) ;
    void run_fsm_end ( ) ;
    void set_inputs 
        ( so_called_platform_pointer_data_type < fsm_inputs_type > 
        , so_called_platform_pointer_data_type < fsm_inputs_type > 
        ) ;
    void set_system_binding ( so_called_loadable_fsm_content_system_binding_type ) ;
    void tick_all_fsms ( ) ;
    void update_fixed_behaviour_inputs ( ) ;
private :
    void _init_system ( ) ;
    void _init_system_machine 
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        ) ;
    void _init_system_machine_state
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        ) ;
    void _init_system_machine_state_action_command
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , so_called_loadable_fsm_content_action_command_container_type :: const_iterator
        ) ;
    void _init_system_machine_state_actions
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , const so_called_loadable_fsm_content_actions_type &
        ) ;
    void _init_system_machine_state_condition_command
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , so_called_loadable_fsm_content_condition_command_container_type :: const_iterator
        ) ;
    void _init_system_machine_state_condition_group
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , so_called_loadable_fsm_content_condition_group_container_type :: const_iterator
        ) ;
    void _init_system_machine_state_condition_groups
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , const so_called_loadable_fsm_content_condition_group_container_type &
        ) ;
    void _init_system_machine_state_condition_state
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , so_called_loadable_fsm_content_condition_state_container_type :: const_iterator
        ) ;
    void _init_system_machine_state_initial
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        ) ;
    void _init_system_machine_state_on_input
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , so_called_loadable_fsm_content_on_input_container_type :: const_iterator
        ) ;
    void _init_system_machine_state_transition
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        , so_called_loadable_fsm_content_state_container_type :: const_iterator 
        , so_called_loadable_fsm_content_transition_container_type :: const_iterator
        ) ;
    void _init_system_machine_states
        ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
        , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
        ) ;
    void _copy_current_behaviour_inputs_to_fixed ( ) ;
private :
    fsm_behaviour_inputs_type _behaviour_inputs_current ;
    fsm_behaviour_inputs_type _behaviour_inputs_fixed ;
    so_called_platform_math_num_whole_type _fsm_running ;
    so_called_platform_pointer_data_type < fsm_inputs_type > _inputs_current ;
    so_called_platform_pointer_data_type < fsm_inputs_type > _inputs_fixed ;
    fsm_machine_container_type _machines ;
    so_called_loadable_fsm_content_system_binding_type _system_binding ;
} ;

template < typename fsm_inputs_type >
shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_behaviour_input_state_type :: fsm_behaviour_input_state_type ( )
: active ( so_called_lib_std_false )
{
}

template < typename fsm_inputs_type >
shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_behaviour_input_command_type :: fsm_behaviour_input_command_type ( )
: active ( so_called_lib_std_false )
{
}

template < typename fsm_inputs_type >
shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_state_type :: fsm_state_type ( )
: _behaviour ( 0 )
{
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_state_type :: on_entry ( )
{
    so_called_trace
        ( so_called_trace_loadable_fsm_behaviour :: machine_state_on_entry
            ( _machine_i -> first . c_str ( )
            , _state_i -> first . c_str ( )
            )
        ) ;
    _execute_actions ( _state_i -> second . on_entry ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_state_type :: on_exit ( )
{
    so_called_trace
        ( so_called_trace_loadable_fsm_behaviour :: machine_state_on_exit
            ( _machine_i -> first . c_str ( )
            , _state_i -> first . c_str ( )
            )
        ) ;
    _execute_actions ( _state_i -> second . on_exit ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_state_type :: on_input ( )
{
    so_called_trace
        ( so_called_trace_loadable_fsm_behaviour :: machine_state_on_input
            ( _machine_i -> first . c_str ( )
            , _state_i -> first . c_str ( )
            )
        ) ;
    for ( so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i = _state_i -> second . on_input . begin ( )
        ; on_input_i != _state_i -> second . on_input . end ( )
        ; ++ on_input_i
        )
    {
        so_called_lib_std_bool conditions = so_called_lib_std_false ;
        _calculate_condition_groups ( conditions , on_input_i -> condition_groups ) ;
        if ( conditions )
            _execute_actions ( on_input_i -> actions ) ;
    }
}

template < typename fsm_inputs_type >
so_called_common_engine_fsm_state_type & shy_loadable_fsm_behaviour < fsm_inputs_type > :: fsm_state_type :: transition ( )
{
    for ( so_called_loadable_fsm_content_transition_container_type :: const_iterator transition_i = _state_i -> second . transitions . begin ( )
        ; transition_i != _state_i -> second . transitions . end ( )
        ; ++ transition_i
        )
    {
        so_called_lib_std_bool conditions = so_called_lib_std_false ;
        _calculate_condition_groups ( conditions , transition_i -> condition_groups ) ;

        if ( conditions )
        {
            typename fsm_machine_container_type :: iterator fsm_machine_i ;
            typename fsm_state_container_type :: iterator fsm_state_i ;

            fsm_machine_i = _behaviour -> _machines . find ( _machine_i -> first ) ;
            if ( fsm_machine_i != _behaviour -> _machines . end ( ) )
            {
                fsm_state_i = fsm_machine_i -> second . states . find ( transition_i -> state ) ;
                if ( fsm_state_i != fsm_machine_i -> second . states . end ( ) )
                    return fsm_state_i -> second ;
            }
        }
    }
    return so_called_common_engine_fsm_state_type :: transition ( ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _calculate_condition_groups 
    ( so_called_lib_std_bool & result 
    , const so_called_loadable_fsm_content_condition_group_container_type & condition_groups
    )
{
    result = condition_groups . empty ( ) ;
    for ( so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i = condition_groups . begin ( )
        ; condition_group_i != condition_groups . end ( )
        ; ++ condition_group_i
        )
    {
        so_called_lib_std_bool result_commands = so_called_lib_std_false ;
        so_called_lib_std_bool result_group = so_called_lib_std_false ;
        so_called_lib_std_bool result_inputs = so_called_lib_std_false ;
        so_called_lib_std_bool result_states = so_called_lib_std_false ;

        _calculate_condition_commands ( result_commands , condition_group_i -> commands ) ;
        _calculate_condition_inputs ( result_inputs , condition_group_i -> inputs ) ;
        _calculate_condition_states ( result_states , condition_group_i -> states ) ;

        result_group = so_called_lib_std_true ;
        result_group &= result_commands ;
        result_group &= result_inputs ;
        result_group &= result_states ;

        if ( result_group )
        {
            result = so_called_lib_std_true ;
            break ;
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _calculate_condition_commands 
    ( so_called_lib_std_bool & result 
    , const so_called_loadable_fsm_content_condition_command_container_type & condition_commands
    )
{
    result = so_called_lib_std_true ;
    for ( so_called_loadable_fsm_content_condition_command_container_type :: const_iterator condition_command_i = condition_commands . begin ( )
        ; condition_command_i != condition_commands . end ( )
        ; ++ condition_command_i
        )
    {
        typename fsm_behaviour_input_machine_container_type :: const_iterator fsm_behaviour_input_machine_i ;
        typename fsm_behaviour_input_command_container_type :: const_iterator fsm_behaviour_input_command_i ;

        fsm_behaviour_input_machine_i = _behaviour -> _behaviour_inputs_fixed . machines . find ( _machine_i -> first ) ;
        if ( fsm_behaviour_input_machine_i != _behaviour -> _behaviour_inputs_fixed . machines . end ( ) )
        {
            fsm_behaviour_input_command_i = fsm_behaviour_input_machine_i -> second . commands . find ( condition_command_i -> command ) ;
            if ( fsm_behaviour_input_command_i != fsm_behaviour_input_machine_i -> second . commands . end ( ) )
            {
                if ( ! fsm_behaviour_input_command_i -> second . active )
                {
                    result = so_called_lib_std_false ;
                    break ;
                }
            }
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _calculate_condition_inputs 
    ( so_called_lib_std_bool & result 
    , const so_called_loadable_fsm_content_condition_input_container_type & condition_inputs
    )
{
    result = so_called_lib_std_true ;
    for ( so_called_loadable_fsm_content_condition_input_container_type :: const_iterator condition_input_i = condition_inputs . begin ( )
        ; condition_input_i != condition_inputs . end ( )
        ; ++ condition_input_i
        )
    {
        so_called_loadable_fsm_content_input_binding_container_type :: const_iterator input_binding_i ;
        so_called_platform_math_num_whole_type condition ;
        fsm_input_binding_type input_binding ;

        input_binding_i = _system_i -> second . inputs . find ( condition_input_i -> input ) ;
        if ( input_binding_i != _system_i -> second . inputs . end ( ) )
        {
            input_binding = reinterpret_cast < fsm_input_binding_type > ( input_binding_i -> second ) ;
            condition = _behaviour -> _inputs_fixed . get ( ) .* input_binding ;
            if ( so_called_platform_conditions :: whole_is_false ( condition ) )
            {
                result = so_called_lib_std_false ;
                break ;
            }
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _calculate_condition_states 
    ( so_called_lib_std_bool & result 
    , const so_called_loadable_fsm_content_condition_state_container_type & condition_states
    )
{
    result = so_called_lib_std_true ;
    for ( so_called_loadable_fsm_content_condition_state_container_type :: const_iterator condition_state_i = condition_states . begin ( )
        ; condition_state_i != condition_states . end ( )
        ; ++ condition_state_i 
        )
    {
        typename fsm_behaviour_input_machine_container_type :: const_iterator fsm_behaviour_input_machine_i ;
        typename fsm_behaviour_input_state_container_type :: const_iterator fsm_behaviour_input_state_i ;

        fsm_behaviour_input_machine_i = _behaviour -> _behaviour_inputs_fixed . machines . find ( condition_state_i -> machine ) ;
        if ( fsm_behaviour_input_machine_i != _behaviour -> _behaviour_inputs_fixed . machines . end ( ) )
        {
            fsm_behaviour_input_state_i = fsm_behaviour_input_machine_i -> second . states . find ( condition_state_i -> state ) ;
            if ( fsm_behaviour_input_state_i != fsm_behaviour_input_machine_i -> second . states . end ( ) )
            {
                if ( ! fsm_behaviour_input_state_i -> second . active )
                {
                    result = so_called_lib_std_false ;
                    break ;
                }
            }
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_actions ( const so_called_loadable_fsm_content_actions_type & actions )
{
    _execute_actions_commands ( actions . commands ) ;
    _execute_actions_do ( actions . actions ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_actions_commands ( const so_called_loadable_fsm_content_action_command_container_type & command_container )
{
    for ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator command_i = command_container . begin ( )
        ; command_i != command_container . end ( )
        ; ++ command_i
        )
    {
        _execute_action_command ( command_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_actions_discard ( const so_called_loadable_fsm_content_action_discard_container_type & action_discard_container )
{
    for ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i = action_discard_container . begin ( )
        ; action_discard_i != action_discard_container . end ( )
        ; ++ action_discard_i
        )
    {
        _execute_action_discard ( action_discard_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_actions_do ( const so_called_loadable_fsm_content_action_do_container_type & action_do_container )
{
    for ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i = action_do_container . begin ( )
        ; action_do_i != action_do_container . end ( )
        ; ++ action_do_i
        )
    {
        _execute_action_do ( action_do_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_action_command ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator command_i )
{
    so_called_trace
        ( so_called_trace_loadable_fsm_behaviour :: machine_state_action_command 
            ( _machine_i -> first . c_str ( )
            , _state_i -> first . c_str ( )
            , command_i -> command . c_str ( )
            , command_i -> machine . c_str ( )
            )
        ) ;

    typename fsm_behaviour_input_command_container_type :: iterator fsm_behaviour_input_command_i ;
    typename fsm_behaviour_input_machine_container_type :: iterator fsm_behaviour_input_machine_i ;

    fsm_behaviour_input_machine_i = _behaviour -> _behaviour_inputs_current . machines . find ( command_i -> machine ) ;
    if ( fsm_behaviour_input_machine_i != _behaviour -> _behaviour_inputs_current . machines . end ( ) )
    {
        fsm_behaviour_input_command_i = fsm_behaviour_input_machine_i -> second . commands . find ( command_i -> command ) ;
        if ( fsm_behaviour_input_command_i != fsm_behaviour_input_machine_i -> second . commands . end ( ) )
            fsm_behaviour_input_command_i -> second . active = so_called_lib_std_true ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_action_discard ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i )
{
    so_called_trace
        ( so_called_trace_loadable_fsm_behaviour :: machine_state_action_discard
            ( _machine_i -> first . c_str ( )
            , _state_i -> first . c_str ( )
            , action_discard_i -> input . c_str ( )
            )
        ) ;

    so_called_loadable_fsm_content_input_binding_container_type :: const_iterator input_binding_i ;
    fsm_input_binding_type input_binding ;

    input_binding_i = _system_i -> second . inputs . find ( action_discard_i -> input ) ;
    if ( input_binding_i != _system_i -> second . inputs . end ( ) )
    {
        input_binding = reinterpret_cast < fsm_input_binding_type > ( input_binding_i -> second ) ;
        _behaviour -> _inputs_current . get ( ) .* input_binding = so_called_platform_math_consts :: whole_false ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > 
:: fsm_state_type 
:: _execute_action_do ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i )
{
    so_called_trace
        ( so_called_trace_loadable_fsm_behaviour :: machine_state_action_do
            ( _machine_i -> first . c_str ( )
            , _state_i -> first . c_str ( )
            , action_do_i -> action . c_str ( )
            )
        ) ;

    so_called_loadable_fsm_content_action_binding_container_type :: const_iterator action_binding_i ;
    action_binding_i = _system_i -> second . actions . find ( action_do_i -> action ) ;
    if ( action_binding_i != _system_i -> second . actions . end ( ) )
        ( * action_binding_i -> second ) ( ) ;
}

template < typename fsm_inputs_type >
shy_loadable_fsm_behaviour < fsm_inputs_type > :: shy_loadable_fsm_behaviour ( )
: _system_binding ( 0 )
{
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: determine_behaviour_inputs_change ( so_called_platform_math_num_whole_type & result )
{
    result = so_called_platform_math_consts :: whole_false ;
    for ( typename fsm_behaviour_input_machine_container_type :: const_iterator input_current_machine_i = _behaviour_inputs_current . machines . begin ( )
        ; input_current_machine_i != _behaviour_inputs_current . machines . end ( )
        ; ++ input_current_machine_i
        )
    {
        typename fsm_behaviour_input_machine_container_type :: const_iterator input_fixed_machine_i ;
        input_fixed_machine_i = _behaviour_inputs_fixed . machines . find ( input_current_machine_i -> first ) ;
        if ( input_fixed_machine_i == _behaviour_inputs_fixed . machines . end ( ) )
            continue ;

        for ( typename fsm_behaviour_input_state_container_type :: const_iterator input_current_state_i = input_current_machine_i -> second . states . begin ( )
            ; input_current_state_i != input_current_machine_i -> second . states . end ( )
            ; ++ input_current_state_i
            )
        {
            typename fsm_behaviour_input_state_container_type :: const_iterator input_fixed_state_i ;
            input_fixed_state_i = input_fixed_machine_i -> second . states . find ( input_current_state_i -> first ) ;

            if ( input_fixed_state_i != input_fixed_machine_i -> second . states . end ( ) )
            {
                if ( input_current_state_i -> second . active != input_fixed_state_i -> second . active )
                {
                    result = so_called_platform_math_consts :: whole_true ;
                    return ;
                }
            }
        }

        for ( typename fsm_behaviour_input_command_container_type :: const_iterator input_current_command_i = input_current_machine_i -> second . commands . begin ( )
            ; input_current_command_i != input_current_machine_i -> second . commands . end ( )
            ; ++ input_current_command_i
            )
        {
            typename fsm_behaviour_input_command_container_type :: const_iterator input_fixed_command_i ;
            input_fixed_command_i = input_fixed_machine_i -> second . commands . find ( input_current_command_i -> first ) ;
            if ( input_fixed_command_i != input_fixed_machine_i -> second . commands . end ( ) )
            {
                if ( input_current_command_i -> second . active != input_fixed_command_i -> second . active )
                {
                    result = so_called_platform_math_consts :: whole_true ;
                    return ;
                }
            }
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: init ( )
{
    _behaviour_inputs_current = fsm_behaviour_inputs_type ( ) ;
    _behaviour_inputs_fixed = fsm_behaviour_inputs_type ( ) ;
    _machines = fsm_machine_container_type ( ) ;
    _fsm_running = so_called_platform_math_consts :: whole_false ;
    _init_system ( ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: is_fsm_running ( so_called_platform_math_num_whole_type & result )
{
    result = _fsm_running ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: recalc_current_behaviour_inputs ( )
{
    for ( typename fsm_behaviour_input_machine_container_type :: iterator input_current_machine_i = _behaviour_inputs_current . machines . begin ( )
        ; input_current_machine_i != _behaviour_inputs_current . machines . end ( )
        ; ++ input_current_machine_i
        )
    {
        typename fsm_machine_container_type :: iterator fsm_machine_i ;
        fsm_machine_i = _machines . find ( input_current_machine_i -> first ) ;
        if ( fsm_machine_i == _machines . end ( ) )
            continue ;
        for ( typename fsm_behaviour_input_state_container_type :: iterator input_current_state_i = input_current_machine_i -> second . states . begin ( )
            ; input_current_state_i != input_current_machine_i -> second . states . end ( )
            ; ++ input_current_state_i
            )
        {
            typename fsm_state_container_type :: iterator fsm_state_i ;
            fsm_state_i = fsm_machine_i -> second . states . find ( input_current_state_i -> first ) ;
            if ( fsm_state_i == fsm_machine_i -> second . states . end ( ) )
                continue ;

            so_called_platform_math_num_whole_type state_active ;
            so_called_platform_pointer :: is_bound_to
                ( state_active
                , fsm_machine_i -> second . state_current
                , fsm_state_i -> second
                ) ;

            if ( so_called_platform_conditions :: whole_is_true ( state_active ) )
                input_current_state_i -> second . active = so_called_lib_std_true ;
            else
                input_current_state_i -> second . active = so_called_lib_std_false ;
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: reset_behaviour_input_events ( )
{
    for ( typename fsm_behaviour_input_machine_container_type :: iterator input_current_machine_i = _behaviour_inputs_current . machines . begin ( )
        ; input_current_machine_i != _behaviour_inputs_current . machines . end ( )
        ; ++ input_current_machine_i
        )
    {
        for ( typename fsm_behaviour_input_command_container_type :: iterator input_current_command_i = input_current_machine_i -> second . commands . begin ( )
            ; input_current_command_i != input_current_machine_i -> second . commands . end ( )
            ; ++ input_current_command_i
            )
        {
            input_current_command_i -> second . active = so_called_lib_std_false ;
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: run_fsm_begin ( )
{
    _fsm_running = so_called_platform_math_consts :: whole_true ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: run_fsm_end ( )
{
    _fsm_running = so_called_platform_math_consts :: whole_false ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: set_system_binding ( so_called_loadable_fsm_content_system_binding_type binding )
{
    _system_binding = binding ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: set_inputs 
    ( so_called_platform_pointer_data_type < fsm_inputs_type > inputs_current
    , so_called_platform_pointer_data_type < fsm_inputs_type > inputs_fixed
    )
{
    _inputs_current = inputs_current ;
    _inputs_fixed = inputs_fixed ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: tick_all_fsms ( )
{
    so_called_trace ( so_called_trace_loadable_fsm_behaviour :: tick_all_fsms ( ) ) ;
    for ( typename fsm_machine_container_type :: iterator machine_i = _machines . begin ( )
        ; machine_i != _machines . end ( )
        ; ++ machine_i
        )
    {
        so_called_common_engine_fsm_stateless :: tick_single_fsm ( machine_i -> second . state_current ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: update_fixed_behaviour_inputs ( )
{
    _copy_current_behaviour_inputs_to_fixed ( ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _copy_current_behaviour_inputs_to_fixed ( )
{
    for ( typename fsm_behaviour_input_machine_container_type :: const_iterator input_current_machine_i = _behaviour_inputs_current . machines . begin ( )
        ; input_current_machine_i != _behaviour_inputs_current . machines . end ( )
        ; ++ input_current_machine_i
        )
    {
        for ( typename fsm_behaviour_input_state_container_type :: const_iterator input_current_state_i = input_current_machine_i -> second . states . begin ( )
            ; input_current_state_i != input_current_machine_i -> second . states . end ( )
            ; ++ input_current_state_i
            )
        {
            _behaviour_inputs_fixed . machines [ input_current_machine_i -> first ] . states [ input_current_state_i -> first ] = input_current_state_i -> second ;
        }

        for ( typename fsm_behaviour_input_command_container_type :: const_iterator input_current_command_i = input_current_machine_i -> second . commands . begin ( )
            ; input_current_command_i != input_current_machine_i -> second . commands . end ( )
            ; ++ input_current_command_i
            )
        {
            _behaviour_inputs_fixed . machines [ input_current_machine_i -> first ] . commands [ input_current_command_i -> first ] = input_current_command_i -> second ;
        }
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system ( )
{
    so_called_loadable_fsm_content_system_binding_container_type * system_binding_container = 0 ;
    so_called_loadable_fsm_content_system_container_type * system_container = 0 ;
    so_called_loadable_fsm_content_system_container_type :: const_iterator system_i ;
    so_called_lib_std_string system_name ;

    so_called_loadable_fsm_content :: get_system_binding_container ( system_binding_container ) ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;

    system_name = ( * system_binding_container ) [ _system_binding ] ;
    system_i = system_container -> find ( system_name ) ;
    if ( system_i != system_container -> end ( ) )
    {
        for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
            ; machine_i != system_i -> second . machines . end ( )
            ; ++ machine_i
            )
        {
            _init_system_machine ( system_i , machine_i ) ;
        }
    }

    _copy_current_behaviour_inputs_to_fixed ( ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine 
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    )
{
    _init_system_machine_states ( system_i , machine_i ) ;
    _init_system_machine_state_initial ( system_i , machine_i ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_states
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    )
{
    for ( so_called_loadable_fsm_content_state_container_type :: const_iterator state_i = machine_i -> second . states . begin ( )
        ; state_i != machine_i -> second . states . end ( )
        ; ++ state_i
        )
    {
        _init_system_machine_state ( system_i , machine_i , state_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_initial
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    )
{
    typename fsm_machine_container_type :: iterator fsm_machine_i ;
    typename fsm_state_container_type :: iterator fsm_state_i ;

    fsm_machine_i = _machines . find ( machine_i -> first ) ;
    if ( fsm_machine_i != _machines . end ( ) )
    {
        fsm_state_i = fsm_machine_i -> second . states . find ( so_called_loadable_fsm_consts :: state_initial ) ;
        if ( fsm_state_i != fsm_machine_i -> second . states . end ( ) )
            so_called_platform_pointer :: bind ( fsm_machine_i -> second . state_current , fsm_state_i -> second ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    fsm_state_type state ;

    state . _behaviour = this ;
    state . _machine_i = machine_i ;
    state . _state_i = state_i ;
    state . _system_i = system_i ;

    _machines [ machine_i -> first ] . states [ state_i -> first ] = state ;

    _init_system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_entry ) ;
    _init_system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_exit ) ;

    for ( so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i = state_i -> second . on_input . begin ( )
        ; on_input_i != state_i -> second . on_input . end ( )
        ; ++ on_input_i
        )
    {
        _init_system_machine_state_on_input ( system_i , machine_i , state_i , on_input_i ) ;
    }

    for ( so_called_loadable_fsm_content_transition_container_type :: const_iterator transition_i = state_i -> second . transitions . begin ( )
        ; transition_i != state_i -> second . transitions . end ( )
        ; ++ transition_i
        )
    {
        _init_system_machine_state_transition ( system_i , machine_i , state_i , transition_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_on_input
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i
    )
{
    _init_system_machine_state_actions ( system_i , machine_i , state_i , on_input_i -> actions ) ;
    _init_system_machine_state_condition_groups ( system_i , machine_i , state_i , on_input_i -> condition_groups ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_transition
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_transition_container_type :: const_iterator transition_i
    )
{
    _init_system_machine_state_condition_groups ( system_i , machine_i , state_i , transition_i -> condition_groups ) ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_actions
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , const so_called_loadable_fsm_content_actions_type & actions
    )
{
    for ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i = actions . commands . begin ( )
        ; action_command_i != actions . commands . end ( )
        ; ++ action_command_i
        )
    {
        _init_system_machine_state_action_command ( system_i , machine_i , state_i , action_command_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_condition_groups
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , const so_called_loadable_fsm_content_condition_group_container_type & condition_groups
    )
{
    for ( so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i = condition_groups . begin ( )
        ; condition_group_i != condition_groups . end ( )
        ; ++ condition_group_i
        )
    {
        _init_system_machine_state_condition_group ( system_i , machine_i , state_i , condition_group_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_condition_group
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i
    )
{
    for ( so_called_loadable_fsm_content_condition_command_container_type :: const_iterator condition_command_i = condition_group_i -> commands . begin ( )
        ; condition_command_i != condition_group_i -> commands . end ( )
        ; ++ condition_command_i
        )
    {
        _init_system_machine_state_condition_command ( system_i , machine_i , state_i , condition_command_i ) ;
    }

    for ( so_called_loadable_fsm_content_condition_state_container_type :: const_iterator condition_state_i = condition_group_i -> states . begin ( )
        ; condition_state_i != condition_group_i -> states . end ( )
        ; ++ condition_state_i
        )
    {
        _init_system_machine_state_condition_state ( system_i , machine_i , state_i , condition_state_i ) ;
    }
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_action_command
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i
    )
{
    _behaviour_inputs_current
        . machines [ action_command_i -> machine ]
        . commands [ action_command_i -> command ]
        . active = so_called_lib_std_false ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_condition_command
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_command_container_type :: const_iterator condition_command_i
    )
{
    _behaviour_inputs_current
        . machines [ machine_i -> first ]
        . commands [ condition_command_i -> command ]
        . active = so_called_lib_std_false ;
}

template < typename fsm_inputs_type >
void shy_loadable_fsm_behaviour < fsm_inputs_type > :: _init_system_machine_state_condition_state
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_state_container_type :: const_iterator condition_state_i
    )
{
    _behaviour_inputs_current 
        . machines [ condition_state_i -> machine ] 
        . states [ condition_state_i -> state ] 
        . active = so_called_lib_std_false ;
}

