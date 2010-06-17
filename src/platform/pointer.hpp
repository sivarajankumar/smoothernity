template < typename platform_insider >
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
} ;

template < typename platform_insider >
template < typename data_type >
shy_platform_pointer < platform_insider > :: pointer < data_type > :: pointer ( )
: _data_ptr ( reinterpret_cast < data_type * > ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
template < typename data_type >
shy_platform_pointer < platform_insider > :: pointer < data_type > :: pointer ( data_type & arg_data )
: _data_ptr ( & arg_data )
{
}

template < typename platform_insider >
template < typename data_type >
data_type & shy_platform_pointer < platform_insider > :: pointer < data_type > :: get ( )
{
    return * _data_ptr ;
}

template < typename platform_insider >
template < typename data_type >
void shy_platform_pointer < platform_insider > :: pointer < data_type > :: set ( data_type & arg_data )
{
    _data_ptr = & arg_data ;
}
