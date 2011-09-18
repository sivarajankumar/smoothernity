class shy_platform_static_assert
{
public :
    template < so_called_lib_std_bool condition >
    class shy_static_assert
    {
        so_called_lib_std_char _data [ condition ? 1 : - 1 ] ;
    } ;
} ;
