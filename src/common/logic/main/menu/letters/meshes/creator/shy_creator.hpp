namespace shy_guts
{
    namespace logic_main_menu_letters_rows_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_whole_type rows ;
    }
    
    namespace logic_main_menu_letters_cols_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_whole_type cols ;
    }

    namespace logic_main_menu_letter_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type requested_row ;
        static so_called_platform_math_num_whole_type requested_col ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_common_logic_text_letter_id_type letter ;
    }

    namespace logic_text_letter_mesh_create_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_common_logic_text_letter_id_type requested_letter ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_common_engine_render_mesh_id_type mesh ;
    }
    
    static so_called_platform_math_num_whole_type first_mesh ;
    static so_called_platform_math_num_whole_type current_row ;
    static so_called_platform_math_num_whole_type current_col ;

    static void proceed_with_creation ( ) ;
    static void obtain_rows_count ( ) ;
    static void start_first_row ( ) ;
    static void start_first_col ( ) ;
    static void move_to_next_row ( ) ;
    static void move_to_next_col ( ) ;
    static void letter_state_received ( ) ;
    static void create_mesh ( ) ;
    static void send_mesh_created_notification ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_rows_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_rows_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: start_first_row ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_cols_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letters_cols_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: start_first_col ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letter_state :: replied ) )
    {
        shy_guts :: logic_main_menu_letter_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: letter_state_received ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_mesh_create_state :: replied ) )
    {
        shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: send_mesh_created_notification ( ) ;
    }
}

void shy_guts :: obtain_rows_count ( )
{
    shy_guts :: logic_main_menu_letters_rows_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_letters_rows_request_sender :: send ( so_called_common_logic_main_menu_letters_rows_request_message ( ) ) ;
}

void shy_guts :: start_first_row ( )
{
    shy_guts :: current_row = so_called_platform_math_consts :: whole_minus_1 ;
    shy_guts :: move_to_next_row ( ) ;
}

void shy_guts :: start_first_col ( )
{
    shy_guts :: current_col = so_called_platform_math_consts :: whole_minus_1 ;
    shy_guts :: move_to_next_col ( ) ;
}

void shy_guts :: move_to_next_row ( )
{
    so_called_platform_math :: inc_whole ( shy_guts :: current_row ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: current_row , shy_guts :: logic_main_menu_letters_rows_state :: rows ) )
    {
        shy_guts :: logic_main_menu_letters_cols_state :: requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_cols_state :: requested_row = shy_guts :: current_row ;

        so_called_common_logic_main_menu_letters_cols_request_message msg ;
        msg . row = shy_guts :: current_row ;
        so_called_common_logic_main_menu_letters_cols_request_sender :: send ( msg ) ;
    }
    else
    {
        shy_guts :: logic_main_menu_letters_cols_state :: cols = so_called_platform_math_consts :: whole_0 ;
        so_called_common_logic_main_menu_letters_meshes_creation_finished_sender :: send ( so_called_common_logic_main_menu_letters_meshes_creation_finished_message ( ) ) ;
    }
}

void shy_guts :: move_to_next_col ( )
{
    so_called_platform_math :: inc_whole ( shy_guts :: current_col ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: current_col , shy_guts :: logic_main_menu_letters_cols_state :: cols ) )
    {
        shy_guts :: logic_main_menu_letter_state :: requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letter_state :: requested_row = shy_guts :: current_row ;
        shy_guts :: logic_main_menu_letter_state :: requested_col = shy_guts :: current_col ;

        so_called_common_logic_main_menu_letters_letter_request_message msg ;
        msg . row = shy_guts :: current_row ;
        msg . col = shy_guts :: current_col ;
        so_called_common_logic_main_menu_letters_letter_request_sender :: send ( msg ) ;
    }
    else
        shy_guts :: move_to_next_row ( ) ;
}

void shy_guts :: letter_state_received ( )
{
    so_called_platform_math_num_whole_type letter_is_whitespace ;
    so_called_common_logic_text_letter_id_type whitespace ;
    
    whitespace = so_called_common_logic_text_consts :: whitespace ;
    
    so_called_common_logic_text_stateless :: are_letters_equal ( letter_is_whitespace , shy_guts :: logic_main_menu_letter_state :: letter , whitespace ) ;
    if ( so_called_platform_conditions :: whole_is_false ( letter_is_whitespace ) )
        shy_guts :: create_mesh ( ) ;
    else
        shy_guts :: move_to_next_col ( ) ;
}

void shy_guts :: create_mesh ( )
{
    so_called_common_logic_text_letter_id_type letter ;

    letter = shy_guts :: logic_main_menu_letter_state :: letter ;

    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_text_letter_mesh_create_state :: requested_letter = letter ;

    so_called_common_logic_text_letter_mesh_create_request_message msg ;
    msg . letter = letter ;
    msg . size = so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_size ;
    msg . color_r = so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_color_r ;
    msg . color_g = so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_color_g ;
    msg . color_b = so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_color_b ;
    msg . color_a = so_called_common_logic_main_menu_letters_meshes_consts :: letter_mesh_color_a ;
    so_called_common_logic_text_letter_mesh_create_request_sender :: send ( msg ) ;
}

void shy_guts :: send_mesh_created_notification ( )
{
    so_called_common_logic_main_menu_letters_meshes_mesh_has_been_created_message msg ;
    msg . row = shy_guts :: current_row ;
    msg . col = shy_guts :: current_col ;
    msg . mesh = shy_guts :: logic_text_letter_mesh_create_state :: mesh ;
    so_called_common_logic_main_menu_letters_meshes_mesh_has_been_created_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_common_init_message )
{
    shy_guts :: current_col = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: current_row = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: first_mesh = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_main_menu_letter_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letter_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_cols_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_cols_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_rows_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_letters_rows_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_common_logic_main_menu_letters_cols_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_cols_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letters_cols_state :: requested_row , msg . row )
       )
    {
        shy_guts :: logic_main_menu_letters_cols_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_cols_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_cols_state :: cols = msg . cols ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_common_logic_main_menu_letters_letter_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letter_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letter_state :: requested_row , msg . row )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_main_menu_letter_state :: requested_col , msg . col )
       )
    {
        shy_guts :: logic_main_menu_letter_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letter_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letter_state :: letter = msg . letter ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_common_logic_main_menu_letters_meshes_mesh_create_next_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: first_mesh ) )
    {
        shy_guts :: first_mesh = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_rows_count ( ) ;
    }
    else
        shy_guts :: move_to_next_col ( ) ;
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_common_logic_main_menu_letters_rows_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_letters_rows_state :: requested ) )
    {
        shy_guts :: logic_main_menu_letters_rows_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_letters_rows_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_letters_rows_state :: rows = msg . rows ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_common_logic_text_letter_mesh_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_mesh_create_state :: requested ) )
    {
        so_called_platform_math_num_whole_type letters_are_equal ;
        so_called_common_logic_text_stateless :: are_letters_equal ( letters_are_equal , shy_guts :: logic_text_letter_mesh_create_state :: requested_letter , msg . letter ) ;
        if ( so_called_platform_conditions :: whole_is_true ( letters_are_equal ) )
        {
            shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
            shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
            shy_guts :: logic_text_letter_mesh_create_state :: mesh = msg . mesh ;
            shy_guts :: proceed_with_creation ( ) ;
        }
    }
}

void _shy_common_logic_main_menu_letters_meshes_creator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

