template < typename platform >
class shy_platform_pointer
{
public :
    template < typename data_type >
    class pointer
    {
    public :
        pointer ( ) ;
        pointer ( data_type & arg_data ) ;
    public :
        data_type & get ( ) ;
        void set ( data_type & arg_data ) ;
    private :
        data_type * _data_ptr ;
    } ;
private :
    static int _uninitialized_value ( ) ;
} ;

template < typename platform >
int shy_platform_pointer < platform > :: _uninitialized_value ( )
{
    return platform :: _uninitialized_value ;
}

template < typename platform >
template < typename data_type >
shy_platform_pointer < platform > :: pointer < data_type > :: pointer ( )
: _data_ptr ( reinterpret_cast < data_type * > ( shy_platform_pointer < platform > :: _uninitialized_value ( ) ) )
{
}

template < typename platform >
template < typename data_type >
shy_platform_pointer < platform > :: pointer < data_type > :: pointer ( data_type & arg_data )
: _data_ptr ( & arg_data )
{
}

template < typename platform >
template < typename data_type >
data_type & shy_platform_pointer < platform > :: pointer < data_type > :: get ( )
{
    return * _data_ptr ;
}

template < typename platform >
template < typename data_type >
void shy_platform_pointer < platform > :: pointer < data_type > :: set ( data_type & arg_data )
{
    _data_ptr = & arg_data ;
}
