//
//  ES1Renderer.m
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "ES1Renderer.h"

@implementation ES1Renderer

// Create an ES 1.1 context
- (id) init
{		
	if (self = [super init])
	{
        [UIApplication sharedApplication].idleTimerDisabled = YES;
		context = [[EAGLContext alloc] initWithAPI:kEAGLRenderingAPIOpenGLES1];
        
        if (!context || ![EAGLContext setCurrentContext:context])
		{
            [self release];
            return nil;
        }
        
        mDevice = alcOpenDevice ( NULL ) ;
        if ( ! mDevice )
        {
            NSLog ( @"Failed to open OpenAl device" ) ;
            [ self release ] ;
            return nil ;
        }
        
        mContext = alcCreateContext ( mDevice , NULL ) ;
        alcMakeContextCurrent ( mContext ) ;
                
		// Create default framebuffer object. The backing will be allocated for the current layer in -resizeFromLayer
		glGenFramebuffersOES(1, &defaultFramebuffer);
		glBindFramebufferOES(GL_FRAMEBUFFER_OES, defaultFramebuffer);

		shyMeasurer . init ( ) ;
        
        ////////////////////////////////////////////
        // Sound experiment begin
        
        if ( mDevice )
        {
            ALfloat listenerPos [ ] = { 0.0 , 0.0 , 4.0 } ;
            ALfloat listenerVel [ ] = { 0.0 , 0.0 , 0.0 } ;
            ALfloat listenerOri [ ] = { 0.0 , 0.0 , 1.0 , 0.0 , 1.0 , 0.0 } ;
            ALfloat source0Pos [ ] = { - 2.0 , 0.0 , 0.0 } ;
            ALfloat source0Vel [ ] = { 0.0 , 0.0 , 0.0 } ;
            
            ALuint  buffer = 0 ;
            ALuint  source = 0 ;

            ALubyte data [ 44100 ] ;
            for ( int i = 0 ; i < 44100 ; ++ i )
            {
                float pos = ( ( float ) i ) * 3.14159 / 44100.0f ;
                float level = sinf ( pos * 10000.0f ) ;
                data [ i ] = ( unsigned char ) ( level * 127.0f + 128.0f ) ;
            }
            
            alListenerfv ( AL_POSITION , listenerPos ) ;
            alListenerfv ( AL_VELOCITY , listenerVel ) ;
            alListenerfv ( AL_ORIENTATION , listenerOri ) ;            
            alGetError ( ) ;
            alGenBuffers ( 1 , & buffer ) ;
            if ( alGetError ( ) == AL_NO_ERROR )
            {
                alGetError ( ) ;
                alBufferData ( buffer , AL_FORMAT_MONO8 , ( ALvoid * ) data , 44100 , 44100 ) ;
                if ( alGetError ( ) == AL_NO_ERROR )
                {
                    alGetError ( ) ;
                    alGenSources( 1 , & source ) ;
                    if ( alGetError ( ) == AL_NO_ERROR ) 
                    {
                        alSourcef ( source , AL_PITCH , 1.0f ) ;
                        alSourcef ( source , AL_GAIN , 1.0f ) ;
                        alSourcefv ( source , AL_POSITION , source0Pos ) ;
                        alSourcefv ( source , AL_VELOCITY , source0Vel ) ;
                        alSourcei ( source , AL_BUFFER , buffer ) ;
                        alSourcei ( source , AL_LOOPING , AL_TRUE ) ;
                        alSourcePlay ( source ) ;
                        NSLog ( @"Successfully created OpenAl sources" ) ;
                    }
                    else
                    {
                        NSLog ( @"Failed creating OpenAl sources" ) ;
                    }
                }
                else
                {
                    NSLog ( @"Failed loading OpenAl buffer data" ) ;
                }

            }
            else
            {
                NSLog ( @"Failed creating OpenAl buffers" ) ;
            }
        }
        
        // Sound experiment end
        ////////////////////////////////////////////
	}
	
	return self;
}

- (void) render
{
    [EAGLContext setCurrentContext:context];
    glBindFramebufferOES(GL_FRAMEBUFFER_OES, defaultFramebuffer);
	shyMeasurer . render ( ) ;
	shyMeasurer . update ( ) ;
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, colorRenderbuffer);
    [context presentRenderbuffer:GL_RENDERBUFFER_OES];
    shyMeasurer . render_finished ( ) ;
}

- (BOOL) resizeFromLayer:(CAEAGLLayer *)layer
{	
	// Allocate color buffer backing based on the current layer size
    glGenRenderbuffersOES(1, &colorRenderbuffer);
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, colorRenderbuffer);
    [context renderbufferStorage:GL_RENDERBUFFER_OES fromDrawable:layer];
	glFramebufferRenderbufferOES(GL_FRAMEBUFFER_OES, GL_COLOR_ATTACHMENT0_OES, GL_RENDERBUFFER_OES, colorRenderbuffer);
    
	glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_WIDTH_OES, &backingWidth);
    glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_HEIGHT_OES, &backingHeight);
	
    // Allocate and attach the depth buffer
    glGenRenderbuffersOES(1, &depthRenderbuffer);
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, depthRenderbuffer);
    glRenderbufferStorageOES(GL_RENDERBUFFER_OES, GL_DEPTH_COMPONENT16_OES, backingWidth, backingHeight);
    glFramebufferRenderbufferOES(GL_FRAMEBUFFER_OES, GL_DEPTH_ATTACHMENT_OES, GL_RENDERBUFFER_OES, depthRenderbuffer);
    
    if (glCheckFramebufferStatusOES(GL_FRAMEBUFFER_OES) != GL_FRAMEBUFFER_COMPLETE_OES)
	{
		NSLog(@"Failed to make complete framebuffer object %x", glCheckFramebufferStatusOES(GL_FRAMEBUFFER_OES));
        return NO;
    }
    
    glViewport(0, 0, backingWidth, backingHeight);
    return YES;
}

- (void) dealloc
{
	shyMeasurer . done ( ) ;
	
	// Tear down GL
	if (defaultFramebuffer)
	{
		glDeleteFramebuffersOES(1, &defaultFramebuffer);
		defaultFramebuffer = 0;
	}

	if (colorRenderbuffer)
	{
		glDeleteRenderbuffersOES(1, &colorRenderbuffer);
		colorRenderbuffer = 0;
	}
	
	// Tear down context
	if ([EAGLContext currentContext] == context)
        [EAGLContext setCurrentContext:nil];
	
 	[context release];
	context = nil;

    // Turn off Open AL
	alcDestroyContext ( mContext ) ;
	alcCloseDevice ( mDevice ) ;
    mContext = nil ;
    mDevice = nil ;
    
	[super dealloc];
}

@end
