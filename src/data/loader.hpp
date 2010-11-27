template 
    < typename _facade
    , template < typename reflection_types > class _reflection
    >
class shy_data_loader_types
{
public :
    typedef _facade facade ;
    template < typename reflection_types >
    class types
    {
    public :
        typedef _reflection < reflection_types > reflection ;
    } ;
} ;

template < typename data_loader_types >
class shy_data_loader
{
    typedef typename data_loader_types :: facade facade ;
    typedef typename data_loader_types :: facade :: mediator mediator ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math platform_math ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_pointer platform_pointer ;

    class _consts
    {
    public :
        static std :: string consts ( ) { return "consts" ; }
        static char divide ( ) { return '/' ; }
        static std :: string error_expected_attribute_name_instead_of ( std :: string token ) { return std :: string ( "expected attribute name, but got '" ) + token + std :: string ( "'" ) ; } 
        static std :: string error_expected_consts_instead_of ( std :: string token ) { return std :: string ( "expected 'consts', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_denominator_instead_of ( std :: string token ) { return std :: string ( "expected denominator, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_divide_or_identifier_instead_of ( std :: string token ) { return std :: string ( "expected '/' or identifier, but got '" ) + token + std :: string ( "'" ) ; } 
        static std :: string error_expected_module_name_instead_of ( std :: string token ) { return std :: string ( "expected module name, but got '" ) + token + std :: string ( "'" ) ; } 
        static std :: string error_expected_numerator_instead_of ( std :: string token ) { return std :: string ( "expected numerator, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_unknown_fract_attribute_in_module ( std :: string attribute , std :: string module ) { return std :: string ( "unknown fract attribute '" ) + attribute + std :: string ( "' in module '" ) + module + std :: string ( "'" ) ; }
        static std :: string error_unknown_module ( std :: string module ) { return std :: string ( "unknown module '" ) + module + std :: string ( "'" ) ; }
        static std :: string error_unknown_whole_attribute_in_module ( std :: string attribute , std :: string module ) { return std :: string ( "unknown whole attribute '" ) + attribute + std :: string ( "' in module '" ) + module + std :: string ( "'" ) ; }
        static std :: string error_whole_line ( ) { return std :: string ( "whole line: " ) ; }
        static std :: string next_line ( ) { return "\n" ; }
        static char underscore ( ) { return '_' ; }
    } ;

    class _reflection_attributes_type
    {
    public :
        typedef std :: map < std :: string , num_fract * > name_to_fract_type ;
        typedef std :: map < std :: string , num_whole * > name_to_whole_type ;
        name_to_fract_type name_to_fract ;
        name_to_whole_type name_to_whole ;
    } ;

    class _reflection_modules_type
    {
    public :
        typedef std :: map < std :: string , _reflection_attributes_type > name_to_module_type ;
        name_to_module_type name_to_module ;
    } ;

    class _reflection_binder_type
    {
    public :
        _reflection_binder_type ( ) ;
        void set_modules ( _reflection_modules_type & ) ;
        void module ( std :: string ) ;
        void bind ( std :: string , const num_fract & ) ;
        void bind ( std :: string , const num_whole & ) ;
    public :
        _reflection_modules_type * _modules ;
        _reflection_attributes_type * _current_attributes ;
    } ;

    class _reflection_parser_type
    {
        enum _token_class_type
        {
            _token_class_none ,
            _token_class_identifier ,
            _token_class_number ,
            _token_class_divide
        } ;
        enum _state_type
        {
            _state_none ,
            _state_error ,
            _state_reading_module_name ,
            _state_reading_attribute_name ,
            _state_reading_attribute_numerator ,
            _state_reading_attribute_denominator ,
            _state_determining_value_format 
        } ;
    public :
        _reflection_parser_type ( ) ;
        void set_modules ( _reflection_modules_type & ) ;
        void parse ( std :: string ) ;
        std :: string error ( ) ;
    private :
        void _store_error ( std :: string ) ;
        void _store_module_name ( std :: string ) ;
        void _store_attribute_name ( std :: string ) ;
        void _store_attribute_numerator ( std :: string ) ;
        void _store_attribute_denominator ( std :: string ) ;
        void _set_whole_value ( ) ;
        void _set_fract_value ( ) ;
        void _read_next_token ( ) ;
        void _trim_first_char ( ) ;
        char _first_char ( ) ;
        bool _any_chars_in_line ( ) ;
    public :
        _reflection_modules_type * _modules ;
        _state_type _state ;
        _token_class_type _token_class ;
        std :: string _token ;
        std :: string _whole_line ;
        std :: string _remaining_line ;
        std :: string _error ;
        std :: string _module_name ;
        std :: string _attribute_name ;
        std :: string _attribute_numerator ;
        std :: string _attribute_denominator ;
    } ;

    class _reflection_types
    {
    public :
        typedef typename data_loader_types :: facade :: mediator mediator ;
        typedef _reflection_binder_type reflection_binder ;
    } ;

public :
    shy_data_loader ( ) ;
    void bind ( facade & ) ;
    void parse ( std :: string ) ;
    std :: string error ( ) ;
private :
    _reflection_binder_type _reflection_binder ;
    _reflection_parser_type _reflection_parser ;
    _reflection_modules_type _reflection_modules ;
} ;

template < typename data_loader_types >
shy_data_loader < data_loader_types > :: _reflection_binder_type :: _reflection_binder_type ( )
: _modules ( 0 )
, _current_attributes ( 0 )
{
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_binder_type :: set_modules ( _reflection_modules_type & modules )
{
    _modules = & modules ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_binder_type :: module ( std :: string name )
{
    _modules -> name_to_module [ name ] = _reflection_attributes_type ( ) ;
    _current_attributes = & ( _modules -> name_to_module [ name ] ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_binder_type :: bind ( std :: string name , const num_fract & value )
{
    if ( _current_attributes )
        _current_attributes -> name_to_fract [ name ] = const_cast < num_fract * > ( & value ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_binder_type :: bind ( std :: string name , const num_whole & value )
{
    if ( _current_attributes )
        _current_attributes -> name_to_whole [ name ] = const_cast < num_whole * > ( & value ) ;
}

template < typename data_loader_types >
shy_data_loader < data_loader_types > :: _reflection_parser_type :: _reflection_parser_type ( )
: _modules ( 0 )
, _state ( _state_none )
, _token_class ( _token_class_none )
{
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: set_modules ( _reflection_modules_type & modules )
{
    _modules = & modules ;
}

template < typename data_loader_types >
std :: string shy_data_loader < data_loader_types > :: _reflection_parser_type :: error ( )
{
    return _error ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: parse ( std :: string line )
{
    _whole_line = line ;
    _remaining_line = line ;
    _read_next_token ( ) ;
    while ( true )
    {
        if ( _state == _state_none )
        {
            if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
            {
                _read_next_token ( ) ;
                _state = _state_reading_module_name ;
            }
            else
            {
                _store_error ( _consts :: error_expected_consts_instead_of ( _token ) ) ;
                _state = _state_error ;
            }
        }
        else if ( _state == _state_reading_module_name )
        {
            if ( _token_class == _token_class_identifier )
            {
                _store_module_name ( _token ) ;
                _read_next_token ( ) ;
                _state = _state_reading_attribute_name ;
            }
            else
            {
                _store_error ( _consts :: error_expected_module_name_instead_of ( _token ) ) ;
                _state = _state_error ;
            }
        }
        else if ( _state == _state_reading_attribute_name )
        {
            if ( _token_class == _token_class_identifier )
            {
                if ( _token == _consts :: consts ( ) ) 
                {
                    _read_next_token ( ) ;
                    _state = _state_reading_module_name ;
                }
                else
                {
                    _store_attribute_name ( _token ) ;
                    _read_next_token ( ) ;
                    _state = _state_reading_attribute_numerator ;
                }
            }
            else if ( _token_class == _token_class_none )
                break ;
            else
            {
                _store_error ( _consts :: error_expected_attribute_name_instead_of ( _token ) ) ;
                _state = _state_error ;
            }
        }
        else if ( _state == _state_reading_attribute_numerator )
        {
            if ( _token_class == _token_class_number )
            {
                _store_attribute_numerator ( _token ) ;
                _read_next_token ( ) ;
                _state = _state_determining_value_format ;
            }
            else
            {
                _store_error ( _consts :: error_expected_numerator_instead_of ( _token ) ) ;
                _state = _state_error ;
            }
        }
        else if ( _state == _state_determining_value_format )
        {
            if ( _token_class == _token_class_divide )
            {
                _read_next_token ( ) ;
                _state = _state_reading_attribute_denominator ;
            }
            else if ( _token_class == _token_class_identifier || _token_class == _token_class_none )
            {
                _set_whole_value ( ) ;
                _state = _state_reading_attribute_name ;
            }
            else
            {
                _store_error ( _consts :: error_expected_divide_or_identifier_instead_of ( _token ) ) ;
                _state = _state_error ;
            }
        }
        else if ( _state == _state_reading_attribute_denominator )
        {
            if ( _token_class == _token_class_number )
            {
                _store_attribute_denominator ( _token ) ;
                _set_fract_value ( ) ;
                _read_next_token ( ) ;
                _state = _state_reading_attribute_name ;
            }
            else
            {
                _store_error ( _consts :: error_expected_denominator_instead_of ( _token ) ) ;
                _state = _state_error ;
            }
        }
        else if ( _state == _state_error )
            break ;
    }
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _read_next_token ( )
{
    std :: locale locale ;
    _token = std :: string ( ) ;
    _token_class = _token_class_none ;
    while ( _any_chars_in_line ( ) )
    {
        if ( std :: isspace ( _first_char ( ) , locale ) )
            _trim_first_char ( ) ;
        else
            break ;
    }
    while ( _any_chars_in_line ( ) )
    {
        if ( _token_class == _token_class_none )
        {
            if ( std :: isdigit ( _first_char ( ) , locale ) )
                _token_class = _token_class_number ;
            else if ( std :: isalpha ( _first_char ( ) , locale ) )
                _token_class = _token_class_identifier ;
            else if ( _first_char ( ) == _consts :: divide ( ) )
                _token_class = _token_class_divide ;
        }
        else if ( _token_class == _token_class_number )
        {
            if ( ! std :: isdigit ( _first_char ( ) , locale ) )
                break ;
        }
        else if ( _token_class == _token_class_identifier )
        {
            if ( ! std :: isalpha ( _first_char ( ) , locale ) 
              && ! std :: isdigit ( _first_char ( ) , locale )
              && _first_char ( ) != _consts :: underscore ( )
               )
            {
                break ;
            }
        }
        else if ( _token_class == _token_class_divide )
            break ;
        _token += std :: string ( 1 , _first_char ( ) ) ;
        _trim_first_char ( ) ;
    }
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _trim_first_char ( )
{
    _remaining_line . erase ( _remaining_line . begin ( ) ) ;
}

template < typename data_loader_types >
char shy_data_loader < data_loader_types > :: _reflection_parser_type :: _first_char ( )
{
    return _remaining_line . at ( 0 ) ;
}

template < typename data_loader_types >
bool shy_data_loader < data_loader_types > :: _reflection_parser_type :: _any_chars_in_line ( )
{
    return ! _remaining_line . empty ( ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _store_error ( std :: string arg_error )
{
    _error = std :: string ( ) ;
    _error += arg_error ;
    _error += _consts :: next_line ( ) ;
    _error += _consts :: error_whole_line ( ) ;
    _error += _whole_line ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _store_module_name ( std :: string module_name )
{
    _module_name = module_name ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _store_attribute_name ( std :: string attribute_name )
{
    _attribute_name = attribute_name ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _store_attribute_numerator ( std :: string attribute_numerator )
{
    _attribute_numerator = attribute_numerator ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _store_attribute_denominator ( std :: string attribute_denominator )
{
    _attribute_denominator = attribute_denominator ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _set_whole_value ( )
{
    typename _reflection_modules_type :: name_to_module_type :: const_iterator module_i ;
    module_i = _modules -> name_to_module . find ( _module_name ) ;
    if ( module_i == _modules -> name_to_module . end ( ) )
        _error = _consts :: error_unknown_module ( _module_name ) ;
    else
    {
        const _reflection_attributes_type & attributes = module_i -> second ;
        typename _reflection_attributes_type :: name_to_whole_type :: const_iterator attribute_i ;
        attribute_i = attributes . name_to_whole . find ( _attribute_name ) ;
        if ( attribute_i == attributes . name_to_whole . end ( ) )
            _error = _consts :: error_unknown_whole_attribute_in_module ( _attribute_name , _module_name ) ;
        else
        {
            num_whole & value = * ( attribute_i -> second ) ;
            int numerator = 0 ;
            std :: istringstream ( _attribute_numerator ) >> numerator ;
            platform_math :: make_num_whole ( value , numerator ) ;
        }
    }
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: _set_fract_value ( )
{
    typename _reflection_modules_type :: name_to_module_type :: const_iterator module_i ;
    module_i = _modules -> name_to_module . find ( _module_name ) ;
    if ( module_i == _modules -> name_to_module . end ( ) )
        _error = _consts :: error_unknown_module ( _module_name ) ;
    else
    {
        const _reflection_attributes_type & attributes = module_i -> second ;
        typename _reflection_attributes_type :: name_to_fract_type :: const_iterator attribute_i ;
        attribute_i = attributes . name_to_fract . find ( _attribute_name ) ;
        if ( attribute_i == attributes . name_to_fract . end ( ) )
            _error = _consts :: error_unknown_fract_attribute_in_module ( _attribute_name , _module_name ) ;
        else
        {
            num_fract & value = * ( attribute_i -> second ) ;
            int numerator = 0 ;
            int denominator = 0 ;
            std :: istringstream ( _attribute_numerator ) >> numerator ;
            std :: istringstream ( _attribute_denominator ) >> denominator ;
            platform_math :: make_num_fract ( value , numerator , denominator ) ;
        }
    }
}

template < typename data_loader_types >
shy_data_loader < data_loader_types > :: shy_data_loader ( )
{
    _reflection_binder . set_modules ( _reflection_modules ) ;
    _reflection_parser . set_modules ( _reflection_modules ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: bind ( facade & arg_facade )
{
    typename platform_pointer :: template pointer < mediator > mediator_obj ;
    typename platform_pointer :: template pointer < _reflection_binder_type > reflection_binder_obj ;
    typename data_loader_types :: template types < _reflection_types > :: reflection reflection ;

    arg_facade . mediator_obj ( mediator_obj ) ;
    platform_pointer :: bind ( reflection_binder_obj , _reflection_binder ) ;
    reflection . bind_all ( mediator_obj , reflection_binder_obj ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: parse ( std :: string line )
{
    _reflection_parser . parse ( line ) ;
}

template < typename data_loader_types >
std :: string shy_data_loader < data_loader_types > :: error ( )
{
    return _reflection_parser . error ( ) ;
}

