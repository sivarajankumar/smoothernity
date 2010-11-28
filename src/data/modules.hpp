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

    typedef std :: map < std :: string , num_fract * > name_to_fract_type ;
    typedef std :: map < std :: string , num_whole * > name_to_whole_type ;
    typedef std :: map < std :: string , data_modules_attributes > name_to_module_type ;

    class data_modules_fract_type
    {
    public :
        data_modules_fract_type ( ) ;
    public :
        num_fract * binding ;
        std :: string numerator_sign ;
        std :: string numerator_value ;
        std :: string denominator_sign ;
        std :: string denominator_value ;
    } ;

    class data_modules_whole_type
    {
    public :
        data_modules_whole_type ( ) ;
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

