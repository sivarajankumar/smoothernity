template < typename mediator >
class shy_engine_math
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
public :
    static void catmull_rom_spline ( vector_data & result , num_fract t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 ) ;
    static void catmull_rom_spline ( num_fract & result , num_fract t , num_fract p0 , num_fract p1 , num_fract p2 , num_fract p3 ) ;
    static void lerp ( num_fract & result , num_fract from_value , num_fract from_weight , num_fract to_value , num_fract to_weight , num_fract weight ) ;
    static void clamp_fract ( num_fract & result , num_fract num , num_fract from , num_fract to ) ;
    static void clamp_fract ( num_fract & num , num_fract from , num_fract to ) ;
    static void min_whole ( num_whole & result , num_whole a , num_whole b ) ;
    static void max_whole ( num_whole & result , num_whole a , num_whole b ) ;
    static void abs_whole ( num_whole & result , num_whole a ) ;
} ;

template < typename mediator >
void shy_engine_math < mediator > :: catmull_rom_spline
    ( vector_data & result , num_fract t , vector_data p0 , vector_data p1 , vector_data p2 , vector_data p3 )
{
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
    num_fract fract_2 ;
    num_fract fract_3 ;
    num_fract fract_4 ;
    num_fract fract_5 ;
    vector_data p0_scaled ;
    vector_data p1_scaled ;
    vector_data p2_scaled ;
    vector_data p3_scaled ;
    vector_data result_p0_p1 ;
    vector_data result_p2_p3 ;
    vector_data result_p0_p1_p2_p3 ;
    platform_math :: make_num_fract ( half , 1 , 2 ) ;    
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    platform_math :: make_num_fract ( fract_3 , 3 , 1 ) ;
    platform_math :: make_num_fract ( fract_4 , 4 , 1 ) ;
    platform_math :: make_num_fract ( fract_5 , 5 , 1 ) ;
    platform_math :: mul_fracts ( t2 , t , t ) ;
    platform_math :: mul_fracts ( t3 , t2 , t ) ;
    platform_math :: mul_fracts ( t2_mul_2 , t2 , fract_2 ) ;
    platform_math :: mul_fracts ( t2_mul_4 , t2 , fract_4 ) ;
    platform_math :: mul_fracts ( t2_mul_5 , t2 , fract_5 ) ;
    platform_math :: mul_fracts ( t3_mul_3 , t3 , fract_3 ) ;
    platform_math :: sub_fracts ( p0_coeff , t2_mul_2 , t ) ;
    platform_math :: sub_from_fract ( p0_coeff , t3 ) ;
    platform_math :: sub_fracts ( p1_coeff , t3_mul_3 , t2_mul_5 ) ;
    platform_math :: add_to_fract ( p1_coeff , fract_2 ) ;
    platform_math :: sub_fracts ( p2_coeff , t2_mul_4 , t3_mul_3 ) ;
    platform_math :: add_to_fract ( p2_coeff , t ) ;
    platform_math :: sub_fracts ( p3_coeff , t3 , t2 ) ;
    platform_vector :: mul ( p0_scaled , p0 , p0_coeff ) ;
    platform_vector :: mul ( p1_scaled , p1 , p1_coeff ) ;
    platform_vector :: mul ( p2_scaled , p2 , p2_coeff ) ;
    platform_vector :: mul ( p3_scaled , p3 , p3_coeff ) ;
    platform_vector :: add ( result_p0_p1 , p0_scaled , p1_scaled ) ;
    platform_vector :: add ( result_p2_p3 , p2_scaled , p3_scaled ) ;
    platform_vector :: add ( result_p0_p1_p2_p3 , result_p0_p1 , result_p2_p3 ) ;
    platform_vector :: mul ( result , result_p0_p1_p2_p3 , half ) ;
}

