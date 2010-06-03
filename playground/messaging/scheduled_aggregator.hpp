template < typename messages >
union cumulative_message
{
    typename messages :: start start ;
    typename messages :: activate_first_module activate_first_module ;
    typename messages :: activate_second_module activate_second_module ;
    typename messages :: on_some_event on_some_event ;
} ;

template < typename type , int max_size >
class static_array
{
public :
    static_array ( )
    : _count ( 0 )
    {
    }
    void add ( type obj )
    {
        _data [ _count ++ ] = obj ;
    }
    int count ( )
    {
        return _count ;
    }
    type & at ( int i )
    {
        return _data [ i ] ;
    }
    void reset ( )
    {
        _count = 0 ;
    }
    type & last ( )
    {
        return _data [ _count - 1 ] ;
    }
private :
    type _data [ max_size ] ;
    int _count ;
} ;

class abstract_invoker
{
public :
    virtual ~ abstract_invoker ( )
    {
    }
    virtual void invoke ( ) = 0 ;
} ;

template < typename module , typename message , typename messages >
class invoker
: public abstract_invoker
{
public :
    invoker ( )
    {
    }
    invoker ( message msg , module * obj )
    : _obj ( obj )
    {
        ( * reinterpret_cast < message * > ( & _msg ) ) = msg ;
    }
    void invoke ( )
    {
        _obj -> receive ( * reinterpret_cast < message * > ( & _msg ) ) ;
    }
private :
    cumulative_message < messages > _msg ;
    module * _obj ;
} ;

template
    < template < typename mediator > class module
    , typename mediator
    >
class scheduled_module
{
    static const int _max_scheduled_messages = 100 ;
    typedef typename mediator :: messages messages ;
    class dummy_message
    {
    } ;
    class dummy_module
    {
    public :
        void receive ( dummy_message msg )
        {
            printf ( "dummy receive\n" ) ;
        }
    } ;
    class dummy_invoker
    {
    public :
        char data [ sizeof ( invoker < dummy_module , dummy_message , messages > ) ] ;
    } ;
public :
    scheduled_module ( mediator * arg_mediator )
    : _module ( arg_mediator )
    , _selector ( 0 )
    {
    }
    template < typename message >
    void receive ( message msg )
    {
        invoker < module < mediator > , message , messages > msg_invoker ( msg , & _module ) ;
        _scheduled [ _selector ] . add ( * reinterpret_cast < dummy_invoker * > ( & msg_invoker ) ) ;
    }
    void run_scheduler ( )
    {
        if ( _scheduled [ _selector ] . count ( ) > 0 )
        {
            _selector = ( _selector + 1 ) % 2 ;
            for ( int i = 0 ; i < _scheduled [ ( _selector + 1 ) % 2 ] . count ( ) ; i ++ )
            {
                abstract_invoker * abs_invoker = reinterpret_cast < abstract_invoker * > ( & _scheduled [ ( _selector + 1 ) % 2 ] . at ( i ) ) ;
                abs_invoker -> invoke ( ) ;
            }
            _scheduled [ ( _selector + 1 ) % 2 ] . reset ( ) ;
        }
    }
private :
    module < mediator > _module ;
    static_array < dummy_invoker , _max_scheduled_messages > _scheduled [ 2 ] ;
    int _selector ;
} ;

template 
    < template < typename mediator > class _first_module
    , template < typename mediator > class _second_module
    , template < typename mediator > class _controller
    >
class scheduled_mediator_types
{
public :
    template < typename mediator >
    class modules
    {
    public :
        typedef scheduled_module < _first_module , mediator > first_module ;
        typedef scheduled_module < _second_module , mediator > second_module ;
        typedef scheduled_module < _controller , mediator > controller ;
    } ;
} ;

template 
    < template < typename > class first_module
    , template < typename > class second_module
    , template < typename > class controller
    , template < typename , typename > class mediator
    , typename messages
    >
class scheduled_aggregator
{
public :
    scheduled_aggregator ( )
    : _first_module ( & _mediator )
    , _second_module ( & _mediator )
    , _controller ( & _mediator )
    {
        _mediator . register_modules 
            ( & _first_module 
            , & _second_module 
            , & _controller 
            ) ;
    }
    void start ( )
    {
        _mediator . send ( typename messages :: start ( ) ) ;
        _run_scheduler ( ) ;
    }
    void on_some_event ( int arg )
    {
        typename messages :: on_some_event msg ;
        msg . arg = arg ;
        _mediator . send ( msg ) ;
        _run_scheduler ( ) ;
    }
private :
    void _run_scheduler ( )
    {
        _first_module . run_scheduler ( ) ;
        _second_module . run_scheduler ( ) ;
        _controller . run_scheduler ( ) ;
    }
private :
    typedef mediator 
        < scheduled_mediator_types
            < first_module 
            , second_module 
            , controller
            >
        , messages
        > mediator_type ;
    mediator_type _mediator ;
    scheduled_module < first_module , mediator_type > _first_module ;
    scheduled_module < second_module , mediator_type > _second_module ;
    scheduled_module < controller , mediator_type > _controller ;
} ;
