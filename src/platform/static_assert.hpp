template < typename platform_insider >
class shy_platform_static_assert
{
public :
    template < bool condition >
    class static_assert
    {
        char _data [ condition ? 1 : - 1 ] ;
    } ;
} ;
