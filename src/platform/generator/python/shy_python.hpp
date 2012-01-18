namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
        static void error_writing_to_file ( so_called_lib_std_string & ) ;
        static void file_generated ( so_called_lib_std_string & ) ;
        static void file_up_to_date ( so_called_lib_std_string & ) ;
        static void path_created ( so_called_lib_std_string & ) ;
        static void script_finished ( so_called_lib_std_string & ) ;
        static void script_started ( so_called_lib_std_string & ) ;
        static void trace_function ( so_called_lib_std_string & ) ;
        static void trace_null_function ( so_called_lib_std_string & ) ;
    }

    static so_called_lib_std_string content ;

    static void main_script ( so_called_lib_std_string & ) ;
}

void shy_guts :: consts :: error_writing_to_file ( so_called_lib_std_string & result )
{
    so_called_lib_std_string string_error_begin ;
    so_called_lib_std_string string_error_end ;
    so_called_lib_std_string string_name_error_begin ;
    so_called_lib_std_string string_name_error_end ;

    so_called_trace ( so_called_platform_trace_consts :: string_error_begin ( string_error_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_error_end ( string_error_end ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_error_begin ( string_name_error_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_error_end ( string_name_error_end ) ) ;

    result . clear ( ) ;
    result += string_error_begin ;
    result += "Error occured while writing to file " ;
    result += string_error_end ;
    result += string_name_error_begin ;
    result += "\"%s\"" ;
    result += string_name_error_end ;
    result += string_error_begin ;
    result += "." ;
    result += string_error_end ;
}

void shy_guts :: consts :: file_generated ( so_called_lib_std_string & result )
{
    so_called_lib_std_string string_highlight_begin ;
    so_called_lib_std_string string_highlight_end ;
    so_called_lib_std_string string_name_highlight_begin ;
    so_called_lib_std_string string_name_highlight_end ;

    so_called_trace ( so_called_platform_trace_consts :: string_highlight_begin ( string_highlight_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_highlight_end ( string_highlight_end ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_highlight_begin ( string_name_highlight_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_highlight_end ( string_name_highlight_end ) ) ;

    result . clear ( ) ;
    result += string_highlight_begin ;
    result += "File " ;
    result += string_highlight_end ;
    result += string_name_highlight_begin ;
    result += "\"%s\"" ;
    result += string_name_highlight_end ;
    result += string_highlight_begin ;
    result += " generated." ;
    result += string_highlight_end ;
}

void shy_guts :: consts :: file_up_to_date ( so_called_lib_std_string & result )
{
    so_called_lib_std_string string_name_begin ;
    so_called_lib_std_string string_name_end ;

    so_called_trace ( so_called_platform_trace_consts :: string_name_begin ( string_name_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_end ( string_name_end ) ) ;

    result . clear ( ) ;
    result += "File " ;
    result += string_name_begin ;
    result += "\"%s\"" ;
    result += string_name_end ;
    result += " is up to date." ;
}

void shy_guts :: consts :: path_created ( so_called_lib_std_string & result )
{
    so_called_lib_std_string string_highlight_begin ;
    so_called_lib_std_string string_highlight_end ;
    so_called_lib_std_string string_name_highlight_begin ;
    so_called_lib_std_string string_name_highlight_end ;

    so_called_trace ( so_called_platform_trace_consts :: string_highlight_begin ( string_highlight_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_highlight_end ( string_highlight_end ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_highlight_begin ( string_name_highlight_begin ) ) ;
    so_called_trace ( so_called_platform_trace_consts :: string_name_highlight_end ( string_name_highlight_end ) ) ;

    result . clear ( ) ;
    result += string_highlight_begin ;
    result += "Path " ;
    result += string_highlight_end ;
    result += string_name_highlight_begin ;
    result += "\"%s\"" ;
    result += string_name_highlight_end ;
    result += string_highlight_begin ;
    result += " created." ;
    result += string_highlight_end ;
}

void shy_guts :: consts :: script_finished ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "Generating script finished." ;
}

void shy_guts :: consts :: script_started ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "Generating script started." ;
}

void shy_guts :: consts :: trace_function ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "def trace ( something ) :\n" ;
    result += "    print something\n" ;
    result += "\n" ;
}

void shy_guts :: consts :: trace_null_function ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "def trace ( something ) :\n" ;
    result += "    pass\n" ;
    result += "\n" ;
}

void shy_guts :: main_script ( so_called_lib_std_string & result )
{
    so_called_lib_std_string error_writing_to_file ;
    so_called_lib_std_string file_generated ;
    so_called_lib_std_string file_up_to_date ;
    so_called_lib_std_string path_created ;
    so_called_lib_std_string script_finished ;
    so_called_lib_std_string script_started ;
    so_called_lib_std_string trace_function ;

    shy_guts :: consts :: error_writing_to_file ( error_writing_to_file ) ;
    shy_guts :: consts :: file_generated ( file_generated ) ;
    shy_guts :: consts :: file_up_to_date ( file_up_to_date ) ;
    shy_guts :: consts :: path_created ( path_created ) ;
    shy_guts :: consts :: script_finished ( script_finished ) ;
    shy_guts :: consts :: script_started ( script_started ) ;

    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace ( shy_guts :: consts :: trace_function ( trace_function ) ) ;
    else
        shy_guts :: consts :: trace_null_function ( trace_function ) ;

    result . clear ( ) ;
    result += so_called_platform_generator_consts :: autogenerated_python_file_begin ;
    result += "# for python 2.5\n" ;
    result += "\n" ;
    result += "import md5\n" ;
    result += "import os\n" ;
    result += "import os . path\n" ;
    result += "\n" ;
    result += trace_function ;
    result += "def generate_file ( path , contents ) :\n" ;
    result += "    dir = os . path . dirname ( path )\n" ;
    result += "    try :\n" ;
    result += "        os . makedirs ( dir )\n" ;
    result += "        trace ( '" + path_created + "' % dir )\n" ;
    result += "    except :\n" ;
    result += "        pass\n" ;
    result += "    old_md5 = str ( )\n" ;
    result += "    new_md5 = md5 . md5 ( contents ) . hexdigest ( )\n" ;
    result += "    try :\n" ;
    result += "        old_md5 = md5 . md5 ( open ( path , 'r' ) . read ( ) ) . hexdigest ( )\n" ;
    result += "    except :\n" ;
    result += "        pass\n" ;
    result += "    if old_md5 != new_md5 :\n" ;
    result += "        try :\n" ;
    result += "            open ( path , 'w' ) . write ( contents )\n" ;
    result += "            trace ( '" + file_generated + "' % path )\n" ;
    result += "        except IOError :\n" ;
    result += "            trace ( '" + error_writing_to_file + "' % path )\n" ;
    result += "    else :\n " ;
    result += "        trace ( '" + file_up_to_date + "' % path )\n" ;
    result += "\n" ;
    result += "trace ( '" + script_started + "' )\n" ;
    result += "trace ( str ( ) )\n" ;
    result += "\n" ;
    result += shy_guts :: content ;
    result += "trace ( str ( ) )\n" ;
    result += "trace ( '" + script_finished + "' )\n" ;
    result += "\n" ;
    result += so_called_platform_generator_consts :: autogenerated_python_file_end ;
}

void shy_platform_generator_python :: generate_file ( so_called_lib_std_string path , so_called_lib_std_string contents )
{
    shy_guts :: content += "generate_file ( '" ;
    shy_guts :: content += path ;
    shy_guts :: content += "' , '''" ;
    shy_guts :: content += contents ;
    shy_guts :: content += "''' )\n" ;
    shy_guts :: content += "\n" ;
}

void shy_platform_generator_python :: write ( )
{
    so_called_lib_std_string script ;
    shy_guts :: main_script ( script ) ;
    so_called_lib_std_cout << script ;
}
