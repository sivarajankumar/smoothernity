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
    so_called_type_platform_pointer_data < shy_guts :: row_state_type > row_state ;
    if ( so_called_platform_conditions :: whole_greater_than_zero ( shy_guts :: rows_state :: rows_count ) )
    {
        so_called_type_platform_math_num_whole last_row ;
        so_called_platform_math :: sub_wholes ( last_row , shy_guts :: rows_state :: rows_count , so_called_platform_math_consts :: whole_1 ) ;
        so_called_platform_static_array :: element_ptr ( row_state , shy_guts :: rows_state :: rows , last_row ) ;
        so_called_common_engine_math_stateless :: max_whole ( shy_guts :: max_cols , shy_guts :: max_cols , row_state . get ( ) . cols_count ) ;
    }
    so_called_platform_static_array :: element_ptr ( row_state , shy_guts :: rows_state :: rows , shy_guts :: rows_state :: rows_count ) ;
    row_state . get ( ) . cols_count = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: inc_whole ( shy_guts :: rows_state :: rows_count ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_init )
{
    shy_guts :: max_cols = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rows_state :: rows_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: next_row ( ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_boundaries_request )
{
    so_called_message_common_logic_main_menu_letters_boundaries_reply reply_msg ;
    reply_msg . rows = shy_guts :: rows_state :: rows_count ;
    reply_msg . cols = shy_guts :: max_cols ;
    so_called_common_logic_main_menu_letters_boundaries_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_cols_request msg )
{
    so_called_type_platform_pointer_data < shy_guts :: row_state_type > row_state ;
    so_called_platform_static_array :: element_ptr ( row_state , shy_guts :: rows_state :: rows , msg . row ) ;
    
    so_called_message_common_logic_main_menu_letters_cols_reply reply_msg ;
    reply_msg . row = msg . row ;
    reply_msg . cols = row_state . get ( ) . cols_count ;
    so_called_common_logic_main_menu_letters_cols_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_letter_add msg )
{
    so_called_type_platform_pointer_data < shy_guts :: row_state_type > row_state ;
    so_called_type_platform_pointer_data < shy_guts :: col_state_type > col_state ;
    so_called_type_platform_math_num_whole last_row ;

    so_called_platform_math :: sub_wholes ( last_row , shy_guts :: rows_state :: rows_count , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( row_state , shy_guts :: rows_state :: rows , last_row ) ;
    so_called_platform_static_array :: element_ptr ( col_state , row_state . get ( ) . cols , row_state . get ( ) . cols_count ) ;
    col_state . get ( ) . letter = msg . letter ;

    so_called_platform_math :: inc_whole ( row_state . get ( ) . cols_count ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_letter_request msg )
{
    so_called_type_platform_pointer_data < shy_guts :: row_state_type > row_state ;
    so_called_type_platform_pointer_data < shy_guts :: col_state_type > col_state ;
    so_called_platform_static_array :: element_ptr ( row_state , shy_guts :: rows_state :: rows , msg . row ) ;
    so_called_platform_static_array :: element_ptr ( col_state , row_state . get ( ) . cols , msg . col ) ;

    so_called_message_common_logic_main_menu_letters_letter_reply reply_msg ;
    reply_msg . row = msg . row ;
    reply_msg . col = msg . col ;
    reply_msg . letter = col_state . get ( ) . letter ;
    so_called_common_logic_main_menu_letters_letter_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_next_row )
{
    shy_guts :: next_row ( ) ;
}

void _shy_common_logic_main_menu_letters_storage :: receive ( so_called_message_common_logic_main_menu_letters_rows_request )
{
    so_called_message_common_logic_main_menu_letters_rows_reply reply_msg ;
    reply_msg . rows = shy_guts :: rows_state :: rows_count ;
    so_called_common_logic_main_menu_letters_rows_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_storage :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

