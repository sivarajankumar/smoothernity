class shy_platform_scheduler_random
{
    static const so_called_lib_std_int32_t _max_scheduled_modules = 100 ;
    static const so_called_lib_std_int32_t _default_max_messages_count = 100 ;
    static const so_called_lib_std_int32_t _default_max_message_size = 32 * 3 ;
    static const so_called_lib_std_int32_t _max_calls_per_run = 10000 ;
    
    class _abstract_scheduled_context
    {
    public :
        virtual ~ _abstract_scheduled_context ( ) ;
        virtual void run ( ) = 0 ;
        virtual void have_messages_to_run ( so_called_lib_std_bool & ) = 0 ;
    } ;
    
    class _abstract_message_invoker
    {
    public :
        virtual ~ _abstract_message_invoker ( ) ;
        virtual void invoke ( ) = 0 ;
    } ;
    
    template < typename _module , typename _message , so_called_lib_std_int32_t _max_message_size >
    class _message_invoker
    : public _abstract_message_invoker
    {
    public :
        _message_invoker ( _message & ) ;
        virtual ~ _message_invoker ( ) ;
        virtual void invoke ( ) ;
    private :
        so_called_lib_std_char _message_data [ _max_message_size ] ;
    } ;
    
    class _message_dummy
    {
    } ;
    
    class _module_dummy
    {
    public :
        template < typename _message >
        static void receive ( _message ) ;
    } ;
    
    template < so_called_lib_std_int32_t _max_message_size >
    class _message_invoker_dummy
    {
        so_called_lib_std_char _data [ sizeof ( _message_invoker < _module_dummy , _message_dummy , _max_message_size > ) ] ;
    } ;
    
    template < so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
    class _messages_queue
    {
    public :
        _messages_queue ( ) ;
    public :
        _message_invoker_dummy < _max_message_size > queue [ _max_messages_count ] ;
        so_called_lib_std_int32_t count ;
        so_called_lib_std_int32_t total_count ;
        so_called_lib_std_int32_t next_to_call ;
    } ;
    
public :
    template 
        < typename _module 
        , so_called_lib_std_int32_t _max_messages_count = _default_max_messages_count
        , so_called_lib_std_int32_t _max_message_size = _default_max_message_size
        >
    class scheduled_context
    : public _abstract_scheduled_context
    {
    public :
        class module
        {
        public :
            template < typename _message >
            static void receive ( _message ) ;
            static void register_in_scheduler ( ) ;
        } ;
    public :
        scheduled_context ( ) ;
        virtual ~ scheduled_context ( ) ;
        virtual void run ( ) ;
        virtual void have_messages_to_run ( so_called_lib_std_bool & ) ;

        static void register_in_scheduler ( ) ;
    private :
        void _switch_queues ( ) ;
        template < typename _message >
        static void _scheduled_receive ( _message ) ;
    private :
        static scheduled_context _singleton ;
        _messages_queue < _max_messages_count , _max_message_size > _queues [ 2 ] ;
        so_called_lib_std_int32_t _accumulation_queue ;
        so_called_lib_std_int32_t _run_queue ;
    } ;
    
public :
    static void init ( ) ;
    static void done ( ) ;
    static void run ( ) ;
private :
    static void _register_context ( _abstract_scheduled_context & context ) ;
private :
    static _abstract_scheduled_context * _contexts [ _max_scheduled_modules ] ;
    static so_called_lib_std_int32_t _contexts_count ;
} ;

template < typename _message >
void shy_platform_scheduler_random :: _module_dummy :: receive ( _message )
{
}

template < typename _module , typename _message , so_called_lib_std_int32_t _max_message_size >
shy_platform_scheduler_random :: _message_invoker < _module , _message , _max_message_size > :: _message_invoker
    ( _message & arg_message )
{
    typename so_called_platform_static_assert :: template shy_static_assert < so_called_lib_std_int32_t ( sizeof ( _message ) ) < _max_message_size > ( ) ;
    ( * reinterpret_cast < _message * > ( & _message_data ) ) = arg_message ;
}

template < typename _module , typename _message , so_called_lib_std_int32_t _max_message_size >
shy_platform_scheduler_random :: _message_invoker < _module , _message , _max_message_size > :: ~ _message_invoker ( )
{
}

template < typename _module , typename _message , so_called_lib_std_int32_t _max_message_size >
void shy_platform_scheduler_random :: _message_invoker < _module , _message , _max_message_size > :: invoke ( )
{
    _module :: receive ( * reinterpret_cast < _message * > ( & _message_data ) ) ;
}

template < so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
shy_platform_scheduler_random :: _messages_queue < _max_messages_count , _max_message_size > :: _messages_queue ( )
{
    count = 0 ;
    total_count = 0 ;
    next_to_call = 0 ;
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
template < typename _message >
void shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: module
    :: receive ( _message msg )
{
    so_called_profile ( so_called_profile_platform_scheduler :: receive ( ) ) ;
    _scheduled_receive ( msg ) ;
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
void shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: module
    :: register_in_scheduler ( )
{
    _module :: register_in_scheduler ( ) ;
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: scheduled_context ( )
: _accumulation_queue ( 0 )
, _run_queue ( 1 )
{
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: ~ scheduled_context ( )
{
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
template < typename _message >
void shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: _scheduled_receive ( _message msg )
{
    _singleton . _queues [ _singleton . _accumulation_queue ] . total_count ++ ;
    if ( _singleton . _queues [ _singleton . _accumulation_queue ] . count < _max_messages_count )
    {
        so_called_lib_std_int32_t index = _singleton . _queues [ _singleton . _accumulation_queue ] . count ++ ;
        void * place = _singleton . _queues [ _singleton . _accumulation_queue ] . queue + index ;
        so_called_lib_std_new ( place ) _message_invoker < _module , _message , _max_message_size > ( msg ) ;
    }
    else
    {
        so_called_trace 
            ( so_called_trace_platform_scheduler_random :: messages_queue_size_exceeds_maximum_size_error 
                ( _singleton . _queues [ _singleton . _accumulation_queue ] . total_count
                , _max_messages_count
                )
            ) ;
    }
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
void shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
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
        so_called_lib_std_int32_t next_to_call = _queues [ _run_queue ] . next_to_call ++ ;
        reinterpret_cast < _abstract_message_invoker * > ( & _queues [ _run_queue ] . queue [ next_to_call ] ) -> invoke ( ) ;
    }
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
void shy_platform_scheduler_random
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: have_messages_to_run ( so_called_lib_std_bool & result )
{
    result = _queues [ _accumulation_queue ] . count 
           + _queues [ _run_queue ] . count 
           - _queues [ _run_queue ] . next_to_call 
           > 0 ;
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
void shy_platform_scheduler_random
    :: scheduled_context < _module , _max_messages_count , _max_message_size > 
    :: _switch_queues ( )
{
    _accumulation_queue = ( _accumulation_queue + 1 ) % 2 ;
    _run_queue = ( _run_queue + 1 ) % 2 ;
}

template < typename _module , so_called_lib_std_int32_t _max_messages_count , so_called_lib_std_int32_t _max_message_size >
void shy_platform_scheduler_random 
    :: scheduled_context < _module , _max_messages_count , _max_message_size >
    :: register_in_scheduler ( )
{
    _register_context ( _singleton ) ;
}
