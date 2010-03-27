inline
void 
shy_iphone_platform :: sound_set_listener_position 
    ( shy_iphone_platform :: vector_data position 
    )
{
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alListenerfv ( AL_POSITION , al_position ) ;
}

inline
void 
shy_iphone_platform :: sound_set_listener_velocity
    ( shy_iphone_platform :: vector_data velocity
    )
{
    ALfloat al_velocity [ ] = { velocity . _x , velocity . _y , velocity . _z } ;
    alListenerfv ( AL_VELOCITY , al_velocity ) ;
}

inline
void 
shy_iphone_platform :: sound_set_listener_orientation 
    ( shy_iphone_platform :: vector_data look_at 
    , shy_iphone_platform :: vector_data up 
    )
{
    ALfloat al_orientation [ ] = 
        { look_at . _x 
        , look_at . _y 
        , look_at . _z 
        , up . _x 
        , up . _y 
        , up . _z 
        } ;
    alListenerfv ( AL_ORIENTATION , al_orientation ) ;
}
