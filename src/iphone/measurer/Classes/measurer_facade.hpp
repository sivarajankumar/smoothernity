#pragma once

#include "measurer_mediator.hpp"

template < typename platform >
class shy_measurer_facade
{
public :
    shy_measurer_facade ( )
    {
    }
    void init ( )
    {
        _mediator . init ( ) ;
    }
    void done ( )
    {
        _mediator . done ( ) ;
    }
    void render ( )
    {
        _mediator . render ( ) ;
    }
    void update ( typename platform :: int_32 current_step , typename platform :: int_32 max_steps )
    {
        _mediator . update ( current_step , max_steps ) ;
    }
private :
    shy_measurer_mediator < platform > _mediator ;
} ;
