namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_int32_t max_texture_pow2 = 16 ;
        static const so_called_lib_std_char module_name [ ] = "platform_render" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }

    static void check_args_projection
        ( so_called_platform_math_num_fract_type left 
        , so_called_platform_math_num_fract_type right 
        , so_called_platform_math_num_fract_type bottom 
        , so_called_platform_math_num_fract_type top 
        , so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        ) ;
    static void check_args_draw
        ( so_called_platform_render_opengl_vertex_buffer_id_type vertices_buffer 
        , so_called_platform_render_opengl_index_buffer_id_type indices_buffer 
        , so_called_platform_math_num_whole_type indices_count 
        ) ;
}

void shy_guts :: check_args_projection
    ( so_called_platform_math_num_fract_type left 
    , so_called_platform_math_num_fract_type right 
    , so_called_platform_math_num_fract_type bottom 
    , so_called_platform_math_num_fract_type top 
    , so_called_platform_math_num_fract_type znear 
    , so_called_platform_math_num_fract_type zfar 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( left ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( right ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( bottom ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( top ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( znear ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( zfar ) ;
        so_called_trace_platform_math :: check_num_fract_non_positive ( znear ) ;
        so_called_trace_platform_math :: check_num_fract_non_positive ( zfar ) ;
        so_called_trace_platform_math :: check_num_fract_not_less_than_fract ( left , right ) ;
        so_called_trace_platform_math :: check_num_fract_not_less_than_fract ( bottom , top ) ;
        so_called_trace_platform_math :: check_num_fract_not_less_than_fract ( znear , zfar ) ;
    }
}

void shy_guts :: check_args_draw
    ( so_called_platform_render_opengl_vertex_buffer_id_type vertices_buffer 
    , so_called_platform_render_opengl_index_buffer_id_type indices_buffer 
    , so_called_platform_math_num_whole_type indices_count 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_render :: check_vertex_buffer_id_uninitialized ( vertices_buffer ) ;
        so_called_trace_platform_render :: check_index_buffer_id_uninitialized ( indices_buffer ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( indices_count ) ;

        so_called_lib_std_int32_t elements = 0 ;
        so_called_platform_render_insider :: get_indices_count ( elements , indices_buffer ) ;

        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( indices_count , 1 , elements ) ;
    }
}
void shy_trace_platform_render :: check_args_projection_frustum
    ( so_called_platform_math_num_fract_type left 
    , so_called_platform_math_num_fract_type right 
    , so_called_platform_math_num_fract_type bottom 
    , so_called_platform_math_num_fract_type top 
    , so_called_platform_math_num_fract_type znear 
    , so_called_platform_math_num_fract_type zfar 
    )
{
    shy_guts :: check_args_projection ( left , right , bottom , top , znear , zfar ) ;
}

void shy_trace_platform_render :: check_args_projection_ortho
    ( so_called_platform_math_num_fract_type left 
    , so_called_platform_math_num_fract_type right 
    , so_called_platform_math_num_fract_type bottom 
    , so_called_platform_math_num_fract_type top 
    , so_called_platform_math_num_fract_type znear 
    , so_called_platform_math_num_fract_type zfar 
    )
{
    shy_guts :: check_args_projection ( left , right , bottom , top , znear , zfar ) ;
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
        so_called_trace_platform_math :: check_num_fract_not_less_than_fract ( znear , zfar ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( r , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( g , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( b , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( a , 0 , 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_set_texel_color
    ( so_called_platform_math_num_fract_type r 
    , so_called_platform_math_num_fract_type g 
    , so_called_platform_math_num_fract_type b 
    , so_called_platform_math_num_fract_type a 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( r ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( g ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( r , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( g , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( b , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( a , 0 , 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_clear_screen
    ( so_called_platform_math_num_fract_type r 
    , so_called_platform_math_num_fract_type g 
    , so_called_platform_math_num_fract_type b 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( r ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( g ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( r , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( g , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( b , 0 , 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_create_texture_id ( so_called_platform_math_num_whole_type size_pow2_base )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( size_pow2_base ) ;
        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( size_pow2_base , 0 , shy_guts :: consts :: max_texture_pow2 ) ;
    }
}

void shy_trace_platform_render :: check_args_use_texture ( so_called_platform_render_texture_id_type arg_texture_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_texture_id_uninitialized ( arg_texture_id ) ;
    }
}

void shy_trace_platform_render :: check_args_delete_texture_id ( so_called_platform_render_texture_id_type arg_texture_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_texture_id_uninitialized ( arg_texture_id ) ;
    }
}

void shy_trace_platform_render :: check_args_create_vertex_buffer ( so_called_platform_math_num_whole_type elements )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( elements ) ;
        so_called_trace_platform_math :: check_num_whole_non_positive ( elements ) ;
    }
}

void shy_trace_platform_render :: check_args_create_index_buffer ( so_called_platform_math_num_whole_type elements )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( elements ) ;
        so_called_trace_platform_math :: check_num_whole_non_positive ( elements ) ;
    }
}

void shy_trace_platform_render :: check_args_map_vertex_buffer ( so_called_platform_render_opengl_vertex_buffer_id_type arg_buffer_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_vertex_buffer_id_uninitialized ( arg_buffer_id ) ;
    }
}

void shy_trace_platform_render :: check_args_map_index_buffer ( so_called_platform_render_opengl_index_buffer_id_type arg_buffer_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_index_buffer_id_uninitialized ( arg_buffer_id ) ;
    }
}

void shy_trace_platform_render :: check_args_unmap_vertex_buffer ( so_called_platform_render_opengl_vertex_buffer_id_type arg_buffer_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_vertex_buffer_id_uninitialized ( arg_buffer_id ) ;
    }
}

void shy_trace_platform_render :: check_args_unmap_index_buffer ( so_called_platform_render_opengl_index_buffer_id_type arg_buffer_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_index_buffer_id_uninitialized ( arg_buffer_id ) ;
    }
}

void shy_trace_platform_render :: check_args_delete_vertex_buffer ( so_called_platform_render_opengl_vertex_buffer_id_type arg_buffer_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_vertex_buffer_id_uninitialized ( arg_buffer_id ) ;
    }
}

void shy_trace_platform_render :: check_args_delete_index_buffer ( so_called_platform_render_opengl_index_buffer_id_type arg_buffer_id )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_index_buffer_id_uninitialized ( arg_buffer_id ) ;
    }
}

void shy_trace_platform_render :: check_args_mapped_vertex_buffer_element ( so_called_platform_render_opengl_vertex_buffer_mapped_data_type data , so_called_platform_math_num_whole_type index )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_vertex_buffer_mapped_data_uninitialized ( data ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( index ) ;

        so_called_lib_std_int32_t elements = 0 ;
        so_called_platform_render_insider :: get_mapped_vertices_count ( elements , data ) ;

        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( index , 0 , elements - 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_mapped_index_buffer_element ( so_called_platform_render_opengl_index_buffer_mapped_data_type data , so_called_platform_math_num_whole_type index )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_index_buffer_mapped_data_uninitialized ( data ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( index ) ;

        so_called_lib_std_int32_t elements = 0 ;
        so_called_platform_render_insider :: get_mapped_indices_count ( elements , data ) ;

        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( index , 0 , elements - 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_set_vertex_position
    ( so_called_platform_math_num_fract_type x 
    , so_called_platform_math_num_fract_type y 
    , so_called_platform_math_num_fract_type z 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( x ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( y ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( z ) ;
    }
}

void shy_trace_platform_render :: check_args_set_vertex_tex_coord
    ( so_called_platform_math_num_fract_type u
    , so_called_platform_math_num_fract_type v
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( u ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( v ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( u , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( v , 0 , 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_set_vertex_color
    ( so_called_platform_math_num_fract_type r
    , so_called_platform_math_num_fract_type g
    , so_called_platform_math_num_fract_type b
    , so_called_platform_math_num_fract_type a
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( r ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( g ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( b ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( a ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( r , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( g , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( b , 0 , 1 ) ;
        so_called_trace_platform_math :: check_num_fract_exceeds_range_int ( a , 0 , 1 ) ;
    }
}

void shy_trace_platform_render :: check_args_set_index_value ( so_called_platform_math_num_whole_type index )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( index ) ;
        so_called_trace_platform_math :: check_num_whole_negative ( index ) ;
    }
}

void shy_trace_platform_render :: check_args_matrix_load ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_matrix :: check_data_uninitialized ( m ) ;
}

void shy_trace_platform_render :: check_args_matrix_mult ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_matrix :: check_data_uninitialized ( m ) ;
}

void shy_trace_platform_render :: check_args_draw_triangle_fan
    ( so_called_platform_render_opengl_vertex_buffer_id_type vertices_buffer 
    , so_called_platform_render_opengl_index_buffer_id_type indices_buffer 
    , so_called_platform_math_num_whole_type indices_count 
    )
{
    shy_guts :: check_args_draw ( vertices_buffer , indices_buffer , indices_count ) ;
}

void shy_trace_platform_render :: check_args_draw_triangle_strip
    ( so_called_platform_render_opengl_vertex_buffer_id_type vertices_buffer 
    , so_called_platform_render_opengl_index_buffer_id_type indices_buffer 
    , so_called_platform_math_num_whole_type indices_count 
    )
{
    shy_guts :: check_args_draw ( vertices_buffer , indices_buffer , indices_count ) ;
}
