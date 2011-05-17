template < typename type_fsm_inputs >
class shy_loadable_fsm_behaviour
{
private :
    class type_fsm_state
    : public so_called_type_common_engine_fsm_state
    {
    public :
        type_fsm_state ( ) ;
        virtual void on_entry ( ) ;
        virtual void on_exit ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;

    public :
        shy_loadable_fsm_behaviour < type_fsm_inputs > * _behaviour ;
        so_called_type_loadable_fsm_content_machine_container :: const_iterator _machine_i ;
        so_called_type_loadable_fsm_content_state_container :: const_iterator _state_i ;
        so_called_type_loadable_fsm_content_system_container :: const_iterator _system_i ;
    } ;

    typedef so_called_std_map < so_called_std_string , type_fsm_state > type_fsm_state_container ;

    class type_fsm_machine
    {
    public :
        type_fsm_state_container states ;
        so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > state_current ;
    } ;

    typedef so_called_std_map < so_called_std_string , type_fsm_machine > type_fsm_machine_container ;

    class type_fsm_behaviour_inputs
    {
    } ;

public :
    shy_loadable_fsm_behaviour ( ) ;
    void determine_behaviour_inputs_change ( so_called_type_platform_math_num_whole & ) ;
    void init ( ) ;
    void is_fsm_running ( so_called_type_platform_math_num_whole & ) ;
    void recalc_current_behaviour_inputs ( ) ;
    void reset_behaviour_input_events ( ) ;
    void run_fsm_begin ( ) ;
    void run_fsm_end ( ) ;
    void set_inputs ( so_called_type_platform_pointer_data < type_fsm_inputs > ) ;
    void set_system_binding ( so_called_type_loadable_fsm_content_system_binding ) ;
    void tick_all_fsms ( ) ;
    void update_fixed_behaviour_inputs ( ) ;
private :
    void _init_system ( ) ;
    void _init_system_machine 
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
        ) ;
    void _init_system_machine_state
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
        , so_called_type_loadable_fsm_content_state_container :: const_iterator 
        ) ;
    void _init_system_machine_state_initial
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
        ) ;
    void _init_system_machine_states
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
        ) ;
private :
    type_fsm_behaviour_inputs _behaviour_inputs_current ;
    type_fsm_behaviour_inputs _behaviour_inputs_fixed ;
    so_called_type_platform_math_num_whole _fsm_running ;
    so_called_type_platform_pointer_data < type_fsm_inputs > _inputs ;
    type_fsm_machine_container _machines ;
    so_called_type_loadable_fsm_content_system_binding _system_binding ;
} ;

template < typename type_fsm_inputs >
shy_loadable_fsm_behaviour < type_fsm_inputs > :: type_fsm_state :: type_fsm_state ( )
: _behaviour ( 0 )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: type_fsm_state :: on_entry ( )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: type_fsm_state :: on_exit ( )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: type_fsm_state :: on_input ( )
{
}

template < typename type_fsm_inputs >
so_called_type_common_engine_fsm_state & shy_loadable_fsm_behaviour < type_fsm_inputs > :: type_fsm_state :: transition ( )
{
    return so_called_type_common_engine_fsm_state :: transition ( ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: determine_behaviour_inputs_change ( so_called_type_platform_math_num_whole & )
{
}

template < typename type_fsm_inputs >
shy_loadable_fsm_behaviour < type_fsm_inputs > :: shy_loadable_fsm_behaviour ( )
: _system_binding ( 0 )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: init ( )
{
    so_called_platform_math :: make_num_whole ( _fsm_running , so_called_std_false ) ;
    _init_system ( ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: is_fsm_running ( so_called_type_platform_math_num_whole & result )
{
    result = _fsm_running ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: recalc_current_behaviour_inputs ( )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: reset_behaviour_input_events ( )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: run_fsm_begin ( )
{
    so_called_platform_math :: make_num_whole ( _fsm_running , so_called_std_true ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: run_fsm_end ( )
{
    so_called_platform_math :: make_num_whole ( _fsm_running , so_called_std_false ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: set_system_binding ( so_called_type_loadable_fsm_content_system_binding binding )
{
    _system_binding = binding ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: set_inputs ( so_called_type_platform_pointer_data < type_fsm_inputs > inputs )
{
    _inputs = inputs ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: tick_all_fsms ( )
{
    for ( typename type_fsm_machine_container :: iterator machine_i = _machines . begin ( )
        ; machine_i != _machines . end ( )
        ; ++ machine_i
        )
    {
        so_called_common_engine_fsm_stateless :: tick_single_fsm ( machine_i -> second . state_current ) ;
    }
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: update_fixed_behaviour_inputs ( )
{
    _behaviour_inputs_fixed = _behaviour_inputs_current ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_system ( )
{
    so_called_type_loadable_fsm_content_system_binding_container * system_binding_container = 0 ;
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_type_loadable_fsm_content_system_container :: const_iterator system_i ;
    so_called_std_string system_name ;

    so_called_loadable_fsm_content :: get_system_binding_container ( system_binding_container ) ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;

    system_name = ( * system_binding_container ) [ _system_binding ] ;
    system_i = system_container -> find ( system_name ) ;

    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        _init_system_machine ( system_i , machine_i ) ;
    }
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_system_machine 
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    _init_system_machine_states ( system_i , machine_i ) ;
    _init_system_machine_state_initial ( system_i , machine_i ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_system_machine_states
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    for ( so_called_type_loadable_fsm_content_state_container :: const_iterator state_i = machine_i -> second . states . begin ( )
        ; state_i != machine_i -> second . states . end ( )
        ; ++ state_i
        )
    {
        _init_system_machine_state ( system_i , machine_i , state_i ) ;
    }
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_system_machine_state_initial
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    typename type_fsm_machine_container :: iterator fsm_machine_i ;
    typename type_fsm_state_container :: iterator fsm_state_i ;

    fsm_machine_i = _machines . find ( machine_i -> first ) ;
    fsm_state_i = fsm_machine_i -> second . states . find ( so_called_loadable_fsm_consts :: state_initial ) ;
    so_called_platform_pointer :: bind ( fsm_machine_i -> second . state_current , fsm_state_i -> second ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_system_machine_state
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    )
{
    type_fsm_state state ;

    state . _behaviour = this ;
    state . _machine_i = machine_i ;
    state . _state_i = state_i ;
    state . _system_i = system_i ;

    _machines [ machine_i -> first ] . states [ state_i -> first ] = state ;
}

