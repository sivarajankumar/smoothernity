template < typename type_fsm_inputs >
class shy_loadable_fsm_behaviour
{
private :
    class type_fsm_state
    : public so_called_type_common_engine_fsm_state
    {
    public :
        virtual void on_entry ( ) ;
        virtual void on_exit ( ) ;
        virtual void on_input ( ) ;
        virtual so_called_type_common_engine_fsm_state & transition ( ) ;
    } ;

    class type_fsm_machine
    {
    public :
        so_called_std_map < so_called_std_string , type_fsm_state > states ;
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
    void _init_machines ( ) ;
    void _init_system ( ) ;
private :
    so_called_type_platform_math_num_whole _fsm_running ;
    so_called_type_platform_pointer_data < type_fsm_inputs > _inputs ;
    so_called_std_map < so_called_std_string , type_fsm_machine > _machines ;
    so_called_type_loadable_fsm_content_system * _system ;
    so_called_type_loadable_fsm_content_system_binding _system_binding ;
} ;

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
: _system ( 0 )
, _system_binding ( 0 )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: init ( )
{
    so_called_platform_math :: make_num_whole ( _fsm_running , so_called_std_false ) ;
    _init_system ( ) ;
    _init_machines ( ) ;
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
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: update_fixed_behaviour_inputs ( )
{
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_system ( )
{
    so_called_type_loadable_fsm_content_system_binding_container * system_binding_container = 0 ;
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_std_string system_name ;

    so_called_loadable_fsm_content :: get_system_binding_container ( system_binding_container ) ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;

    system_name = ( * system_binding_container ) [ _system_binding ] ;
    _system = & ( ( * system_container ) [ system_name ] ) ;
}

template < typename type_fsm_inputs >
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: _init_machines ( )
{
}

