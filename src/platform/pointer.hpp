template < typename platform_insider >
class shy_platform_pointer
{
public :
    template < typename data_type >
    class pointer
    {
        friend class shy_platform_pointer ;
        typedef data_type _data_type ;
    public :
        pointer ( ) ;
    public :
        data_type & get ( ) const ;
    private :
        data_type * _data_ptr ;
    } ;
    
    template < typename pointer_type >
    static void bind ( pointer_type & ptr , typename pointer_type :: _data_type & data ) ;
} ;

template < typename platform_insider >
template < typename data_type >
shy_platform_pointer < platform_insider > :: pointer < data_type > :: pointer ( )
: _data_ptr ( reinterpret_cast < data_type * > ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
template < typename data_type >
data_type & shy_platform_pointer < platform_insider > :: pointer < data_type > :: get ( ) const
{
    return * _data_ptr ;
}

template < typename platform_insider >
template < typename pointer_type >
void shy_platform_pointer < platform_insider > :: bind ( pointer_type & ptr , typename pointer_type :: _data_type & data )
{
    ptr . _data_ptr = & data ;
}
