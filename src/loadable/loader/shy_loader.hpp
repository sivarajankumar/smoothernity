namespace shy_guts
{
    static void get_error ( so_called_lib_std_bool & ) ;
    static void prepare ( ) ;
    static void read_input ( ) ;
    static void write_output ( ) ;
    static void use_loaded_data ( ) ;
}

void shy_guts :: prepare ( )
{
    so_called_loadable_consts_assigner :: prepare ( ) ;
    so_called_loadable_consts_reflection :: prepare ( ) ;
    so_called_loadable_fsm_assigner :: prepare ( ) ;
    so_called_loadable_fsm_reflection :: prepare ( ) ;
    so_called_loadable_parser :: prepare ( ) ;
}

void shy_guts :: read_input ( )
{
    while ( ! so_called_lib_std_cin . eof ( ) )
    {
        so_called_lib_std_string line ;
        so_called_lib_std_getline ( so_called_lib_std_cin , line ) ;
        so_called_loadable_parser :: parse ( line ) ;
    }
    so_called_loadable_parser :: terminate ( ) ;
}

void shy_guts :: write_output ( )
{
    so_called_lib_std_bool error ;
    shy_guts :: get_error ( error ) ;
    if ( ! error )
    {
        so_called_loadable_consts_generator :: generate ( ) ;
        so_called_loadable_fsm_generator :: generate ( ) ;
    }
}

void shy_guts :: use_loaded_data ( )
{
    so_called_loadable_consts_assigner :: assign ( ) ;
    so_called_loadable_fsm_assigner :: assign ( ) ;
}

void shy_guts :: get_error ( so_called_lib_std_bool & error )
{
    so_called_lib_std_bool parser_error = so_called_lib_std_false ;
    so_called_lib_std_bool consts_assigner_error = so_called_lib_std_false ;
    so_called_lib_std_bool fsm_assigner_error = so_called_lib_std_false ;

    so_called_loadable_parser :: get_error ( parser_error ) ;
    so_called_loadable_consts_assigner :: get_error ( consts_assigner_error ) ;
    so_called_loadable_fsm_assigner :: get_error ( fsm_assigner_error ) ;

    error = parser_error || consts_assigner_error || fsm_assigner_error ;
}

void shy_loadable_loader :: load ( )
{
    shy_guts :: prepare ( ) ;
    shy_guts :: read_input ( ) ;
    shy_guts :: use_loaded_data ( ) ;
    shy_guts :: write_output ( ) ;
}

