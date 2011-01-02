#ifndef _shy_platform_scheduler_direct_call_included
#define _shy_platform_scheduler_direct_call_included

class shy_platform_scheduler_direct_call
{
public :
    template < typename _module >
    class scheduled_context
    {
    public :
        typedef _module module ;
    public :
        static void register_in_scheduler ( ) ;
    private :
        static scheduled_context _singleton ;
    } ;
public :
    static void init ( ) ;
    static void run ( ) ;
} ;

template < typename _module >
void shy_platform_scheduler_direct_call :: scheduled_context < _module > :: register_in_scheduler ( )
{
}

#endif
