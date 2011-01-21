class shy_platform_static_assert
{
public :
    template < bool condition >
    class shy_static_assert
    {
        char _data [ condition ? 1 : - 1 ] ;
    } ;
} ;
