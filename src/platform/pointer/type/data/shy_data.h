template < typename data_type >
class shy_type_platform_pointer_data
{
    friend class shy_platform_pointer ;
    typedef data_type _data_type ;
public :
    shy_type_platform_pointer_data ( ) ;
public :
    data_type & get ( ) const ;
private :
    data_type * _data_ptr ;
} ;

template < typename data_type >
shy_type_platform_pointer_data < data_type > :: shy_type_platform_pointer_data ( )
: _data_ptr ( reinterpret_cast < data_type * > ( so_called_platform_consts_insider :: uninitialized_value ) )
{
}

template < typename data_type >
data_type & shy_type_platform_pointer_data < data_type > :: get ( ) const
{
    return * _data_ptr ;
}

