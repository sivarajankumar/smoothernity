template
    < typename _data_content
    , typename _platform
    >
class shy_data_assigner_types
{
public :
    typedef _data_content data_content ;
    typedef _platform platform ;
} ;

template < typename data_assigner_types >
class shy_data_assigner
{
    typedef typename data_assigner_types :: data_content data_content ;
    typedef typename data_assigner_types :: data_content :: data_content_fract data_content_fract ;
    typedef typename data_assigner_types :: data_content :: data_content_fract_container data_content_fract_container ;
    typedef typename data_assigner_types :: data_content :: data_content_fsm_machine data_content_fsm_machine ;
    typedef typename data_assigner_types :: data_content :: data_content_fsm_machine_container data_content_fsm_machine_container ;
    typedef typename data_assigner_types :: data_content :: data_content_fsm_system data_content_fsm_system ;
    typedef typename data_assigner_types :: data_content :: data_content_fsm_system_container data_content_fsm_system_container ;
    typedef typename data_assigner_types :: data_content :: data_content_module data_content_module ;
    typedef typename data_assigner_types :: data_content :: data_content_module_container data_content_module_container ;
    typedef typename data_assigner_types :: data_content :: data_content_whole data_content_whole ;
    typedef typename data_assigner_types :: data_content :: data_content_whole_container data_content_whole_container ;
    typedef typename data_assigner_types :: platform :: platform_math platform_math ;

    class _consts
    {
    public :
        static std :: string error_no_initial_state_in_machine_of_system ( std :: string fsm_machine , std :: string fsm_system ) { return std :: string ( "no state 'initial' in fsm machine '" ) + fsm_machine + std :: string ( "' of fsm system '" ) + fsm_system + std :: string ( "'" ) ; }
        static std :: string error_no_value_assigned_to_module_attribute ( std :: string module , std :: string attribute ) { return std :: string ( "no value assigned to module '" ) + module + std :: string ( "' attribute '" ) + attribute + std :: string ( "'" ) ; }
        static std :: string state_initial ( ) { return std :: string ( "initial" ) ; }
    } ;

public :
    shy_data_assigner ( ) ;
    void set_content ( data_content & ) ;
    void assign ( ) ;
    std :: string error ( ) ;
private :
    void _assign_modules ( ) ;
    void _assign_fsm_systems ( ) ;
private :
    data_content * _content ;
    std :: string _error ;
} ;

template < typename data_assigner_types >
shy_data_assigner < data_assigner_types > :: shy_data_assigner ( )
: _content ( 0 )
{
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: set_content ( data_content & content )
{
    _content = & content ;
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: assign ( )
{
    _assign_modules ( ) ;
    _assign_fsm_systems ( ) ;
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: _assign_modules ( )
{
    for ( typename data_content_module_container :: const_iterator module_i = _content -> modules . begin ( )
        ; module_i != _content -> modules . end ( )
        ; ++ module_i
        )
    {
        std :: string module_name = module_i -> first ;
        const data_content_module & module = module_i -> second ;
        for ( typename data_content_whole_container :: const_iterator whole_i = module . name_to_whole . begin ( )
            ; whole_i != module . name_to_whole . end ( )
            ; ++ whole_i
            )
        {
            std :: string whole_name = whole_i -> first ;
            const data_content_whole & whole = whole_i -> second ;
            
            std :: string string_value = whole . sign + whole . value ;
            if ( string_value . empty ( ) )
                _error = _consts :: error_no_value_assigned_to_module_attribute ( module_name , whole_name ) ;
            else
            {
                int int_value = 0 ;
                std :: istringstream ( string_value ) >> int_value ;
                platform_math :: make_num_whole ( * whole . binding , int_value ) ;
            }
        }
        for ( typename data_content_fract_container :: const_iterator fract_i = module . name_to_fract . begin ( )
            ; fract_i != module . name_to_fract . end ( )
            ; ++ fract_i
            )
        {
            std :: string fract_name = fract_i -> first ;
            const data_content_fract & fract = fract_i -> second ;
            
            std :: string string_numerator = fract . numerator_sign + fract . numerator_value ;
            std :: string string_denominator = fract . denominator_sign + fract . denominator_value ;
            if ( string_numerator . empty ( ) || string_denominator . empty ( ) )
                _error = _consts :: error_no_value_assigned_to_module_attribute ( module_name , fract_name ) ;
            else
            {
                int int_numerator = 0 ;
                int int_denominator = 0 ;
                std :: istringstream ( string_numerator ) >> int_numerator ;
                std :: istringstream ( string_denominator ) >> int_denominator ;
                platform_math :: make_num_fract ( * fract . binding , int_numerator , int_denominator ) ;
            }
        }
    }
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: _assign_fsm_systems ( )
{
    for ( typename data_content_fsm_system_container :: const_iterator fsm_system_i = _content -> fsm_systems . begin ( )
        ; fsm_system_i != _content -> fsm_systems . end ( )
        ; ++ fsm_system_i
        )
    {
        std :: string fsm_system_name = fsm_system_i -> first ;
        const data_content_fsm_system & fsm_system = fsm_system_i -> second ;
        for ( typename data_content_fsm_machine_container :: const_iterator fsm_machine_i = fsm_system . machines . begin ( )
            ; fsm_machine_i != fsm_system . machines . end ( )
            ; ++ fsm_machine_i
            )
        {
            std :: string fsm_machine_name = fsm_machine_i -> first ;
            const data_content_fsm_machine & fsm_machine = fsm_machine_i -> second ;
            if ( fsm_machine . states . find ( _consts :: state_initial ( ) ) == fsm_machine . states . end ( ) )
                _error = _consts :: error_no_initial_state_in_machine_of_system ( fsm_machine_name , fsm_system_name ) ;
        }
    }
}

template < typename data_assigner_types >
std :: string shy_data_assigner < data_assigner_types > :: error ( )
{
    return _error ;
}

