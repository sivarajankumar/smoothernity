#include "shy_camera_stateless.h"

void shy_common_engine_camera_stateless :: matrix_look_at
    ( so_called_type_platform_matrix_data & matrix 
    , so_called_type_platform_vector_data from 
    , so_called_type_platform_vector_data to 
    , so_called_type_platform_vector_data norm_up 
    )
{
    so_called_type_platform_vector_data dir ;
    so_called_type_platform_vector_data axis_x ;
    so_called_type_platform_vector_data axis_y ;
    so_called_type_platform_vector_data axis_z ;
    so_called_platform_vector :: sub ( dir , from , to ) ;
    so_called_platform_vector :: normalize ( axis_z , dir ) ;
    so_called_platform_vector :: cross_product ( axis_x , norm_up , axis_z ) ;
    so_called_platform_vector :: cross_product ( axis_y , axis_z , axis_x ) ;
    so_called_platform_matrix :: set_axis_x ( matrix , axis_x ) ;
    so_called_platform_matrix :: set_axis_y ( matrix , axis_y ) ;
    so_called_platform_matrix :: set_axis_z ( matrix , axis_z ) ;
    so_called_platform_matrix :: set_origin ( matrix , from ) ;
    so_called_platform_matrix :: inverse_rotation_translation ( matrix ) ;
}

