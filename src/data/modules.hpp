template < typename _platform >
class shy_data_modules_types
{
public :
    typedef _platform platform ;
} ;

template < typename data_modules_types >
class shy_data_modules
{
    typedef typename data_modules_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_modules_types :: platform :: platform_math :: num_whole num_whole ;

public :
    class data_modules_attributes ;
    class data_modules_fract ;
    class data_modules_fsm_action_command ;
    class data_modules_fsm_action_do ;
    class data_modules_fsm_actions ;
    class data_modules_fsm_condition_command ;
    class data_modules_fsm_condition_group ;
    class data_modules_fsm_condition_input ;
    class data_modules_fsm_condition_state ;
    class data_modules_fsm_machine ;
    class data_modules_fsm_on_input ;
    class data_modules_fsm_state ;
    class data_modules_fsm_system ;
    class data_modules_fsm_transition ;
    class data_modules_whole ;

    typedef std :: vector < data_modules_fsm_action_command > data_modules_fsm_action_command_container ;
    typedef std :: vector < data_modules_fsm_action_do > data_modules_fsm_action_do_container ;
    typedef std :: vector < data_modules_fsm_condition_command > data_modules_fsm_condition_command_container ;
    typedef std :: vector < data_modules_fsm_condition_group > data_modules_fsm_condition_group_container ;
    typedef std :: vector < data_modules_fsm_condition_input > data_modules_fsm_condition_input_container ;
    typedef std :: vector < data_modules_fsm_condition_state > data_modules_fsm_condition_state_container ;
    typedef std :: map < std :: string , data_modules_fsm_machine > data_modules_fsm_machine_container ;
    typedef std :: vector < data_modules_fsm_on_input > data_modules_fsm_on_input_container ;
    typedef std :: map < std :: string , data_modules_fsm_system > data_modules_fsm_system_container ;
    typedef std :: vector < data_modules_fsm_transition > data_modules_fsm_transition_container ;
    typedef std :: map < std :: string , data_modules_fsm_state > data_modules_fsm_state_container ;
    typedef std :: map < std :: string , data_modules_fract > name_to_fract_type ;
    typedef std :: map < std :: string , data_modules_whole > name_to_whole_type ;
    typedef std :: map < std :: string , data_modules_attributes > data_modules_attributes_container ;

    class data_modules_fract
    {
    public :
        data_modules_fract ( ) ;
    public :
        num_fract * binding ;
        std :: string numerator_sign ;
        std :: string numerator_value ;
        std :: string denominator_sign ;
        std :: string denominator_value ;
    } ;

    class data_modules_whole
    {
    public :
        data_modules_whole ( ) ;
    public :
        num_whole * binding ;
        std :: string sign ;
        std :: string value ;
    } ;

    class data_modules_attributes
    {
    public :
        name_to_fract_type name_to_fract ;
        name_to_whole_type name_to_whole ;
    } ;

    class data_modules_fsm_system
    {
    public :
        data_modules_fsm_machine_container machines ;
    } ;

    class data_modules_fsm_machine
    {
    public :
        data_modules_fsm_state_container states ;
    } ;

    class data_modules_fsm_state
    {
    public :
        data_modules_fsm_actions on_entry ;
        data_modules_fsm_actions on_exit ;
        data_modules_fsm_on_input_container on_input ;
        data_modules_fsm_transition_container transitions ;
    } ;

    class data_modules_fsm_transition
    {
    public :
        data_modules_fsm_condition_group_container condition_groups ;
        std :: string state ;
    } ;

    class data_modules_fsm_on_input
    {
    public :
        data_modules_fsm_condition_group_container condition_groups ;
        data_modules_fsm_actions actions ;
    } ;

    class data_modules_fsm_actions
    {
    public :
        data_modules_fsm_action_do_container actions ;
        data_modules_fsm_action_command_container commands ;
    } ;

    class data_modules_fsm_action_do
    {
    public :
        std :: string action ;
    } ;

    class data_modules_fsm_action_command
    {
    public :
        std :: string command ;
        std :: string machine ;
    } ;

    class data_modules_fsm_condition_group
    {
    public :
        data_modules_fsm_condition_input_container inputs ;
        data_modules_fsm_condition_state_container states ;
        data_modules_fsm_condition_command_container commands ;
    } ;

    class data_modules_fsm_condition_input
    {
    public :
        std :: string input ;
    } ;

    class data_modules_fsm_condition_state
    {
    public :
        std :: string machine ;
        std :: string state ;
    } ;

    class data_modules_fsm_condition_command
    {
    public :
        std :: string command ;
    } ;

    data_modules_attributes_container modules ;
    data_modules_fsm_system_container fsm_systems ;
} ;

template < typename data_modules_types >
shy_data_modules < data_modules_types > :: data_modules_fract :: data_modules_fract ( )
: binding ( 0 )
{
}

template < typename data_modules_types >
shy_data_modules < data_modules_types > :: data_modules_whole :: data_modules_whole ( )
: binding ( 0 )
{
}

