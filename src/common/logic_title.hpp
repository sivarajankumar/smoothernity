template < typename mediator >
class shy_logic_title
{
    typedef typename mediator :: alphabet_english alphabet_english ;
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: mesh_id mesh_id ;
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
    static const_int_32 _title_duration_in_frames = 200 ;
    
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
        letter_id letter ;
    } ;
    
public :
    shy_logic_title ( mediator * arg_mediator ) ;
    void title_render ( ) ;
    void title_update ( ) ;
    void title_launch_permit ( ) ;
private :
    void _title_create ( ) ;
    void _title_render ( ) ;
    void _title_update ( ) ;
    void _add_letter ( letter_id letter ) ;
    void _bake_letters ( ) ;
private :
    mediator * _mediator ;
    num_whole _title_launch_permitted ;
    num_whole _title_created ;
    num_whole _title_finished ;
    num_whole _title_frames ;
    num_whole _letters_count ;
    typename platform :: template static_array < _letter_state , _max_letters > _letters ;
} ;

template < typename mediator >
shy_logic_title < mediator > :: shy_logic_title ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _title_launch_permitted , false ) ;
    platform :: math_make_num_whole ( _title_finished , false ) ;
    platform :: math_make_num_whole ( _title_created , false ) ;
    _letters_count = platform :: whole_0 ;
    _title_frames = platform :: whole_0 ;
}

template < typename mediator >
void shy_logic_title < mediator > :: title_render ( )
{
    platform :: render_clear_screen ( platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: render_disable_depth_test ( ) ;
    platform :: render_fog_disable ( ) ;
    _mediator -> use_ortho_projection ( ) ;
    _mediator -> fidget_render ( ) ;
    if ( platform :: condition_true ( _title_created ) && platform :: condition_false ( _title_finished ) )
        _title_render ( ) ;
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
        if ( platform :: condition_false ( _title_created ) )
        {
            _title_create ( ) ;
            platform :: math_make_num_whole ( _title_created , true ) ;
        }
    }
    if ( platform :: condition_true ( _title_created ) && platform :: condition_false ( _title_finished ) )
    {
        num_whole whole_title_duration_in_frames ;
        platform :: math_make_num_whole ( whole_title_duration_in_frames , _title_duration_in_frames ) ;
        platform :: math_inc_whole ( _title_frames ) ;
        if ( platform :: condition_whole_greater_than_whole ( _title_frames , whole_title_duration_in_frames ) )
        {
            platform :: math_make_num_whole ( _title_finished , true ) ;
            _mediator -> title_finished ( ) ;
        }
        else
        {
            _title_update ( ) ;
        }
    }
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_create ( )
{
    const alphabet_english & eng = _mediator -> text_alphabet_english ( ) ;
    _add_letter ( eng . S ) ;
    _add_letter ( eng . M ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . O ) ;
    _add_letter ( eng . T ) ;
    _add_letter ( eng . H ) ;
    _add_letter ( eng . E ) ;
    _add_letter ( eng . R ) ;
    _add_letter ( eng . N ) ;
    _add_letter ( eng . I ) ;
    _add_letter ( eng . T ) ;
    _add_letter ( eng . Y ) ;
    _bake_letters ( ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_render ( )
{
}

template < typename mediator >
void shy_logic_title < mediator > :: _title_update ( )
{
}

template < typename mediator >
void shy_logic_title < mediator > :: _add_letter ( letter_id letter )
{
    platform :: array_element ( _letters , _letters_count ) . letter = letter ;
    platform :: math_inc_whole ( _letters_count ) ;
}

template < typename mediator >
void shy_logic_title < mediator > :: _bake_letters ( )
{
}
