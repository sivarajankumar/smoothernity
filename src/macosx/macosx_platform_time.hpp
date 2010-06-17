template < typename platform >
class shy_macosx_platform_time
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: num_whole num_whole ;
public :
    class time_data
    {
        friend class shy_macosx_platform ;
    public :
        time_data ( ) ;
    private :
        CFAbsoluteTime _time ;
    } ;
public :
    static void time_get_current ( time_data & time ) ;
    static void time_diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 ) ;
private :
    static int _uninitialized_value ( ) ;
} ;

template < typename platform >
int shy_macosx_platform_time < platform > :: _uninitialized_value ( )
{
    return platform :: _uninitialized_value ;
}

template < typename platform >
shy_macosx_platform_time < platform > :: time_data :: time_data ( )
: _time ( shy_macosx_platform_time < platform > :: _uninitialized_value ( ) )
{
}
    
template < typename platform >
inline void shy_macosx_platform_time < platform > :: time_get_current ( time_data & time )
{
    time . _time = CFAbsoluteTimeGetCurrent ( ) ;
}

template < typename platform >
inline void shy_macosx_platform_time < platform > :: time_diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 )
{
    CFAbsoluteTime diff = 0 ;
    if ( time1 . _time > time2 . _time )
        diff = time1 . _time - time2 . _time ;
    else
        diff = time2 . _time - time1 . _time ;
    _platform_math_insider :: num_whole_unsafe_value_set ( result , ( int ) ( diff * ( CFAbsoluteTime ) 1000000 ) ) ;
}
