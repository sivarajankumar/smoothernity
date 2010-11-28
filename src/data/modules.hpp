template < typename _platform >
class shy_data_modules_types
{
public :
    typedef _platform platform ;
} ;

template < typename data_modules_types >
class shy_data_modules
{
    typedef typename data_modules_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename data_modules_types :: platform :: platform_math :: num_whole num_whole ;

public :
    class data_modules_attributes ;
    class data_modules_fract ;
    class data_modules_whole ;

    typedef std :: map < std :: string , data_modules_fract > name_to_fract_type ;
    typedef std :: map < std :: string , data_modules_whole > name_to_whole_type ;
    typedef std :: map < std :: string , data_modules_attributes > name_to_module_type ;

    class data_modules_fract
    {
    public :
        data_modules_fract ( ) ;
    public :
        num_fract * binding ;
        std :: string numerator_sign ;
        std :: string numerator_value ;
        std :: string denominator_sign ;
        std :: string denominator_value ;
    } ;

    class data_modules_whole
    {
    public :
        data_modules_whole ( ) ;
    public :
        num_whole * binding ;
        std :: string sign ;
        std :: string value ;
    } ;

    class data_modules_attributes
    {
    public :
        name_to_fract_type name_to_fract ;
        name_to_whole_type name_to_whole ;
    } ;

    name_to_module_type name_to_module ;
} ;

template < typename data_modules_types >
shy_data_modules < data_modules_types > :: data_modules_fract :: data_modules_fract ( )
: binding ( 0 )
{
}

template < typename data_modules_types >
shy_data_modules < data_modules_types > :: data_modules_whole :: data_modules_whole ( )
: binding ( 0 )
{
}

