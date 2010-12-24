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
    class _state_type ;
    class _state_action_command_type ;
    class _state_condition_command_type ;
    class _state_condition_group_type ;
    class _state_condition_input_type ;
    class _state_condition_state_type ;
    class _state_on_input_type ;

    typedef typename data_fsm_loadable_types :: logic_fsm logic_fsm ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: actions_type actions_type ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: inputs_type inputs_type ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type mediator_type ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: engine_fsm engine_fsm ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: fsm_collection fsm_collection ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: fsm_collection :: data_binder data_binder ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: fsm_collection :: data_content data_content ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_conditions platform_conditions ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_math platform_math ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_math :: num_whole num_whole ;
    typedef typename data_fsm_loadable_types :: logic_fsm :: mediator_type :: platform :: platform_pointer platform_pointer ;

    typedef typename data_content :: data_content_fsm_action_do_container data_content_fsm_action_do_container ;
    typedef typename data_content :: data_content_fsm_actions data_content_fsm_actions ;
    typedef typename data_content :: data_content_fsm_condition_group data_content_fsm_condition_group ;
    typedef typename data_content :: data_content_fsm_condition_group_container data_content_fsm_condition_group_container ;
    typedef typename data_content :: data_content_fsm_condition_input data_content_fsm_condition_input ;
    typedef typename data_content :: data_content_fsm_condition_input_container data_content_fsm_condition_input_container ;
    typedef typename data_content :: data_content_fsm_machine_container data_content_fsm_machine_container ;
    typedef typename data_content :: data_content_fsm_machine data_content_fsm_machine ;
    typedef typename data_content :: data_content_fsm_on_input_container data_content_fsm_on_input_container ;
    typedef typename data_content :: data_content_fsm_state_container data_content_fsm_state_container ;
    typedef typename data_content :: data_content_fsm_state data_content_fsm_state ;
    typedef typename data_content :: data_content_fsm_system data_content_fsm_system ;

    typedef typename fsm_collection :: template reflection < mediator_type > reflection ;
    typedef shy_data_fsm_loadable < data_fsm_loadable_types > data_fsm_loadable ;

    typedef void ( actions_type :: * _action_binding_type ) ( ) ;

    typedef typename std :: map < std :: string , _action_binding_type > _action_binding_container_type ;
    typedef typename std :: map < std :: string , num_whole * > _input_binding_container_type ;
    typedef typename std :: map < std :: string , _state_type * > _machine_state_current_container_type ;
    typedef typename std :: map < std :: string , _state_type > _state_container_type ;
    typedef typename std :: map < std :: string , _state_container_type > _machine_states_container_type ;
    typedef typename std :: vector < _action_binding_type > _state_action_do_container_type ;
    typedef typename std :: vector < _state_action_command_type > _state_action_command_container_type ;
    typedef typename std :: vector < _state_condition_command_type > _state_condition_command_container_type ;
    typedef typename std :: vector < _state_condition_group_type > _state_condition_group_container_type ;
    typedef typename std :: vector < _state_condition_input_type > _state_condition_input_container_type ;
    typedef typename std :: vector < _state_condition_state_type > _state_condition_state_container_type ;
    typedef typename std :: vector < _state_on_input_type > _state_on_input_container_type ;

    class _consts
    {
    public :
        static std :: string state_initial ( ) { return "initial" ; }
    } ;

    class _loadable_inputs_type
    {
    } ;

    class _state_environment_type
    {
    } ;

    class _state_action_command_type
    {
    } ;

    class _state_actions_type
    {
    public :
        _state_action_do_container_type actions ;
        _state_action_command_container_type commands ;
    } ;

    class _state_condition_input_type
    {
    public :
        _state_condition_input_type ( ) ;
    public :
        num_whole * binding ;
    } ;

    class _state_condition_state_type
    {
    } ;

    class _state_condition_command_type
    {
    } ;

    class _state_condition_group_type
    {
    public :
        _state_condition_input_container_type inputs ;
        _state_condition_state_container_type states ;
        _state_condition_command_container_type commands ;
    } ;

    class _state_on_input_type
    {
    public :
        _state_condition_group_container_type condition_groups ;
        _state_actions_type actions ;
    } ;

    class _state_type
    : public engine_fsm :: template fsm_state_type < _state_environment_type >
    {
    public :
        _state_type ( ) ;
        virtual ~ _state_type ( ) ;

        virtual void on_entry ( _state_environment_type & ) ;
        virtual void on_exit ( _state_environment_type & ) ;
        virtual void on_input ( _state_environment_type & ) ;
        virtual _state_type & transition ( _state_environment_type & ) ;

        void set_fsm ( data_fsm_loadable & ) ;
        void set_machine_name ( std :: string ) ;
        void load_from ( const data_content_fsm_state & ) ;
    private :
        void _load_actions ( _state_actions_type & , const data_content_fsm_actions & ) ;
        void _load_condition_groups ( _state_condition_group_container_type & , const data_content_fsm_condition_group_container & ) ;
        void _perform_actions ( _state_actions_type & ) ;
    private :
        data_fsm_loadable * _fsm ;
        _state_actions_type _on_entry ;
        _state_actions_type _on_exit ;
        _state_on_input_container_type _on_input ;
        std :: string _machine_name ;
    } ;

