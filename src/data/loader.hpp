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
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_pointer platform_pointer ;

    class _consts
    {
    public :
        static std :: string consts ( ) { return "consts" ; }
        static char divide ( ) { return '/' ; }
        static std :: string error_expected_consts_instead_of ( std :: string token ) { return std :: string ( "expected 'consts', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_whole_line ( ) { return std :: string ( "whole line: " ) ; }
        static std :: string next_line ( ) { return "\n" ; }
        static std :: string report_consts_in ( ) { return " consts in " ; }
        static std :: string report_indent ( ) { return "    " ; }
        static std :: string report_modules ( ) { return " modules" ; }
        static std :: string report_summary ( ) { return "summary: " ; }
        static char underscore ( ) { return '_' ; }
        static std :: string whitespace ( ) { return " " ; }
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
            _state_reading_attribute_denominator
        } ;
    public :
        _reflection_parser_type ( ) ;
        void set_modules ( _reflection_modules_type & ) ;
        void parse ( std :: string ) ;
        std :: string error ( ) ;
    private :
        void _store_error ( std :: string ) ;
        void _read_next_token ( ) ;
        void _trim_first_char ( ) ;
        char _first_char ( ) ;
        bool _any_chars_in_line ( ) ;
    public :
        _reflection_modules_type * _modules ;
        _state_type _state ;
        _token_class_type _token_class ;
        std :: string _token ;
        std :: string _error ;
        std :: string _whole_line ;
        std :: string _remaining_line ;
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
    void _report ( ) ;
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
    do
    {
        _read_next_token ( ) ;
        if ( _state == _state_none )
        {
            if ( _token_class == _token_class_identifier )
            {
                if ( _token == _consts :: consts ( ) )
                    _state = _state_reading_module_name ;
                else
                {
                    _store_error ( _consts :: error_expected_consts_instead_of ( _token ) ) ;
                    _state = _state_error ;
                }
            }
        }
    }
    while ( _token_class != _token_class_none ) ;
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
    _report ( ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _report ( )
{
    int modules = 0 ;
    int attrs = 0 ;
    for ( typename _reflection_modules_type :: name_to_module_type :: const_iterator module_i = _reflection_modules . name_to_module . begin ( )
        ; module_i != _reflection_modules . name_to_module . end ( )
        ; ++ module_i
        )
    {
        std :: string module_name = module_i -> first ;
        const _reflection_attributes_type & attributes = module_i -> second ;

        ++ modules ;
        std :: cout << std :: endl ;
        std :: cout << _consts :: consts ( ) << _consts :: whitespace ( ) << std :: string ( module_name ) << std :: endl ;

        for ( typename _reflection_attributes_type :: name_to_fract_type :: const_iterator fract_i = attributes . name_to_fract . begin ( )
            ; fract_i != attributes . name_to_fract . end ( )
            ; ++ fract_i
            )
        {
            ++ attrs ;
            std :: string fract_name = fract_i -> first ;
            std :: cout << _consts :: report_indent ( ) << std :: string ( fract_name ) << std :: endl ;
        }

        for ( typename _reflection_attributes_type :: name_to_whole_type :: const_iterator whole_i = attributes . name_to_whole . begin ( )
            ; whole_i != attributes . name_to_whole . end ( )
            ; ++ whole_i
            )
        {
            ++ attrs ;
            std :: string whole_name = whole_i -> first ;
            std :: cout << _consts :: report_indent ( ) << std :: string ( whole_name ) << std :: endl ;
        }
    }
    std :: cout << std :: endl ;
    std :: cout << _consts :: report_summary ( ) << attrs << _consts :: report_consts_in ( ) << modules << _consts :: report_modules ( ) << std :: endl ;
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

