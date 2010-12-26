#ifndef _macosx_platform_included_
#define _macosx_platform_included_

#include <iostream>
#include <set>

class macosx_platform
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
        class _scheduled_context_base ;
        typedef std :: set < _scheduled_context_base * > _scheduled_context_container ;

        class _scheduled_context_base
        {
        public :
            virtual ~ _scheduled_context_base ( ) { }
            virtual void run ( ) = 0 ;
        } ;
    public :
        template < typename _module >
        class scheduled_context
        : public _scheduled_context_base
        {
            class _scheduled_module
            {
            public :
                static void register_in_scheduler ( ) ;

                template < typename _message >
                static void receive ( _message ) ;
            } ;
        public :
            typedef _scheduled_module module ;
        public :
            scheduled_context ( ) ;
            virtual ~ scheduled_context ( ) ;
            virtual void run ( ) ;
            static void register_in_scheduler ( ) ;
        private :
            static scheduled_context _singleton ;
            int _some_data ;
        } ;
    public :
        static void run ( ) ;
    private :
        static _scheduled_context_container _all_contexts ;
    } ;
} ;

template < typename _module >
void macosx_platform :: platform_scheduler :: scheduled_context < _module > :: _scheduled_module :: register_in_scheduler ( )
{
    _module :: register_in_scheduler ( ) ;
}

template < typename _module >
template < typename _message >
void macosx_platform :: platform_scheduler :: scheduled_context < _module > :: _scheduled_module :: receive ( _message arg )
{
    _module :: receive ( arg ) ;
    ++ _singleton . _some_data ;
}

template < typename _module >
macosx_platform :: platform_scheduler :: scheduled_context < _module > :: scheduled_context ( )
: _some_data ( 0 )
{
}

template < typename _module >
macosx_platform :: platform_scheduler :: scheduled_context < _module > :: ~ scheduled_context ( )
{
}

template < typename _module >
void macosx_platform :: platform_scheduler :: scheduled_context < _module > :: run ( )
{
    std :: cout << "some data = " << _some_data << std :: endl ;
}

template < typename _module >
void macosx_platform :: platform_scheduler :: scheduled_context < _module > :: register_in_scheduler ( )
{
    _all_contexts . insert ( & _singleton ) ;
}

#endif

