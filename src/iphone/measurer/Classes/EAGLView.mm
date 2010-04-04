#import "EAGLView.h"

@implementation EAGLView

+ ( Class ) layerClass
{
    return [ CAEAGLLayer class ] ;
}

- ( void ) touchesBegan : ( NSSet * ) touches withEvent : ( UIEvent * ) event
{
    UITouch * touch = [ touches anyObject ] ;
    CGPoint point = [ touch locationInView : [ touch view ] ] ;
    NSLog ( @"touch began x=%f, y=%f" , point . x , point . y ) ;
}

- ( id ) initWithCoder : ( NSCoder * ) coder
{    
    if ( ( self = [ super initWithCoder : coder ] ) )
	{
   		_animating = FALSE ;
        
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
        if ( ! _gl_context || ! [ EAGLContext setCurrentContext : _gl_context ] )
		{
            [ self release ] ;
            return nil ;
        }
		glGenFramebuffersOES ( 1 , & _gl_default_framebuffer ) ;
		glBindFramebufferOES ( GL_FRAMEBUFFER_OES , _gl_default_framebuffer ) ;
        
        _al_device = alcOpenDevice ( NULL ) ;
        if ( ! _al_device )
        {
            NSLog ( @"Failed to open OpenAl device" ) ;
            [ self release ] ;
            return nil ;
        }
        _al_context = alcCreateContext ( _al_device , NULL ) ;
        alcMakeContextCurrent ( _al_context ) ;
        
        shy_iphone_platform :: _sound_loader = [ [ sound_loader alloc ] init ] ;
   		_shy_measurer . init ( ) ;        
	}
	
    return self ;
}

- ( void ) drawView : ( id ) sender
{
    [ EAGLContext setCurrentContext : _gl_context ] ;
    glBindFramebufferOES ( GL_FRAMEBUFFER_OES , _gl_default_framebuffer ) ;
	_shy_measurer . render ( ) ;
	_shy_measurer . update ( ) ;
    glBindRenderbufferOES ( GL_RENDERBUFFER_OES , _gl_color_renderbuffer ) ;
    [ _gl_context presentRenderbuffer : GL_RENDERBUFFER_OES ] ;
    _shy_measurer . render_finished ( ) ;
	[ NSTimer 
	    scheduledTimerWithTimeInterval : 0.0
		target : self
	    selector : @ selector ( drawView : )
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
    [ self drawView : nil ] ;
}

- ( void ) startAnimation
{
	if ( ! _animating )
	{
		[ NSTimer scheduledTimerWithTimeInterval : 0.0 target : self selector : @selector ( drawView : ) userInfo : nil repeats : NO ] ;
		_animating = TRUE ;
	}
}

- ( void ) stopAnimation
{
	if ( _animating )
		_animating = FALSE;
}

- (void) dealloc
{
	_shy_measurer . done ( ) ;
    [ shy_iphone_platform :: _sound_loader release ] ;
    shy_iphone_platform :: _sound_loader = nil ;
	
	// Tear down GL
	if (_gl_default_framebuffer)
	{
		glDeleteFramebuffersOES(1, &_gl_default_framebuffer);
		_gl_default_framebuffer = 0;
	}

	if (_gl_color_renderbuffer)
	{
		glDeleteRenderbuffersOES(1, &_gl_color_renderbuffer);
		_gl_color_renderbuffer = 0;
	}
    
    if (_gl_depth_renderbuffer)
    {
		glDeleteRenderbuffersOES(1, &_gl_depth_renderbuffer);
        _gl_depth_renderbuffer = 0;
    }
	
	// Tear down context
	if ([EAGLContext currentContext] == _gl_context)
        [EAGLContext setCurrentContext:nil];
	
 	[_gl_context release];
	_gl_context = nil;

    // Turn off Open AL
	alcDestroyContext ( _al_context ) ;
	alcCloseDevice ( _al_device ) ;
    _al_context = nil ;
    _al_device = nil ;

    [super dealloc];
}

@end
