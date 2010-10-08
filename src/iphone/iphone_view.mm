#import "iphone_view.h"

@implementation EAGLView

- ( id ) initWithCoder : ( NSCoder * ) coder
{    
    if ( ( self = [ super initWithCoder : coder ] ) )
	{
   		_animating = FALSE ;
        [ self _init_platform ] ;
        [ self _init_game ] ;
	}
    return self ;
}

- ( void ) dealloc
{
    [ self _done_game ] ;
    [ self _done_platform ] ;
    [ super dealloc ] ;
}

- ( void ) _init_platform
{        
    CAEAGLLayer * eagl_layer = ( CAEAGLLayer * ) self . layer ;
    eagl_layer . opaque = TRUE ;
    eagl_layer . drawableProperties = [ NSDictionary dictionaryWithObjectsAndKeys 
        : [ NSNumber numberWithBool : FALSE ]
        , kEAGLDrawablePropertyRetainedBacking
        , kEAGLColorFormatRGBA8
        , kEAGLDrawablePropertyColorFormat
        , nil
        ] ;		
    [ UIApplication sharedApplication ] . idleTimerDisabled = YES ;
    
    _gl_context = [ [ EAGLContext alloc ] initWithAPI : kEAGLRenderingAPIOpenGLES1 ] ;
    [ EAGLContext setCurrentContext : _gl_context ] ;
    glGenFramebuffersOES ( 1 , & _gl_default_framebuffer ) ;
    glBindFramebufferOES ( GL_FRAMEBUFFER_OES , _gl_default_framebuffer ) ;
    
    _al_device = alcOpenDevice ( NULL ) ;
    _al_context = alcCreateContext ( _al_device , NULL ) ;
    alcMakeContextCurrent ( _al_context ) ;
    
    _sound_loader = [ [ shy_iphone_sound_loader alloc ] init ] ;
    _texture_loader = [ [ shy_iphone_texture_loader alloc ] init ] ;
    [ _sound_loader thread_run ] ;
    [ _texture_loader thread_run ] ;
    _platform_insider = new shy_iphone_platform_insider ( ) ;
    _platform_insider -> render_insider . set_texture_loader ( _texture_loader ) ;
    _platform_insider -> sound_insider . set_sound_loader ( _sound_loader ) ;

	_platform_insider -> render_insider . set_aspect_width ( 1.0f ) ;
	_platform_insider -> render_insider . set_aspect_height ( 1.5f ) ;
    
    _platform_insider -> touch_insider . set_enabled ( true ) ;
    _platform_insider -> touch_insider . set_occured ( false ) ;

    _frame_time = 0 ;
}

- ( void ) _done_platform
{
    [ _sound_loader thread_stop ] ;
    [ _texture_loader thread_stop ] ;
    _sound_loader = nil ;
    _texture_loader = nil ;
    
    delete _platform_insider ;
    _platform_insider = 0 ;	
	
	if ( _gl_default_framebuffer )
	{
		glDeleteFramebuffersOES ( 1 , & _gl_default_framebuffer ) ;
		_gl_default_framebuffer = 0 ;
	}

	if ( _gl_color_renderbuffer )
	{
		glDeleteRenderbuffersOES ( 1 , & _gl_color_renderbuffer ) ;
		_gl_color_renderbuffer = 0 ;
	}
    
    if ( _gl_depth_renderbuffer )
    {
		glDeleteRenderbuffersOES ( 1 , & _gl_depth_renderbuffer ) ;
        _gl_depth_renderbuffer = 0 ;
    }
	
	if ( [ EAGLContext currentContext ] == _gl_context )
        [ EAGLContext setCurrentContext : nil ] ;
	
 	[ _gl_context release ] ;
	_gl_context = nil ;

	alcDestroyContext ( _al_context ) ;
	alcCloseDevice ( _al_device ) ;
    _al_context = nil ;
    _al_device = nil ;
}

- ( void ) _init_game
{
    shy_iphone_platform_insider :: platform_pointer :: pointer < const shy_platform < shy_iphone_platform_insider > > platform_ptr ;
    shy_iphone_platform_insider :: platform_pointer :: bind ( platform_ptr , _platform_insider -> platform ) ;
    _facade = new shy_facade < shy_platform < shy_iphone_platform_insider > > ( platform_ptr ) ;
    _facade -> init ( ) ;
}

- ( void ) _done_game
{
	_facade -> done ( ) ;
	delete _facade ;
	_facade = 0 ;
}

+ ( Class ) layerClass
{
    return [ CAEAGLLayer class ] ;
}

- ( void ) touchesBegan : ( NSSet * ) touches withEvent : ( UIEvent * ) event
{
    UITouch * touch = [ touches anyObject ] ;
    CGPoint point = [ touch locationInView : [ touch view ] ] ;
    _platform_insider -> touch_insider . set_occured ( true ) ;
    _platform_insider -> touch_insider . set_x (   2.0f * ( float ) ( point . x - _gl_backing_width  / 2 ) / ( float ) _gl_backing_width ) ;
    _platform_insider -> touch_insider . set_y ( - 2.0f * ( float ) ( point . y - _gl_backing_height / 2 ) / ( float ) _gl_backing_width ) ;
}

