template < typename mediator >
class shy_logic_title
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
public :
    shy_logic_title ( mediator * arg_mediator ) ;
    void title_render ( ) ;
    void title_update ( ) ;
    void title_launch_permit ( ) ;
private :
    mediator * _mediator ;
    int_32 _title_launch_permitted ;
    int_32 _title_finished ;
} ;

template < typename mediator >
shy_logic_title < mediator > :: shy_logic_title ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _title_launch_permitted ( false )
, _title_finished ( false )
{
}

template < typename mediator >
void shy_logic_title < mediator > :: title_render ( )
{
}

template < typename mediator >
void shy_logic_title < mediator > :: title_launch_permit ( )
{
    _title_launch_permitted = true ;
}

template < typename mediator >
void shy_logic_title < mediator > :: title_update ( )
{
    if ( _title_launch_permitted )
    {
        if ( ! _title_finished )
        {
            _title_finished = true ;
            _mediator -> title_finished ( ) ;
        }
    }
}
