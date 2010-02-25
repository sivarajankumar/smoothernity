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
    void render_finished ( )
    {
        _logic . render_finished ( ) ;
    }
    void update ( typename platform :: int_32 step )
    {
        _logic . update ( step ) ;
    }
private :
    measurer_logic _logic ;
} ;
