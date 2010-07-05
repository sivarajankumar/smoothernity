template < typename mediator >
class shy_logic_land
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _land_r = 255 ;
    static const_int_32 _land_g = 255 ;
    static const_int_32 _land_b = 255 ;
    static const_int_32 _land_grid = 10 ;
    static const_int_32 _land_radius = 10 ;
    static const_int_32 _create_rows_per_frame = 8 ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: land_done msg ) ;
    void receive ( typename messages :: land_prepare_permit msg ) ;
    void receive ( typename messages :: land_render_request msg ) ;
    void receive ( typename messages :: land_update msg ) ;
    void receive ( typename messages :: render_texture_create_reply msg ) ;
    void receive ( typename messages :: render_mesh_create_reply msg ) ;
private :
    void _render_land ( ) ;
    void _create_land_mesh ( ) ;
    void _create_land_texture ( ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_whole _land_mesh_created ;
    num_whole _land_texture_created ;
    num_whole _land_prepare_permitted ;
    num_whole _land_texture_creation_row ;
    num_fract _land_scale ;
    num_whole _texture_create_requested ;
    num_whole _texture_create_replied ;
    num_whole _mesh_create_requested ;
    mesh_id _land_mesh_id ;
    texture_id _land_texture_id ;
} ;

template < typename mediator >
void shy_logic_land < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: init msg )
{
    platform_math :: make_num_whole ( _land_mesh_created , false ) ;
    platform_math :: make_num_whole ( _land_texture_created , false ) ;
    platform_math :: make_num_whole ( _land_prepare_permitted , false ) ;
    platform_math :: make_num_whole ( _land_texture_creation_row , 0 ) ;
    platform_math :: make_num_fract ( _land_scale , 0 , 1 ) ;
    _texture_create_requested = platform :: math_consts . whole_false ;
    _texture_create_replied = platform :: math_consts . whole_false ;
    _mesh_create_requested = platform :: math_consts . whole_false ;
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: land_done msg )
{
    if ( platform_conditions :: whole_is_true ( _land_mesh_created ) )
    {
        typename messages :: render_mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _land_mesh_id ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: land_prepare_permit msg )
{
    platform_math :: make_num_whole ( _land_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: land_render_request msg )
{
    if ( platform_conditions :: whole_is_true ( _land_mesh_created ) && platform_conditions :: whole_is_true ( _land_texture_created ) )
        _render_land ( ) ;
    _mediator . get ( ) . send ( typename messages :: land_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: render_texture_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _texture_create_requested ) )
    {
        _texture_create_requested = platform :: math_consts . whole_false ;
        _texture_create_replied = platform :: math_consts . whole_true ;
        _land_texture_id = msg . texture ;
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: land_update msg )
{
    if ( platform_conditions :: whole_is_true ( _land_prepare_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _land_texture_created ) )
        {
            if ( platform_conditions :: whole_is_false ( _texture_create_replied ) )
            {
                _texture_create_requested = platform :: math_consts . whole_true ;
                _mediator . get ( ) . send ( typename messages :: render_texture_create_request ( ) ) ;
            }
            else
                _create_land_texture ( ) ;
        }
        else if ( platform_conditions :: whole_is_false ( _land_mesh_created ) )
        {
            _mesh_create_requested = platform :: math_consts . whole_true ;
        
            num_whole total_vertices ;
            num_whole total_indices ;
            platform_math :: make_num_whole ( total_vertices , ( _land_grid + 1 ) * ( _land_grid + 1 ) ) ;
            platform_math :: make_num_whole ( total_indices , ( _land_grid + 1 ) * 2 * _land_grid ) ;
            
            typename messages :: render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = total_vertices ;
            mesh_create_msg . triangle_strip_indices = total_indices ;
            mesh_create_msg . triangle_fan_indices = platform :: math_consts . whole_0 ;
            _mediator . get ( ) . send ( mesh_create_msg ) ;
        }
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: receive ( typename messages :: render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = platform :: math_consts . whole_false ;
        _land_mesh_id = msg . mesh ;
        _create_land_mesh ( ) ;
        if ( platform_conditions :: whole_is_true ( _land_mesh_created ) )
            _mediator . get ( ) . send ( typename messages :: land_prepared ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: _render_land ( )
{
    matrix_data matrix ;
    num_fract scale_step ;
    num_fract increased_scale ;
    num_fract fract_scale_in_frames ;
    
    {
        typename messages :: render_texture_select texture_select_msg ;
        texture_select_msg . texture = _land_texture_id ;
        _mediator . get ( ) . send ( texture_select_msg ) ;
    }
    platform_math :: make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform_math :: div_fracts ( scale_step , platform :: math_consts . fract_1 , fract_scale_in_frames ) ;
    platform_math :: add_fracts ( increased_scale , _land_scale , scale_step ) ;
    if ( platform_conditions :: fract_less_than_fract ( increased_scale , platform :: math_consts . fract_1 ) )
        _land_scale = increased_scale ;
    else
        _land_scale = platform :: math_consts . fract_1 ;
    platform_matrix :: set_axis_x ( matrix , _land_scale , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_y ( matrix , platform :: math_consts . fract_0 , _land_scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_z ( matrix , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , _land_scale ) ;
    platform_matrix :: set_origin ( matrix , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    {
        typename messages :: render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = _land_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    }
    {
        typename messages :: render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = _land_mesh_id ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: _create_land_mesh ( )
{    
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
    
    platform_math :: make_num_whole ( vertices_count , 0 ) ;
    platform_math :: make_num_whole ( indices_count , 0 ) ;
    platform_math :: make_num_whole ( whole_land_grid , _land_grid ) ;
    platform_math :: make_num_fract ( fract_land_grid , _land_grid , 1 ) ;
    platform_math :: make_num_fract ( grid_step , _land_radius * 2 , _land_grid ) ;
    platform_math :: make_num_fract ( grid_origin_x , - _land_radius , 1 ) ;
    platform_math :: make_num_fract ( grid_origin_z , - _land_radius , 1 ) ;
    
    for ( platform_math :: make_num_whole ( iz , 0 )
        , platform_math :: make_num_whole ( iz_max , _land_grid + 1 )
        ; platform_conditions :: whole_less_than_whole ( iz , iz_max )
        ; platform_math :: inc_whole ( iz )
        )
    {
        for ( platform_math :: make_num_whole ( ix , 0 )
            , platform_math :: make_num_whole ( ix_max , _land_grid + 1 )
            ; platform_conditions :: whole_less_than_whole ( ix , ix_max )
            ; platform_math :: inc_whole ( ix )
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
            num_fract vertex_r ;
            num_fract vertex_g ;
            num_fract vertex_b ;
            num_fract vertex_a ;
            
            platform_math :: make_fract_from_whole ( fract_ix , ix ) ;
            platform_math :: make_fract_from_whole ( fract_iz , iz ) ;
            platform_math :: mul_fracts ( x , grid_step , fract_ix ) ;
            platform_math :: mul_fracts ( z , grid_step , fract_iz ) ;
            platform_math :: add_to_fract ( x , grid_origin_x ) ;
            platform_math :: add_to_fract ( z , grid_origin_z ) ;
            vertex_x = x ;
            vertex_y = platform :: math_consts . fract_0 ;
            vertex_z = z ;
            platform_math :: div_fracts ( vertex_u , fract_iz , fract_land_grid ) ;
            platform_math :: div_fracts ( vertex_v , fract_ix , fract_land_grid ) ;
            platform_math :: make_num_fract ( vertex_r , _land_r , 255 ) ;
            platform_math :: make_num_fract ( vertex_g , _land_g , 255 ) ;
            platform_math :: make_num_fract ( vertex_b , _land_b , 255 ) ;
            platform_math :: make_num_fract ( vertex_a , 1 , 1 ) ;
            
            typename messages :: render_mesh_set_vertex_position set_pos_msg ;
            set_pos_msg . mesh = _land_mesh_id ;
            set_pos_msg . offset = vertices_count ;
            set_pos_msg . x = vertex_x ;
            set_pos_msg . y = vertex_y ;
            set_pos_msg . z = vertex_z ;
            _mediator . get ( ) . send ( set_pos_msg ) ;
            
            typename messages :: render_mesh_set_vertex_color set_col_msg ;
            set_col_msg . mesh = _land_mesh_id ;
            set_col_msg . offset = vertices_count ;
            set_col_msg . r = vertex_r ;
            set_col_msg . g = vertex_g ;
            set_col_msg . b = vertex_b ;
            set_col_msg . a = vertex_a ;
            _mediator . get ( ) . send ( set_col_msg ) ;
            
            typename messages :: render_mesh_set_vertex_tex_coord set_tex_msg ;
            set_tex_msg . mesh = _land_mesh_id ;
            set_tex_msg . offset = vertices_count ;
            set_tex_msg . u = vertex_u ;
            set_tex_msg . v = vertex_v ;
            _mediator . get ( ) . send ( set_tex_msg ) ;
            
            platform_math :: inc_whole ( vertices_count ) ;
        }
    }
    
    for ( platform_math :: make_num_whole ( iz , 0 ) 
        , platform_math :: make_num_whole ( iz_max , _land_grid )
        ; platform_conditions :: whole_less_than_whole ( iz , iz_max )
        ; platform_math :: inc_whole ( iz )
        )
    {
        for ( platform_math :: make_num_whole ( ix , 0 ) 
            , platform_math :: make_num_whole ( ix_max , _land_grid + 1 )
            ; platform_conditions :: whole_less_than_whole ( ix , ix_max )
            ; platform_math :: inc_whole ( ix )
            )
        {
            num_whole index ;
            num_whole row_size ;
            
            platform_math :: make_num_whole ( row_size , _land_grid + 1 ) ;
            
            if ( platform_conditions :: whole_is_even ( iz ) )
            {
                platform_math :: mul_wholes ( index , row_size , iz ) ;
                platform_math :: add_to_whole ( index , ix ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
                
                platform_math :: add_to_whole ( index , row_size ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
            }
            else
            {
                platform_math :: mul_wholes ( index , row_size , iz ) ;
                platform_math :: add_to_whole ( index , whole_land_grid ) ;
                platform_math :: sub_from_whole ( index , ix ) ;
                platform_math :: add_to_whole ( index , row_size ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
                
                platform_math :: sub_from_whole ( index , row_size ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
            }
        }
    }
    typename messages :: render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _land_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
    platform_math :: make_num_whole ( _land_mesh_created , true ) ;
}

template < typename mediator >
void shy_logic_land < mediator > :: _create_land_texture ( )
{
    num_whole texture_width ;
    num_whole texture_height ;
    num_whole whole_create_rows_per_frame ;
    num_whole prev_creation_row = _land_texture_creation_row ;
    
    platform_math :: make_num_whole ( whole_create_rows_per_frame , _create_rows_per_frame ) ;
    
    texture_width = _mediator . get ( ) . engine_render_consts ( ) . texture_width ;
    texture_height = _mediator . get ( ) . engine_render_consts ( ) . texture_height ;
    for ( ; ; )
    {
        num_whole x ;
        num_whole rows_delta ;
        num_whole y = _land_texture_creation_row ;
        
        platform_math :: sub_wholes ( rows_delta , _land_texture_creation_row , prev_creation_row ) ;
        if ( ! platform_conditions :: whole_less_than_whole ( _land_texture_creation_row , texture_height )
          || ! platform_conditions :: whole_less_or_equal_to_whole ( rows_delta , whole_create_rows_per_frame )
           )
        {
            break ;
        }
        for ( platform_math :: make_num_whole ( x , 0 )
            ; platform_conditions :: whole_less_than_whole ( x , texture_width )
            ; platform_math :: inc_whole ( x )
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
            num_fract fract_r ;
            num_fract fract_g ;
            num_fract fract_b ;
            num_fract fract_a ;
            num_fract color_scale ;
            
            platform_math :: make_num_whole ( modulator_1 , 32 ) ;
            platform_math :: make_num_whole ( modulator_2 , 64 ) ;
            platform_math :: make_num_whole ( modulator_3 , 128 ) ;
            platform_math :: make_num_whole ( multiplier_1 , 8 ) ;
            platform_math :: make_num_whole ( multiplier_2 , 4 ) ;
            platform_math :: make_num_whole ( multiplier_3 , 2 ) ;
            platform_math :: make_num_whole ( texel_a , 255 ) ;
            platform_math :: xor_wholes ( c , x , y ) ;
            platform_math :: mod_wholes ( texel_r , c , modulator_1 ) ;
            platform_math :: mod_wholes ( texel_g , c , modulator_2 ) ;
            platform_math :: mod_wholes ( texel_b , c , modulator_3 ) ;
            platform_math :: mul_whole_by ( texel_r , multiplier_1 ) ;
            platform_math :: mul_whole_by ( texel_g , multiplier_2 ) ;
            platform_math :: mul_whole_by ( texel_b , multiplier_3 ) ;

            platform_math :: make_num_fract ( color_scale , 255 , 1 ) ;
            platform_math :: make_fract_from_whole ( fract_r , texel_r ) ;
            platform_math :: make_fract_from_whole ( fract_g , texel_g ) ;
            platform_math :: make_fract_from_whole ( fract_b , texel_b ) ;
            platform_math :: make_fract_from_whole ( fract_a , texel_a ) ;
            platform_math :: div_fract_by ( fract_r , color_scale ) ;
            platform_math :: div_fract_by ( fract_g , color_scale ) ;
            platform_math :: div_fract_by ( fract_b , color_scale ) ;
            platform_math :: div_fract_by ( fract_a , color_scale ) ;
            
            typename messages :: render_texture_set_texel_rgba texture_set_texel_rgba_msg ;
            texture_set_texel_rgba_msg . texture = _land_texture_id ;
            texture_set_texel_rgba_msg . x = x ;
            texture_set_texel_rgba_msg . y = y ;
            texture_set_texel_rgba_msg . r = fract_r ;
            texture_set_texel_rgba_msg . g = fract_g ;
            texture_set_texel_rgba_msg . b = fract_b ;
            texture_set_texel_rgba_msg . a = fract_a ;
            _mediator . get ( ) . send ( texture_set_texel_rgba_msg ) ;
        }
        platform_math :: inc_whole ( _land_texture_creation_row ) ;
    }
    if ( platform_conditions :: wholes_are_equal ( _land_texture_creation_row , texture_height ) )
    {
        typename messages :: render_texture_finalize texture_finalize_msg ;
        texture_finalize_msg . texture = _land_texture_id ;
        _mediator . get ( ) . send ( texture_finalize_msg ) ;
        platform_math :: make_num_whole ( _land_texture_created , true ) ;
    }
}

template < typename mediator >
void shy_logic_land < mediator > :: _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index )
{
    typename messages :: render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = _land_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}

