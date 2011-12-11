namespace shy_guts
{
    typedef so_called_lib_std_map < so_called_lib_std_int32_t , so_called_lib_std_string > id_to_name_type ;
    typedef so_called_lib_std_map < so_called_lib_std_int32_t , so_called_lib_std_int32_t > frame_type ;
    typedef so_called_lib_std_vector < shy_guts :: frame_type > history_type ;

    namespace consts
    {
        static const so_called_lib_std_string file_name = "../../../../temp/utils/all/profile/frames.py" ;
    }

    static so_called_lib_std_int32_t last_id = 0 ;
    static id_to_name_type id_to_name ;
    static history_type history ;

    static void generate_names ( so_called_lib_std_string & ) ;
    static void generate_frames ( so_called_lib_std_string & ) ;
}

void shy_guts :: generate_frames ( so_called_lib_std_string & result )
{
    so_called_lib_std_ostringstream frames ;
    frames << "frames = [ ]\n" ;
    for ( shy_guts :: history_type :: const_iterator history_i = shy_guts :: history . begin ( ) ; history_i != shy_guts :: history . end ( ) ; ++ history_i )
    {
        frames << "frames . append (\n" ;
        for ( shy_guts :: frame_type :: const_iterator frame_i = history_i -> begin ( ) ; frame_i != history_i -> end ( ) ; ++ frame_i )
        {
            if ( frame_i == history_i -> begin ( ) )
                frames << "    { " ;
            else
                frames << "    , " ;
            frames << frame_i -> first ;
            frames << " : " ;
            frames << frame_i -> second ;
            frames << "\n" ;
        }
        frames << "    } )\n" ;
    }
    result = frames . str ( ) ;
}

void shy_guts :: generate_names ( so_called_lib_std_string & result )
{
    so_called_lib_std_ostringstream names ;
    if ( ! shy_guts :: id_to_name . empty ( ) )
    {
        names << "names = \\\\\n" ;
        for ( shy_guts :: id_to_name_type :: const_iterator it = shy_guts :: id_to_name . begin ( ) ; it != shy_guts :: id_to_name . end ( ) ; ++ it )
        {
            if ( it == shy_guts :: id_to_name . begin ( ) )
                names << "    { " ;
            else
                names << "    , " ;
            names << it -> first ;
            names << " : \"" ;
            names << it -> second ;
            names << "\"\n" ;
        }
        names << "    }\n" ;
    }
    result = names . str ( ) ;
}

void shy_platform_profile_insider :: generate ( )
{
    so_called_lib_std_string names ;
    so_called_lib_std_string frames ;
    shy_guts :: generate_names ( names ) ;
    shy_guts :: generate_frames ( frames ) ;
    so_called_platform_generator :: generate_file 
        ( shy_guts :: consts :: file_name
        , so_called_platform_generator_consts :: autogenerated_python_file_begin
        + so_called_platform_generator_consts :: new_line
        + names 
        + frames 
        + so_called_platform_generator_consts :: new_line
        + so_called_platform_generator_consts :: autogenerated_python_file_end
        ) ;
}

void shy_platform_profile_insider :: id_value_add ( so_called_platform_math_num_whole_type id_whole , so_called_platform_math_num_whole_type value_whole )
{
    if ( ! shy_guts :: history . empty ( ) )
    {
        so_called_lib_std_int32_t id ;
        so_called_lib_std_int32_t value ;
        so_called_platform_math_insider :: num_whole_value_get ( id , id_whole ) ;
        so_called_platform_math_insider :: num_whole_value_get ( value , value_whole ) ;
        shy_guts :: frame_type & last_frame = shy_guts :: history . back ( ) ;
        if ( last_frame . find ( id ) == last_frame . end ( ) )
            last_frame [ id ] = value ;
        else
            last_frame [ id ] += value ;
    }
}

void shy_platform_profile_insider :: id_value_max ( so_called_platform_math_num_whole_type id_whole , so_called_platform_math_num_whole_type value_whole )
{
    if ( ! shy_guts :: history . empty ( ) )
    {
        so_called_lib_std_int32_t id ;
        so_called_lib_std_int32_t value ;
        so_called_platform_math_insider :: num_whole_value_get ( id , id_whole ) ;
        so_called_platform_math_insider :: num_whole_value_get ( value , value_whole ) ;
        shy_guts :: frame_type & last_frame = shy_guts :: history . back ( ) ;
        if ( last_frame . find ( id ) == last_frame . end ( ) )
            last_frame [ id ] = value ;
        else if ( last_frame [ id ] < value )
            last_frame [ id ] = value ;
    }
}

void shy_platform_profile_insider :: init ( )
{
    shy_guts :: last_id = 0 ;
    shy_guts :: id_to_name . clear ( ) ;
    shy_guts :: history . clear ( ) ;
}

void shy_platform_profile_insider :: next_frame ( )
{
    shy_guts :: history . push_back ( shy_guts :: frame_type ( ) ) ;
}

void shy_platform_profile_insider :: make_name_id ( so_called_platform_math_num_whole_type & id , const so_called_lib_std_char * name )
{
    so_called_platform_math_insider :: num_whole_value_set ( id , shy_guts :: last_id ) ;
    shy_guts :: id_to_name [ shy_guts :: last_id ] = so_called_lib_std_string ( name ) ;
    ++ shy_guts :: last_id ;
}
