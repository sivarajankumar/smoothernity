template < typename platform_insider >
class shy_platform_static_array_insider ;

template < typename platform_insider >
class shy_platform_static_array
{
    typedef typename platform_insider :: platform_math :: const_int_32 const_int_32 ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    template < typename data_type , const_int_32 size >
    class static_array
    {
        friend class shy_platform_static_array ;
        friend class shy_platform_static_array_insider < platform_insider > ;
    private :
        typedef data_type _data_type ;
        static const_int_32 _array_size = size ;
        data_type _elements [ _array_size ] ;
    } ;
public :
    template < typename array_type , typename pointer_type >
    static void element_ptr ( pointer_type & , array_type & , num_whole ) ;
} ;

template < typename platform_insider >
template < typename array_type , typename pointer_type >
inline void shy_platform_static_array < platform_insider > :: element_ptr ( pointer_type & element_ptr , array_type & array , num_whole index )
{
    int index_int = 0 ;
    platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    element_ptr = array . _elements [ index_int ] ;
}
