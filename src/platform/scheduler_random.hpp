template < typename platform_insider >
class shy_platform_scheduler_random
{
    typedef typename platform_insider :: platform_pointer platform_pointer ;

    static const int _max_scheduled_modules = 100 ;
    static const int _max_message_size = 100 ;
    static const int _max_messages_count = 100 ;
    
    class _abstract_scheduled_module
    {
    public :
        virtual ~ _abstract_scheduled_module ( ) ;
        virtual void run ( ) = 0 ;
    } ;
    
    class _abstract_message_invoker
    {
    public :
        virtual ~ _abstract_message_invoker ( ) ;
        virtual void invoke ( void * arg_module ) = 0 ;
    } ;
    
    template < typename module , typename message >
    class _message_invoker
    : public _abstract_message_invoker
    {
    public :
        virtual void invoke ( void * arg_module ) ;
    private :
        char _message [ _max_message_size ] ;
    } ;
    
    class _message_dummy
    {
    } ;
    
    class _module_dummy
    {
    public :
        template < typename message >
        void receive ( message msg ) ;
    } ;
    
    class _message_invoker_dummy
    {
        char _data [ sizeof ( _message_invoker < _module_dummy , _message_dummy > ) ] ;
    } ;
    
    class _messages_queue
    {
    public :
        _messages_queue ( ) ;
    public :
        _message_invoker_dummy queue [ _max_messages_count ] ;
        int count ;
    } ;
    
public :
    template < template < typename mediator > class module >
    class module_wrapper
    {
    public :
        template < typename mediator >
        class scheduled_module
        : public _abstract_scheduled_module
        {
        public :
            template < typename message_type >
            void receive ( message_type msg ) ;
            
            void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
            virtual void run ( ) ;
        private :
            module < mediator > _module ;
            _messages_queue _run_queue ;
            _messages_queue _accumulation_queue ;
        } ;
    } ;
    
    class scheduler
    {
        friend class shy_platform_scheduler_random ;
    public :
        scheduler ( ) ;
    private :
        _abstract_scheduled_module * _modules [ _max_scheduled_modules ] ;
        int _count ;
    } ;
    
public :
    template < typename module_type >
    static void register_module_in_scheduler ( module_type & module , scheduler & arg_scheduler ) ;
    
    static void run ( scheduler & arg_scheduler ) ;
} ;

template < typename platform_insider >
shy_platform_scheduler_random < platform_insider > :: _abstract_scheduled_module :: ~ _abstract_scheduled_module ( )
{
}

template < typename platform_insider >
shy_platform_scheduler_random < platform_insider > :: _abstract_message_invoker :: ~ _abstract_message_invoker ( )
{
}

template < typename platform_insider >
template < typename module , typename message >
void shy_platform_scheduler_random < platform_insider > :: _message_invoker < module , message > :: invoke ( void * arg_module )
{
}

template < typename platform_insider >
template < typename message >
void shy_platform_scheduler_random < platform_insider > :: _module_dummy :: receive ( message msg )
{
}

template < typename platform_insider >
shy_platform_scheduler_random < platform_insider > :: _messages_queue :: _messages_queue ( )
{
    count = 0 ;
}

template < typename platform_insider >
shy_platform_scheduler_random < platform_insider > :: scheduler :: scheduler ( )
{
    _count = 0;
    for ( int i = 0 ; i < _max_scheduled_modules ; i ++ )
        _modules [ i ] = 0 ;
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
    arg_scheduler . _modules [ arg_scheduler . _count ++ ] = ( _abstract_scheduled_module * ) & module ;
}

template < typename platform_insider >
void shy_platform_scheduler_random < platform_insider > :: run ( scheduler & arg_scheduler )
{
    for ( int i = 0 ; i < arg_scheduler . _count ; i ++ )
        arg_scheduler . _modules [ i ] -> run ( ) ;
}
