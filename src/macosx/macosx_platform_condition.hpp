inline int shy_macosx_platform :: condition_equal ( num_whole a , num_whole b )
{
    return a . _value == b . _value ;
}

inline int shy_macosx_platform :: condition_true ( num_whole num )
{
    return num . _value == true ;
}

inline int shy_macosx_platform :: condition_false ( num_whole num )
{
    return num . _value == false ;
}
