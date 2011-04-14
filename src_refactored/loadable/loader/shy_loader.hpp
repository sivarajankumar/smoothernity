namespace shy_guts
{
    static void prepare ( ) ;
    static void read_from_standard_input ( ) ;
    static void use_loaded_data ( ) ;
    static void write_to_standard_output ( ) ;
}

void shy_guts :: prepare ( )
{
    so_called_loadable_consts_binder :: bind_all ( ) ;
}

void shy_guts :: read_from_standard_input ( )
{
}

void shy_guts :: use_loaded_data ( )
{
}

void shy_guts :: write_to_standard_output ( )
{
}

void shy_loadable_loader :: load ( )
{
    shy_guts :: prepare ( ) ;
    shy_guts :: read_from_standard_input ( ) ;
    shy_guts :: write_to_standard_output ( ) ;
    shy_guts :: use_loaded_data ( ) ;
}