- ( void ) touchesMoved : ( NSSet * ) touches withEvent : ( UIEvent * ) event
{
    UITouch * touch = [ touches anyObject ] ;
    CGPoint point = [ touch locationInView : [ touch view ] ] ;
    _platform_insider -> touch_insider . set_x (   2.0f * ( float ) ( point . x - _gl_backing_width  / 2 ) / ( float ) _gl_backing_width ) ;
    _platform_insider -> touch_insider . set_y ( - 2.0f * ( float ) ( point . y - _gl_backing_height / 2 ) / ( float ) _gl_backing_width ) ;
}

- ( void ) touchesEnded : ( NSSet * ) touches withEvent : ( UIEvent * ) event
{
    UITouch * touch = [ touches anyObject ] ;
    CGPoint point = [ touch locationInView : [ touch view ] ] ;
    _platform_insider -> touch_insider . set_occured ( false ) ;
    _platform_insider -> touch_insider . set_x (   2.0f * ( float ) ( point . x - _gl_backing_width  / 2 ) / ( float ) _gl_backing_width ) ;
    _platform_insider -> touch_insider . set_y ( - 2.0f * ( float ) ( point . y - _gl_backing_height / 2 ) / ( float ) _gl_backing_width ) ;
}

- ( void ) touchesCancelled : ( NSSet * ) touches withEvent : ( UIEvent * ) event
{
    UITouch * touch = [ touches anyObject ] ;
    CGPoint point = [ touch locationInView : [ touch view ] ] ;
    _platform_insider -> touch_insider . set_occured ( false ) ;
    _platform_insider -> touch_insider . set_x (   2.0f * ( float ) ( point . x - _gl_backing_width  / 2 ) / ( float ) _gl_backing_width ) ;
    _platform_insider -> touch_insider . set_y ( - 2.0f * ( float ) ( point . y - _gl_backing_height / 2 ) / ( float ) _gl_backing_width ) ;
}

- ( void ) draw_view : ( id ) sender
{
    [ EAGLContext setCurrentContext : _gl_context ] ;
    glBindFramebufferOES ( GL_FRAMEBUFFER_OES , _gl_default_framebuffer ) ;
	_facade -> render ( ) ;
	_facade -> update ( ) ;
    glBindRenderbufferOES ( GL_RENDERBUFFER_OES , _gl_color_renderbuffer ) ;
    [ _gl_context presentRenderbuffer : GL_RENDERBUFFER_OES ] ;
    CFAbsoluteTime finish_time = CFAbsoluteTimeGetCurrent ( ) ;
    _platform_insider -> render_insider . set_frame_loss ( finish_time - _frame_time > 1.4 / 60.0 ) ;
    _frame_time = finish_time ;
    [ self _schedule_draw ] ;
}

- ( void ) _schedule_draw
{
	[ NSTimer 
	    scheduledTimerWithTimeInterval : 0.0
		target : self
	    selector : @ selector ( draw_view : )
	    userInfo : nil
	    repeats : NO
    ] ;
}

- ( void ) layoutSubviews
{
    glGenRenderbuffersOES ( 1 , & _gl_color_renderbuffer ) ;
    glBindRenderbufferOES ( GL_RENDERBUFFER_OES , _gl_color_renderbuffer ) ;
    [ _gl_context renderbufferStorage : GL_RENDERBUFFER_OES fromDrawable : ( CAEAGLLayer * ) self . layer ] ;
	glFramebufferRenderbufferOES ( GL_FRAMEBUFFER_OES , GL_COLOR_ATTACHMENT0_OES , GL_RENDERBUFFER_OES , _gl_color_renderbuffer ) ;
    
	glGetRenderbufferParameterivOES ( GL_RENDERBUFFER_OES , GL_RENDERBUFFER_WIDTH_OES , & _gl_backing_width ) ;
    glGetRenderbufferParameterivOES ( GL_RENDERBUFFER_OES , GL_RENDERBUFFER_HEIGHT_OES , & _gl_backing_height ) ;
	
    glGenRenderbuffersOES ( 1 , & _gl_depth_renderbuffer ) ;
    glBindRenderbufferOES ( GL_RENDERBUFFER_OES , _gl_depth_renderbuffer ) ;
    glRenderbufferStorageOES ( GL_RENDERBUFFER_OES , GL_DEPTH_COMPONENT16_OES , _gl_backing_width , _gl_backing_height ) ;
    glFramebufferRenderbufferOES ( GL_FRAMEBUFFER_OES , GL_DEPTH_ATTACHMENT_OES , GL_RENDERBUFFER_OES , _gl_depth_renderbuffer ) ;
    
    if ( glCheckFramebufferStatusOES ( GL_FRAMEBUFFER_OES ) != GL_FRAMEBUFFER_COMPLETE_OES )
	{
		NSLog ( @"Failed to make complete framebuffer object %x" , glCheckFramebufferStatusOES ( GL_FRAMEBUFFER_OES ) ) ;
    }
    
    glViewport ( 0 , 0 , _gl_backing_width , _gl_backing_height ) ;
    [ self draw_view : nil ] ;
}

- ( void ) start_animation
{
	if ( ! _animating )
	{
        [ self _schedule_draw ] ;
		_animating = TRUE ;
	}
}

- ( void ) stop_animation
{
	if ( _animating )
		_animating = FALSE ;
}

@end
