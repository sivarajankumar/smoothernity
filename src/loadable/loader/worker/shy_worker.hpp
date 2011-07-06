namespace shy_guts
{
    static void get_error ( so_called_lib_std_string & ) ;
    static void prepare ( ) ;
    static void read_input ( ) ;
    static void write_output ( ) ;
    static void use_loaded_data ( ) ;
}

void shy_guts :: prepare ( )
{
    so_called_loadable_consts_reflection :: prepare ( ) ;
    so_called_loadable_fsm_reflection :: prepare ( ) ;
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
    so_called_lib_std_string error ;
    shy_guts :: get_error ( error ) ;
    if ( error . empty ( ) )
    {
        so_called_lib_std_string generated ;
        so_called_loadable_generator :: generate ( generated ) ;
        so_called_lib_std_cout << generated << so_called_lib_std_endl ;
    }
    else
        so_called_lib_std_cerr << error << so_called_lib_std_endl ;
}

void shy_guts :: use_loaded_data ( )
{
    so_called_loadable_consts_assigner :: assign ( ) ;
    so_called_loadable_fsm_assigner :: assign ( ) ;
}

void shy_guts :: get_error ( so_called_lib_std_string & error )
{
    so_called_lib_std_string parser_error ;
    so_called_lib_std_string consts_assigner_error ;
    so_called_lib_std_string fsm_assigner_error ;

    so_called_loadable_parser :: get_error ( parser_error ) ;
    so_called_loadable_consts_assigner :: get_error ( consts_assigner_error ) ;
    so_called_loadable_fsm_assigner :: get_error ( fsm_assigner_error ) ;

    if ( ! parser_error . empty ( ) )
        error = parser_error ;
    else if ( ! consts_assigner_error . empty ( ) )
        error = consts_assigner_error ;
    else if ( ! fsm_assigner_error . empty ( ) )
        error = fsm_assigner_error ;
}

void shy_loadable_loader_worker :: load ( )
{
    shy_guts :: prepare ( ) ;
    shy_guts :: read_input ( ) ;
    shy_guts :: use_loaded_data ( ) ;
    shy_guts :: write_output ( ) ;
}
