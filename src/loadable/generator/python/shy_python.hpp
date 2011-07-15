namespace shy_guts
{
    namespace consts
    {
        static void error_writing_to_file ( so_called_lib_std_string & result ) ;
        static void file_generated ( so_called_lib_std_string & result ) ;
        static void file_up_to_date ( so_called_lib_std_string & result ) ;
        static void path_created ( so_called_lib_std_string & result ) ;
        static void script_finished ( so_called_lib_std_string & result ) ;
        static void script_started ( so_called_lib_std_string & result ) ;
    }
}

void shy_guts :: consts :: error_writing_to_file ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_white ;
    result += "Error occured while writing to file " ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_green ;
    result += "\"%s\"" ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_white ;
    result += "." ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: file_generated ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += so_called_platform_terminal_consts :: background_color_green ;
    result += "File " ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += so_called_platform_terminal_consts :: background_color_green ;
    result += so_called_platform_terminal_consts :: text_color_magenta ;
    result += "\"%s\"" ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += so_called_platform_terminal_consts :: background_color_green ;
    result += " generated." ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: file_up_to_date ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "File \"%s\" is up to date." ;
}

void shy_guts :: consts :: path_created ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "Path \"%s\" created." ;
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

void shy_loadable_generator_python :: main_script ( so_called_lib_std_string & result , so_called_lib_std_string logic )
{
    so_called_lib_std_string error_writing_to_file ;
    so_called_lib_std_string file_generated ;
    so_called_lib_std_string file_up_to_date ;
    so_called_lib_std_string path_created ;
    so_called_lib_std_string script_finished ;
    so_called_lib_std_string script_started ;

    shy_guts :: consts :: error_writing_to_file ( error_writing_to_file ) ;
    shy_guts :: consts :: file_generated ( file_generated ) ;
    shy_guts :: consts :: file_up_to_date ( file_up_to_date ) ;
    shy_guts :: consts :: path_created ( path_created ) ;
    shy_guts :: consts :: script_finished ( script_finished ) ;
    shy_guts :: consts :: script_started ( script_started ) ;

    result . clear ( ) ;
    result += "# autogenerated file begin\n" ;
    result += "# for python 2.5\n" ;
    result += "\n" ;
    result += "import md5\n" ;
    result += "import os\n" ;
    result += "import os . path\n" ;
    result += "\n" ;
    result += "def generate_file ( path , contents ) :\n" ;
    result += "    dir = os . path . dirname ( path )\n" ;
    result += "    try :\n" ;
    result += "        os . makedirs ( dir )\n" ;
    result += "        print '" + path_created + "' % dir\n" ;
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
    result += "            print '" + file_generated + "' % path\n" ;
    result += "        except IOError :\n" ;
    result += "            print '" + error_writing_to_file + "' % ( path )\n" ;
    result += "    else :\n " ;
    result += "        print '" + file_up_to_date + "' % path\n" ;
    result += "\n" ;
    result += "print '" + script_started + "'\n" ;
    result += "print str ( )\n" ;
    result += "\n" ;
    result += logic ;
    result += "print str ( )\n" ;
    result += "print '" + script_finished + "'\n" ;
    result += "\n" ;
    result += "# autogenerated file end\n" ;
}

void shy_loadable_generator_python :: generate_file ( so_called_lib_std_string & result , so_called_lib_std_string path , so_called_lib_std_string contents )
{
    result . clear ( ) ;
    result += "generate_file ( '" ;
    result += path ;
    result += "' , '''// autogenerated file begin\n" ;
    result += "\n" ;
    result += contents ;
    result += "\n" ;
    result += "// autogenerated file end\n" ;
    result += "''' )\n" ;
    result += "\n" ;
}

