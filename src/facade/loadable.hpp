#include "../data/assigner.hpp"
#include "../data/binder.hpp"
#include "../data/content.hpp"
#include "../data/fsm_loadable.hpp"
#include "../data/generator.hpp"
#include "../data/parser.hpp"
#include "../common/reflection.hpp"

template < typename platform >
class shy_facade_loadable
: public shy_facade_interface
{
    typedef shy_composer < platform , shy_fsm_collection_loadable > composer ;
    typedef typename composer :: mediator mediator ;
    typedef typename platform :: platform_pointer platform_pointer ;

    typedef shy_data_content < shy_data_content_types < platform > > data_content ;

    typedef shy_data_assigner < shy_data_assigner_types < data_content , platform > > data_assigner ;
    typedef shy_data_binder < shy_data_binder_types < data_content , platform > > data_binder ;
    typedef shy_data_generator < shy_data_generator_types < data_content > > data_generator ;
    typedef shy_data_parser < shy_data_parser_types < data_content > > data_parser ;

    class _reflection_types
    {
    public :
        typedef typename composer :: mediator mediator ;
        typedef data_binder reflection_binder ;
    } ;

public :
    shy_facade_loadable ( typename platform_pointer :: template pointer < const platform > ) ;
    virtual ~ shy_facade_loadable ( ) ;

    virtual void init ( ) ;
    virtual void done ( ) ;
    virtual void render ( ) ;
    virtual void update ( ) ;
    virtual void video_mode_changed ( ) ;

    std :: string error ( ) ;
private :
    composer _composer ;
    shy_fsm_collection_loadable _fsm_collection ;
    data_binder _binder ;
    data_parser _parser ;
    data_assigner _assigner ;
    data_generator _generator ;
    data_content _content ;
} ;

template < typename platform >
shy_facade_loadable < platform > :: shy_facade_loadable ( typename platform_pointer :: template pointer < const platform > platform_ptr )
{
    _binder . set_content ( _content ) ;
    _parser . set_content ( _content ) ;
    _assigner . set_content ( _content ) ;
    _generator . set_content ( _content ) ;

    typename platform_pointer :: template pointer < shy_fsm_collection_loadable > fsm_collection_ptr ;
    platform_pointer :: bind ( fsm_collection_ptr , _fsm_collection ) ;
    _composer . register_components ( platform_ptr , fsm_collection_ptr ) ;

    typename platform_pointer :: template pointer < mediator > mediator_obj ;
    typename platform_pointer :: template pointer < data_binder > binder_obj ;
    shy_reflection < _reflection_types > reflection ;

    _composer . mediator_obj ( mediator_obj ) ;
    platform_pointer :: bind ( binder_obj , _binder ) ;
    reflection . bind_modules ( mediator_obj , binder_obj ) ;

    while ( ! std :: cin . eof ( ) )
    {
        std :: string line ;
        std :: getline ( std :: cin , line ) ;
        _parser . parse ( line ) ;
    }

    _parser . parse ( "#" ) ;
    _assigner . assign ( ) ;

    if ( _parser . error ( ) . empty ( ) && _assigner . error ( ) . empty ( ) )
        std :: cout << _generator . generate ( ) << std :: endl ;
}

template < typename platform >
shy_facade_loadable < platform > :: ~ shy_facade_loadable ( )
{
}

template < typename platform >
void shy_facade_loadable < platform > :: init ( )
{
    _composer . init ( ) ;
}

template < typename platform >
void shy_facade_loadable < platform > :: done ( )
{
    _composer . done ( ) ;
}

template < typename platform >
void shy_facade_loadable < platform > :: update ( )
{
    _composer . update ( ) ;
}

template < typename platform >
void shy_facade_loadable < platform > :: render ( )
{
    _composer . render ( ) ;
}

template < typename platform >
void shy_facade_loadable < platform > :: video_mode_changed ( )
{
    _composer . video_mode_changed ( ) ;
}

template < typename data_loader_types >
std :: string shy_facade_loadable < data_loader_types > :: error ( )
{
    std :: string result ;
    if ( result . empty ( ) )
        result = _parser . error ( ) ;
    if ( result . empty ( ) )
        result = _assigner . error ( ) ;
    return result ;
}

