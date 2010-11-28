template < typename _data_modules >
class shy_data_parser_types
{
public :
    typedef _data_modules data_modules ;
} ;

template < typename data_parser_types >
class shy_data_parser
{
    typedef typename data_parser_types :: data_modules data_modules ;
    typedef typename data_parser_types :: data_modules :: data_modules_attributes data_modules_attributes ;
    typedef typename data_parser_types :: data_modules :: data_modules_fract data_modules_fract ;
    typedef typename data_parser_types :: data_modules :: data_modules_whole data_modules_whole ;

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
        static char minus ( ) { return '-' ; }
        static std :: string next_line ( ) { return "\n" ; }
        static char underscore ( ) { return '_' ; }
    } ;

    enum _token_class_type
    {
        _token_class_none ,
        _token_class_identifier ,
        _token_class_number ,
        _token_class_divide ,
        _token_class_minus ,
        _token_class_unknown
    } ;

    enum _state_type
    {
        _state_none ,
        _state_error ,
        _state_reading_module_name ,
        _state_reading_attribute_name ,
        _state_reading_attribute_numerator_sign ,
        _state_reading_attribute_numerator_value ,
        _state_reading_attribute_denominator_sign ,
        _state_reading_attribute_denominator_value ,
        _state_determining_value_format 
    } ;

public :
    shy_data_parser ( ) ;
    void set_modules ( data_modules & ) ;
    void parse ( std :: string ) ;
    std :: string error ( ) ;

private :
    void _handle_token_class_none ( ) ;
    void _handle_token_class_identifier ( ) ;
    void _handle_token_class_number ( ) ;
    void _handle_token_class_divide ( ) ;
    void _handle_token_class_minus ( ) ;
    void _handle_token_class_unknown ( ) ;
    void _handle_state_none ( ) ;
    void _handle_state_error ( ) ;
    void _handle_state_reading_module_name ( ) ;
    void _handle_state_reading_attribute_name ( ) ;
    void _handle_state_reading_attribute_numerator_sign ( ) ;
    void _handle_state_reading_attribute_numerator_value ( ) ;
    void _handle_state_reading_attribute_denominator_sign ( ) ;
    void _handle_state_reading_attribute_denominator_value ( ) ;
    void _handle_state_determining_value_format ( ) ;
    void _store_error ( std :: string ) ;
    void _store_module_name ( std :: string ) ;
    void _store_attribute_name ( std :: string ) ;
    void _store_attribute_numerator_sign ( std :: string ) ;
    void _store_attribute_numerator_value ( std :: string ) ;
    void _store_attribute_denominator_sign ( std :: string ) ;
    void _store_attribute_denominator_value ( std :: string ) ;
    void _set_whole_value ( ) ;
    void _set_fract_value ( ) ;
    void _read_next_token ( ) ;
    void _trim_first_char ( ) ;
    void _trim_whitespaces ( ) ;
    void _append_first_char_to_token ( ) ;
    void _move_first_char_to_token ( ) ;
    char _first_char ( ) ;
    bool _any_chars_in_line ( ) ;

private :
    data_modules * _modules ;
    _state_type _state ;
    _token_class_type _token_class ;
    bool _continue_parsing ;
    bool _continue_reading_next_token ;
    std :: locale _locale ;
    std :: string _token ;
    std :: string _whole_line ;
    std :: string _remaining_line ;
    std :: string _error ;
    std :: string _module_name ;
    std :: string _attribute_name ;
    std :: string _attribute_numerator_sign ;
    std :: string _attribute_numerator_value ;
    std :: string _attribute_denominator_sign ;
    std :: string _attribute_denominator_value ;
} ;

