template < typename platform_insider >
class shy_platform_scheduler_random
{
    typedef typename platform_insider :: platform_pointer platform_pointer ;
    typedef typename platform_insider :: platform_static_assert platform_static_assert ;

    static const int _max_scheduled_modules = 100 ;
    static const int _default_max_messages_count = 100 ;
    static const int _default_max_message_size = 32 * 3 ;
    static const int _max_calls_per_run = 10000 ;
    
    class _abstract_scheduled_module
    {
    public :
        virtual ~ _abstract_scheduled_module ( ) ;
        virtual void run ( ) = 0 ;
        virtual bool have_messages_to_run ( ) = 0 ;
    } ;
    
    class _abstract_message_invoker
    {
    public :
        virtual ~ _abstract_message_invoker ( ) ;
        virtual void invoke ( void * arg_module ) = 0 ;
    } ;
    
    template < typename module , typename message , int max_message_size >
    class _message_invoker
    : public _abstract_message_invoker
    {
    public :
        _message_invoker ( message & arg_message ) ;
        virtual void invoke ( void * arg_module ) ;
    private :
        char _message [ max_message_size ] ;
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
    
    template < int max_message_size >
    class _message_invoker_dummy
    {
        char _data [ sizeof ( _message_invoker < _module_dummy , _message_dummy , max_message_size > ) ] ;
    } ;
    
    template < int max_messages_count , int max_message_size >
    class _messages_queue
    {
    public :
        _messages_queue ( ) ;
    public :
        _message_invoker_dummy < max_message_size > queue [ max_messages_count ] ;
        int count ;
        int total_count ;
        int next_to_call ;
    } ;
    
public :
    template 
        < template < typename mediator > class module 
        , int max_messages_count = _default_max_messages_count
        , int max_message_size = _default_max_message_size
        >
    class module_wrapper
    {
    public :
        template < typename mediator >
        class scheduled_module
        : public _abstract_scheduled_module
        {
        public :
            scheduled_module ( ) ;
            
            template < typename message_type >
            void receive ( message_type msg ) ;
            
            void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
            virtual void run ( ) ;
            virtual bool have_messages_to_run ( ) ;
        private :
            void _switch_queues ( ) ;
        private :
            module < mediator > _module ;
            _messages_queue < max_messages_count , max_message_size > _queues [ 2 ] ;
            int _accumulation_queue ;
            int _run_queue ;
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
template < typename module , typename message , int max_message_size >
shy_platform_scheduler_random < platform_insider > :: _message_invoker < module , message , max_message_size > :: _message_invoker
    ( message & arg_message )
{
    typename platform_static_assert :: template static_assert < int ( sizeof ( message ) ) < max_message_size > ( ) ;
    ( * reinterpret_cast < message * > ( & _message ) ) = arg_message ;
}

template < typename platform_insider >
template < typename module , typename message , int max_message_size >
void shy_platform_scheduler_random < platform_insider > :: _message_invoker < module , message , max_message_size > :: invoke ( void * arg_module )
{
    reinterpret_cast < module * > ( arg_module ) -> receive ( * reinterpret_cast < message * > ( & _message ) ) ;
}

template < typename platform_insider >
template < typename message >
void shy_platform_scheduler_random < platform_insider > :: _module_dummy :: receive ( message msg )
{
}

template < typename platform_insider >
template < int max_messages_count , int max_message_size >
shy_platform_scheduler_random < platform_insider > :: _messages_queue < max_messages_count , max_message_size > :: _messages_queue ( )
{
    count = 0 ;
    total_count = 0 ;
    next_to_call = 0 ;
}

template < typename platform_insider >
shy_platform_scheduler_random < platform_insider > :: scheduler :: scheduler ( )
{
    _count = 0;
    for ( int i = 0 ; i < _max_scheduled_modules ; i ++ )
        _modules [ i ] = 0 ;
}

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
shy_platform_scheduler_random < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: scheduled_module ( )
: _accumulation_queue ( 0 )
, _run_queue ( 1 )
{
}

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
void shy_platform_scheduler_random < platform_insider > 
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
void shy_platform_scheduler_random < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: receive ( message_type msg )
{
    if ( _queues [ _accumulation_queue ] . count < max_messages_count )
    {
        int index = _queues [ _accumulation_queue ] . count ++ ;
        void * place = _queues [ _accumulation_queue ] . queue + index ;
        new ( place ) _message_invoker < module < mediator > , message_type , max_message_size > ( msg ) ;
    }
    _queues [ _accumulation_queue ] . total_count ++ ;
}

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
void shy_platform_scheduler_random < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: run ( )
{
    if ( _queues [ _run_queue ] . next_to_call >= _queues [ _run_queue ] . count )
    {
        _switch_queues ( ) ;
        _queues [ _accumulation_queue ] . count = 0 ;
        _queues [ _accumulation_queue ] . total_count = 0 ;
        _queues [ _accumulation_queue ] . next_to_call = 0 ;
    }
    if ( _queues [ _run_queue ] . next_to_call < _queues [ _run_queue ] . count )
    {
        int next_to_call = _queues [ _run_queue ] . next_to_call ++ ;
        reinterpret_cast < _abstract_message_invoker * > ( & _queues [ _run_queue ] . queue [ next_to_call ] ) -> invoke ( & _module ) ;
    }
}

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
bool shy_platform_scheduler_random < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: have_messages_to_run ( )
{
    return _queues [ _accumulation_queue ] . count 
         + _queues [ _run_queue ] . count 
         - _queues [ _run_queue ] . next_to_call 
         > 0 ;
}

template < typename platform_insider >
template < template < typename mediator > class module , int max_messages_count , int max_message_size >
template < typename mediator >
void shy_platform_scheduler_random < platform_insider > 
    :: module_wrapper < module , max_messages_count , max_message_size > 
    :: scheduled_module < mediator > 
    :: _switch_queues ( )
{
    _accumulation_queue = ( _accumulation_queue + 1 ) % 2 ;
    _run_queue = ( _run_queue + 1 ) % 2 ;
}

template < typename platform_insider >
template < typename module_type >
void shy_platform_scheduler_random < platform_insider > :: register_module_in_scheduler ( module_type & module , scheduler & arg_scheduler )
{
    if ( arg_scheduler . _count < _max_scheduled_modules )
        arg_scheduler . _modules [ arg_scheduler . _count ++ ] = ( _abstract_scheduled_module * ) & module ;
}

template < typename platform_insider >
void shy_platform_scheduler_random < platform_insider > :: run ( scheduler & arg_scheduler )
{
    bool keep_running = false ;
    int calls_performed = 0 ;
    do
    {
        for ( int i = 0 ; i < arg_scheduler . _count ; i ++ )
        {
            int first_index = rand ( ) % arg_scheduler . _count ;
            int second_index = rand ( ) % arg_scheduler . _count ;
            _abstract_scheduled_module * first_module = arg_scheduler . _modules [ first_index ] ;
            arg_scheduler . _modules [ first_index ] = arg_scheduler . _modules [ second_index ] ;
            arg_scheduler . _modules [ second_index ] = first_module ;
        }
        for ( int i = 0 ; i < arg_scheduler . _count ; i ++ )
            arg_scheduler . _modules [ i ] -> run ( ) ;
        keep_running = false ;
        for ( int i = 0 ; i < arg_scheduler . _count ; i ++ )
            keep_running |= arg_scheduler . _modules [ i ] -> have_messages_to_run ( ) ;
        calls_performed ++ ;
    } while ( keep_running && calls_performed < _max_calls_per_run ) ;
}
