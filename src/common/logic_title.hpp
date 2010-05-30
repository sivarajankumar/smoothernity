template < typename mediator >
class shy_logic_title
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const_int_32 _max_letters = 32 ;
    
    class _letter_state
    {
    public :
        num_fract pos_radius_current ;
        num_fract pos_radius_desired ;
        num_fract pos_radius_rubber ;
        num_fract pos_angle_current ;
        num_fract pos_angle_desired ;
        num_fract pos_angle_rubber ;
        num_fract rot_angle_current ;
        num_fract rot_angle_desired ;
        num_fract rot_angle_rubber ;
        num_fract scale_current ;
        num_fract scale_desired ;
        num_fract scale_rubber ;
        vector_data pos_offset ;
        mesh_id mesh ;
    } ;
    
public :
    shy_logic_title ( mediator * arg_mediator ) ;
    void title_render ( ) ;
    void title_update ( ) ;
    void title_launch_permit ( ) ;
private :
    mediator * _mediator ;
    num_whole _title_launch_permitted ;
    num_whole _title_finished ;
    num_whole _letters_count ;
    typename platform :: template static_array < _letter_state , _max_letters > _letters ;
} ;

template < typename mediator >
shy_logic_title < mediator > :: shy_logic_title ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _title_launch_permitted , false ) ;
    platform :: math_make_num_whole ( _title_finished , false ) ;
    _letters_count = platform :: whole_0 ;
}

template < typename mediator >
void shy_logic_title < mediator > :: title_render ( )
{
}

template < typename mediator >
void shy_logic_title < mediator > :: title_launch_permit ( )
{
    platform :: math_make_num_whole ( _title_launch_permitted , true ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: title_update ( )
{
    if ( platform :: condition_true ( _title_launch_permitted ) )
    {
        if ( platform :: condition_false ( _title_finished ) )
        {
            platform :: math_make_num_whole ( _title_finished , true ) ;
            _mediator -> title_finished ( ) ;
        }
    }
}
