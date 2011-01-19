const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_pi ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_pi2 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_2pi ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_0 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_1 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_2 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_3 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_4 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_5 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_6 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_7 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_8 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_9 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_1 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_2 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_3 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_4 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_5 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_6 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_7 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_8 ;
const so_called_type_platform_math_num_fract shy_platform_math_consts :: fract_minus_9 ;

const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_true ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_false ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_0 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_1 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_2 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_3 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_4 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_5 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_6 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_7 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_8 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_9 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_1 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_2 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_3 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_4 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_5 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_6 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_7 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_8 ;
const so_called_type_platform_math_num_whole shy_platform_math_consts :: whole_minus_9 ;

void shy_platform_math_consts :: init ( )
{
    _assign_const_num_fract ( fract_pi , 3.141592f ) ;
    _assign_const_num_fract ( fract_pi2 , 1.570796f ) ;
    _assign_const_num_fract ( fract_2pi , 6.283184f ) ;
    _assign_const_num_fract ( fract_0 , 0 ) ;
    _assign_const_num_fract ( fract_1 , 1 ) ;
    _assign_const_num_fract ( fract_2 , 2 ) ;
    _assign_const_num_fract ( fract_3 , 3 ) ;
    _assign_const_num_fract ( fract_4 , 4 ) ;
    _assign_const_num_fract ( fract_5 , 5 ) ;
    _assign_const_num_fract ( fract_6 , 6 ) ;
    _assign_const_num_fract ( fract_7 , 7 ) ;
    _assign_const_num_fract ( fract_8 , 8 ) ;
    _assign_const_num_fract ( fract_9 , 9 ) ;
    _assign_const_num_fract ( fract_minus_1 , - 1 ) ;
    _assign_const_num_fract ( fract_minus_2 , - 2 ) ;
    _assign_const_num_fract ( fract_minus_3 , - 3 ) ;
    _assign_const_num_fract ( fract_minus_4 , - 4 ) ;
    _assign_const_num_fract ( fract_minus_5 , - 5 ) ;
    _assign_const_num_fract ( fract_minus_6 , - 6 ) ;
    _assign_const_num_fract ( fract_minus_7 , - 7 ) ;
    _assign_const_num_fract ( fract_minus_8 , - 8 ) ;
    _assign_const_num_fract ( fract_minus_9 , - 9 ) ;
        
    _assign_const_num_whole ( whole_true , true ) ;
    _assign_const_num_whole ( whole_false , false ) ;
    _assign_const_num_whole ( whole_0 , 0 ) ;
    _assign_const_num_whole ( whole_1 , 1 ) ;
    _assign_const_num_whole ( whole_2 , 2 ) ;
    _assign_const_num_whole ( whole_3 , 3 ) ;
    _assign_const_num_whole ( whole_4 , 4 ) ;
    _assign_const_num_whole ( whole_5 , 5 ) ;
    _assign_const_num_whole ( whole_6 , 6 ) ;
    _assign_const_num_whole ( whole_7 , 7 ) ;
    _assign_const_num_whole ( whole_8 , 8 ) ;
    _assign_const_num_whole ( whole_9 , 9 ) ;
    _assign_const_num_whole ( whole_minus_1 , - 1 ) ;
    _assign_const_num_whole ( whole_minus_2 , - 2 ) ;
    _assign_const_num_whole ( whole_minus_3 , - 3 ) ;
    _assign_const_num_whole ( whole_minus_4 , - 4 ) ;
    _assign_const_num_whole ( whole_minus_5 , - 5 ) ;
    _assign_const_num_whole ( whole_minus_6 , - 6 ) ;
    _assign_const_num_whole ( whole_minus_7 , - 7 ) ;
    _assign_const_num_whole ( whole_minus_8 , - 8 ) ;
    _assign_const_num_whole ( whole_minus_9 , - 9 ) ;    
}

void shy_platform_math_consts :: _assign_const_num_fract ( const so_called_type_platform_math_num_fract & num , float value )
{
    so_called_platform_math_insider :: num_fract_value_set ( const_cast < so_called_type_platform_math_num_fract & > ( num ) , value ) ;
}

void shy_platform_math_consts :: _assign_const_num_whole ( const so_called_type_platform_math_num_whole & num , int value )
{
    so_called_platform_math_insider :: num_whole_value_set ( const_cast < so_called_type_platform_math_num_whole & > ( num ) , value ) ;
}

