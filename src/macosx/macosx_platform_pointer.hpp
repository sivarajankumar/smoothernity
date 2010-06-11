template < typename data_type >
shy_macosx_platform :: pointer < data_type > :: pointer ( )
: _data_ptr ( reinterpret_cast < data_type * > ( shy_macosx_platform_utility :: _uninitialized_value ) )
{
}

template < typename data_type >
shy_macosx_platform :: pointer < data_type > :: pointer ( data_type & arg_data )
: _data_ptr ( & arg_data )
{
}

template < typename data_type >
data_type & shy_macosx_platform :: pointer < data_type > :: get ( )
{
    return * _data_ptr ;
}

template < typename data_type >
void shy_macosx_platform :: pointer < data_type > :: set ( data_type & arg_data )
{
    _data_ptr = & arg_data ;
}