template < typename mediator >
void shy_engine_math < mediator > :: catmull_rom_spline
    ( num_fract & result , num_fract t , num_fract p0 , num_fract p1 , num_fract p2 , num_fract p3 )
{
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
    num_fract fract_2 ;
    num_fract fract_3 ;
    num_fract fract_4 ;
    num_fract fract_5 ;
    num_fract p0_scaled ;
    num_fract p1_scaled ;
    num_fract p2_scaled ;
    num_fract p3_scaled ;
    num_fract result_p0_p1 ;
    num_fract result_p2_p3 ;
    num_fract result_p0_p1_p2_p3 ;
    platform_math :: make_num_fract ( half , 1 , 2 ) ;    
    platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    platform_math :: make_num_fract ( fract_3 , 3 , 1 ) ;
    platform_math :: make_num_fract ( fract_4 , 4 , 1 ) ;
    platform_math :: make_num_fract ( fract_5 , 5 , 1 ) ;
    platform_math :: mul_fracts ( t2 , t , t ) ;
    platform_math :: mul_fracts ( t3 , t2 , t ) ;
    platform_math :: mul_fracts ( t2_mul_2 , t2 , fract_2 ) ;
    platform_math :: mul_fracts ( t2_mul_4 , t2 , fract_4 ) ;
    platform_math :: mul_fracts ( t2_mul_5 , t2 , fract_5 ) ;
    platform_math :: mul_fracts ( t3_mul_3 , t3 , fract_3 ) ;
    platform_math :: sub_fracts ( p0_coeff , t2_mul_2 , t ) ;
    platform_math :: sub_from_fract ( p0_coeff , t3 ) ;
    platform_math :: sub_fracts ( p1_coeff , t3_mul_3 , t2_mul_5 ) ;
    platform_math :: add_to_fract ( p1_coeff , fract_2 ) ;
    platform_math :: sub_fracts ( p2_coeff , t2_mul_4 , t3_mul_3 ) ;
    platform_math :: add_to_fract ( p2_coeff , t ) ;
    platform_math :: sub_fracts ( p3_coeff , t3 , t2 ) ;
    platform_math :: mul_fracts ( p0_scaled , p0 , p0_coeff ) ;
    platform_math :: mul_fracts ( p1_scaled , p1 , p1_coeff ) ;
    platform_math :: mul_fracts ( p2_scaled , p2 , p2_coeff ) ;
    platform_math :: mul_fracts ( p3_scaled , p3 , p3_coeff ) ;
    platform_math :: add_fracts ( result_p0_p1 , p0_scaled , p1_scaled ) ;
    platform_math :: add_fracts ( result_p2_p3 , p2_scaled , p3_scaled ) ;
    platform_math :: add_fracts ( result_p0_p1_p2_p3 , result_p0_p1 , result_p2_p3 ) ;
    platform_math :: mul_fracts ( result , result_p0_p1_p2_p3 , half ) ;
}

template < typename mediator >
void shy_engine_math < mediator > :: lerp 
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
    platform_math :: sub_fracts ( value_diff , to_value , from_value ) ;
    platform_math :: sub_fracts ( weight_diff , to_weight , from_weight ) ;
    platform_math :: sub_fracts ( current_diff , weight , from_weight ) ;
    platform_math :: mul_fracts ( result , value_diff , current_diff ) ;
    platform_math :: div_fract_by ( result , weight_diff ) ;
    platform_math :: add_to_fract ( result , from_value ) ;
}

template < typename mediator >
void shy_engine_math < mediator > :: clamp_fract ( num_fract & result , num_fract num , num_fract from , num_fract to )
{
    if ( platform_conditions :: fract_less_than_fract ( num , from ) )
        result = from ;
    else if ( platform_conditions :: fract_greater_than_fract ( num , to ) )
        result = to ;
    else
        result = num ;
}

template < typename mediator >
void shy_engine_math < mediator > :: clamp_fract ( num_fract & num , num_fract from , num_fract to )
{
    if ( platform_conditions :: fract_less_than_fract ( num , from ) )
        num = from ;
    else if ( platform_conditions :: fract_greater_than_fract ( num , to ) )
        num = to ;
}

template < typename mediator >
void shy_engine_math < mediator > :: min_whole ( num_whole & result , num_whole a , num_whole b )
{
    if ( platform_conditions :: whole_less_than_whole ( a , b ) )
        result = a ;
    else
        result = b ;
}

template < typename mediator >
void shy_engine_math < mediator > :: max_whole ( num_whole & result , num_whole a , num_whole b )
{
    if ( platform_conditions :: whole_greater_than_whole ( a , b ) )
        result = a ;
    else
        result = b ;
}
    
template < typename mediator >
void shy_engine_math < mediator > :: abs_whole ( num_whole & result , num_whole a )
{
    if ( platform_conditions :: whole_less_than_zero ( a ) )
        platform_math :: neg_whole ( result , a ) ;
    else
        result = a ;
}
