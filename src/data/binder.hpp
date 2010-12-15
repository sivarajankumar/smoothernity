template 
    < typename _data_content
    , typename _platform
    >
class shy_data_binder_types
{
public :
    typedef _data_content data_content ;
    typedef _platform platform ;
} ;

template < typename data_binder_types >
class shy_data_binder
{
    typedef typename data_binder_types :: data_content data_content ;
    typedef typename data_binder_types :: data_content :: data_content_fract data_content_fract ;
    typedef typename data_binder_types :: data_content :: data_content_module data_content_module ;
    typedef typename data_binder_types :: data_content :: data_content_whole data_content_whole ;
    typedef typename data_binder_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_binder_types :: platform :: platform_math :: num_whole num_whole ;
public :
    shy_data_binder ( ) ;
    void set_content ( data_content & ) ;
    void module ( std :: string ) ;
    void bind ( std :: string , const num_fract & ) ;
    void bind ( std :: string , const num_whole & ) ;
public :
    data_content * _content ;
    data_content_module * _current_module ;
} ;

template < typename data_binder_types >
shy_data_binder < data_binder_types > :: shy_data_binder ( )
: _content ( 0 )
, _current_module ( 0 )
{
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: set_content ( data_content & content )
{
    _content = & content ;
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: module ( std :: string name )
{
    _content -> modules [ name ] = data_content_module ( ) ;
    _current_module = & ( _content -> modules [ name ] ) ;
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: bind ( std :: string name , const num_fract & value )
{
    if ( _current_module )
    {
        _current_module -> name_to_fract [ name ] = data_content_fract ( ) ;
        _current_module -> name_to_fract [ name ] . binding = const_cast < num_fract * > ( & value ) ;
    }
}

template < typename data_binder_types >
void shy_data_binder < data_binder_types > :: bind ( std :: string name , const num_whole & value )
{
    if ( _current_module )
    {
        _current_module -> name_to_whole [ name ] = data_content_whole ( ) ;
        _current_module -> name_to_whole [ name ] . binding = const_cast < num_whole * > ( & value ) ;
    }
}

