class _shy_common_logic_sound
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_sound_prepare_permit ) ;
    static void receive ( so_called_message_common_logic_sound_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_sound > :: module shy_common_logic_sound_scheduled ;
