template < typename type >
inline void shy_macosx_platform :: memory_pointer_offset ( type * & result , type * base , num_whole offset )
{
    result = base + offset . _value ;
}
