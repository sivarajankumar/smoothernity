template < typename data_type , int size >
inline data_type & shy_macosx_platform :: array_element ( static_array < data_type , size > & array , num_whole index )
{
    return array . _elements [ index . _value ] ;
}

template < typename data_type , int size >
inline const data_type & shy_macosx_platform :: array_element ( const static_array < data_type , size > & array , num_whole index )
{
    return array . _elements [ index . _value ] ;
}
