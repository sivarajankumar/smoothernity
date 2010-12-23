class shy_facade_interface
{
public :
    virtual ~ shy_facade_interface ( ) { }
    virtual void init ( ) = 0 ;
    virtual void done ( ) = 0 ;
    virtual void render ( ) = 0 ;
    virtual void update ( ) = 0 ;
    virtual void video_mode_changed ( ) = 0 ;
} ;

