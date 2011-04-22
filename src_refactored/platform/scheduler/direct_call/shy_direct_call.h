class shy_platform_scheduler_direct_call
{
public :
    template 
        < typename _module 
        , int _max_messages_count = 0 
        , int _max_message_size = 0
        >
    class scheduled_context
    {
    public :
        typedef _module module ;
    public :
        static void register_in_scheduler ( ) ;
    private :
        static scheduled_context _singleton ;
    } ;
public :
    static void init ( ) ;
    static void run ( ) ;
} ;

template < typename _module , int _max_messages_count , int _max_message_size >
void shy_platform_scheduler_direct_call :: scheduled_context < _module , _max_messages_count , _max_message_size > :: register_in_scheduler ( )
{
}
