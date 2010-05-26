template < typename mediator >
class shy_logic_land
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    
    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _land_r = 255 ;
    static const_int_32 _land_g = 255 ;
    static const_int_32 _land_b = 255 ;
    static const_int_32 _land_grid = 10 ;
    static const_int_32 _land_radius = 10 ;
    static const_int_32 _create_rows_per_frame = 8 ;
public :
    shy_logic_land ( mediator * arg_mediator ) ;
    void land_prepare_permit ( ) ;
    void land_render ( ) ;
    void land_update ( ) ;
private :
    void _render_land ( ) ;
    void _create_land_mesh ( ) ;
    void _create_land_texture ( ) ;
private :
    mediator * _mediator ;
    num_whole _land_mesh_created ;
    num_whole _land_texture_created ;
    num_whole _land_prepare_permitted ;
    num_whole _land_texture_creation_row ;
    num_fract _land_scale ;
    mesh_id _land_mesh_id ;
    texture_id _land_texture_id ;
} ;

template < typename mediator >
shy_logic_land < mediator > :: shy_logic_land ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _land_mesh_created , false ) ;
    platform :: math_make_num_whole ( _land_texture_created , false ) ;
    platform :: math_make_num_whole ( _land_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _land_texture_creation_row , 0 ) ;
    platform :: math_make_num_fract ( _land_scale , 0 , 1 ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: land_prepare_permit ( )
{
    platform :: math_make_num_whole ( _land_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: land_render ( )
{
    if ( platform :: condition_true ( _land_mesh_created ) && platform :: condition_true ( _land_texture_created ) )
        _render_land ( ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: land_update ( )
{
    if ( platform :: condition_true ( _land_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _land_texture_created ) )
            _create_land_texture ( ) ;
        else if ( platform :: condition_false ( _land_mesh_created ) )
        {
            _create_land_mesh ( ) ;
            if ( platform :: condition_true ( _land_mesh_created ) )
                _mediator -> land_prepared ( ) ;
        }
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: _render_land ( )
{
    matrix_data matrix ;
    num_fract scale_step ;
    num_fract increased_scale ;
    num_fract fract_scale_in_frames ;
    
    _mediator -> texture_select ( _land_texture_id ) ;
    platform :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform :: math_div_fracts ( scale_step , platform :: fract_1 , fract_scale_in_frames ) ;
    platform :: math_add_fracts ( increased_scale , _land_scale , scale_step ) ;
    if ( platform :: condition_fract_less_than_fract ( increased_scale , platform :: fract_1 ) )
        _land_scale = increased_scale ;
    else
        _land_scale = platform :: fract_1 ;
    platform :: matrix_set_axis_x ( matrix , _land_scale , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: matrix_set_axis_y ( matrix , platform :: fract_0 , _land_scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_z ( matrix , platform :: fract_0 , platform :: fract_0 , _land_scale ) ;
    platform :: matrix_set_origin ( matrix , platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
    _mediator -> mesh_set_transform ( _land_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _land_mesh_id ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: _create_land_mesh ( )
{    
    typedef typename platform :: template static_array < vertex_data , ( _land_grid + 1 ) * ( _land_grid + 1 ) > vertex_array ;
    vertex_array vertices ;
    index_data indices [ ( _land_grid + 1 ) * 2 * _land_grid ] ;
    num_whole vertices_count ;
    num_whole indices_count ;
    num_whole ix ;
    num_whole iz ;
    num_whole ix_max ;
    num_whole iz_max ;
    num_whole whole_land_grid ;
    num_fract grid_step ;
    num_fract grid_origin_x ;
    num_fract grid_origin_z ;
    num_fract fract_land_grid ;
    
    platform :: math_make_num_whole ( vertices_count , 0 ) ;
    platform :: math_make_num_whole ( indices_count , 0 ) ;
    platform :: math_make_num_whole ( whole_land_grid , _land_grid ) ;
    platform :: math_make_num_fract ( fract_land_grid , _land_grid , 1 ) ;
    platform :: math_make_num_fract ( grid_step , _land_radius * 2 , _land_grid ) ;
    platform :: math_make_num_fract ( grid_origin_x , - _land_radius , 1 ) ;
    platform :: math_make_num_fract ( grid_origin_z , - _land_radius , 1 ) ;
    
    for ( platform :: math_make_num_whole ( iz , 0 )
        , platform :: math_make_num_whole ( iz_max , _land_grid + 1 )
        ; platform :: condition_whole_less_than_whole ( iz , iz_max )
        ; platform :: math_inc_whole ( iz )
        )
    {
        for ( platform :: math_make_num_whole ( ix , 0 )
            , platform :: math_make_num_whole ( ix_max , _land_grid + 1 )
            ; platform :: condition_whole_less_than_whole ( ix , ix_max )
            ; platform :: math_inc_whole ( ix )
            )
        {
            num_fract x ;
            num_fract z ;
            num_fract fract_ix ;
            num_fract fract_iz ;
            num_fract vertex_x ;
            num_fract vertex_y ;
            num_fract vertex_z ;
            num_fract vertex_u ;
            num_fract vertex_v ;
            num_whole vertex_r ;
            num_whole vertex_g ;
            num_whole vertex_b ;
            num_whole vertex_a ;
            
            platform :: math_make_fract_from_whole ( fract_ix , ix ) ;
            platform :: math_make_fract_from_whole ( fract_iz , iz ) ;
            platform :: math_mul_fracts ( x , grid_step , fract_ix ) ;
            platform :: math_mul_fracts ( z , grid_step , fract_iz ) ;
            platform :: math_add_to_fract ( x , grid_origin_x ) ;
            platform :: math_add_to_fract ( z , grid_origin_z ) ;
            vertex_x = x ;
            vertex_y = platform :: fract_0 ;
            vertex_z = z ;
            platform :: math_div_fracts ( vertex_u , fract_iz , fract_land_grid ) ;
            platform :: math_div_fracts ( vertex_v , fract_ix , fract_land_grid ) ;
            platform :: math_make_num_whole ( vertex_r , _land_r ) ;
            platform :: math_make_num_whole ( vertex_g , _land_g ) ;
            platform :: math_make_num_whole ( vertex_b , _land_b ) ;
            platform :: math_make_num_whole ( vertex_a , 255 ) ;
            {
                vertex_data & vertex = platform :: array_element ( vertices , vertices_count ) ;
                platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
                platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
                platform :: render_set_vertex_tex_coord ( vertex , vertex_u , vertex_v ) ;
            }
            platform :: math_inc_whole ( vertices_count ) ;
        }
    }
    
    for ( platform :: math_make_num_whole ( iz , 0 ) 
        , platform :: math_make_num_whole ( iz_max , _land_grid )
        ; platform :: condition_whole_less_than_whole ( iz , iz_max )
        ; platform :: math_inc_whole ( iz )
        )
    {
        for ( platform :: math_make_num_whole ( ix , 0 ) 
            , platform :: math_make_num_whole ( ix_max , _land_grid + 1 )
            ; platform :: condition_whole_less_than_whole ( ix , ix_max )
            ; platform :: math_inc_whole ( ix )
            )
        {
            num_whole index ;
            num_whole row_size ;
            index_data * index_ptr = 0 ;
            
            platform :: math_make_num_whole ( row_size , _land_grid + 1 ) ;
            
            if ( platform :: condition_whole_is_even ( iz ) )
            {
                platform :: math_mul_wholes ( index , row_size , iz ) ;
                platform :: math_add_to_whole ( index , ix ) ;
                platform :: memory_pointer_offset ( index_ptr , indices , indices_count ) ;
                platform :: render_set_index_value ( * index_ptr , index ) ;
                platform :: math_inc_whole ( indices_count ) ;
                
                platform :: math_add_to_whole ( index , row_size ) ;
                platform :: memory_pointer_offset ( index_ptr , indices , indices_count ) ;
                platform :: render_set_index_value ( * index_ptr , index ) ;
                platform :: math_inc_whole ( indices_count ) ;
            }
            else
            {
                platform :: math_mul_wholes ( index , row_size , iz ) ;
                platform :: math_add_to_whole ( index , whole_land_grid ) ;
                platform :: math_sub_from_whole ( index , ix ) ;
                platform :: math_add_to_whole ( index , row_size ) ;
                platform :: memory_pointer_offset ( index_ptr , indices , indices_count ) ;
                platform :: render_set_index_value ( * index_ptr , index ) ;
                platform :: math_inc_whole ( indices_count ) ;
                
                platform :: math_sub_from_whole ( index , row_size ) ;
                platform :: memory_pointer_offset ( index_ptr , indices , indices_count ) ;
                platform :: render_set_index_value ( * index_ptr , index ) ;
                platform :: math_inc_whole ( indices_count ) ;
            }
        }
    }
    _mediator -> template mesh_create < vertex_array >
        ( _land_mesh_id 
        , vertices 
        , indices 
        , 0 
        , vertices_count 
        , indices_count 
        , platform :: whole_0 
        ) ;
    platform :: math_make_num_whole ( _land_mesh_created , true ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: _create_land_texture ( )
{
    num_whole texture_width ;
    num_whole texture_height ;
    num_whole whole_create_rows_per_frame ;
    num_whole prev_creation_row = _land_texture_creation_row ;
    
    if ( platform :: condition_whole_is_zero ( _land_texture_creation_row ) )
        _mediator -> texture_create ( _land_texture_id ) ;
    platform :: math_make_num_whole ( whole_create_rows_per_frame , _create_rows_per_frame ) ;
    
    _mediator -> texture_width ( texture_width ) ;
    _mediator -> texture_height ( texture_height ) ;
    while ( true )
    {
        num_whole x ;
        num_whole rows_delta ;
        num_whole y = _land_texture_creation_row ;
        
        platform :: math_sub_wholes ( rows_delta , _land_texture_creation_row , prev_creation_row ) ;
        if ( ! platform :: condition_whole_less_than_whole ( _land_texture_creation_row , texture_height )
          || ! platform :: condition_whole_less_or_equal_to_whole ( rows_delta , whole_create_rows_per_frame )
           )
        {
            break ;
        }
        for ( platform :: math_make_num_whole ( x , 0 )
            ; platform :: condition_whole_less_than_whole ( x , texture_width )
            ; platform :: math_inc_whole ( x )
            )
        {
            num_whole c ;
            num_whole modulator_1 ;
            num_whole modulator_2 ;
            num_whole modulator_3 ;
            num_whole multiplier_1 ;
            num_whole multiplier_2 ;
            num_whole multiplier_3 ;
            num_whole texel_r ;
            num_whole texel_g ;
            num_whole texel_b ;
            num_whole texel_a ;
            
            platform :: math_make_num_whole ( modulator_1 , 32 ) ;
            platform :: math_make_num_whole ( modulator_2 , 64 ) ;
            platform :: math_make_num_whole ( modulator_3 , 128 ) ;
            platform :: math_make_num_whole ( multiplier_1 , 8 ) ;
            platform :: math_make_num_whole ( multiplier_2 , 4 ) ;
            platform :: math_make_num_whole ( multiplier_3 , 2 ) ;
            platform :: math_make_num_whole ( texel_a , 255 ) ;
            platform :: math_xor_wholes ( c , x , y ) ;
            platform :: math_mod_wholes ( texel_r , c , modulator_1 ) ;
            platform :: math_mod_wholes ( texel_g , c , modulator_2 ) ;
            platform :: math_mod_wholes ( texel_b , c , modulator_3 ) ;
            platform :: math_mul_whole_by ( texel_r , multiplier_1 ) ;
            platform :: math_mul_whole_by ( texel_g , multiplier_2 ) ;
            platform :: math_mul_whole_by ( texel_b , multiplier_3 ) ;

            _mediator -> texture_set_texel ( _land_texture_id , x , y , texel_r , texel_g , texel_b , texel_a ) ;
        }
        platform :: math_inc_whole ( _land_texture_creation_row ) ;
    }
    if ( platform :: condition_wholes_are_equal ( _land_texture_creation_row , texture_height ) )
    {
        _mediator -> texture_finalize ( _land_texture_id ) ;
        platform :: math_make_num_whole ( _land_texture_created , true ) ;
    }
}
