template < typename type_fsm_inputs >
class shy_loadable_fsm_behaviour
{
public :
    void determine_behaviour_inputs_change ( so_called_type_platform_math_num_whole & ) ;
    void init ( ) ;
    void is_fsm_running ( so_called_type_platform_math_num_whole & ) ;
    void recalc_current_behaviour_inputs ( ) ;
    void reset_behaviour_input_events ( ) ;
    void run_fsm_begin ( ) ;
    void run_fsm_end ( ) ;
    void set_inputs ( so_called_type_platform_pointer_data < type_fsm_inputs > ) ;
    void tick_all_fsms ( ) ;
    void update_fixed_behaviour_inputs ( ) ;
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

    so_called_type_platform_math_num_whole _fsm_running ;
    so_called_type_platform_pointer_data < type_fsm_inputs > _inputs ;
    so_called_std_vector < type_fsm_state > _states ;
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
void shy_loadable_fsm_behaviour < type_fsm_inputs > :: init ( )
{
    so_called_platform_math :: make_num_whole ( _fsm_running , so_called_std_false ) ;
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

