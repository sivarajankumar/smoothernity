template < typename platform >
class shy_logic_title_consts_type
{
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    shy_logic_title_consts_type ( ) ;
public :
    num_fract appear_pos_angle_periods ;
    num_fract appear_rubber_first ;
    num_fract appear_rubber_last ;
    num_whole appear_duration_in_frames ;
    
    num_fract disappear_pos_angle_periods ;
    num_fract disappear_rubber_first ;
    num_fract disappear_rubber_last ;
    num_whole disappear_duration_in_frames ;

    num_fract scene_scale_min ;
    num_fract scene_scale_max ;
    
    num_fract spin_radius_in_letters ;
    num_whole frames_between_letters ;
    num_whole never ;
} ;

template < typename platform >
class shy_logic_main_menu_letters_animation_idle_consts_type
{
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    shy_logic_main_menu_letters_animation_idle_consts_type ( ) ;
public :
    num_fract vertical_shift_period_in_seconds ;
    num_fract vertical_shift_phase_per_col ;
    num_fract vertical_shift_phase_per_row ;
    num_fract vertical_shift_amplitude ;
    num_fract horizontal_shift_period_in_seconds ;
    num_fract horizontal_shift_phase_per_row ;
    num_fract horizontal_shift_amplitude ;
} ;

template < typename context >
class shy_data_consts_reflection_registrator
{
    typename context :: platform :: platform_pointer platform_pointer ;
    typename context :: data_consts_type data_consts_type ;
    typename context :: data_consts_reflection_type data_consts_reflection_type ;
public :
    void register_reflections
        ( typename platform_pointer :: template pointer < data_consts_type > data_consts 
        , typename platform_pointer :: template pointer < data_consts_reflection_type > reflection
        )
    {
        _data_consts = data_consts ;
        _reflection = reflection ;

        _register_logic_title ( ) ;
        _register_logic_main_menu_letters_animation_idle ( ) ;
    }

    void _register_logic_title ( )
    {
        typename platform_pointer :: template pointer < typename data_consts_type :: logic_title_consts_type > consts_container ;
        consts_container = _data_consts . get ( ) . logic_title_consts ;
        reflection . get ( ) . set_consts_container ( "logic_title" ) ;
        reflection . get ( ) . set_attribute ( "appear_pos_angle_periods" , consts_container . get ( ) . appear_pos_angle_periods ) ;
        reflection . get ( ) . set_attribute ( "appear_rubber_first" , consts_container . get ( ) . appear_rubber_first ) ;
        reflection . get ( ) . set_attribute ( "appear_rubber_last" , consts_container . get ( ) . appear_rubber_last ) ;
        reflection . get ( ) . set_attribute ( "appear_duration_in_frames" , consts_container . get ( ) . appear_duration_in_frames ) ; 
        reflection . get ( ) . set_attribute ( "disappear_pos_angle_periods" , consts_container . get ( ) . disappear_pos_angle_periods ) ;
        reflection . get ( ) . set_attribute ( "disappear_rubber_first" , consts_container . get ( ) . disappear_rubber_first ) ;
        reflection . get ( ) . set_attribute ( "disappear_rubber_last" , consts_container . get ( ) . disappear_rubber_last ) ;
        reflection . get ( ) . set_attribute ( "disappear_duration_in_frames" , consts_container . get ( ) . disappear_duration_in_frames ) ;
        reflection . get ( ) . set_attribute ( "scene_scale_min" , consts_container . get ( ) . scene_scale_min ) ;
        reflection . get ( ) . set_attribute ( "scene_scale_max" , consts_container . get ( ) . scene_scale_max ) ;
        reflection . get ( ) . set_attribute ( "spin_radius_in_letters" , consts_container . get ( ) . spin_radius_in_letters ) ;
        reflection . get ( ) . set_attribute ( "frames_between_letters" , consts_container . get ( ) . frames_between_letters ) ;
        reflection . get ( ) . set_attribute ( "never" , consts_container . get ( ) . never ) ;
    }

    void _register_logic_main_menu_letters_animation_idle ( )
    {
        typename platform_pointer :: template pointer < typename data_consts_type :: logic_main_menu_letters_animation_idle_consts_type > consts_container ;
        consts_container = _data_consts . get ( ) . logic_main_menu_letters_animation_idle_consts ;
        reflection . get ( ) . set_consts_container ( "logic_main_menu_letters_animation_idle" ) ;
        reflection . get ( ) . set_attribute ( "vertical_shift_period_in_seconds" , consts_container . get ( ) . vertical_shift_period_in_seconds ) ;
        reflection . get ( ) . set_attribute ( "vertical_shift_phase_per_col" , consts_container . get ( ) . vertical_shift_phase_per_col ) ;
        reflection . get ( ) . set_attribute ( "vertical_shift_phase_per_row" , consts_container . get ( ) . vertical_shift_phase_per_row ) ;
        reflection . get ( ) . set_attribute ( "vertical_shift_amplitude" , consts_container . get ( ) . vertical_shift_amplitude ) ;
        reflection . get ( ) . set_attribute ( "horizontal_shift_period_in_seconds" , consts_container . get ( ) . horizontal_shift_period_in_seconds ) ;
        reflection . get ( ) . set_attribute ( "horizontal_shift_phase_per_row" , consts_container . get ( ) . horizontal_shift_phase_per_row ) ;
        reflection . get ( ) . set_attribute ( "horizontal_shift_amplitude" , consts_container . get ( ) . horizontal_shift_amplitude ) ;
    }

private :
    typename platform_pointer :: template pointer < data_consts_type > _data_consts ;
    typename platform_pointer :: template pointer < data_consts_reflection_type > _reflection ;
} ;

template < typename platform >
class shy_data_consts
{
    typedef platform :: platform_pointer platform_pointer ;
public :
    typename platform_pointer :: template pointer < typename shy_logic_title_consts_type < platform > > logic_title_consts ;
    typename platform_pointer :: template pointer < typename shy_logic_main_menu_letters_animation_idle_consts_type < platform > > logic_main_menu_letters_animation_idle_consts ;
} ;

template < typename platform >
class shy_data_parser
{
public :
    static const int max_string_length = 256 ;
    struct string_data
    {
    public :
        char chars [ max_string_length ] ;
    } ;
public :
    void parse_line ( string_data ) ;
} ;

