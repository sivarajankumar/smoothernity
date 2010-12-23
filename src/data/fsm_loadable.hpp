template 
    < typename _logic_fsm
    >
class shy_data_fsm_loadable_types
{
public :
    typedef _logic_fsm logic_fsm ;
} ;

template < typename data_fsm_loadable_types >
class shy_data_fsm_loadable
{
    typedef typename data_fsm_loadable_types :: logic_fsm :: actions_type actions_type ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: inputs_type inputs_type ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type mediator_type ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: engine_fsm engine_fsm ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: fsm_collection fsm_collection ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: fsm_collection :: data_binder data_binder ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_conditions platform_conditions ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_math platform_math ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_math :: num_whole num_whole ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_pointer platform_pointer ;

    typedef typename fsm_collection :: template reflection < mediator_type > reflection ;

public :
    shy_data_fsm_loadable ( ) ;

    void set_mediator ( typename platform_pointer :: template pointer < mediator_type > ) ;
    void set_actions ( typename platform_pointer :: template pointer < actions_type > ) ;
    void set_inputs ( typename platform_pointer :: template pointer < inputs_type > ) ;

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
    typename platform_pointer :: template pointer < fsm_collection > _fsm_collection ;
} ;

template < typename data_fsm_loadable_types >
shy_data_fsm_loadable < data_fsm_loadable_types > :: shy_data_fsm_loadable ( )
{
    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: set_mediator ( typename platform_pointer :: template pointer < mediator_type > mediator )
{
    mediator . get ( ) . fsm_collection_obj ( _fsm_collection ) ;

    typename platform_pointer :: template pointer < data_binder > binder_ptr ;
    _fsm_collection . get ( ) . binder ( binder_ptr ) ;

    actions_type dummy_actions ;
    inputs_type dummy_inputs ;

    typename platform_pointer :: template pointer < actions_type > dummy_actions_ptr ;
    typename platform_pointer :: template pointer < inputs_type > dummy_inputs_ptr ;

    platform_pointer :: bind ( dummy_actions_ptr , dummy_actions ) ;
    platform_pointer :: bind ( dummy_inputs_ptr , dummy_inputs ) ;

    reflection :: bind ( dummy_actions_ptr , dummy_inputs_ptr , binder_ptr ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: set_actions ( typename platform_pointer :: template pointer < actions_type > )
{
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: set_inputs ( typename platform_pointer :: template pointer < inputs_type > )
{
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: is_fsm_running ( num_whole & result )
{
    result = _fsm_running ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: run_fsm_begin ( )
{
    platform_math :: make_num_whole ( _fsm_running , true ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: run_fsm_end ( )
{
    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: reset_autogenerated_input_events ( )
{
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: recalc_current_autogenerated_inputs ( )
{
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: determine_autogenerated_inputs_change ( num_whole & result )
{
    platform_math :: make_num_whole ( result , false ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: update_fixed_autogenerated_inputs ( )
{
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: tick_all_fsms ( )
{
}

