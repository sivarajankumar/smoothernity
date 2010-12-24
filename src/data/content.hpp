template < typename _platform >
class shy_data_content_types
{
public :
    typedef _platform platform ;
} ;

template < typename data_content_types >
class shy_data_content
{
    typedef typename data_content_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_content_types :: platform :: platform_math :: num_whole num_whole ;

public :
    class data_content_fract ;
    class data_content_fsm_action_binding ;
    class data_content_fsm_action_command ;
    class data_content_fsm_action_do ;
    class data_content_fsm_actions ;
    class data_content_fsm_condition_command ;
    class data_content_fsm_condition_group ;
    class data_content_fsm_condition_input ;
    class data_content_fsm_condition_state ;
    class data_content_fsm_input_binding ;
    class data_content_fsm_machine ;
    class data_content_fsm_on_input ;
    class data_content_fsm_state ;
    class data_content_fsm_system ;
    class data_content_fsm_transition ;
    class data_content_module ;
    class data_content_whole ;

    typedef std :: map < std :: string , data_content_fract > data_content_fract_container ;
    typedef std :: set < std :: string > data_content_fsm_action_binding_container ;
    typedef std :: vector < data_content_fsm_action_command > data_content_fsm_action_command_container ;
    typedef std :: vector < data_content_fsm_action_do > data_content_fsm_action_do_container ;
    typedef std :: vector < data_content_fsm_condition_command > data_content_fsm_condition_command_container ;
    typedef std :: vector < data_content_fsm_condition_group > data_content_fsm_condition_group_container ;
    typedef std :: vector < data_content_fsm_condition_input > data_content_fsm_condition_input_container ;
    typedef std :: vector < data_content_fsm_condition_state > data_content_fsm_condition_state_container ;
    typedef std :: map < std :: string , data_content_fsm_machine > data_content_fsm_machine_container ;
    typedef std :: vector < data_content_fsm_on_input > data_content_fsm_on_input_container ;
    typedef std :: set < std :: string > data_content_fsm_input_binding_container ;
    typedef std :: map < std :: string , data_content_fsm_system > data_content_fsm_system_container ;
    typedef std :: vector < data_content_fsm_transition > data_content_fsm_transition_container ;
    typedef std :: map < std :: string , data_content_fsm_state > data_content_fsm_state_container ;
    typedef std :: map < std :: string , data_content_module > data_content_module_container ;
    typedef std :: map < std :: string , data_content_whole > data_content_whole_container ;

    class data_content_fract
    {
    public :
        data_content_fract ( ) ;
    public :
        num_fract * binding ;
        std :: string numerator_sign ;
        std :: string numerator_value ;
        std :: string denominator_sign ;
        std :: string denominator_value ;
    } ;

    class data_content_whole
    {
    public :
        data_content_whole ( ) ;
    public :
        num_whole * binding ;
        std :: string sign ;
        std :: string value ;
    } ;

    class data_content_module
    {
    public :
        data_content_fract_container name_to_fract ;
        data_content_whole_container name_to_whole ;
    } ;

    class data_content_fsm_system
    {
    public :
        data_content_fsm_machine_container machines ;
        data_content_fsm_input_binding_container inputs ;
        data_content_fsm_action_binding_container actions ;
    } ;

    class data_content_fsm_machine
    {
    public :
        data_content_fsm_state_container states ;
    } ;

    class data_content_fsm_state
    {
    public :
        data_content_fsm_actions on_entry ;
        data_content_fsm_actions on_exit ;
        data_content_fsm_on_input_container on_input ;
        data_content_fsm_transition_container transitions ;
    } ;

    class data_content_fsm_transition
    {
    public :
        data_content_fsm_condition_group_container condition_groups ;
        std :: string state ;
    } ;

    class data_content_fsm_on_input
    {
    public :
        data_content_fsm_condition_group_container condition_groups ;
        data_content_fsm_actions actions ;
    } ;

    class data_content_fsm_actions
    {
    public :
        data_content_fsm_action_do_container actions ;
        data_content_fsm_action_command_container commands ;
    } ;

    class data_content_fsm_action_do
    {
    public :
        std :: string action ;
    } ;

    class data_content_fsm_action_command
    {
    public :
        std :: string command ;
        std :: string machine ;
    } ;

    class data_content_fsm_condition_group
    {
    public :
        data_content_fsm_condition_input_container inputs ;
        data_content_fsm_condition_state_container states ;
        data_content_fsm_condition_command_container commands ;
    } ;

    class data_content_fsm_condition_input
    {
    public :
        std :: string input ;
    } ;

    class data_content_fsm_condition_state
    {
    public :
        std :: string machine ;
        std :: string state ;
    } ;

    class data_content_fsm_condition_command
    {
    public :
        std :: string command ;
    } ;

    data_content_module_container modules ;
    data_content_fsm_system_container fsm_systems ;
} ;

template < typename data_content_types >
shy_data_content < data_content_types > :: data_content_fract :: data_content_fract ( )
: binding ( 0 )
{
}

template < typename data_content_types >
shy_data_content < data_content_types > :: data_content_whole :: data_content_whole ( )
: binding ( 0 )
{
}

