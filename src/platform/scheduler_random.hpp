template < typename platform_insider >
class shy_platform_scheduler_random
{
    typedef typename platform_insider :: platform_pointer platform_pointer ;
public :
    template < template < typename mediator > class module >
    class module_wrapper
    {
    public :
        template < typename mediator >
        class scheduled_module
        {
        public :
            void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
            {
                _module . set_mediator ( arg_mediator ) ;
            }
            template < typename message_type >
            void receive ( message_type msg )
            {
                _module . receive ( msg ) ;
            }
        private :
            module < mediator > _module ;
        } ;
    } ;
} ;
