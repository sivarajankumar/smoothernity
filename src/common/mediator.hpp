template 
    < typename _platform
    , template < typename mediator > class engine_camera
    , template < typename mediator > class measurer_logic 
    , template < typename mediator > class measurer_logic_camera
    , template < typename mediator > class measurer_logic_entities
    , template < typename mediator > class measurer_logic_fidget
    , template < typename mediator > class measurer_logic_land
    , template < typename mediator > class measurer_logic_sound
    , template < typename mediator > class measurer_logic_touch
    , template < typename mediator > class engine_mesh
    >
class shy_mediator
{
public :
    typedef _platform platform ;
    typedef typename engine_mesh < shy_mediator > :: mesh_id mesh_id ;
    typedef typename platform :: int_32 int_32 ;
    typedef typename platform :: index_data index_data ;
    typedef typename platform :: matrix_data matrix_data ;
    typedef typename platform :: vector_data vector_data ;
    typedef typename platform :: vertex_data vertex_data ;
public :
    shy_mediator ( )
    : _logic ( this )
    , _logic_camera ( this )
    , _logic_entities ( this )
    , _logic_fidget ( this )
    , _logic_land ( this )
    , _logic_sound ( this )
    , _logic_touch ( this )
    {
    }
public :
    void camera_matrix_look_at ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up )
    {
        _engine_camera . camera_matrix_look_at ( matrix , from , to , norm_up ) ;
    }
    void done ( )
    {
        _logic . done ( ) ;
    }
    vector_data get_entity_origin ( int_32 index )
    {
        return _logic_entities . get_entity_origin ( index ) ;
    }
    void init ( )
    {
        _logic . init ( ) ;
        _logic_sound . init ( ) ;
    }
    mesh_id mesh_create 
        ( vertex_data * vertices 
        , index_data * triangle_strip_indices 
        , index_data * triangle_fan_indices
        , int_32 vertices_count
        , int_32 triangle_strip_indices_count 
        , int_32 triangle_fan_indices_count
        )
    {
        return _engine_mesh . mesh_create 
            ( vertices
            , triangle_strip_indices
            , triangle_fan_indices
            , vertices_count
            , triangle_strip_indices_count
            , triangle_fan_indices_count
            ) ;
    }
    void mesh_render ( mesh_id arg_mesh_id )
    {
        _engine_mesh . mesh_render ( arg_mesh_id ) ;
    }
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform )
    {
        _engine_mesh . mesh_set_transform ( arg_mesh_id , transform ) ;
    }
    void render ( )
    {
        _logic . render ( ) ;
    }
    void render_entities ( )
    {
        _logic_entities . render_entities ( ) ;
    }
    void render_fidget ( )
    {
        _logic_fidget . render_fidget ( ) ;
    }
    void render_land ( )
    {
        _logic_land . render_land ( ) ;
    }
    void render_touch ( )
    {
        _logic_touch . render_touch ( ) ;
    }
    void update ( )
    {
        _logic . update ( ) ;
        _logic_camera . update ( ) ;
        _logic_entities . update ( ) ;
        _logic_fidget . update ( ) ;
        _logic_land . update ( ) ;
        _logic_sound . update ( ) ;
        _logic_touch . update ( ) ;
    }
    void use_camera_matrix ( )
    {
        _logic_camera . use_camera_matrix ( ) ;
    }
private :
    engine_camera < shy_mediator > _engine_camera ;
    measurer_logic < shy_mediator > _logic ;
    measurer_logic_camera < shy_mediator > _logic_camera ;
    measurer_logic_entities < shy_mediator > _logic_entities ;
    measurer_logic_fidget < shy_mediator > _logic_fidget ;
    measurer_logic_land < shy_mediator > _logic_land ;
    measurer_logic_sound < shy_mediator > _logic_sound ;
    measurer_logic_touch < shy_mediator > _logic_touch ;
    engine_mesh < shy_mediator > _engine_mesh ;
} ;