public :
    shy_data_fsm_loadable ( ) ;

    void set_mediator ( typename platform_pointer :: template pointer < mediator_type > ) ;
    void set_actions ( typename platform_pointer :: template pointer < actions_type > ) ;
    void set_inputs ( typename platform_pointer :: template pointer < inputs_type > ) ;

    void init ( ) ;
    void is_fsm_running ( num_whole & ) ;
    void run_fsm_begin ( ) ;
    void run_fsm_end ( ) ;
    void reset_autogenerated_input_events ( ) ;
    void recalc_current_autogenerated_inputs ( ) ;
    void determine_autogenerated_inputs_change ( num_whole & ) ;
    void update_fixed_autogenerated_inputs ( ) ;
    void tick_all_fsms ( ) ;

    void bind_fsm_system ( std :: string ) ;
    void bind_fsm_input ( std :: string , num_whole & ) ;
    void bind_fsm_action ( std :: string , _action_binding_type ) ;
private :
    num_whole _fsm_running ;
    typename platform_pointer :: template pointer < fsm_collection > _fsm_collection ;
    typename platform_pointer :: template pointer < actions_type > _actions ;
    typename platform_pointer :: template pointer < inputs_type > _inputs ;
    typename platform_pointer :: template pointer < data_binder > _binder ;
    typename platform_pointer :: template pointer < data_content > _content ;

    std :: string _fsm_system_name ;
    _input_binding_container_type _inputs_binding ;
    _action_binding_container_type _actions_binding ;
    _machine_state_current_container_type _machine_state_current ;
    _machine_states_container_type _machine_states ;
    _loadable_inputs_type _fixed_loadable_inputs ;
    _loadable_inputs_type _current_loadable_inputs ;
} ;

template < typename data_fsm_loadable_types >
shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_condition_input_type :: _state_condition_input_type ( )
: binding ( 0 )
{
}

template < typename data_fsm_loadable_types >
shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: _state_type ( )
: _fsm ( 0 )
{
}

