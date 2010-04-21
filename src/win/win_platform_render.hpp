inline void shy_win_platform :: render_enable_face_culling ( )
{
}

inline void shy_win_platform :: render_enable_depth_test ( )
{
}

inline void shy_win_platform :: render_disable_depth_test ( )
{
}

inline void shy_win_platform :: render_fog_disable ( )
{
}

inline void shy_win_platform :: render_fog_linear 
    ( shy_win_platform :: float_32 near 
    , shy_win_platform :: float_32 far 
    , shy_win_platform :: float_32 r 
    , shy_win_platform :: float_32 g 
    , shy_win_platform :: float_32 b 
    , shy_win_platform :: float_32 a 
    )
{
}

inline void shy_win_platform :: render_clear_screen 
    ( shy_win_platform :: float_32 r 
    , shy_win_platform :: float_32 g 
    , shy_win_platform :: float_32 b 
    )
{
    HRESULT hr ;
	D3DCOLOR color = D3DCOLOR_ARGB ( 0 , int ( r * 255.0f ) , int ( g * 255.0f ) , int ( b * 255.0f ) ) ;
	V ( DXUTGetD3D9Device ( ) -> Clear ( 0 , NULL , D3DCLEAR_TARGET | D3DCLEAR_ZBUFFER , color , 1.0f , 0 ) ) ;
}

inline void shy_win_platform :: render_projection_frustum 
    ( shy_win_platform :: float_32 left 
    , shy_win_platform :: float_32 right 
    , shy_win_platform :: float_32 bottom 
    , shy_win_platform :: float_32 top 
    , shy_win_platform :: float_32 near 
    , shy_win_platform :: float_32 far 
    )
{
}

inline void shy_win_platform :: render_projection_ortho 
    ( shy_win_platform :: float_32 left 
    , shy_win_platform :: float_32 right 
    , shy_win_platform :: float_32 bottom 
    , shy_win_platform :: float_32 top 
    , shy_win_platform :: float_32 near 
    , shy_win_platform :: float_32 far 
    )
{
}

inline void shy_win_platform :: render_create_buffer_id 
    ( shy_win_platform :: render_buffer_id & arg_buffer_id 
    )
{
}

inline void shy_win_platform :: render_load_vertex_buffer 
    ( const shy_win_platform :: render_buffer_id & arg_buffer_id 
    , shy_win_platform :: int_32 elements 
    , shy_win_platform :: vertex_data * data 
    )
{
}

inline void shy_win_platform :: render_set_vertex_position 
    ( shy_win_platform :: vertex_data & vertex 
    , shy_win_platform :: float_32 x 
    , shy_win_platform :: float_32 y 
    , shy_win_platform :: float_32 z 
    )
{
}

inline void shy_win_platform :: render_set_vertex_tex_coord
    ( shy_win_platform :: vertex_data & vertex 
    , shy_win_platform :: float_32 u
    , shy_win_platform :: float_32 v 
    )
{
}

inline void shy_win_platform :: render_set_vertex_color 
    ( shy_win_platform :: vertex_data & vertex 
    , shy_win_platform :: int_32 r 
    , shy_win_platform :: int_32 g 
    , shy_win_platform :: int_32 b 
    , shy_win_platform :: int_32 a 
    )
{
}

inline void shy_win_platform :: render_load_index_buffer 
    ( const shy_win_platform :: render_buffer_id & arg_buffer_id 
    , shy_win_platform :: int_32 elements 
    , shy_win_platform :: index_data * data 
    )
{
}

inline void shy_win_platform :: render_set_index_value 
    ( shy_win_platform :: index_data & data 
    , shy_win_platform :: int_32 index 
    )
{
}

inline void shy_win_platform :: render_matrix_identity ( )
{
}

inline void shy_win_platform :: render_matrix_load 
    ( const shy_win_platform :: matrix_data & matrix 
    )
{
}

inline void shy_win_platform :: render_matrix_mult 
    ( const shy_win_platform :: matrix_data & matrix 
    )
{
}

inline void shy_win_platform :: render_matrix_push ( )
{
}

inline void shy_win_platform :: render_matrix_pop ( )
{
}

inline void shy_win_platform :: render_draw_triangle_strip 
    ( const shy_win_platform :: render_buffer_id & vertices_buffer 
    , const shy_win_platform :: render_buffer_id & indices_buffer
    , shy_win_platform :: int_32 indices_count
    )
{
}

inline void shy_win_platform :: render_draw_triangle_fan
    ( const shy_win_platform :: render_buffer_id & vertices_buffer 
    , const shy_win_platform :: render_buffer_id & indices_buffer
    , shy_win_platform :: int_32 indices_count
    )
{
}
