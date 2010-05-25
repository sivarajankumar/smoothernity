template < typename mediator >
class shy_engine_math
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    
    static const float_32 _pi ( ) { return 3.141592f ; }
    
public :
    void math_catmull_rom_spline ( vector_data & result , float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 ) ;
    void math_lerp ( float_32 & result , float_32 from_value , float_32 from_weight , float_32 to_value , float_32 to_weight , float_32 weight ) ;
    void math_lerp ( num_fract & result , num_fract from_value , num_fract from_weight , num_fract to_value , num_fract to_weight , num_fract weight ) ;
    void math_pi ( float_32 & result ) ;
    template < typename type > void math_clamp ( type & result , type f , type from , type to ) ;
    template < typename type > void math_abs ( type & result , type f ) ;
    template < typename type > void math_max ( type & result , type f1 , type f2 ) ;
    template < typename type > void math_min ( type & result , type f1 , type f2 ) ;
} ;

template < typename mediator >
void shy_engine_math < mediator > :: math_catmull_rom_spline
    ( vector_data & result , float_32 t_float_32 , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
{
    num_fract t ;
    num_fract t2 ;
    num_fract t3 ;
    num_fract t2_mul_2 ;
    num_fract t2_mul_4 ;
    num_fract t2_mul_5 ;
    num_fract t3_mul_3 ;
    num_fract p0_coeff ;
    num_fract p1_coeff ;
    num_fract p2_coeff ;
    num_fract p3_coeff ;
    num_fract half ;
    vector_data p0_scaled ;
    vector_data p1_scaled ;
    vector_data p2_scaled ;
    vector_data p3_scaled ;
    vector_data result_p0_p1 ;
    vector_data result_p2_p3 ;
    vector_data result_p0_p1_p2_p3 ;
    platform :: math_make_num_fract ( t , int_32 ( t_float_32 * 10000.0f ) , 10000 ) ;
    platform :: math_mul_fracts ( t2 , t , t ) ;
    platform :: math_mul_fracts ( t3 , t2 , t ) ;
    platform :: math_mul_fracts ( t2_mul_2 , t2 , platform :: fract_2 ) ;
    platform :: math_mul_fracts ( t2_mul_4 , t2 , platform :: fract_4 ) ;
    platform :: math_mul_fracts ( t2_mul_5 , t2 , platform :: fract_5 ) ;
    platform :: math_mul_fracts ( t3_mul_3 , t3 , platform :: fract_3 ) ;
    platform :: math_make_num_fract ( half , 1 , 2 ) ;    
    platform :: math_sub_fracts ( p0_coeff , t2_mul_2 , t ) ;
    platform :: math_sub_from_fract ( p0_coeff , t3 ) ;
    platform :: math_sub_fracts ( p1_coeff , t3_mul_3 , t2_mul_5 ) ;
    platform :: math_add_to_fract ( p1_coeff , platform :: fract_2 ) ;
    platform :: math_sub_fracts ( p2_coeff , t2_mul_4 , t3_mul_3 ) ;
    platform :: math_add_to_fract ( p2_coeff , t ) ;
    platform :: math_sub_fracts ( p3_coeff , t3 , t2 ) ;
    platform :: vector_mul ( p0_scaled , p0 , p0_coeff ) ;
    platform :: vector_mul ( p1_scaled , p1 , p1_coeff ) ;
    platform :: vector_mul ( p2_scaled , p2 , p2_coeff ) ;
    platform :: vector_mul ( p3_scaled , p3 , p3_coeff ) ;
    platform :: vector_add ( result_p0_p1 , p0_scaled , p1_scaled ) ;
    platform :: vector_add ( result_p2_p3 , p2_scaled , p3_scaled ) ;
    platform :: vector_add ( result_p0_p1_p2_p3 , result_p0_p1 , result_p2_p3 ) ;
    platform :: vector_mul ( result , result_p0_p1_p2_p3 , half ) ;
}

template < typename mediator >
template < typename type >
void shy_engine_math < mediator > :: math_clamp ( type & result , type f , type from , type to )
{
    if ( f < from )
        result = from ;
    else if ( f > to )
        result = to ;
    else
        result = f ;
}

template < typename mediator >
template < typename type >
void shy_engine_math < mediator > :: math_abs ( type & result , type f )
{
    result = f < type ( 0 ) ? - f : f ;
}

template < typename mediator >
template < typename type >
void shy_engine_math < mediator > :: math_max ( type & result , type f1 , type f2 )
{
    result = f1 > f2 ? f1 : f2 ;
}

template < typename mediator >
template < typename type >
void shy_engine_math < mediator > :: math_min ( type & result , type f1 , type f2 )
{
    result = f1 < f2 ? f1 : f2 ;
}

template < typename mediator >
void shy_engine_math < mediator > :: math_pi ( float_32 & result )
{
    result = _pi ( ) ;
}

template < typename mediator >
void shy_engine_math < mediator > :: math_lerp 
    ( float_32 & result
    , float_32 from_value 
    , float_32 from_weight 
    , float_32 to_value 
    , float_32 to_weight 
    , float_32 weight 
    )
{
    result = from_value + ( to_value - from_value ) * ( weight - from_weight ) / ( to_weight - from_weight ) ;
}

template < typename mediator >
void shy_engine_math < mediator > :: math_lerp 
    ( num_fract & result
    , num_fract from_value 
    , num_fract from_weight 
    , num_fract to_value 
    , num_fract to_weight 
    , num_fract weight 
    )
{
    num_fract value_diff ;
    num_fract weight_diff ;
    num_fract current_diff ;
    platform :: math_sub_fracts ( value_diff , to_value , from_value ) ;
    platform :: math_sub_fracts ( weight_diff , to_weight , from_weight ) ;
    platform :: math_sub_fracts ( current_diff , weight , from_weight ) ;
    platform :: math_mul_fracts ( result , value_diff , current_diff ) ;
    platform :: math_div_fract_by ( result , weight_diff ) ;
    platform :: math_add_to_fract ( result , from_value ) ;
}
