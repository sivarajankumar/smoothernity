#ifndef _shy_platform_pointer_included
#define _shy_platform_pointer_included

class shy_platform_pointer
{
    typedef typename so_called_platform_math :: num_whole num_whole ;
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

    template < typename pointer_type >
    static void are_equal ( num_whole & , pointer_type , pointer_type ) ;

    template < typename pointer_type >
    static void is_bound_to ( num_whole & , pointer_type , typename pointer_type :: _data_type & data ) ;
} ;

template < typename data_type >
shy_platform_pointer :: pointer < data_type > :: pointer ( )
: _data_ptr ( reinterpret_cast < data_type * > ( so_called_platform_consts_insider :: uninitialized_value ) )
{
}

template < typename data_type >
data_type & shy_platform_pointer :: pointer < data_type > :: get ( ) const
{
    return * _data_ptr ;
}

template < typename pointer_type >
void shy_platform_pointer :: bind ( pointer_type & ptr , typename pointer_type :: _data_type & data )
{
    ptr . _data_ptr = & data ;
}

template < typename pointer_type >
void shy_platform_pointer :: are_equal ( num_whole & result , pointer_type pointer1 , pointer_type pointer2 )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , pointer1 . _data_ptr == pointer2 . _data_ptr ) ;
}

template < typename pointer_type >
void shy_platform_pointer :: is_bound_to ( num_whole & result , pointer_type pointer , typename pointer_type :: _data_type & data )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , pointer . _data_ptr == & data ) ;
}

#endif
