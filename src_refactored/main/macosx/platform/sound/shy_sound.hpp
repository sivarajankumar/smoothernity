void * shy_macosx_platform_sound :: _sound_loader = 0 ;

void shy_macosx_platform_sound :: set_listener_position ( so_called_type_platform_vector_data position )
{
    so_called_lib_std_float x ;
    so_called_lib_std_float y ;
    so_called_lib_std_float z ;

    so_called_platform_vector_insider :: x_get ( x , position ) ;
    so_called_platform_vector_insider :: y_get ( y , position ) ;
    so_called_platform_vector_insider :: z_get ( z , position ) ;

    so_called_lib_openal_ALfloat al_position [ ] = { x , y , z } ;
    so_called_lib_openal_alListenerfv ( so_called_lib_openal_AL_POSITION , al_position ) ;
}

void shy_macosx_platform_sound :: set_listener_velocity ( so_called_type_platform_vector_data velocity )
{
    so_called_lib_std_float x ;
    so_called_lib_std_float y ;
    so_called_lib_std_float z ;

    so_called_platform_vector_insider :: x_get ( x , velocity ) ;
    so_called_platform_vector_insider :: y_get ( y , velocity ) ;
    so_called_platform_vector_insider :: z_get ( z , velocity ) ;

    so_called_lib_openal_ALfloat al_velocity [ ] = { x , y , z } ;
    so_called_lib_openal_alListenerfv ( so_called_lib_openal_AL_VELOCITY , al_velocity ) ;
}

void shy_macosx_platform_sound :: set_listener_orientation ( so_called_type_platform_vector_data look_at , so_called_type_platform_vector_data up )
{
    so_called_lib_std_float look_at_x ;
    so_called_lib_std_float look_at_y ;
    so_called_lib_std_float look_at_z ;
    so_called_lib_std_float up_x ;
    so_called_lib_std_float up_y ;
    so_called_lib_std_float up_z ;

    so_called_platform_vector_insider :: x_get ( look_at_x , look_at ) ;
    so_called_platform_vector_insider :: y_get ( look_at_y , look_at ) ;
    so_called_platform_vector_insider :: z_get ( look_at_z , look_at ) ;
    so_called_platform_vector_insider :: x_get ( up_x , up ) ;
    so_called_platform_vector_insider :: y_get ( up_y , up ) ;
    so_called_platform_vector_insider :: z_get ( up_z , up ) ;

    so_called_lib_openal_ALfloat al_orientation [ ] = 
        { look_at_x
        , look_at_y
        , look_at_z
        , up_x
        , up_y
        , up_z
        } ;
    so_called_lib_openal_alListenerfv ( so_called_lib_openal_AL_ORIENTATION , al_orientation ) ;
}

void shy_macosx_platform_sound :: set_sample_value ( so_called_type_platform_sound_sample_mono & sample , so_called_type_platform_math_num_fract value )
{
    so_called_lib_std_float value_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( value_float , value ) ;
    sample . _value = ( so_called_lib_openal_ALubyte ) ( ( value_float * so_called_lib_std_float ( 127 ) ) + so_called_lib_std_float ( 127 ) ) ;
}

void shy_macosx_platform_sound :: create_stereo_resource_id 
    ( so_called_type_platform_sound_stereo_resource_id & result 
    , so_called_type_platform_math_num_whole resource_index
    )
{
    so_called_lib_std_int32_t resource_index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( resource_index_int , resource_index ) ;
    result . _resource_id = resource_index_int ;
}

void shy_macosx_platform_sound :: loader_ready ( so_called_type_platform_math_num_whole & result )
{
    shy_macosx_sound_loader * loader = reinterpret_cast < shy_macosx_sound_loader * > ( _sound_loader ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , [ loader loader_ready ] ) ;
}

void shy_macosx_platform_sound :: loaded_samples_count ( so_called_type_platform_math_num_whole & result )
{
    shy_macosx_sound_loader * loader = reinterpret_cast < shy_macosx_sound_loader * > ( _sound_loader ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , [ loader loaded_samples_count ] ) ;
}

void shy_macosx_platform_sound :: create_source ( so_called_type_platform_sound_source_id & result )
{
    so_called_lib_openal_alGenSources ( 1 , & result . _source_id ) ;
}

void shy_macosx_platform_sound :: set_source_pitch ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_math_num_fract pitch )
{
    so_called_lib_std_float pitch_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( pitch_float , pitch ) ;
    so_called_lib_openal_alSourcef ( source_id . _source_id , so_called_lib_openal_AL_PITCH , pitch_float ) ;
}

void shy_macosx_platform_sound :: set_source_gain ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_math_num_fract gain )
{
    so_called_lib_std_float gain_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( gain_float , gain ) ;
    so_called_lib_openal_alSourcef ( source_id . _source_id , so_called_lib_openal_AL_GAIN , gain_float ) ;
}

