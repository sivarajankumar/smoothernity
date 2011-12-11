namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "common_logic_game" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_common_logic_game :: camera_prepare_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Camera preparation permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_logic_game :: entities_prepare_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Entities preparation permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_logic_game :: game_launch_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Game launch permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_logic_game :: image_prepare_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Image preparation permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_logic_game :: land_prepare_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Land preparation permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_logic_game :: sound_prepare_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Sound preparation permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_logic_game :: touch_prepare_permitted ( )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Touch preparation permitted." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
