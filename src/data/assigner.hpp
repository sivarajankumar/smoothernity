template
    < typename _data_content
    , typename _platform
    >
class shy_data_assigner_types
{
public :
    typedef _data_content data_content ;
    typedef _platform platform ;
} ;

template < typename data_assigner_types >
class shy_data_assigner
{
    typedef typename data_assigner_types :: data_content data_content ;
    typedef typename data_assigner_types :: data_content :: data_content_attributes data_content_attributes ;
    typedef typename data_assigner_types :: data_content :: data_content_attributes_container data_content_attributes_container ;
    typedef typename data_assigner_types :: data_content :: data_content_fract data_content_fract ;
    typedef typename data_assigner_types :: data_content :: data_content_fract_container data_content_fract_container ;
    typedef typename data_assigner_types :: data_content :: data_content_whole data_content_whole ;
    typedef typename data_assigner_types :: data_content :: data_content_whole_container data_content_whole_container ;
    typedef typename data_assigner_types :: platform :: platform_math platform_math ;

    class _consts
    {
    public :
        static std :: string error_no_value_assigned_to_module_attribute ( std :: string module , std :: string attribute ) { return std :: string ( "no value assigned to module '" ) + module + std :: string ( "' attribute '" ) + attribute + std :: string ( "'" ) ; }
    } ;

public :
    shy_data_assigner ( ) ;
    void set_content ( data_content & ) ;
    void assign ( ) ;
    std :: string error ( ) ;
private :
    data_content * _content ;
    std :: string _error ;
} ;

template < typename data_assigner_types >
shy_data_assigner < data_assigner_types > :: shy_data_assigner ( )
: _content ( 0 )
{
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: set_content ( data_content & content )
{
    _content = & content ;
}

template < typename data_assigner_types >
void shy_data_assigner < data_assigner_types > :: assign ( )
{
    for ( typename data_content_attributes_container :: const_iterator content_i = _content -> modules . begin ( )
        ; content_i != _content -> modules . end ( )
        ; ++ content_i
        )
    {
        std :: string module_name = content_i -> first ;
        const data_content_attributes & attributes = content_i -> second ;
        for ( typename data_content_whole_container :: const_iterator attribute_i = attributes . name_to_whole . begin ( )
            ; attribute_i != attributes . name_to_whole . end ( )
            ; ++ attribute_i
            )
        {
            std :: string whole_name = attribute_i -> first ;
            const data_content_whole & whole = attribute_i -> second ;
            
            std :: string string_value = whole . sign + whole . value ;
            if ( string_value . empty ( ) )
                _error = _consts :: error_no_value_assigned_to_module_attribute ( module_name , whole_name ) ;
            else
            {
                int int_value = 0 ;
                std :: istringstream ( string_value ) >> int_value ;
                platform_math :: make_num_whole ( * whole . binding , int_value ) ;
            }
        }
        for ( typename data_content_fract_container :: const_iterator attribute_i = attributes . name_to_fract . begin ( )
            ; attribute_i != attributes . name_to_fract . end ( )
            ; ++ attribute_i
            )
        {
            std :: string fract_name = attribute_i -> first ;
            const data_content_fract & fract = attribute_i -> second ;
            
            std :: string string_numerator = fract . numerator_sign + fract . numerator_value ;
            std :: string string_denominator = fract . denominator_sign + fract . denominator_value ;
            if ( string_numerator . empty ( ) || string_denominator . empty ( ) )
                _error = _consts :: error_no_value_assigned_to_module_attribute ( module_name , fract_name ) ;
            else
            {
                int int_numerator = 0 ;
                int int_denominator = 0 ;
                std :: istringstream ( string_numerator ) >> int_numerator ;
                std :: istringstream ( string_denominator ) >> int_denominator ;
                platform_math :: make_num_fract ( * fract . binding , int_numerator , int_denominator ) ;
            }
        }
    }
}

template < typename data_assigner_types >
std :: string shy_data_assigner < data_assigner_types > :: error ( )
{
    return _error ;
}

