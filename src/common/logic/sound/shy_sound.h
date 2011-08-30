class _shy_common_logic_sound
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_sound_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_sound_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_sound > :: module shy_common_logic_sound_scheduled ;
