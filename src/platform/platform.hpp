template < typename platform_insider >
class shy_platform
{
public :
    typedef typename platform_insider :: platform_conditions platform_conditions ;
    typedef typename platform_insider :: platform_math platform_math ;
    typedef typename platform_insider :: platform_math_consts platform_math_consts ;
    typedef typename platform_insider :: platform_matrix platform_matrix ;
    typedef typename platform_insider :: platform_mouse platform_mouse ;
    typedef typename platform_insider :: platform_pointer platform_pointer ;
    typedef typename platform_insider :: platform_render platform_render ;
    typedef typename platform_insider :: platform_scheduler platform_scheduler ;
    typedef typename platform_insider :: platform_sound platform_sound ;
    typedef typename platform_insider :: platform_static_array platform_static_array ;
    typedef typename platform_insider :: platform_static_assert platform_static_assert ;
    typedef typename platform_insider :: platform_time platform_time ;
    typedef typename platform_insider :: platform_touch platform_touch ;
    typedef typename platform_insider :: platform_vector platform_vector ;

    static typename platform_math :: const_int_32 frames_per_second = platform_insider :: frames_per_second ;
    
    typename platform_pointer :: template pointer < const platform_math_consts > math_consts ;
    typename platform_pointer :: template pointer < platform_mouse > mouse ;
    typename platform_pointer :: template pointer < platform_render > render ;
    typename platform_pointer :: template pointer < platform_sound > sound ;
} ;
