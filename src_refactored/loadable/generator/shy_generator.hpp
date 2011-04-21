namespace shy_guts
{
    namespace consts
    {
        static const so_called_std_string autogenerated_folder_path = "../common/autogenerated_test/" ;
        static const so_called_std_string new_line = "\n" ;
    }

    namespace files
    {
        static void consts_hpp ( so_called_std_string & , so_called_std_string ) ;
        static void consts_injections_hpp ( so_called_std_string & , so_called_std_string ) ;
        static void fsm_hpp ( so_called_std_string & , so_called_std_string ) ;
        static void fsm_injections_hpp ( so_called_std_string & , so_called_std_string ) ;
    }

    namespace python
    {
        static void main_script ( so_called_std_string & , so_called_std_string ) ;
        static void generate_file ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
    }

    static void generate_consts ( so_called_std_string & ) ;
    static void generate_fsm ( so_called_std_string & ) ;
}

void shy_guts :: files :: consts_hpp ( so_called_std_string & path , so_called_std_string module )
{
    path . clear ( ) ;
    path += module ;
    path += "_consts/shy_" ;
    path += module ;
    path += "_consts.hpp" ;
}

void shy_guts :: files :: consts_injections_hpp ( so_called_std_string & path , so_called_std_string module )
{
    path . clear ( ) ;
    path += module ;
    path += "_consts/shy_" ;
    path += module ;
    path += "_consts_injections.hpp" ;
}

void shy_guts :: files :: fsm_hpp ( so_called_std_string & path , so_called_std_string system )
{
    path . clear ( ) ;
    path += system ;
    path += "_fsm_behaviour/shy_" ;
    path += system ;
    path += "_fsm_behaviour.hpp" ;
}

void shy_guts :: files :: fsm_injections_hpp ( so_called_std_string & path , so_called_std_string system )
{
    path . clear ( ) ;
    path += system ;
    path += "_fsm_behaviour/shy_" ;
    path += system ;
    path += "_fsm_behaviour_injections.hpp" ;
}

void shy_guts :: python :: main_script ( so_called_std_string & result , so_called_std_string logic )
{
    result . clear ( ) ;
    result += "# autogenerated file begin\n" ;
    result += "\n" ;
    result += "import os\n" ;
    result += "import os . path\n" ;
    result += "\n" ;
    result += "def generate_file ( path , contents ) :\n" ;
    result += "    dir = os . path . dirname ( path )\n" ;
    result += "    try :\n" ;
    result += "        os . makedirs ( dir )\n" ;
    result += "        print 'Path \"%s\" created.' % dir\n" ;
    result += "    except :\n" ;
    result += "        pass\n" ;
    result += "    try :\n" ;
    result += "        open ( path , 'w' ) . write ( contents )\n" ;
    result += "        print 'File \"%s\" generated.' % path\n" ;
    result += "    except IOError ( error ) :\n" ;
    result += "        print 'Error occured at writing to file \"%s\": %s' % ( path , error )\n" ;
    result += "\n" ;
    result += "print 'Generating script started.'\n" ;
    result += "print str ( )\n" ;
    result += "\n" ;
    result += logic ;
    result += "print str ( )\n" ;
    result += "print 'Generating script finished.'\n" ;
    result += "\n" ;
    result += "#autogenerated file end\n" ;
}

void shy_guts :: python :: generate_file ( so_called_std_string & result , so_called_std_string path , so_called_std_string contents )
{
    result . clear ( ) ;
    result += "generate_file ( '" ;
    result += path ;
    result += "' , '''" ;
    result += contents ;
    result += "''' )\n" ;
    result += "\n" ;
}

void shy_guts :: generate_consts ( so_called_std_string & result )
{
    result . clear ( ) ;
    so_called_type_loadable_consts_content_module_container * module_container = 0 ;
    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    for ( so_called_type_loadable_consts_content_module_container :: const_iterator module_i = module_container -> begin ( )
        ; module_i != module_container -> end ( )
        ; ++ module_i
        )
    {
        so_called_std_string module_name ;
        so_called_std_string consts_hpp_path ;
        so_called_std_string consts_injections_hpp_path ;
        so_called_std_string generate_consts_hpp ;
        so_called_std_string generate_consts_injections_hpp ;
        so_called_std_string consts_hpp_contents ;
        so_called_std_string consts_injections_hpp_contents ;

        module_name = module_i -> first ;
        shy_guts :: files :: consts_hpp ( consts_hpp_path , module_name ) ;
        shy_guts :: files :: consts_injections_hpp ( consts_injections_hpp_path , module_name ) ;
        shy_guts :: python :: generate_file 
            ( generate_consts_hpp
            , shy_guts :: consts :: autogenerated_folder_path + consts_hpp_path
            , consts_hpp_contents
            ) ;
        shy_guts :: python :: generate_file 
            ( generate_consts_injections_hpp 
            , shy_guts :: consts :: autogenerated_folder_path + consts_injections_hpp_path 
            , consts_injections_hpp_contents 
            ) ;
        result += generate_consts_hpp ;
        result += generate_consts_injections_hpp ;
    }
}

void shy_guts :: generate_fsm ( so_called_std_string & result )
{
    result . clear ( ) ;
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i = system_container -> begin ( )
        ; system_i != system_container -> end ( )
        ; ++ system_i
        )
    {
        so_called_std_string system_name ;
        so_called_std_string fsm_hpp_path ;
        so_called_std_string fsm_injections_hpp_path ;
        so_called_std_string generate_fsm_hpp ;
        so_called_std_string generate_fsm_injections_hpp ;
        so_called_std_string fsm_hpp_contents ;
        so_called_std_string fsm_injections_hpp_contents ;

        system_name = system_i -> first ;
        shy_guts :: files :: fsm_hpp ( fsm_hpp_path , system_name ) ;
        shy_guts :: files :: fsm_injections_hpp ( fsm_injections_hpp_path , system_name ) ;
        shy_guts :: python :: generate_file 
            ( generate_fsm_hpp 
            , shy_guts :: consts :: autogenerated_folder_path + fsm_hpp_path 
            , fsm_hpp_contents 
            ) ;
        shy_guts :: python :: generate_file 
            ( generate_fsm_injections_hpp 
            , shy_guts :: consts :: autogenerated_folder_path + fsm_injections_hpp_path 
            , fsm_injections_hpp_contents 
            ) ;
        result += generate_fsm_hpp ;
        result += generate_fsm_injections_hpp ;
    }
}

void shy_loadable_generator :: generate ( so_called_std_string & result )
{
    so_called_std_string consts_logic ;
    so_called_std_string fsm_logic ;
    shy_guts :: generate_consts ( consts_logic ) ;
    shy_guts :: generate_fsm ( fsm_logic ) ;
    shy_guts :: python :: main_script ( result , consts_logic + fsm_logic ) ;
}

