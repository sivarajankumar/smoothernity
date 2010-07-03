template < typename platform_insider >
class shy_win_platform_time
{
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    class time_data
    {
        friend class shy_win_platform_time ;
    public :
        time_data ( ) ;
    private :
        int _dummy ;
    } ;
public :
    static void get_current ( time_data & time ) ;
    static void diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 ) ;
} ;

template < typename platform_insider >
shy_win_platform_time < platform_insider > :: time_data :: time_data ( )
{
}
    
template < typename platform_insider >
inline void shy_win_platform_time < platform_insider > :: get_current ( time_data & time )
{
}

template < typename platform_insider >
inline void shy_win_platform_time < platform_insider > :: diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 )
{
}
