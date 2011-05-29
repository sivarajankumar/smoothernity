template < typename platform_insider >
class shy_iphone_platform_sound_insider
{
public :
    shy_iphone_platform_sound_insider ( ) ;
    void set_platform_insider ( platform_insider * arg_platform_insider ) ;
    void set_sound_loader ( shy_iphone_sound_loader * loader ) ;
private :
    platform_insider * _platform_insider ;
} ;

template < typename platform_insider >
shy_iphone_platform_sound_insider < platform_insider > :: shy_iphone_platform_sound_insider ( )
: _platform_insider ( 0 )
{
}

template < typename platform_insider >
void shy_iphone_platform_sound_insider < platform_insider > :: set_platform_insider ( platform_insider * arg_platform_insider )
{
    _platform_insider = arg_platform_insider ;
}

template < typename platform_insider >
void shy_iphone_platform_sound_insider < platform_insider > :: set_sound_loader ( shy_iphone_sound_loader * loader )
{
    _platform_insider -> sound . _sound_loader = loader ;
}
