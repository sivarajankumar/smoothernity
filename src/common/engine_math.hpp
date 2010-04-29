template < typename mediator >
class shy_engine_math
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: vector_data vector_data ;
public :
    vector_data math_catmull_rom_spline ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 ) ;
    template < typename T > T math_clamp ( T f , T from , T to ) ;
    template < typename T > T math_abs ( T f ) ;
    template < typename T > T math_max ( T f1 , T f2 ) ;
    template < typename T > T math_min ( T f1 , T f2 ) ;
    float_32 math_pi ( ) ;
} ;

template < typename mediator >
typename shy_engine_math < mediator > :: vector_data
shy_engine_math < mediator > :: math_catmull_rom_spline
    ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
{
    float_32 t2 = t * t ;
    float_32 t3 = t * t * t ;
    float_32 p0_coeff = - t + 2.0f * t2 - t3 ;
    float_32 p1_coeff = 2.0f - 5.0f * t2 + 3.0f * t3 ;
    float_32 p2_coeff = t + 4.0f * t2 - 3.0f * t3 ;
    float_32 p3_coeff = - t2 + t3 ;
    vector_data result_p0_p1 = platform :: vector_add 
        ( platform :: vector_mul ( p0 , p0_coeff )
        , platform :: vector_mul ( p1 , p1_coeff )
        ) ;
    vector_data result_p2_p3 = platform :: vector_add
        ( platform :: vector_mul ( p2 , p2_coeff )
        , platform :: vector_mul ( p3 , p3_coeff )
        ) ;
    return platform :: vector_mul ( platform :: vector_add ( result_p0_p1 , result_p2_p3 ) , 0.5f ) ;
}

template < typename mediator >
template < typename T >
T shy_engine_math < mediator > :: math_clamp ( T f , T from , T to )
{
    if ( f < from )
        return from ;
    else if ( f > to )
        return to ;
    else
        return f ;
}

template < typename mediator >
template < typename T >
T shy_engine_math < mediator > :: math_abs ( T f )
{
    return f < T ( 0 ) ? - f : f ;
}

template < typename mediator >
template < typename T >
T shy_engine_math < mediator > :: math_max ( T f1 , T f2 )
{
    return f1 > f2 ? f1 : f2 ;
}

template < typename mediator >
template < typename T >
T shy_engine_math < mediator > :: math_min ( T f1 , T f2 )
{
    return f1 < f2 ? f1 : f2 ;
}

template < typename mediator >
typename shy_engine_math < mediator > :: float_32
shy_engine_math < mediator > :: math_pi ( )
{
    return 3.141592f ;
}
