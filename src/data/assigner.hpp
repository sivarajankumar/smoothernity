template
    < typename _data_modules
    , typename _platform
    >
class shy_data_assigner_types
{
public :
    typedef _data_modules data_modules ;
    typedef _platform platform ;
} ;

template < typename data_assigner_types >
class shy_data_assigner
{
    typedef typename data_assigner_types :: data_modules data_modules ;
public :
    shy_data_assigner ( ) ;
    void set_modules ( data_modules & ) ;
    void assign ( ) ;
    std :: string error ( ) ;
private :
    data_modules * _modules ;
    std :: string _error ;
} ;

template < typename data_assigner_types >
shy_data_assigner < data_assigner_types > :: shy_data_assigner ( )
: _modules ( 0 )
{
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: set_modules ( data_modules & modules )
{
    _modules = & modules ;
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: assign ( )
{
}

template < typename data_assigner_types >
std :: string shy_data_assigner < data_assigner_types > :: error ( )
{
    return _error ;
}