void shy_macosx_platform_sound :: set_source_position ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_vector_data position )
{
    so_called_lib_std_float x ;
    so_called_lib_std_float y ;
    so_called_lib_std_float z ;
    so_called_platform_vector_insider :: x_get ( x , position ) ;
    so_called_platform_vector_insider :: y_get ( y , position ) ;
    so_called_platform_vector_insider :: z_get ( z , position ) ;
    so_called_lib_openal_ALfloat al_position [ ] = { x , y , z } ;
    so_called_lib_openal_alSourcefv ( source_id . _source_id , so_called_lib_openal_AL_POSITION , al_position ) ;
}

void shy_macosx_platform_sound :: set_source_velocity ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_vector_data velocity )
{
    so_called_lib_std_float x ;
    so_called_lib_std_float y ;
    so_called_lib_std_float z ;
    so_called_platform_vector_insider :: x_get ( x , velocity ) ;
    so_called_platform_vector_insider :: y_get ( y , velocity ) ;
    so_called_platform_vector_insider :: z_get ( z , velocity ) ;
    so_called_lib_openal_ALfloat al_velocity [ ] = { x , y , z } ;
    so_called_lib_openal_alSourcefv ( source_id . _source_id , so_called_lib_openal_AL_VELOCITY , al_velocity ) ;
}

void shy_macosx_platform_sound :: set_source_buffer ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_sound_buffer_id & buffer_id )
{
    so_called_lib_openal_alSourcei ( source_id . _source_id , so_called_lib_openal_AL_BUFFER , buffer_id . _buffer_id ) ;
}

void shy_macosx_platform_sound :: set_source_playback_looping ( const so_called_type_platform_sound_source_id & source_id )
{
    so_called_lib_openal_alSourcei ( source_id . _source_id , so_called_lib_openal_AL_LOOPING , so_called_lib_openal_AL_TRUE ) ;
}

void shy_macosx_platform_sound :: set_source_playback_once ( const so_called_type_platform_sound_source_id & source_id )
{
    so_called_lib_openal_alSourcei ( source_id . _source_id , so_called_lib_openal_AL_LOOPING , so_called_lib_openal_AL_FALSE ) ;
}

void shy_macosx_platform_sound :: source_play ( const so_called_type_platform_sound_source_id & source_id )
{
    so_called_lib_openal_alSourcePlay ( source_id . _source_id ) ;
}

void shy_macosx_platform_sound :: source_stop ( const so_called_type_platform_sound_source_id & source_id )
{
    so_called_lib_openal_alSourceStop ( source_id . _source_id ) ;
}

void shy_macosx_platform_sound :: _load_stereo_sample_data
    ( const so_called_type_platform_sound_sample_stereo * samples_ptr
    , int samples_count
    , const so_called_type_platform_sound_stereo_resource_id & resource_id 
    )
{
    shy_macosx_sound_loader * loader = reinterpret_cast < shy_macosx_sound_loader * > ( _sound_loader ) ;
    [ loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) samples_ptr
        with_max_samples_count_of : samples_count
    ] ;
}

void shy_macosx_platform_sound :: _create_mono_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const so_called_type_platform_sound_sample_mono * samples_ptr
    , so_called_type_platform_math_num_whole samples_count 
    )
{
    int samples_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( samples_count_int , samples_count ) ;

    union al_buffer_data_static_proc_type
    {
        void * void_ptr ;
        alBufferDataStaticProcPtr func_ptr ;
    } ;
    al_buffer_data_static_proc_type al_buffer_data_static_proc ;
    al_buffer_data_static_proc . void_ptr = alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    
    al_buffer_data_static_proc . func_ptr
        ( result . _buffer_id 
        , AL_FORMAT_MONO8 
        , ( ALvoid * ) samples_ptr
        , samples_count_int * sizeof ( so_called_type_platform_sound_sample_mono )
        , mono_sound_samples_per_second
        ) ;
}

void shy_macosx_platform_sound :: _create_stereo_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const so_called_type_platform_sound_sample_stereo * samples_ptr 
    , so_called_type_platform_math_num_whole samples_count 
    )
{
    union al_buffer_data_static_proc_type
    {
        void * void_ptr ;
        alBufferDataStaticProcPtr func_ptr ;
    } ;
    al_buffer_data_static_proc_type al_buffer_data_static_proc ;
    al_buffer_data_static_proc . void_ptr = alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    
    int samples_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( samples_count_int , samples_count ) ;
    
    al_buffer_data_static_proc . func_ptr
        ( result . _buffer_id 
        , AL_FORMAT_STEREO16 
        , ( ALvoid * ) samples_ptr
        , samples_count_int * sizeof ( so_called_type_platform_sound_sample_stereo )
        , stereo_sound_samples_per_second
        ) ;
}

