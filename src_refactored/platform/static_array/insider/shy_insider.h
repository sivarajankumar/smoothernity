#ifndef _shy_platform_static_array_insider_included
#define _shy_platform_static_array_insider_included

class shy_platform_static_array_insider
{
public :
    template < typename static_array >
    static void elements_ptr ( typename static_array :: _data_type * & , static_array & ) ;
    
    template < typename static_array >
    static void elements_ptr ( const typename static_array :: _data_type * & , const static_array & ) ;
    
    template < typename static_array >
    static void elements_count ( int & ) ;
} ;

template < typename static_array >
void shy_platform_static_array_insider :: elements_ptr ( typename static_array :: _data_type * & result , static_array & array )
{
    result = array . _elements ;
}

template < typename static_array >
void shy_platform_static_array_insider :: elements_ptr ( const typename static_array :: _data_type * & result , const static_array & array )
{
    result = array . _elements ;
}

template < typename static_array >
void shy_platform_static_array_insider :: elements_count ( int & count )
{
    count = int ( static_array :: _array_size ) ;
}

#endif
