template 
    < typename facade
    , template < typename context > class reflection
    >
class shy_data_loader
{
    typedef typename facade :: mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename facade :: mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename facade :: mediator :: platform :: platform_pointer platform_pointer ;

    class reflection_attributes_type
    {
    public :
        typedef std :: map < std :: string , num_fract * > name_to_fract_type ;
        typedef std :: map < std :: string , num_whole * > name_to_whole_type ;

        name_to_fract_type name_to_fract ;
        name_to_whole_type name_to_whole ;
    } ;

    class reflection_modules_type
    {
    public :
        typedef std :: map < std :: string , reflection_attributes_type > name_to_module_type ;
        name_to_module_type name_to_module ;
    } ;

    class reflection_binder_type
    {
    public :
        reflection_binder_type ( )
        : _modules ( 0 )
        , _current_attributes ( 0 )
        {
        }
        void set_modules ( reflection_modules_type & modules )
        {
            _modules = & modules ;
        }
        void module ( std :: string name )
        {
            _modules -> name_to_module [ name ] = reflection_attributes_type ( ) ;
            _current_attributes = & ( _modules -> name_to_module [ name ] ) ;
        }
        void bind ( std :: string name , const num_fract & value )
        {
            if ( _current_attributes )
                _current_attributes -> name_to_fract [ name ] = const_cast < num_fract * > ( & value ) ;
        }
        void bind ( std :: string name , const num_whole & value )
        {
            if ( _current_attributes )
                _current_attributes -> name_to_whole [ name ] = const_cast < num_whole * > ( & value ) ;
        }
    public :
        reflection_modules_type * _modules ;
        reflection_attributes_type * _current_attributes ;
    } ;

    class reflection_context_type
    {
    public :
        typedef typename facade :: mediator mediator ;
        typedef reflection_binder_type reflection_binder ;
    } ;

public :
    void load ( facade & arg_facade )
    {
        typename platform_pointer :: template pointer < typename facade :: mediator > mediator_obj ;
        typename platform_pointer :: template pointer < reflection_binder_type > reflection_binder_obj ;
        arg_facade . mediator_obj ( mediator_obj ) ;
        platform_pointer :: bind ( reflection_binder_obj , _reflection_binder ) ;
        _reflection_binder . set_modules ( _reflection_modules ) ;
        reflection < reflection_context_type > ( ) . bind_all ( mediator_obj , reflection_binder_obj ) ;
        _report ( ) ;
    }
private :
    void _report ( )
    {
        int modules = 0 ;
        int consts = 0 ;
        for ( typename reflection_modules_type :: name_to_module_type :: const_iterator module_i = _reflection_modules . name_to_module . begin ( )
            ; module_i != _reflection_modules . name_to_module . end ( )
            ; ++ module_i
            )
        {
            std :: string module_name = module_i -> first ;
            const reflection_attributes_type & attributes = module_i -> second ;

            ++ modules ;
            std :: cout << std :: endl ;
            std :: cout << std :: string ( "consts " ) << std :: string ( module_name ) << std :: endl ;

            for ( typename reflection_attributes_type :: name_to_fract_type :: const_iterator fract_i = attributes . name_to_fract . begin ( )
                ; fract_i != attributes . name_to_fract . end ( )
                ; ++ fract_i
                )
            {
                ++ consts ;
                std :: string fract_name = fract_i -> first ;
                std :: cout << std :: string ( "    " ) << std :: string ( fract_name ) << std :: endl ;
            }

            for ( typename reflection_attributes_type :: name_to_whole_type :: const_iterator whole_i = attributes . name_to_whole . begin ( )
                ; whole_i != attributes . name_to_whole . end ( )
                ; ++ whole_i
                )
            {
                ++ consts ;
                std :: string whole_name = whole_i -> first ;
                std :: cout << std :: string ( "    " ) << std :: string ( whole_name ) << std :: endl ;
            }
        }
        std :: cout << std :: endl ;
        std :: cout << std :: string ( "summary: " ) << consts << std :: string ( " consts in " ) << modules << std :: string ( " modules" ) << std :: endl ;
    }
private :
    reflection_binder_type _reflection_binder ;
    reflection_modules_type _reflection_modules ;
} ;

