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
    vector_data dir ;
    vector_data axis_x ;
    vector_data axis_y ;
    vector_data axis_z ;
    platform :: vector_sub ( dir , from , to ) ;
    platform :: vector_normalize ( axis_z , dir ) ;
    platform :: vector_cross_product ( axis_x , norm_up , axis_z ) ;
    platform :: vector_cross_product ( axis_y , axis_z , axis_x ) ;
    platform :: matrix_set_axis_x ( matrix , axis_x ) ;
    platform :: matrix_set_axis_y ( matrix , axis_y ) ;
    platform :: matrix_set_axis_z ( matrix , axis_z ) ;
    platform :: matrix_set_origin ( matrix , from ) ;
    platform :: matrix_inverse_rotation_translation ( matrix ) ;
}
