template < typename platform_insider >
class shy_platform_scheduler_direct_call
{
    typedef typename platform_insider :: platform_pointer platform_pointer ;
    typedef typename platform_insider :: platform_static_assert platform_static_assert ;

public :
    template 
        < template < typename mediator > class module 
        , int max_messages_count = 0
        , int max_message_size = 0
        >
    class module_wrapper
    {
    public :
        template < typename mediator >
        class scheduled_module
        {
        public :
            template < typename message_type >
            void receive ( message_type ) ;
            
            void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
        private :
            module < mediator > _module ;
        } ;
    } ;
    
    class scheduler
    {
    } ;
    
public :
    template < typename module_type >
    static void register_module_in_scheduler 
        ( typename platform_pointer :: template pointer < module_type > 
        , typename platform_pointer :: template pointer < scheduler > 
        ) ;
    
    static void run ( typename platform_pointer :: template pointer < scheduler > ) ;
} ;

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
void shy_platform_scheduler_direct_call < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _module . set_mediator ( arg_mediator ) ;
}

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
template < typename message_type >
void shy_platform_scheduler_direct_call < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: receive ( message_type msg )
{
    _module . receive ( msg ) ;
}

template < typename platform_insider >
template < typename module_type >
void shy_platform_scheduler_direct_call < platform_insider > :: register_module_in_scheduler
    ( typename platform_pointer :: template pointer < module_type > 
    , typename platform_pointer :: template pointer < scheduler > 
    )
{
}

template < typename platform_insider >
void shy_platform_scheduler_direct_call < platform_insider > :: run ( typename platform_pointer :: template pointer < scheduler > )
{
}
