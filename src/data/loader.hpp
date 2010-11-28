#include "assigner.hpp"
#include "binder.hpp"
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

    class _consts
    {
    public :
    } ;

    class _reflection_attribute_fract_type
    {
    public :
        _reflection_attribute_fract_type ( ) ;
    public :
        num_fract * binding ;
        std :: string numerator_sign ;
        std :: string numerator_value ;
        std :: string denominator_sign ;
        std :: string denominator_value ;
    } ;

    class _reflection_attribute_whole_type
    {
    public :
        _reflection_attribute_whole_type ( ) ;
    public :
        num_whole * binding ;
        std :: string sign ;
        std :: string value ;
    } ;

    class _reflection_attributes_type
    {
    public :
        typedef std :: map < std :: string , num_fract * > name_to_fract_type ;
        typedef std :: map < std :: string , num_whole * > name_to_whole_type ;
        name_to_fract_type name_to_fract ;
        name_to_whole_type name_to_whole ;
    } ;

    class _reflection_modules_type
    {
    public :
        typedef _reflection_attributes_type data_modules_attributes ;
        typedef std :: map < std :: string , _reflection_attributes_type > name_to_module_type ;
        name_to_module_type name_to_module ;
    } ;

    typedef shy_data_assigner < shy_data_assigner_types < _reflection_modules_type , platform > > _reflection_assigner_type ;
    typedef shy_data_binder < shy_data_binder_types < _reflection_modules_type , platform > > _reflection_binder_type ;
    typedef shy_data_generator < shy_data_generator_types < _reflection_modules_type > > _reflection_generator_type ;
    typedef shy_data_parser < shy_data_parser_types < _reflection_modules_type , platform > > _reflection_parser_type ;

    class _reflection_types
    {
    public :
        typedef typename data_loader_types :: facade :: mediator mediator ;
        typedef _reflection_binder_type reflection_binder ;
    } ;

public :
    shy_data_loader ( ) ;
    void bind ( facade & ) ;
    void parse ( std :: string ) ;
    void assign ( ) ;
    std :: string generate ( ) ;
    std :: string error ( ) ;
private :
    _reflection_binder_type _reflection_binder ;
    _reflection_parser_type _reflection_parser ;
    _reflection_assigner_type _reflection_assigner ;
    _reflection_generator_type _reflection_generator ;
    _reflection_modules_type _reflection_modules ;
} ;

template < typename data_loader_types >
shy_data_loader < data_loader_types > :: shy_data_loader ( )
{
    _reflection_binder . set_modules ( _reflection_modules ) ;
    _reflection_parser . set_modules ( _reflection_modules ) ;
    _reflection_assigner . set_modules ( _reflection_modules ) ;
    _reflection_generator . set_modules ( _reflection_modules ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: bind ( facade & arg_facade )
{
    typename platform_pointer :: template pointer < mediator > mediator_obj ;
    typename platform_pointer :: template pointer < _reflection_binder_type > reflection_binder_obj ;
    typename data_loader_types :: template types < _reflection_types > :: reflection reflection ;

    arg_facade . mediator_obj ( mediator_obj ) ;
    platform_pointer :: bind ( reflection_binder_obj , _reflection_binder ) ;
    reflection . bind_all ( mediator_obj , reflection_binder_obj ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: parse ( std :: string line )
{
    _reflection_parser . parse ( line ) ;
}

template < typename data_loader_types >
void shy_data_loader < data_loader_types > :: assign ( )
{
    _reflection_assigner . assign ( ) ;
}

template < typename data_loader_types >
std :: string shy_data_loader < data_loader_types > :: generate ( )
{
    return _reflection_generator . generate ( ) ;
}

template < typename data_loader_types >
std :: string shy_data_loader < data_loader_types > :: error ( )
{
    std :: string result ;
    if ( result . empty ( ) )
        result = _reflection_parser . error ( ) ;
    if ( result . empty ( ) )
        result = _reflection_assigner . error ( ) ;
    return result ;
}

