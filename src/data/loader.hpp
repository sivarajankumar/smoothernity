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
        static std :: string report_consts_in ( ) { return " consts in " ; }
        static std :: string report_indent ( ) { return "    " ; }
        static std :: string report_modules ( ) { return " modules" ; }
        static std :: string report_summary ( ) { return "summary: " ; }
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
    public :
        _reflection_parser_type ( ) ;
        void set_modules ( _reflection_modules_type & ) ;
        void parse ( std :: string ) ;
    public :
        _reflection_modules_type * _modules ;
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
{
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: set_modules ( _reflection_modules_type & modules )
{
    _modules = & modules ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: _reflection_parser_type :: parse ( std :: string line )
{
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

