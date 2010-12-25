#ifndef _platform_included_
#define _platform_included_

class my_platform
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
            class _scheduled_module
            {
            public :
                template < typename _message >
                static void receive ( _message ) ;
            } ;
        public :
            typedef _scheduled_module module ;
        public :
            scheduled_context ( ) ;
        private :
            static scheduled_context _singleton ;
            int _some_data ;
        } ;
    public :
        static void run ( ) ;
    } ;
} ;

template < typename _module >
template < typename _message >
void my_platform :: platform_scheduler :: scheduled_context < _module > :: _scheduled_module :: receive ( _message arg )
{
    _module :: receive ( arg ) ;
    ++ _singleton . _some_data ;
}

template < typename _module >
my_platform :: platform_scheduler :: scheduled_context < _module > :: scheduled_context ( )
: _some_data ( 0 )
{
}

#endif

