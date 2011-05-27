namespace shy_guts
{
    so_called_lib_std_float aspect_width = 1 ;
    so_called_lib_std_float aspect_height = 1 ;
    so_called_lib_std_bool frame_loss = so_called_lib_std_false ;
}

void shy_platform_render_opengl_insider :: set_aspect_width ( so_called_lib_std_float aspect_width )
{
    shy_guts :: aspect_width = aspect_width ;
}

void shy_platform_render_opengl_insider :: get_aspect_width ( so_called_lib_std_float & aspect_width )
{
    aspect_width = shy_guts :: aspect_width ;
}

void shy_platform_render_opengl_insider :: set_aspect_height ( so_called_lib_std_float aspect_height )
{
    shy_guts :: aspect_height = aspect_height ;
}

void shy_platform_render_opengl_insider :: get_aspect_height ( so_called_lib_std_float & aspect_height )
{
    aspect_height = shy_guts :: aspect_height ;
}

void shy_platform_render_opengl_insider :: set_frame_loss ( so_called_lib_std_bool frame_loss )
{
    shy_guts :: frame_loss = frame_loss ;
}

void shy_platform_render_opengl_insider :: get_frame_loss ( so_called_lib_std_bool & frame_loss )
{
    frame_loss = shy_guts :: frame_loss ;
}


