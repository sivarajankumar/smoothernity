#pragma once

#include "measurer_mediator.hpp"
#include "measurer_logic.hpp"

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
    void update ( typename platform :: int_32 step )
    {
        _mediator . update ( step ) ;
    }
private :
    shy_measurer_mediator < platform , shy_measurer_logic < platform > > _mediator ;
} ;
