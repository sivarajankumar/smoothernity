namespace shy_guts
{
    class col_state_type
    {
    public :
        so_called_type_common_logic_text_letter_id letter ;
    } ;
    
    class row_state_type
    {
    public :
        so_called_type_platform_static_array_data < col_state_type , so_called_common_logic_main_menu_consts :: max_cols > cols ;
        so_called_type_platform_math_num_whole cols_count ;
    } ;
    
    namespace rows_state
    {
        static so_called_type_platform_static_array_data < row_state_type , so_called_common_logic_main_menu_consts :: max_rows > rows ;
        static so_called_type_platform_math_num_whole rows_count ;
    }

    static so_called_type_platform_math_num_whole max_cols ;

    static void next_row ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: next_row ( )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_boundaries_request )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_cols_request )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_letter_add )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_letter_request )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_next_row )
{
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_rows_request )
{
}
