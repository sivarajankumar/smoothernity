#include "measurer_camera.hpp"
#include "measurer_logic.hpp"
#include "measurer_logic_fidget.hpp"
#include "measurer_mediator.hpp"
#include "measurer_mesh.hpp"

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
    void render_finished ( )
    {
        _mediator . render_finished ( ) ;
    }
    void update ( )
    {
        _mediator . update ( ) ;
    }
private :
    shy_measurer_mediator 
        < platform 
        , shy_measurer_camera
        , shy_measurer_logic
        , shy_measurer_logic_fidget
        , shy_measurer_mesh 
        > 
        _mediator ;
} ;
