class shy_platform_pointer
{
public :
    template < typename pointer_type >
    static void bind ( pointer_type & ptr , typename pointer_type :: _data_type & data ) ;

    template < typename pointer_type >
    static void are_equal ( so_called_platform_math_num_whole_type & , pointer_type , pointer_type ) ;

    template < typename pointer_type >
    static void is_bound_to ( so_called_platform_math_num_whole_type & , pointer_type , typename pointer_type :: _data_type & data ) ;
} ;

template < typename pointer_type >
void shy_platform_pointer :: bind ( pointer_type & ptr , typename pointer_type :: _data_type & data )
{
    so_called_profile ( so_called_profile_platform_pointer :: bind ( ) ) ;
    ptr . _data_ptr = & data ;
}

template < typename pointer_type >
void shy_platform_pointer :: are_equal 
    ( so_called_platform_math_num_whole_type & result 
    , pointer_type pointer1 
    , pointer_type pointer2 
    )
{
    so_called_trace ( so_called_trace_platform_pointer :: check_args_are_equal ( pointer1 , pointer2 ) ) ;
    so_called_profile ( so_called_profile_platform_pointer :: compare ( ) ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , so_called_lib_std_int32_t ( pointer1 . _data_ptr == pointer2 . _data_ptr ) ) ;
}

template < typename pointer_type >
void shy_platform_pointer :: is_bound_to 
    ( so_called_platform_math_num_whole_type & result 
    , pointer_type pointer 
    , typename pointer_type :: _data_type & data 
    )
{
    so_called_trace ( so_called_trace_platform_pointer :: check_args_is_bound_to ( pointer ) ) ;
    so_called_profile ( so_called_profile_platform_pointer :: compare ( ) ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , so_called_lib_std_int32_t ( pointer . _data_ptr == & data ) ) ;
}
