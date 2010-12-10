template < typename mediator >
class shy_logic_application_fsm_autogenerated ;

template < typename mediator >
class shy_logic_application_fsm
{
    typedef typename mediator :: engine_fsm engine_fsm ;
    typedef typename mediator :: logic_application_stateless :: logic_application_stateless_consts_type logic_application_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef shy_logic_application_fsm < mediator > logic_application_fsm ;
    typedef shy_logic_application_fsm_autogenerated < logic_application_fsm > logic_application_fsm_autogenerated ;

public :
    typedef mediator mediator_type ;

    class logic_application_fsm_inputs_type
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
        num_whole stage_amusement_disabled ;
        num_whole stage_amusement_enabled ;
        num_whole stage_main_menu_disabled ;
        num_whole stage_main_menu_enabled ;
        num_whole stage_title_disabled ;
        num_whole stage_title_enabled ;
    } ;

    class logic_application_fsm_actions_type
    {
    public :
        void set_fsm ( typename platform_pointer :: template pointer < logic_application_fsm > ) ;

        void logic_amusement_creation_permit ( ) ;
        void logic_amusement_launch_permit ( ) ;
        void logic_amusement_render ( ) ;
        void logic_amusement_update ( ) ;
        void logic_game_launch_permit ( ) ;
        void logic_game_render ( ) ;
        void logic_game_update ( ) ;
        void logic_main_menu_creation_permit ( ) ;
        void logic_main_menu_launch_permit ( ) ;
        void logic_main_menu_render ( ) ;
        void logic_main_menu_update ( ) ;
        void logic_text_prepare_permit ( ) ;
        void logic_text_update ( ) ;
        void logic_title_launch_permit ( ) ;
        void logic_title_render ( ) ;
        void logic_title_update ( ) ;
    private :
        typename platform_pointer :: template pointer < logic_application_fsm > _fsm ;
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
    void _reset_input_events ( ) ;
    void _recalc_current_inputs ( ) ;
    void _determine_inputs_change ( num_whole & ) ;
    void _update_fixed_inputs ( ) ;
public :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_application_stateless_consts_type > _logic_application_stateless_consts ;

    logic_application_fsm_autogenerated _logic_application_fsm_autogenerated ;

    logic_application_fsm_actions_type _logic_application_fsm_actions ;
    logic_application_fsm_inputs_type _current_inputs ;
    logic_application_fsm_inputs_type _fixed_inputs ;
} ;

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: set_fsm ( typename platform_pointer :: template pointer < logic_application_fsm > arg_fsm )
{
    _fsm = arg_fsm ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_amusement_creation_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_amusement_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_amusement_launch_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_amusement_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_amusement_render ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_amusement_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_amusement_update ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_amusement_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_game_launch_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_game_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_game_render ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_game_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_game_update ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_game_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_creation_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_main_menu_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_launch_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_main_menu_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_render ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_main_menu_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_main_menu_update ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_main_menu_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_text_prepare_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_text_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_text_update ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_text_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_title_launch_permit ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_title_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_title_render ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_title_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: logic_application_fsm_actions_type :: logic_title_update ( )
{
    _fsm . get ( ) . _mediator . get ( ) . send ( typename messages :: logic_title_update ( ) ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . logic_application_stateless_consts ( _logic_application_stateless_consts ) ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    typename platform_pointer :: template pointer < logic_application_fsm > fsm ;
    platform_pointer :: bind ( fsm , * this ) ;
    _logic_application_fsm_actions . set_fsm ( fsm ) ;

    platform_pointer :: bind ( _logic_application_fsm_autogenerated . _logic_application_fsm_state_environment . actions , _logic_application_fsm_actions ) ;
    platform_pointer :: bind ( _logic_application_fsm_autogenerated . _logic_application_fsm_state_environment . inputs , _fixed_inputs ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_amusement_created )
{
    _current_inputs . logic_amusement_created = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_amusement_finished )
{
    _current_inputs . logic_amusement_finished = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_render )
{
    _current_inputs . logic_application_render = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_update )
{
    _current_inputs . logic_application_update = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_text_prepared )
{
    _current_inputs . logic_text_prepared = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_created )
{
    _current_inputs . logic_title_created = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_finished )
{
    _current_inputs . logic_title_finished = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_created )
{
    _current_inputs . logic_main_menu_created = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_finished )
{
    _current_inputs . logic_main_menu_finished = _platform_math_consts . get ( ) . whole_true ;
    engine_fsm :: run_fsm ( * this , _logic_application_fsm_autogenerated ) ;
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
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _determine_inputs_change ( num_whole & inputs_changed )
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
      && platform_conditions :: wholes_are_equal ( _current_inputs . stage_amusement_disabled , _fixed_inputs . stage_amusement_disabled )
      && platform_conditions :: wholes_are_equal ( _current_inputs . stage_amusement_enabled , _fixed_inputs . stage_amusement_enabled )
      && platform_conditions :: wholes_are_equal ( _current_inputs . stage_main_menu_disabled , _fixed_inputs . stage_main_menu_disabled )
      && platform_conditions :: wholes_are_equal ( _current_inputs . stage_main_menu_enabled , _fixed_inputs . stage_main_menu_enabled )
      && platform_conditions :: wholes_are_equal ( _current_inputs . stage_title_disabled , _fixed_inputs . stage_title_disabled )
      && platform_conditions :: wholes_are_equal ( _current_inputs . stage_title_enabled , _fixed_inputs . stage_title_enabled )
       )
    {
        inputs_changed = _platform_math_consts . get ( ) . whole_false ;
    }
    else
        inputs_changed = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _recalc_current_inputs ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_application_stateless_consts . get ( ) . skip_amusement ) )
    {
        _current_inputs . stage_amusement_disabled = _platform_math_consts . get ( ) . whole_true ;
        _current_inputs . stage_amusement_enabled = _platform_math_consts . get ( ) . whole_false ;
    }
    else
    {
        _current_inputs . stage_amusement_disabled = _platform_math_consts . get ( ) . whole_false ;
        _current_inputs . stage_amusement_enabled = _platform_math_consts . get ( ) . whole_true ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_application_stateless_consts . get ( ) . skip_main_menu ) )
    {
        _current_inputs . stage_main_menu_disabled = _platform_math_consts . get ( ) . whole_true ;
        _current_inputs . stage_main_menu_enabled = _platform_math_consts . get ( ) . whole_false ;
    }
    else
    {
        _current_inputs . stage_main_menu_disabled = _platform_math_consts . get ( ) . whole_false ;
        _current_inputs . stage_main_menu_enabled = _platform_math_consts . get ( ) . whole_true ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_application_stateless_consts . get ( ) . skip_title ) )
    {
        _current_inputs . stage_title_disabled = _platform_math_consts . get ( ) . whole_true ;
        _current_inputs . stage_title_enabled = _platform_math_consts . get ( ) . whole_false ;
    }
    else
    {
        _current_inputs . stage_title_disabled = _platform_math_consts . get ( ) . whole_false ;
        _current_inputs . stage_title_enabled = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _update_fixed_inputs ( )
{
    _fixed_inputs = _current_inputs ;
}

