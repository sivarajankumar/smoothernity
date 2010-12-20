template < typename logic_fsm >
class shy_data_fsm_loadable
{
    typedef typename logic_fsm :: mediator_type :: engine_fsm engine_fsm ;
    typedef typename logic_fsm :: mediator_type :: platform :: platform_conditions platform_conditions ;
    typedef typename logic_fsm :: mediator_type :: platform :: platform_math platform_math ;
    typedef typename logic_fsm :: mediator_type :: platform :: platform_math :: num_whole num_whole ;
    typedef typename logic_fsm :: mediator_type :: platform :: platform_pointer platform_pointer ;

public :
    shy_data_fsm_loadable ( ) ;

    template < typename inputs_type >
    void set_inputs ( typename platform_pointer :: template pointer < inputs_type > ) ;

    template < typename actions_type >
    void set_actions ( typename platform_pointer :: template pointer < actions_type > ) ;

    void is_fsm_running ( num_whole & ) ;
    void run_fsm_begin ( ) ;
    void run_fsm_end ( ) ;
    void reset_autogenerated_input_events ( ) ;
    void recalc_current_autogenerated_inputs ( ) ;
    void determine_autogenerated_inputs_change ( num_whole & ) ;
    void update_fixed_autogenerated_inputs ( ) ;
    void tick_all_fsms ( ) ;
private :
    num_whole _fsm_running ;
} ;

template < typename logic_fsm >
shy_data_fsm_loadable < logic_fsm > :: shy_data_fsm_loadable ( )
{
    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

template < typename logic_fsm >
template < typename inputs_type >
void shy_data_fsm_loadable < logic_fsm > :: set_inputs ( typename platform_pointer :: template pointer < inputs_type > )
{
}

template < typename logic_fsm >
template < typename actions_type >
void shy_data_fsm_loadable < logic_fsm > :: set_actions ( typename platform_pointer :: template pointer < actions_type > )
{
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: is_fsm_running ( num_whole & result )
{
    result = _fsm_running ;
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: run_fsm_begin ( )
{
    platform_math :: make_num_whole ( _fsm_running , true ) ;
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: run_fsm_end ( )
{
    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: reset_autogenerated_input_events ( )
{
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: recalc_current_autogenerated_inputs ( )
{
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: determine_autogenerated_inputs_change ( num_whole & result )
{
    platform_math :: make_num_whole ( result , false ) ;
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: update_fixed_autogenerated_inputs ( )
{
}

template < typename logic_fsm >
void shy_data_fsm_loadable < logic_fsm > :: tick_all_fsms ( )
{
}

