template < typename mediator >
class shy_engine_math
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: vector_data vector_data ;
public :
    vector_data math_catmull_rom_spline ( float_32 t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
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
    float_32 math_clamp ( float_32 f , float_32 from , float_32 to )
    {
        if ( f < from )
            return from ;
        else if ( f > to )
            return to ;
        else
            return f ;
    }
} ;
