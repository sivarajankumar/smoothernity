template < typename mediator >
class shy_engine_camera
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
public :
    static void camera_matrix_look_at ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up ) ;
} ;

template < typename mediator >
void shy_engine_camera < mediator > :: camera_matrix_look_at
    ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up )
{
    vector_data dir ;
    vector_data axis_x ;
    vector_data axis_y ;
    vector_data axis_z ;
    platform_vector :: vector_sub ( dir , from , to ) ;
    platform_vector :: vector_normalize ( axis_z , dir ) ;
    platform_vector :: vector_cross_product ( axis_x , norm_up , axis_z ) ;
    platform_vector :: vector_cross_product ( axis_y , axis_z , axis_x ) ;
    platform_matrix :: matrix_set_axis_x ( matrix , axis_x ) ;
    platform_matrix :: matrix_set_axis_y ( matrix , axis_y ) ;
    platform_matrix :: matrix_set_axis_z ( matrix , axis_z ) ;
    platform_matrix :: matrix_set_origin ( matrix , from ) ;
    platform_matrix :: matrix_inverse_rotation_translation ( matrix ) ;
}
