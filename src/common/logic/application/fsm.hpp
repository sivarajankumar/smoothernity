template < typename mediator >
class shy_logic_application_fsm
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef shy_logic_application_fsm < mediator > logic_application_fsm ;

    class _logic_application_fsm_inputs_type
    {
    public :
        num_whole logic_amusement_created ;
        num_whole logic_amusement_finished ;
        num_whole logic_application_render ;
        num_whole logic_application_update ;
        num_whole logic_text_prepared ;
        num_whole logic_title_created ;
        num_whole logic_title_finished ;
        num_whole logic_main_menu_created ;
        num_whole logic_main_menu_finished ;
        num_whole machine_amusement_generator_command_start ;
        num_whole machine_amusement_generator_state_is_finished ;
        num_whole machine_amusement_performer_command_start ;
        num_whole machine_amusement_performer_state_is_finished ;
        num_whole machine_game_performer_command_start ;
        num_whole machine_main_menu_generator_command_start ;
        num_whole machine_main_menu_generator_state_is_finished ;
        num_whole machine_main_menu_performer_command_start ;
        num_whole machine_main_menu_performer_state_is_finished ;
        num_whole machine_text_generator_command_start ;
        num_whole machine_text_generator_state_is_finished ;
        num_whole machine_title_generator_command_start ;
        num_whole machine_title_generator_state_is_finished ;
        num_whole machine_title_performer_command_start ;
        num_whole machine_title_performer_state_is_finished ;
    } ;

    class _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_exit ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ; 
    } ;

    //
    // performer
    //

    class _machine_performer_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_performer_state_title_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_performer_state_main_menu_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_performer_state_amusement_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_performer_state_game_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
    } ;

    //
    // generator
    //

    class _machine_generator_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_generator_state_text_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_generator_state_title_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_generator_state_main_menu_type
    : public _logic_application_fsm_state_type
    {
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_generator_state_amusement_type
    : public _logic_application_fsm_state_type
    {
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_generator_state_game_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // text_generator
    //

    class _machine_text_generator_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_text_generator_state_generating_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_text_generator_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // title_generator
    //

    class _machine_title_generator_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_title_generator_state_generating_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_title_generator_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // title_performer
    //

    class _machine_title_performer_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_title_performer_state_performing_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_title_performer_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // main_menu_generator
    //

    class _machine_main_menu_generator_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_main_menu_generator_state_generating_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_main_menu_generator_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // main_menu_performer
    //

    class _machine_main_menu_performer_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_main_menu_performer_state_performing_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_main_menu_performer_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // amusement_generator
    //

    class _machine_amusement_generator_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_amusement_generator_state_generating_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_amusement_generator_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // amusement_performer
    //

    class _machine_amusement_performer_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_amusement_performer_state_performing_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_amusement_performer_state_finished_type
    : public _logic_application_fsm_state_type
    {
    } ;

    //
    // game_performer
    //

    class _machine_game_performer_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_game_performer_state_performing_type
    : public _logic_application_fsm_state_type
    {
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_amusement_created ) ;
    void receive ( typename messages :: logic_amusement_finished ) ;
    void receive ( typename messages :: logic_application_render ) ;
    void receive ( typename messages :: logic_application_update ) ;
    void receive ( typename messages :: logic_text_prepared ) ;
    void receive ( typename messages :: logic_title_created ) ;
    void receive ( typename messages :: logic_title_finished ) ;
    void receive ( typename messages :: logic_main_menu_created ) ;
    void receive ( typename messages :: logic_main_menu_finished ) ;
public :
    void _machine_amusement_generator_command_start ( ) ;
    void _machine_amusement_performer_command_start ( ) ;
    void _machine_game_performer_command_start ( ) ;
    void _machine_main_menu_generator_command_start ( ) ;
    void _machine_main_menu_performer_command_start ( ) ;
    void _machine_text_generator_command_start ( ) ;
    void _machine_title_generator_command_start ( ) ;
    void _machine_title_performer_command_start ( ) ;

    void _run_fsm ( ) ;
    void _stabilize_fsm ( ) ;
    void _reset_input_events ( ) ;
    void _recalc_current_inputs ( ) ;
    void _determine_inputs_change ( ) ;
    void _update_fixed_inputs ( ) ;
    void _tick_all_fsms ( ) ;
    void _tick_single_fsm ( typename platform_pointer :: template pointer < _logic_application_fsm_state_type > & ) ;
public :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _machine_amusement_generator_state_finished_type _machine_amusement_generator_state_finished ;
    _machine_amusement_generator_state_generating_type _machine_amusement_generator_state_generating ;
    _machine_amusement_generator_state_initial_type _machine_amusement_generator_state_initial ;
    _machine_amusement_performer_state_finished_type _machine_amusement_performer_state_finished ;
    _machine_amusement_performer_state_initial_type _machine_amusement_performer_state_initial ;
    _machine_amusement_performer_state_performing_type _machine_amusement_performer_state_performing ;
    _machine_game_performer_state_initial_type _machine_game_performer_state_initial ;
    _machine_game_performer_state_performing_type _machine_game_performer_state_performing ;
    _machine_generator_state_amusement_type _machine_generator_state_amusement ;
    _machine_generator_state_game_type _machine_generator_state_game ;
    _machine_generator_state_initial_type _machine_generator_state_initial ;
    _machine_generator_state_main_menu_type _machine_generator_state_main_menu ;
    _machine_generator_state_text_type _machine_generator_state_text ;
    _machine_generator_state_title_type _machine_generator_state_title ;
    _machine_main_menu_generator_state_finished_type _machine_main_menu_generator_state_finished ;
    _machine_main_menu_generator_state_generating_type _machine_main_menu_generator_state_generating ;
    _machine_main_menu_generator_state_initial_type _machine_main_menu_generator_state_initial ;
    _machine_main_menu_performer_state_finished_type _machine_main_menu_performer_state_finished ;
    _machine_main_menu_performer_state_initial_type _machine_main_menu_performer_state_initial ;
    _machine_main_menu_performer_state_performing_type _machine_main_menu_performer_state_performing ;
    _machine_performer_state_amusement_type _machine_performer_state_amusement ;
    _machine_performer_state_game_type _machine_performer_state_game ;
    _machine_performer_state_initial_type _machine_performer_state_initial ;
    _machine_performer_state_main_menu_type _machine_performer_state_main_menu ;
    _machine_performer_state_title_type _machine_performer_state_title ;
    _machine_text_generator_state_finished_type _machine_text_generator_state_finished ;
    _machine_text_generator_state_generating_type _machine_text_generator_state_generating ;
    _machine_text_generator_state_initial_type _machine_text_generator_state_initial ;
    _machine_title_generator_state_finished_type _machine_title_generator_state_finished ;
    _machine_title_generator_state_generating_type _machine_title_generator_state_generating ;
    _machine_title_generator_state_initial_type _machine_title_generator_state_initial ;
    _machine_title_performer_state_finished_type _machine_title_performer_state_finished ;
    _machine_title_performer_state_initial_type _machine_title_performer_state_initial ;
    _machine_title_performer_state_performing_type _machine_title_performer_state_performing ;

    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_amusement_generator_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_amusement_performer_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_game_performer_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_generator_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_main_menu_generator_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_main_menu_performer_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_performer_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_text_generator_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_title_generator_state ;
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_title_performer_state ;

    num_whole _inputs_changed ;
    num_whole _fsm_running ;
    _logic_application_fsm_inputs_type _current_inputs ;
    _logic_application_fsm_inputs_type _fixed_inputs ;
} ;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_performer_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    return fsm . _machine_performer_state_title ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_performer_state_title_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_title_performer_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_performer_state_title_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_title_performer_state_is_finished ) )
        return fsm . _machine_performer_state_main_menu ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_performer_state_main_menu_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_main_menu_performer_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_performer_state_main_menu_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_main_menu_performer_state_is_finished ) )
        return fsm . _machine_performer_state_amusement ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_performer_state_amusement_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_amusement_performer_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_performer_state_amusement_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_amusement_performer_state_is_finished ) )
        return fsm . _machine_performer_state_game ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_performer_state_game_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_game_performer_command_start ( ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_generator_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    return fsm . _machine_generator_state_text ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_generator_state_text_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_text_generator_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_generator_state_text_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_text_generator_state_is_finished ) )
        return fsm . _machine_generator_state_title ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_generator_state_title_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_title_generator_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_generator_state_title_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_title_generator_state_is_finished ) )
        return fsm . _machine_generator_state_main_menu ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_generator_state_main_menu_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_main_menu_generator_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_generator_state_main_menu_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_main_menu_generator_state_is_finished ) )
        return fsm . _machine_generator_state_amusement ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_generator_state_amusement_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _machine_amusement_generator_command_start ( ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_generator_state_amusement_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_amusement_generator_state_is_finished ) )
        return fsm . _machine_generator_state_game ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_text_generator_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_text_generator_command_start ) )
        return fsm . _machine_text_generator_state_generating ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_text_generator_state_generating_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_text_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_text_generator_state_generating_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_text_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_text_generator_state_generating_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_text_prepared ) )
        return fsm . _machine_text_generator_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_title_generator_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_title_generator_command_start ) )
        return fsm . _machine_title_generator_state_generating ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_title_generator_state_generating_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_title_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_title_generator_state_generating_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_title_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_title_generator_state_generating_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_title_created ) )
        return fsm . _machine_title_generator_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_title_performer_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_title_performer_command_start ) )
        return fsm . _machine_title_performer_state_performing ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_title_performer_state_performing_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_render ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_title_render ( ) ) ;
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_title_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_title_performer_state_performing_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_title_finished ) )
        return fsm . _machine_title_performer_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_main_menu_generator_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_main_menu_generator_command_start ) )
        return fsm . _machine_main_menu_generator_state_generating ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_main_menu_generator_state_generating_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_main_menu_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_main_menu_generator_state_generating_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_main_menu_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_main_menu_generator_state_generating_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_main_menu_created ) )
        return fsm . _machine_main_menu_generator_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_main_menu_performer_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_main_menu_performer_command_start ) )
        return fsm . _machine_main_menu_performer_state_performing ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_main_menu_performer_state_performing_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_main_menu_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_main_menu_performer_state_performing_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_render ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_main_menu_render ( ) ) ;
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_main_menu_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_main_menu_performer_state_performing_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_main_menu_finished ) )
        return fsm . _machine_main_menu_performer_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_amusement_generator_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_amusement_generator_command_start ) )
        return fsm . _machine_amusement_generator_state_generating ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_amusement_generator_state_generating_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_amusement_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_amusement_generator_state_generating_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_amusement_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_amusement_generator_state_generating_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_amusement_created ) )
        return fsm . _machine_amusement_generator_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_amusement_performer_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_amusement_performer_command_start ) )
        return fsm . _machine_amusement_performer_state_performing ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_amusement_performer_state_performing_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_amusement_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_amusement_performer_state_performing_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_render ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_amusement_render ( ) ) ;
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_amusement_update ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_amusement_performer_state_performing_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_amusement_finished ) )
        return fsm . _machine_amusement_performer_state_finished ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_game_performer_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . machine_game_performer_command_start ) )
        return fsm . _machine_game_performer_state_performing ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_game_performer_state_performing_type :: on_entry ( logic_application_fsm & fsm )
{
    fsm . _mediator . get ( ) . send ( typename messages :: logic_game_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_game_performer_state_performing_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_render ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_game_render ( ) ) ;
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_game_update ( ) ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: on_entry ( logic_application_fsm & )
{
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: on_exit ( logic_application_fsm & )
{
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: on_input ( logic_application_fsm & )
{
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: transition ( logic_application_fsm & )
{
    return * this ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _inputs_changed = _platform_math_consts . get ( ) . whole_false ;
    _fsm_running = _platform_math_consts . get ( ) . whole_false ;

    platform_pointer :: bind ( _machine_amusement_generator_state , _machine_amusement_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_amusement_performer_state , _machine_amusement_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_game_performer_state , _machine_game_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_generator_state , _machine_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_main_menu_generator_state , _machine_main_menu_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_main_menu_performer_state , _machine_main_menu_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_performer_state , _machine_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_text_generator_state , _machine_text_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_title_generator_state , _machine_title_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_title_performer_state , _machine_title_performer_state_initial ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_amusement_created )
{
    _current_inputs . logic_amusement_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_amusement_finished )
{
    _current_inputs . logic_amusement_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_render )
{
    _current_inputs . logic_application_render = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_update )
{
    _current_inputs . logic_application_update = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_text_prepared )
{
    _current_inputs . logic_text_prepared = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_created )
{
    _current_inputs . logic_title_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_finished )
{
    _current_inputs . logic_title_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_created )
{
    _current_inputs . logic_main_menu_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_finished )
{
    _current_inputs . logic_main_menu_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_amusement_generator_command_start ( )
{
    _current_inputs . machine_amusement_generator_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_amusement_performer_command_start ( )
{
    _current_inputs . machine_amusement_performer_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_game_performer_command_start ( )
{
    _current_inputs . machine_game_performer_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_main_menu_generator_command_start ( )
{
    _current_inputs . machine_main_menu_generator_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_main_menu_performer_command_start ( )
{
    _current_inputs . machine_main_menu_performer_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_text_generator_command_start ( )
{
    _current_inputs . machine_text_generator_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_title_generator_command_start ( )
{
    _current_inputs . machine_title_generator_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_title_performer_command_start ( )
{
    _current_inputs . machine_title_performer_command_start = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _reset_input_events ( )
{
    _current_inputs . logic_amusement_created = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_amusement_finished = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_application_render = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_application_update = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_main_menu_created = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_main_menu_finished = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_text_prepared = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_title_created = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_title_finished = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_amusement_generator_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_amusement_performer_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_game_performer_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_main_menu_generator_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_main_menu_performer_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_text_generator_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_title_generator_command_start = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . machine_title_performer_command_start = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _determine_inputs_change ( )
{
    if ( platform_conditions :: wholes_are_equal ( _current_inputs . logic_amusement_created , _fixed_inputs . logic_amusement_created )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_amusement_finished , _fixed_inputs . logic_amusement_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_application_render , _fixed_inputs . logic_application_render )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_application_update , _fixed_inputs . logic_application_update )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_main_menu_created , _fixed_inputs . logic_main_menu_created )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_main_menu_finished , _fixed_inputs . logic_main_menu_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_text_prepared , _fixed_inputs . logic_text_prepared )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_title_created , _fixed_inputs . logic_title_created )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_title_finished , _fixed_inputs . logic_title_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_amusement_generator_command_start , _fixed_inputs . machine_amusement_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_amusement_generator_state_is_finished , _fixed_inputs . machine_amusement_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_amusement_performer_command_start , _fixed_inputs . machine_amusement_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_amusement_performer_state_is_finished , _fixed_inputs . machine_amusement_performer_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_game_performer_command_start , _fixed_inputs . machine_game_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_main_menu_generator_command_start , _fixed_inputs . machine_main_menu_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_main_menu_generator_state_is_finished , _fixed_inputs . machine_main_menu_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_main_menu_performer_command_start , _fixed_inputs . machine_main_menu_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_main_menu_performer_state_is_finished , _fixed_inputs . machine_main_menu_performer_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_text_generator_command_start , _fixed_inputs . machine_text_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_text_generator_state_is_finished , _fixed_inputs . machine_text_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_title_generator_command_start , _fixed_inputs . machine_title_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_title_generator_state_is_finished , _fixed_inputs . machine_title_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_title_performer_command_start , _fixed_inputs . machine_title_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_inputs . machine_title_performer_state_is_finished , _fixed_inputs . machine_title_performer_state_is_finished )
       )
    {
        _inputs_changed = _platform_math_consts . get ( ) . whole_false ;
    }
    else
        _inputs_changed = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _recalc_current_inputs ( )
{
    platform_pointer :: is_bound_to ( _current_inputs . machine_amusement_generator_state_is_finished , _machine_amusement_generator_state , _machine_amusement_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_inputs . machine_amusement_performer_state_is_finished , _machine_amusement_performer_state , _machine_amusement_performer_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_inputs . machine_main_menu_generator_state_is_finished , _machine_main_menu_generator_state , _machine_main_menu_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_inputs . machine_main_menu_performer_state_is_finished , _machine_main_menu_performer_state , _machine_main_menu_performer_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_inputs . machine_text_generator_state_is_finished , _machine_text_generator_state , _machine_text_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_inputs . machine_title_generator_state_is_finished , _machine_title_generator_state , _machine_title_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_inputs . machine_title_performer_state_is_finished , _machine_title_performer_state , _machine_title_performer_state_finished ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _update_fixed_inputs ( )
{
    _fixed_inputs = _current_inputs ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _run_fsm ( )
{
    if ( platform_conditions :: whole_is_false ( _fsm_running ) )
    {
        _fsm_running = _platform_math_consts . get ( ) . whole_true ;
        _stabilize_fsm ( ) ;
        _reset_input_events ( ) ;
        _stabilize_fsm ( ) ;
        _fsm_running = _platform_math_consts . get ( ) . whole_false ;
    }
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _stabilize_fsm ( )
{
    for ( ; ; )
    {
        _recalc_current_inputs ( ) ;
        _determine_inputs_change ( ) ;
        if ( platform_conditions :: whole_is_true ( _inputs_changed ) )
        {
            _update_fixed_inputs ( ) ;
            _tick_all_fsms ( ) ;
        }
        else
            break ;
    }
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _tick_all_fsms ( )
{
    _tick_single_fsm ( _machine_amusement_generator_state ) ;
    _tick_single_fsm ( _machine_amusement_performer_state ) ;
    _tick_single_fsm ( _machine_game_performer_state ) ;
    _tick_single_fsm ( _machine_generator_state ) ;
    _tick_single_fsm ( _machine_main_menu_generator_state ) ;
    _tick_single_fsm ( _machine_main_menu_performer_state ) ;
    _tick_single_fsm ( _machine_performer_state ) ;
    _tick_single_fsm ( _machine_text_generator_state ) ;
    _tick_single_fsm ( _machine_title_generator_state ) ;
    _tick_single_fsm ( _machine_title_performer_state ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _tick_single_fsm ( typename platform_pointer :: template pointer < _logic_application_fsm_state_type > & state )
{
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > next_state ;
    num_whole states_are_equal ;

    state . get ( ) . on_input ( * this ) ;
    for ( ; ; )
    {
        platform_pointer :: bind ( next_state , state . get ( ) . transition ( * this ) ) ;
        platform_pointer :: are_equal ( states_are_equal , state , next_state ) ;
        if ( platform_conditions :: whole_is_true ( states_are_equal ) )
            break ;
        else
        {
            state . get ( ) . on_exit ( * this ) ;
            state = next_state ;
            state . get ( ) . on_entry ( * this ) ;
        }
    }
}

