template < typename mediator >
class shy_engine_math
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: vector_data vector_data ;
public :
    vector_data math_catmull_rom_spline ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 ) ;
    template < typename type > type math_clamp ( type f , type from , type to ) ;
    template < typename type > type math_abs ( type f ) ;
    template < typename type > type math_max ( type f1 , type f2 ) ;
    template < typename type > type math_min ( type f1 , type f2 ) ;
    float_32 math_lerp ( float_32 from_value , float_32 from_weight , float_32 to_value , float_32 to_weight , float_32 weight ) ;
    float_32 math_pi ( ) ;
} ;

template < typename mediator >
typename shy_engine_math < mediator > :: vector_data
shy_engine_math < mediator > :: math_catmull_rom_spline
    ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
{
    vector_data p0_scaled ;
    vector_data p1_scaled ;
    vector_data p2_scaled ;
    vector_data p3_scaled ;
    vector_data result_p0_p1 ;
    vector_data result_p2_p3 ;
    vector_data result_p0_p1_p2_p3 ;
    vector_data result ;
    float_32 t2 = t * t ;
    float_32 t3 = t * t * t ;
    float_32 p0_coeff = - t + 2.0f * t2 - t3 ;
    float_32 p1_coeff = 2.0f - 5.0f * t2 + 3.0f * t3 ;
    float_32 p2_coeff = t + 4.0f * t2 - 3.0f * t3 ;
    float_32 p3_coeff = - t2 + t3 ;
    platform :: vector_mul ( p0_scaled , p0 , p0_coeff ) ;
    platform :: vector_mul ( p1_scaled , p1 , p1_coeff ) ;
    platform :: vector_mul ( p2_scaled , p2 , p2_coeff ) ;
    platform :: vector_mul ( p3_scaled , p3 , p3_coeff ) ;
    platform :: vector_add ( result_p0_p1 , p0_scaled , p1_scaled ) ;
    platform :: vector_add ( result_p2_p3 , p2_scaled , p3_scaled ) ;
    platform :: vector_add ( result_p0_p1_p2_p3 , result_p0_p1 , result_p2_p3 ) ;
    platform :: vector_mul ( result , result_p0_p1_p2_p3 , 0.5f ) ;
    return result ;
}

template < typename mediator >
template < typename type >
type shy_engine_math < mediator > :: math_clamp ( type f , type from , type to )
{
    if ( f < from )
        return from ;
    else if ( f > to )
        return to ;
    else
        return f ;
}

template < typename mediator >
template < typename type >
type shy_engine_math < mediator > :: math_abs ( type f )
{
    return f < type ( 0 ) ? - f : f ;
}

template < typename mediator >
template < typename type >
type shy_engine_math < mediator > :: math_max ( type f1 , type f2 )
{
    return f1 > f2 ? f1 : f2 ;
}

template < typename mediator >
template < typename type >
type shy_engine_math < mediator > :: math_min ( type f1 , type f2 )
{
    return f1 < f2 ? f1 : f2 ;
}

template < typename mediator >
typename shy_engine_math < mediator > :: float_32
shy_engine_math < mediator > :: math_pi ( )
{
    return 3.141592f ;
}

template < typename mediator >
typename shy_engine_math < mediator > :: float_32 
shy_engine_math < mediator > :: math_lerp 
    ( float_32 from_value 
    , float_32 from_weight 
    , float_32 to_value 
    , float_32 to_weight 
    , float_32 weight 
    )
{
    return from_value + ( to_value - from_value ) * ( weight - from_weight ) / ( to_weight - from_weight ) ;
}
