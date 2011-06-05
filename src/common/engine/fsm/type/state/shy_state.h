class shy_type_common_engine_fsm_state
{
public :
    virtual ~ shy_type_common_engine_fsm_state ( ) ;
    virtual void on_entry ( ) ;
    virtual void on_exit ( ) ;
    virtual void on_input ( ) ;
    virtual shy_type_common_engine_fsm_state & transition ( ) ;
} ;
