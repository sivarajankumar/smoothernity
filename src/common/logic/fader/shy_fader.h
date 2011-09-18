class _shy_common_logic_fader
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_fader_render_message ) ;
    static void receive ( so_called_common_logic_fader_start_message ) ;
    static void receive ( so_called_common_logic_fader_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fader > :: module shy_common_logic_fader_scheduled ;
