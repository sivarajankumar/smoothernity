template < typename platform_insider >
class shy_macosx_platform_time
{
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    class time_data
    {
        friend class shy_macosx_platform_time ;
    public :
        time_data ( ) ;
    private :
        CFAbsoluteTime _time ;
    } ;
public :
    static void get_current ( time_data & time ) ;
    static void diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 ) ;
} ;

template < typename platform_insider >
shy_macosx_platform_time < platform_insider > :: time_data :: time_data ( )
: _time ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
inline void shy_macosx_platform_time < platform_insider > :: get_current ( time_data & time )
{
    time . _time = CFAbsoluteTimeGetCurrent ( ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_time < platform_insider > :: diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 )
{
    CFAbsoluteTime diff = 0 ;
    if ( time1 . _time > time2 . _time )
        diff = time1 . _time - time2 . _time ;
    else
        diff = time2 . _time - time1 . _time ;
    platform_math_insider :: num_whole_value_set ( result , ( int ) ( diff * ( CFAbsoluteTime ) 1000000 ) ) ;
}
