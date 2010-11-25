template 
    < typename facade
    , template < typename context > class reflection
    >
class shy_data_loader
{
    typedef typename facade :: mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename facade :: mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename facade :: mediator :: platform :: platform_pointer platform_pointer ;

    class context
    {
    public :
        typedef typename facade :: mediator mediator ;

        class reflection_binder
        {
        public :
            reflection_binder ( )
            : _modules ( 0 )
            , _consts ( 0 )
            {
            }
            void module ( const char * name )
            {
                ++ _modules ;
                std :: cout << std :: endl ;
                std :: cout << std :: string ( "consts " ) << std :: string ( name ) << std :: endl ;
            }
            void bind ( const char * name , const num_fract & value )
            {
                ++ _consts ;
                std :: cout << std :: string ( "    " ) << std :: string ( name ) << std :: endl ;
            }
            void bind ( const char * name , const num_whole & value )
            {
                ++ _consts ;
                std :: cout << std :: string ( "    " ) << std :: string ( name ) << std :: endl ;
            }
            void report ( )
            {
                std :: cout << std :: endl ;
                std :: cout << std :: string ( "summary: " ) << _consts << std::string ( " consts in " ) << _modules << std :: string ( " modules" ) << std :: endl ;
            }
        private :
            int _modules ;
            int _consts ;
        } ;
    } ;

public :
    void load ( facade & arg_facade )
    {
        typename platform_pointer :: template pointer < typename facade :: mediator > mediator_obj ;
        typename platform_pointer :: template pointer < typename context :: reflection_binder > reflection_binder_obj ;
        arg_facade . mediator_obj ( mediator_obj ) ;
        platform_pointer :: bind ( reflection_binder_obj , _reflection_binder ) ;
        _reflection . bind_all ( mediator_obj , reflection_binder_obj ) ;
        _reflection_binder . report ( ) ;
    }

private :
    reflection < context > _reflection ; 
    typename context :: reflection_binder _reflection_binder ;
} ;

