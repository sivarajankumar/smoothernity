template < typename platform_insider >
class shy_platform_touch_insider ;

template < typename platform_insider >
class shy_platform_touch
{
    friend class shy_platform_touch_insider < platform_insider > ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    shy_platform_touch ( ) ;
	void occured ( num_whole & ) ;
	void x ( num_fract & ) ;
	void y ( num_fract & ) ;
private :
	bool _occured ;
	float _x ;
	float _y ;
} ;

template < typename platform_insider >
shy_platform_touch < platform_insider > :: shy_platform_touch ( )
: _occured ( false )
, _x ( 0 )
, _y ( 0 )
{
}

template < typename platform_insider >
inline void shy_platform_touch < platform_insider > :: occured ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , ( int ) _occured ) ;
}

template < typename platform_insider >
inline void shy_platform_touch < platform_insider > :: x ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _x ) ;
}

template < typename platform_insider >
inline void shy_platform_touch < platform_insider > :: y ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _y ) ;
}
