template < typename mediator >
class shy_engine_camera
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
public :
    void camera_matrix_look_at ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up ) ;
} ;

template < typename mediator >
void shy_engine_camera < mediator > :: camera_matrix_look_at
    ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up )
{
    vector_data axis_z = platform :: vector_normalize ( platform :: vector_sub ( from , to ) ) ;
    vector_data axis_x = platform :: vector_cross_product ( norm_up , axis_z ) ;
    vector_data axis_y = platform :: vector_cross_product ( axis_z , axis_x ) ;
    platform :: matrix_set_axis_x ( matrix , axis_x ) ;
    platform :: matrix_set_axis_y ( matrix , axis_y ) ;
    platform :: matrix_set_axis_z ( matrix , axis_z ) ;
    platform :: matrix_set_origin ( matrix , from ) ;
    platform :: matrix_inverse_rotation_translation ( matrix ) ;
}