template < typename data_fsm_loadable_types >
shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: ~ _state_type ( )
{
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: set_fsm ( data_fsm_loadable & fsm )
{
    _fsm = & fsm ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: set_machine_name ( std :: string name )
{
    _machine_name = name ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: load_from ( const data_content_fsm_state & fsm_state )
{
    _load_actions ( _on_entry , fsm_state . on_entry ) ;
    _load_actions ( _on_exit , fsm_state . on_exit ) ;
    for ( typename data_content_fsm_on_input_container :: const_iterator on_input_i = fsm_state . on_input . begin ( )
        ; on_input_i != fsm_state . on_input . end ( )
        ; ++ on_input_i
        )
    {
        _state_on_input_type state_on_input ;
        _load_actions ( state_on_input . actions , on_input_i -> actions ) ;
        _load_condition_groups ( state_on_input . condition_groups , on_input_i -> condition_groups ) ;
        _on_input . push_back ( state_on_input ) ;
    }
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: _load_actions 
    ( _state_actions_type & actions_to 
    , const data_content_fsm_actions & actions_from
    )
{
    for ( typename data_content_fsm_action_do_container :: const_iterator action_i = actions_from . actions . begin ( )
        ; action_i != actions_from . actions . end ( )
        ; ++ action_i
        )
    {
        std :: string action_name = action_i -> action ;
        actions_to . actions . push_back ( _fsm -> _actions_binding [ action_name ] ) ;
    }
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: _load_condition_groups
    ( _state_condition_group_container_type & condition_groups_to
    , const data_content_fsm_condition_group_container & condition_groups_from
    )
{
    for ( typename data_content_fsm_condition_group_container :: const_iterator condition_group_i = condition_groups_from . begin ( )
        ; condition_group_i != condition_groups_from . end ( )
        ; ++ condition_group_i
        )
    {
        const data_content_fsm_condition_group & data_condition_group = * condition_group_i ;
        _state_condition_group_type condition_group ;
        for ( typename data_content_fsm_condition_input_container :: const_iterator condition_input_i = data_condition_group . inputs . begin ( )
            ; condition_input_i != data_condition_group . inputs . end ( )
            ; ++ condition_input_i
            )
        {
            const data_content_fsm_condition_input & data_condition_input = * condition_input_i ;
            _state_condition_input_type condition_input ;
            std :: string input_name = data_condition_input . input ;
            condition_input . binding = _fsm -> _inputs_binding [ input_name ] ;
            condition_group . inputs . push_back ( condition_input ) ;
        }
        condition_groups_to . push_back ( condition_group ) ;
    }
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: _perform_actions ( _state_actions_type & actions )
{
    for ( typename _state_action_do_container_type :: const_iterator action_i = actions . actions . begin ( )
        ; action_i != actions . actions . end ( )
        ; ++ action_i
        )
    {
        _action_binding_type binding = * action_i ;
        ( _fsm -> _actions . get ( ) .* binding ) ( ) ;
    }
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: on_entry ( _state_environment_type & )
{
    _perform_actions ( _on_entry ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: on_exit ( _state_environment_type & )
{
    _perform_actions ( _on_exit ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: on_input ( _state_environment_type & )
{
}

template < typename data_fsm_loadable_types >
typename shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type &
shy_data_fsm_loadable < data_fsm_loadable_types > :: _state_type :: transition ( _state_environment_type & )
{
    return * this ;
}

template < typename data_fsm_loadable_types >
shy_data_fsm_loadable < data_fsm_loadable_types > :: shy_data_fsm_loadable ( )
{
    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: set_mediator ( typename platform_pointer :: template pointer < mediator_type > mediator )
{
    mediator . get ( ) . fsm_collection_obj ( _fsm_collection ) ;

    _fsm_collection . get ( ) . binder ( _binder ) ;
    _fsm_collection . get ( ) . content ( _content ) ;

    typename platform_pointer :: template pointer < data_fsm_loadable > this_ptr ;
    platform_pointer :: bind ( this_ptr , * this ) ;

    reflection :: bind ( _actions , _inputs , this_ptr ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: set_actions ( typename platform_pointer :: template pointer < actions_type > actions )
{
    _actions = actions ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: set_inputs ( typename platform_pointer :: template pointer < inputs_type > inputs )
{
    _inputs = inputs ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: init ( )
{
    data_content_fsm_system & fsm_system = _content . get ( ) . fsm_systems [ _fsm_system_name ] ;
    for ( typename data_content_fsm_machine_container :: const_iterator fsm_machine_i = fsm_system . machines . begin ( )
        ; fsm_machine_i != fsm_system . machines . end ( )
        ; ++ fsm_machine_i
        )
    {
        std :: string fsm_machine_name = fsm_machine_i -> first ;
        const data_content_fsm_machine & fsm_machine = fsm_machine_i -> second ;
        _state_container_type states ;
        for ( typename data_content_fsm_state_container :: const_iterator fsm_state_i = fsm_machine . states . begin ( )
            ; fsm_state_i != fsm_machine . states . end ( )
            ; ++ fsm_state_i
            )
        {
            std :: string fsm_state_name = fsm_state_i -> first ;
            const data_content_fsm_state & fsm_state = fsm_state_i -> second ;
            _state_type state ;
            state . set_fsm ( * this ) ;
            state . set_machine_name ( fsm_machine_name ) ;
            state . load_from ( fsm_state ) ;
            states [ fsm_state_name ] = _state_type ( ) ;
        }
        _machine_states [ fsm_machine_name ] = states ;
    }
    for ( typename data_content_fsm_machine_container :: const_iterator fsm_machine_i = fsm_system . machines . begin ( )
        ; fsm_machine_i != fsm_system . machines . end ( )
        ; ++ fsm_machine_i
        )
    {
        std :: string fsm_machine_name = fsm_machine_i -> first ;
        _machine_state_current [ fsm_machine_name ] = & _machine_states [ fsm_machine_name ] [ _consts :: state_initial ( ) ] ;
    }
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: bind_fsm_system ( std :: string name )
{
    _fsm_system_name = name ;
    _binder . get ( ) . bind_fsm_system ( name ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: bind_fsm_input ( std :: string name , num_whole & input )
{
    _inputs_binding [ name ] = & input ;
    _binder . get ( ) . bind_fsm_input ( name ) ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: bind_fsm_action ( std :: string name , _action_binding_type action )
{
    _actions_binding [ name ] = action ;
    _binder . get ( ) . bind_fsm_action ( name ) ;
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
    _fixed_loadable_inputs = _current_loadable_inputs ;
}

template < typename data_fsm_loadable_types >
void shy_data_fsm_loadable < data_fsm_loadable_types > :: tick_all_fsms ( )
{
}

