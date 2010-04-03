template < typename mediator >
class shy_measurer_logic
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: time_data time_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
public :
    shy_measurer_logic ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    {
    }
    void init ( )
    {
        _init_render ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        _clear_screen ( ) ;
        _mediator -> use_camera_matrix ( ) ;
        _mediator -> render_land ( ) ;
        _mediator -> render_entities ( ) ;
        _mediator -> render_fidget ( ) ;
    }
    void render_finished ( )
    {
    }
    void update ( )
    {
    }
private :
    void _init_render ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_enable_depth_test ( ) ;
        platform :: render_fog_linear ( 10 , 20 , 0.0f , 0.1f , 0.4f , 0 ) ;
        platform :: render_projection_frustum ( - 1.0f , 1.0f , - 1.515f , 1.515f , 1.0f , 50.0f ) ;
        platform :: render_select_modelview_matrix ( ) ;
        platform :: render_matrix_identity ( ) ;
    }
    void _clear_screen ( )
    {
        platform :: render_clear_screen ( 0 , 0.1f , 0.4f ) ;
    }
private :
    mediator * _mediator ;
} ;