template < typename data_parser_types >
shy_data_parser < data_parser_types > :: shy_data_parser ( )
: _modules ( 0 )
, _state ( _state_none )
, _token_class ( _token_class_none )
, _continue_parsing ( false )
, _continue_reading_next_token ( false )
{
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: set_modules ( data_modules & modules )
{
    _modules = & modules ;
}

template < typename data_parser_types >
std :: string shy_data_parser < data_parser_types > :: error ( )
{
    return _error ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: parse ( std :: string line )
{
    _whole_line = line ;
    _remaining_line = line ;
    _continue_parsing = true ;
    _read_next_token ( ) ;
    while ( _continue_parsing )
    {
        if ( _state == _state_none )
            _handle_state_none ( ) ;
        else if ( _state == _state_reading_module_name )
            _handle_state_reading_module_name ( ) ;
        else if ( _state == _state_reading_attribute_name )
            _handle_state_reading_attribute_name ( ) ;
        else if ( _state == _state_reading_attribute_numerator_sign )
            _handle_state_reading_attribute_numerator_sign ( ) ;
        else if ( _state == _state_reading_attribute_numerator_value )
            _handle_state_reading_attribute_numerator_value ( ) ;
        else if ( _state == _state_determining_value_format )
            _handle_state_determining_value_format ( ) ;
        else if ( _state == _state_reading_attribute_denominator_sign )
            _handle_state_reading_attribute_denominator_sign ( ) ;
        else if ( _state == _state_reading_attribute_denominator_value )
            _handle_state_reading_attribute_denominator_value ( ) ;
        else if ( _state == _state_error )
            _handle_state_error ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_none ( )
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

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_module_name ( )
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

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_name ( )
{
    if ( _token_class == _token_class_none )
        _continue_parsing = false ;
    else if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else if ( _token_class == _token_class_identifier )
    {
        _store_attribute_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_numerator_sign ;
    }
    else
    {
        _store_error ( _consts :: error_expected_attribute_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_numerator_sign ( )
{
    if ( _token_class == _token_class_minus )
    {
        _store_attribute_numerator_sign ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_numerator_value ;
    }
    else
    {
        _store_attribute_numerator_sign ( std :: string ( ) ) ;
        _state = _state_reading_attribute_numerator_value ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_numerator_value ( )
{
    if ( _token_class == _token_class_number )
    {
        _store_attribute_numerator_value ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_determining_value_format ;
    }
    else
    {
        _store_error ( _consts :: error_expected_numerator_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_determining_value_format ( )
{
    if ( _token_class == _token_class_divide )
    {
        _read_next_token ( ) ;
        _state = _state_reading_attribute_denominator_sign ;
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

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_denominator_sign ( )
{
    if ( _token_class == _token_class_minus )
    {
        _store_attribute_denominator_sign ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_denominator_value ;
    }
    else
    {
        _store_attribute_denominator_sign ( std :: string ( ) ) ;
        _state = _state_reading_attribute_denominator_value ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_denominator_value ( )
{
    if ( _token_class == _token_class_number )
    {
        _store_attribute_denominator_value ( _token ) ;
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

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_error ( )
{
    _continue_parsing = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _read_next_token ( )
{
    _token = std :: string ( ) ;
    _token_class = _token_class_none ;
    _trim_whitespaces ( ) ;
    _continue_reading_next_token = true ;
    while ( _any_chars_in_line ( ) && _continue_reading_next_token )
    {
        if ( _token_class == _token_class_none )
            _handle_token_class_none ( ) ;
        else if ( _token_class == _token_class_number )
            _handle_token_class_number ( ) ;
        else if ( _token_class == _token_class_identifier )
            _handle_token_class_identifier ( ) ;
        else if ( _token_class == _token_class_divide )
            _handle_token_class_divide ( ) ;
        else if ( _token_class == _token_class_minus )
            _handle_token_class_minus ( ) ;
        else
            _handle_token_class_unknown ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_none ( )
{
    if ( std :: isdigit ( _first_char ( ) , _locale ) )
        _token_class = _token_class_number ;
    else if ( std :: isalpha ( _first_char ( ) , _locale ) )
        _token_class = _token_class_identifier ;
    else if ( _first_char ( ) == _consts :: divide ( ) )
        _token_class = _token_class_divide ;
    else if ( _first_char ( ) == _consts :: minus ( ) )
        _token_class = _token_class_minus ;
    else
        _token_class = _token_class_unknown ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_number ( )
{
    if ( std :: isdigit ( _first_char ( ) , _locale ) )
        _move_first_char_to_token ( ) ;
    else
        _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_identifier ( )
{
    if ( std :: isalpha ( _first_char ( ) , _locale ) 
      || std :: isdigit ( _first_char ( ) , _locale )
      || _first_char ( ) == _consts :: underscore ( )
       )
    {
        _move_first_char_to_token ( ) ;
    }
    else
        _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_divide ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_minus ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_unknown ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _move_first_char_to_token ( )
{
    _append_first_char_to_token ( ) ;
    _trim_first_char ( ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _trim_whitespaces ( )
{
    while ( _any_chars_in_line ( ) && std :: isspace ( _first_char ( ) , _locale ) )
        _trim_first_char ( ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _trim_first_char ( )
{
    _remaining_line . erase ( _remaining_line . begin ( ) ) ;
}

template < typename data_parser_types >
char shy_data_parser < data_parser_types > :: _first_char ( )
{
    return _remaining_line . at ( 0 ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _append_first_char_to_token ( )
{
    _token += std :: string ( 1 , _first_char ( ) ) ;
}

template < typename data_parser_types >
bool shy_data_parser < data_parser_types > :: _any_chars_in_line ( )
{
    return ! _remaining_line . empty ( ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_error ( std :: string arg_error )
{
    _error = std :: string ( ) ;
    _error += arg_error ;
    _error += _consts :: next_line ( ) ;
    _error += _consts :: error_whole_line ( ) ;
    _error += _whole_line ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_module_name ( std :: string module_name )
{
    _module_name = module_name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_name ( std :: string attribute_name )
{
    _attribute_name = attribute_name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_numerator_sign ( std :: string attribute_numerator_sign )
{
    _attribute_numerator_sign = attribute_numerator_sign ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_numerator_value ( std :: string attribute_numerator_value )
{
    _attribute_numerator_value = attribute_numerator_value ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_denominator_sign ( std :: string attribute_denominator_sign )
{
    _attribute_denominator_sign = attribute_denominator_sign ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_denominator_value ( std :: string attribute_denominator_value )
{
    _attribute_denominator_value = attribute_denominator_value ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _set_whole_value ( )
{
    typename data_modules :: name_to_module_type :: iterator module_i ;
    module_i = _modules -> name_to_module . find ( _module_name ) ;
    if ( module_i == _modules -> name_to_module . end ( ) )
        _error = _consts :: error_unknown_module ( _module_name ) ;
    else
    {
        data_modules_attributes & attributes = module_i -> second ;
        typename data_modules :: name_to_whole_type :: iterator attribute_i ;
        attribute_i = attributes . name_to_whole . find ( _attribute_name ) ;
        if ( attribute_i == attributes . name_to_whole . end ( ) )
            _error = _consts :: error_unknown_whole_attribute_in_module ( _attribute_name , _module_name ) ;
        else
        {
            data_modules_whole & whole = attribute_i -> second ;
            whole . sign = _attribute_numerator_sign ;
            whole . value = _attribute_numerator_value ;
        }
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _set_fract_value ( )
{
    typename data_modules :: name_to_module_type :: iterator module_i ;
    module_i = _modules -> name_to_module . find ( _module_name ) ;
    if ( module_i == _modules -> name_to_module . end ( ) )
        _error = _consts :: error_unknown_module ( _module_name ) ;
    else
    {
        data_modules_attributes & attributes = module_i -> second ;
        typename data_modules :: name_to_fract_type :: iterator attribute_i ;
        attribute_i = attributes . name_to_fract . find ( _attribute_name ) ;
        if ( attribute_i == attributes . name_to_fract . end ( ) )
            _error = _consts :: error_unknown_fract_attribute_in_module ( _attribute_name , _module_name ) ;
        else
        {
            data_modules_fract & fract = attribute_i -> second ;
            fract . numerator_sign = _attribute_numerator_sign ;
            fract . numerator_value = _attribute_numerator_value ;
            fract . denominator_sign = _attribute_denominator_sign ;
            fract . denominator_value = _attribute_denominator_value ;
        }
    }
}

