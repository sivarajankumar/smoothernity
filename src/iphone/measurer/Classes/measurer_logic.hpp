#pragma once

template < typename platform >
class shy_measurer_logic
{
public :
    void init ( )
    {
        platform :: render_enable_face_culling ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        platform :: render_clear_screen ( 0 , 0 , 0 ) ;
    }
    void update ( typename platform :: int_32 current_step , typename platform :: int_32 max_steps )
    {
    }
} ;