shy_platform_scheduler_random :: _abstract_scheduled_context * shy_platform_scheduler_random :: _contexts [ _max_scheduled_modules ] ;
int shy_platform_scheduler_random :: _contexts_count = 0 ;

shy_platform_scheduler_random :: _abstract_scheduled_context :: ~ _abstract_scheduled_context ( )
{
}

shy_platform_scheduler_random :: _abstract_message_invoker :: ~ _abstract_message_invoker ( )
{
}

void shy_platform_scheduler_random :: init ( )
{
    _message_dummy my_message ;
    _message_invoker < _module_dummy , _message_dummy , _default_max_message_size > my_invoker ( my_message ) ;
    my_invoker . invoke ( ) ;

    _contexts_count = 0 ;
    for ( int i = 0 ; i < _max_scheduled_modules ; i ++ )
        _contexts [ i ] = 0 ;
}

void shy_platform_scheduler_random :: _register_context ( _abstract_scheduled_context & context )
{
    if ( _contexts_count < _max_scheduled_modules )
        _contexts [ _contexts_count ++ ] = & context ;
}

void shy_platform_scheduler_random :: run ( )
{
    bool keep_running = false ;
    int calls_performed = 0 ;
    do
    {
        for ( int i = 0 ; i < _contexts_count ; i ++ )
        {
            int first_index = rand ( ) % _contexts_count ;
            int second_index = rand ( ) % _contexts_count ;
            _abstract_scheduled_context * first_context = _contexts [ first_index ] ;
            _contexts [ first_index ] = _contexts [ second_index ] ;
            _contexts [ second_index ] = first_context ;
        }
        for ( int i = 0 ; i < _contexts_count ; i ++ )
            _contexts [ i ] -> run ( ) ;
        keep_running = false ;
        for ( int i = 0 ; i < _contexts_count ; i ++ )
        {
            bool have_messages_to_run = false ;
            _contexts [ i ] -> have_messages_to_run ( have_messages_to_run ) ;
            keep_running |= have_messages_to_run ;
        }
        calls_performed ++ ;
    }
    while ( keep_running && calls_performed < _max_calls_per_run ) ;
}

