#include "engine_camera.hpp"
#include "engine_mesh.hpp"
#include "logic.hpp"
#include "logic_camera.hpp"
#include "logic_entities.hpp"
#include "logic_fidget.hpp"
#include "logic_land.hpp"
#include "logic_sound.hpp"
#include "logic_touch.hpp"
#include "mediator.hpp"

template < typename platform >
class shy_facade
{
public :
    shy_facade ( )
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
    void update ( )
    {
        _mediator . update ( ) ;
    }
private :
    shy_mediator 
        < platform 
        , shy_engine_camera
        , shy_logic
        , shy_logic_camera
        , shy_logic_entities
        , shy_logic_fidget
        , shy_logic_land
        , shy_measurer_logic_sound
        , shy_measurer_logic_touch
        , shy_engine_mesh 
        > 
        _mediator ;
} ;
