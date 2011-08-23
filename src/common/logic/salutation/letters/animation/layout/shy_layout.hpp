template 
    < typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
class so_called_common_engine_taker
{
public :
    void init ( ) ;
    void request ( ) ;
    void should_handle ( so_called_type_platform_math_num_whole & , type_message_reply ) ;

    type_message_reply msg_reply ;
    type_message_request msg_request ;
    so_called_type_platform_math_num_whole requested ;
} ;

template 
    < typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
void so_called_common_engine_taker < type_message_reply , type_message_request , type_sender_request > :: request ( )
{
    requested = so_called_platform_math_consts :: whole_true ;
    type_sender_request :: send ( msg_request ) ;
}

template 
    < typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
void so_called_common_engine_taker < type_message_reply , type_message_request , type_sender_request > :: init ( )
{
    requested = so_called_platform_math_consts :: whole_false ;
}

template 
    < typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
void so_called_common_engine_taker < type_message_reply , type_message_request , type_sender_request > :: should_handle
    ( so_called_type_platform_math_num_whole & result
    , type_message_reply msg
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( requested ) )
    {
        requested = so_called_platform_math_consts :: whole_false ;
        msg_reply = msg ;
        result = so_called_platform_math_consts :: whole_true ;
    }
    else
        result = so_called_platform_math_consts :: whole_false ;
}


typedef so_called_common_engine_taker
    < so_called_message_common_logic_salutation_letters_meshes_storage_size_reply
    , so_called_message_common_logic_salutation_letters_meshes_storage_size_request
    , so_called_sender_common_logic_salutation_letters_meshes_storage_size_request
    > so_called_common_logic_salutation_letters_meshes_storage_size_taker ;






namespace shy_guts
{
    namespace logic_salutation_letters_animation_layout_transform_state
    {
        static so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg_requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_common_logic_salutation_letters_meshes_storage_size_taker taker ;
        static void on_replied ( ) ;
    }

    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_layout > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_requested ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . request ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( )
{
    so_called_type_platform_vector_data origin ;
    so_called_platform_vector :: xyz
        ( origin
        , so_called_platform_math_consts :: fract_0
        , so_called_platform_math_consts :: fract_0
        , so_called_platform_math_consts :: fract_0
        ) ;

    so_called_type_platform_math_num_fract scale ;
    scale = so_called_platform_math_consts :: fract_1 ;

    so_called_message_common_logic_salutation_letters_animation_layout_transform_reply msg ;
    msg . letter = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_requested . letter ;
    msg . origin = origin ;
    msg . scale = scale ;
    so_called_sender_common_logic_salutation_letters_animation_layout_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg )
{
    so_called_type_platform_math_num_whole should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_requested = msg ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_requested ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
