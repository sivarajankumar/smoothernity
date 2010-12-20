#include "assigner.hpp"
#include "binder.hpp"
#include "content.hpp"
#include "fsm_loadable.hpp"
#include "generator.hpp"
#include "parser.hpp"

template 
    < typename _facade
    , template < typename reflection_types > class _reflection
    >
class shy_data_loader_types
{
public :
    typedef _facade facade ;
    template < typename reflection_types >
    class types
    {
    public :
        typedef _reflection < reflection_types > reflection ;
    } ;
} ;

template < typename data_loader_types >
class shy_data_loader
{
    typedef typename data_loader_types :: facade facade ;
    typedef typename data_loader_types :: facade :: mediator mediator ;
    typedef typename data_loader_types :: facade :: mediator :: platform platform ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math platform_math ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename data_loader_types :: facade :: mediator :: platform :: platform_pointer platform_pointer ;

    typedef shy_data_content < shy_data_content_types < platform > > data_content ;

    typedef shy_data_assigner < shy_data_assigner_types < data_content , platform > > data_assigner ;
    typedef shy_data_binder < shy_data_binder_types < data_content , platform > > data_binder ;
    typedef shy_data_generator < shy_data_generator_types < data_content > > data_generator ;
    typedef shy_data_parser < shy_data_parser_types < data_content > > data_parser ;

    class _reflection_types
    {
    public :
        typedef typename data_loader_types :: facade :: mediator mediator ;
        typedef data_binder reflection_binder ;
    } ;

public :
    shy_data_loader ( ) ;
    void bind ( facade & ) ;
    void parse ( std :: string ) ;
    void assign ( ) ;
    std :: string generate ( ) ;
    std :: string error ( ) ;
private :
    data_binder _binder ;
    data_parser _parser ;
    data_assigner _assigner ;
    data_generator _generator ;
    data_content _content ;
} ;

template < typename data_loader_types >
shy_data_loader < data_loader_types > :: shy_data_loader ( )
{
    _binder . set_content ( _content ) ;
    _parser . set_content ( _content ) ;
    _assigner . set_content ( _content ) ;
    _generator . set_content ( _content ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: bind ( facade & arg_facade )
{
    typename platform_pointer :: template pointer < mediator > mediator_obj ;
    typename platform_pointer :: template pointer < data_binder > binder_obj ;
    typename data_loader_types :: template types < _reflection_types > :: reflection reflection ;

    arg_facade . mediator_obj ( mediator_obj ) ;
    platform_pointer :: bind ( binder_obj , _binder ) ;
    reflection . bind_all ( mediator_obj , binder_obj ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: parse ( std :: string line )
{
    _parser . parse ( line ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: assign ( )
{
    _assigner . assign ( ) ;
}

template < typename data_loader_types >
std :: string shy_data_loader < data_loader_types > :: generate ( )
{
    return _generator . generate ( ) ;
}

template < typename data_loader_types >
std :: string shy_data_loader < data_loader_types > :: error ( )
{
    std :: string result ;
    if ( result . empty ( ) )
        result = _parser . error ( ) ;
    if ( result . empty ( ) )
        result = _assigner . error ( ) ;
    return result ;
}

