template < typename platform_insider >
class shy_platform_scheduler_random
{
    typedef typename platform_insider :: platform_pointer platform_pointer ;

    class abstract_scheduled_module
    {
    public :
        virtual ~ abstract_scheduled_module ( ) ;
        virtual void run ( ) = 0 ;
    } ;
    
public :
    template < template < typename mediator > class module >
    class module_wrapper
    {
    public :
        template < typename mediator >
        class scheduled_module
        : public abstract_scheduled_module
        {
        public :
            template < typename message_type >
            void receive ( message_type msg ) ;
            
            void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
            virtual void run ( ) ;
        private :
            module < mediator > _module ;
        } ;
    } ;
    
    class scheduler
    {
    } ;
    
public :
    template < typename module_type >
    static void register_module_in_scheduler ( module_type & module , scheduler & arg_scheduler ) ;
    
    static void run ( scheduler & arg_scheduler ) ;
} ;

template < typename platform_insider >
shy_platform_scheduler_random < platform_insider > :: abstract_scheduled_module :: ~ abstract_scheduled_module ( )
{
}

template < typename platform_insider >
template < template < typename mediator > class module >
template < typename mediator >
void shy_platform_scheduler_random < platform_insider > :: module_wrapper < module > :: scheduled_module < mediator > :: set_mediator
    ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _module . set_mediator ( arg_mediator ) ;
}

template < typename platform_insider >
template < template < typename mediator > class module >
template < typename mediator >
template < typename message_type >
void shy_platform_scheduler_random < platform_insider > :: module_wrapper < module > :: scheduled_module < mediator > :: receive ( message_type msg )
{
    _module . receive ( msg ) ;
}

template < typename platform_insider >
template < template < typename mediator > class module >
template < typename mediator >
void shy_platform_scheduler_random < platform_insider > :: module_wrapper < module > :: scheduled_module < mediator > :: run ( )
{
}

template < typename platform_insider >
template < typename module_type >
void shy_platform_scheduler_random < platform_insider > :: register_module_in_scheduler ( module_type & module , scheduler & arg_scheduler )
{
}

template < typename platform_insider >
void shy_platform_scheduler_random < platform_insider > :: run ( scheduler & arg_scheduler )
{
}
