class _shy_common_logic_font_texture_generator
{
public :
    static void receive ( so_called_common_logic_font_texture_generator_generate_message ) ;
    static void receive ( so_called_common_logic_font_texture_generator_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_font_texture_generator 
    > :: module 
    shy_common_logic_font_texture_generator_scheduled ;
