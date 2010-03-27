inline
void 
shy_iphone_platform :: sound_set_listener_position 
    ( shy_iphone_platform :: vector_data position 
    )
{
    ALfloat al_position [ ] = { position . _x , position . _y , position . _z } ;
    alListenerfv ( AL_POSITION , al_position ) ;
}
