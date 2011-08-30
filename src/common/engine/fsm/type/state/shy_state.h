class shy_common_engine_fsm_state_type
{
public :
    virtual ~ shy_common_engine_fsm_state_type ( ) ;
    virtual void on_entry ( ) ;
    virtual void on_exit ( ) ;
    virtual void on_input ( ) ;
    virtual shy_common_engine_fsm_state_type & transition ( ) ;
} ;
