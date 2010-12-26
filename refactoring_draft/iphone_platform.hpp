#ifndef _iphone_platform_included_
#define _iphone_platform_included_

class iphone_platform
{
public :
    class platform_math
    {
    public :
        class num_whole
        {
        public :
            int value ;
        } ;
    } ;

    class platform_print
    {
    public :
        static void print_string ( const char * ) ;
        static void print_int ( int ) ;
    } ;

    class platform_scheduler
    {
    public :
        template < typename _module >
        class scheduled_context
        {
        public :
            typedef _module module ;
        public :
            static void register_in_scheduler ( ) { }
        private :
            static scheduled_context _singleton ;
        } ;
    public :
        static void run ( ) ;
    } ;
} ;

#endif

