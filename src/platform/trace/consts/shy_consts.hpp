void shy_platform_trace_consts :: module_name_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: background_color_default ;
    result += so_called_platform_terminal_consts :: text_color_cyan ;
}

void shy_platform_trace_consts :: module_name_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: number_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: background_color_default ;
    result += so_called_platform_terminal_consts :: text_color_blue ;
}

void shy_platform_trace_consts :: number_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: number_error_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_yellow ;
}

void shy_platform_trace_consts :: number_error_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: string_name_error_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_blue ;
}

void shy_platform_trace_consts :: string_name_error_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: string_name_highlight_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_blue ;
    result += so_called_platform_terminal_consts :: text_color_yellow ;
}

void shy_platform_trace_consts :: string_name_highlight_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: string_name_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: background_color_default ;
    result += so_called_platform_terminal_consts :: text_color_magenta ;
}

void shy_platform_trace_consts :: string_name_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: string_error_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_white ;
}

void shy_platform_trace_consts :: string_error_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_platform_trace_consts :: string_highlight_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_blue ;
    result += so_called_platform_terminal_consts :: text_color_white ;
}

void shy_platform_trace_consts :: string_highlight_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}
