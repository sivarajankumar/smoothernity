template < typename mediator >
class shy_logic_game
{
public :
    shy_logic_game ( mediator * arg_mediator ) ;
    void game_render ( ) ;
    void game_update ( ) ;
private :
    mediator * _mediator ;
} ;

template < typename mediator >
shy_logic_game < mediator > :: shy_logic_game ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
}

template < typename mediator >
void shy_logic_game < mediator > :: game_render ( )
{
}

template < typename mediator >
void shy_logic_game < mediator > :: game_update ( )
{
}
