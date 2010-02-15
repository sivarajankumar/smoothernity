#pragma once

template < typename platform , typename measurer_logic >
class shy_measurer_mediator
{
public :
    shy_measurer_mediator ( )
    {
    }
    void init ( )
    {
        _logic . init ( ) ;
    }
    void done ( )
    {
        _logic . done ( ) ;
    }
    void render ( )
    {
        _logic . render ( ) ;
    }
    void update ( typename platform :: int_32 current_step , typename platform :: int_32 max_steps )
    {
        _logic . update ( current_step , max_steps ) ;
    }
private :
    measurer_logic _logic ;
} ;
