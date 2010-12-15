template 
    < typename _data_modules
    , typename _platform
    >
class shy_data_binder_types
{
public :
    typedef _data_modules data_modules ;
    typedef _platform platform ;
} ;

template < typename data_binder_types >
class shy_data_binder
{
    typedef typename data_binder_types :: data_modules data_modules ;
    typedef typename data_binder_types :: data_modules :: data_modules_attributes data_modules_attributes ;
    typedef typename data_binder_types :: data_modules :: data_modules_fract data_modules_fract ;
    typedef typename data_binder_types :: data_modules :: data_modules_whole data_modules_whole ;
    typedef typename data_binder_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_binder_types :: platform :: platform_math :: num_whole num_whole ;
public :
    shy_data_binder ( ) ;
    void set_modules ( data_modules & ) ;
    void module ( std :: string ) ;
    void bind ( std :: string , const num_fract & ) ;
    void bind ( std :: string , const num_whole & ) ;
public :
    data_modules * _modules ;
    data_modules_attributes * _current_attributes ;
} ;

template < typename data_binder_types >
shy_data_binder < data_binder_types > :: shy_data_binder ( )
: _modules ( 0 )
, _current_attributes ( 0 )
{
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: set_modules ( data_modules & modules )
{
    _modules = & modules ;
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: module ( std :: string name )
{
    _modules -> modules [ name ] = data_modules_attributes ( ) ;
    _current_attributes = & ( _modules -> modules [ name ] ) ;
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: bind ( std :: string name , const num_fract & value )
{
    if ( _current_attributes )
    {
        _current_attributes -> name_to_fract [ name ] = data_modules_fract ( ) ;
        _current_attributes -> name_to_fract [ name ] . binding = const_cast < num_fract * > ( & value ) ;
    }
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: bind ( std :: string name , const num_whole & value )
{
    if ( _current_attributes )
    {
        _current_attributes -> name_to_whole [ name ] = data_modules_whole ( ) ;
        _current_attributes -> name_to_whole [ name ] . binding = const_cast < num_whole * > ( & value ) ;
    }
}

