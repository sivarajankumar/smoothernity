namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_render" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_render :: check_index_buffer_id_uninitialized ( so_called_platform_render_index_buffer_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_render_insider :: index_buffer_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized index buffer id value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_render :: check_index_buffer_mapped_data_uninitialized ( so_called_platform_render_index_buffer_mapped_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_render_insider :: index_buffer_mapped_data_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized index buffer mapped data value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_render :: check_vertex_buffer_id_uninitialized ( so_called_platform_render_vertex_buffer_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_render_insider :: vertex_buffer_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized vertex buffer id value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_render :: check_vertex_buffer_mapped_data_uninitialized ( so_called_platform_render_vertex_buffer_mapped_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_render_insider :: vertex_buffer_mapped_data_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized vertex buffer mapped data value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_render :: check_texture_id_uninitialized ( so_called_platform_render_texture_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_render_insider :: texture_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized texture id value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_render :: _check_args_load_texture_subdata
    ( so_called_lib_std_int32_t texels_count
    , so_called_platform_render_opengl_texture_id_type arg_texture_id 
    , so_called_platform_math_num_whole_type x_offset 
    , so_called_platform_math_num_whole_type y_offset 
    , so_called_platform_math_num_whole_type width
    , so_called_platform_math_num_whole_type height
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_texture_id_uninitialized ( arg_texture_id ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( x_offset ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( y_offset ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( width ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( height ) ;

        so_called_lib_std_int32_t width_int = 0 ;
        so_called_lib_std_int32_t height_int = 0 ;
        so_called_lib_std_int32_t texture_width = 0 ;
        so_called_lib_std_int32_t texture_height = 0 ;

        so_called_platform_render_insider :: get_texture_size ( texture_width , texture_height , arg_texture_id ) ;
        so_called_platform_math_insider :: num_whole_value_get ( width_int , width ) ;
        so_called_platform_math_insider :: num_whole_value_get ( height_int , height ) ;

        if ( width_int * height_int > texels_count )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Texture area " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( width_int * height_int ) ;
            so_called_platform_trace :: trace_string_error ( " exceeds supplied array of " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( texels_count ) ;
            so_called_platform_trace :: trace_string_error ( " texels." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }

        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( width , 1 , texture_width ) ;
        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( height , 1 , texture_height ) ;
        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( x_offset , 0 , texture_width - width_int ) ;
        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( y_offset , 0 , texture_height - height_int ) ;
    }
}

void shy_trace_platform_render :: check_args_fog_linear
    ( so_called_platform_math_num_fract_type znear 
    , so_called_platform_math_num_fract_type zfar 
    , so_called_platform_math_num_fract_type r 
    , so_called_platform_math_num_fract_type g 
    , so_called_platform_math_num_fract_type b 
    , so_called_platform_math_num_fract_type a 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( znear ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( zfar ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( r ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( g ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_fract_non_positive ( znear ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( r , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( g , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( b , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( a , 0 , 1 ) ;

        so_called_lib_std_float near_float = 0 ;
        so_called_lib_std_float far_float = 0 ;
        so_called_platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
        so_called_platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;

        if ( far_float <= near_float )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Near Z plane " ) ;
            so_called_platform_trace :: trace_num_fract_error ( znear ) ;
            so_called_platform_trace :: trace_string_error ( " must be less than far Z plane " ) ;
            so_called_platform_trace :: trace_num_fract_error ( zfar ) ;
            so_called_platform_trace :: trace_string_error ( "." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}
