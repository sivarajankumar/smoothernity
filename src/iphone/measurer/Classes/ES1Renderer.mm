//
//  ES1Renderer.m
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "ES1Renderer.h"
#import <AudioToolbox/AudioToolbox.h>
#import <AudioToolbox/ExtendedAudioFile.h>

typedef ALvoid AL_APIENTRY ( * alBufferDataStaticProcPtr ) 
    ( const ALint bid , ALenum format , ALvoid * data , ALsizei size , ALsizei freq ) ;
ALvoid alBufferDataStaticProc ( const ALint bid, ALenum format, ALvoid * data , ALsizei size , ALsizei freq )
{
	static alBufferDataStaticProcPtr proc = NULL ;
    if ( proc == NULL )
        proc = ( alBufferDataStaticProcPtr ) alcGetProcAddress ( NULL , ( const ALCchar * ) "alBufferDataStatic" ) ;
    if ( proc )
        proc ( bid , format , data , size , freq ) ;
    return ;
}

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

        /////////////////////////////////////
        // EXPERIMENTAL CODE
        {
            ALvoid * outData = 0 ;
            ALenum  error = AL_NO_ERROR ;
            ALenum  format ;
            ALsizei size ;
            ALsizei freq ;
         
            NSBundle * bundle = [ NSBundle mainBundle ] ;
         
            // get some audio data from a wave file
            CFURLRef fileURL = ( CFURLRef ) [ [ NSURL fileURLWithPath : [ bundle pathForResource : @"rough_n_heavy_v37" ofType : @"mp3" ] ] retain ] ;
         
            if ( fileURL )
            {
                {
                    CFURLRef inFileURL = fileURL ;
                    ALsizei * outDataSize = & size ;
                    ALenum * outDataFormat = & format ;
                    ALsizei * outSampleRate = & freq ;
                    OSStatus err = noErr ;
                    SInt64 theFileLengthInFrames = 0 ;
                    AudioStreamBasicDescription theFileFormat ;
                    UInt32 thePropertySize = sizeof ( theFileFormat ) ;
                    ExtAudioFileRef extRef = NULL ;
                    void * theData = NULL ;
                    AudioStreamBasicDescription theOutputFormat ;
                 
                    // Open a file with ExtAudioFileOpen()
                    err = ExtAudioFileOpenURL ( inFileURL , & extRef ) ;
                    if ( ! err )
                    {
                        // Get the audio data format
                        err = ExtAudioFileGetProperty ( extRef , kExtAudioFileProperty_FileDataFormat , & thePropertySize , & theFileFormat ) ;
                        if ( ! err )
                        {
                            if ( theFileFormat . mChannelsPerFrame <= 2 )
                            {
                                // Set the client format to 16 bit signed integer (native-endian) data
                                // Maintain the channel count and sample rate of the original source format
                                theOutputFormat . mSampleRate = theFileFormat . mSampleRate ;
                                theOutputFormat . mChannelsPerFrame = theFileFormat . mChannelsPerFrame;
                             
                                theOutputFormat . mFormatID = kAudioFormatLinearPCM ;
                                theOutputFormat . mBytesPerPacket = 2 * theOutputFormat . mChannelsPerFrame ;
                                theOutputFormat . mFramesPerPacket = 1 ;
                                theOutputFormat . mBytesPerFrame = 2 * theOutputFormat . mChannelsPerFrame ;
                                theOutputFormat . mBitsPerChannel = 16;
                                theOutputFormat . mFormatFlags = kAudioFormatFlagsNativeEndian | kAudioFormatFlagIsPacked | kAudioFormatFlagIsSignedInteger ;
                             
                                // Set the desired client (output) data format
                                err = ExtAudioFileSetProperty ( extRef , kExtAudioFileProperty_ClientDataFormat , sizeof ( theOutputFormat ) , & theOutputFormat ) ;
                                if ( ! err )
                                {
                                    // Get the total frame count
                                    thePropertySize = sizeof ( theFileLengthInFrames ) ;
                                    err = ExtAudioFileGetProperty ( extRef , kExtAudioFileProperty_FileLengthFrames , & thePropertySize , & theFileLengthInFrames ) ;
                                    if ( ! err )
                                    {
                                        // Read all the data into memory
                                        UInt32 dataSize = theFileLengthInFrames * theOutputFormat . mBytesPerFrame ;
                                        theData = malloc ( dataSize ) ;
                                        if ( theData )
                                        {
                                            AudioBufferList theDataBuffer;
                                            theDataBuffer . mNumberBuffers = 1;
                                            theDataBuffer . mBuffers [ 0 ] . mDataByteSize = dataSize;
                                            theDataBuffer . mBuffers [ 0 ] . mNumberChannels = theOutputFormat . mChannelsPerFrame;
                                            theDataBuffer . mBuffers [ 0 ] . mData = theData ;
                                     
                                            // Read the data into an AudioBufferList
                                            err = ExtAudioFileRead ( extRef , ( UInt32 * ) & theFileLengthInFrames , & theDataBuffer ) ;
                                            if(err == noErr)
                                            {
                                                // success
                                                * outDataSize = ( ALsizei ) dataSize;
                                                * outDataFormat = ( theOutputFormat . mChannelsPerFrame > 1 ) ? AL_FORMAT_STEREO16 : AL_FORMAT_MONO16 ;
                                                * outSampleRate = ( ALsizei ) theOutputFormat . mSampleRate ;
                                                outData = theData ;
                                                if ( extRef )
                                                    ExtAudioFileDispose ( extRef ) ;
                                                NSLog ( @"load music ok" ) ;
                                            }
                                            else
                                            {
                                                // failure
                                                free ( theData ) ;
                                                theData = NULL ; // make sure to return NULL
                                                NSLog ( @"MyGetOpenALAudioData: ExtAudioFileRead FAILED, Error = %ld" , err ) ;
                                            }
                                        }
                                    }
                                    else
                                    {
                                        NSLog ( @"MyGetOpenALAudioData: ExtAudioFileGetProperty(kExtAudioFileProperty_FileLengthFrames) FAILED, Error = %ld" , err ) ;
                                    }                                 
                                }
                                else
                                {
                                    NSLog ( @"MyGetOpenALAudioData: ExtAudioFileSetProperty(kExtAudioFileProperty_ClientDataFormat) FAILED, Error = %ld" , err ) ;
                                }
                             
                            }
                            else
                            {
                                NSLog ( @"MyGetOpenALAudioData - Unsupported Format, channel count is greater than stereo" ) ;
                            }                         
                        }
                        else
                        {
                            NSLog ( @"MyGetOpenALAudioData: ExtAudioFileGetProperty(kExtAudioFileProperty_FileDataFormat) FAILED, Error = %ld" , err ) ;
                        }
                    }
                    else
                    {
                        NSLog ( @"MyGetOpenALAudioData: ExtAudioFileOpenURL FAILED, Error = %ld" , err ) ;
                    }
                }
                CFRelease ( fileURL ) ;
                if ( ( error = alGetError ( ) ) == AL_NO_ERROR )
                {
                    NSUInteger bufferID ;
                    alGenBuffers ( 1 , & bufferID ) ;
                    alBufferData ( bufferID , format , outData , size - 2 * 2 * 2293 , freq ) ; 
                    shy_iphone_platform :: _experimental_buffer_id = bufferID ;
                }
                else
                {
                    NSLog ( @"error loading sound" ) ;
                }
            }
            else
            {
                NSLog ( @"file not found." ) ;
            }
        }
        // EXPERIMENTAL CODE
        /////////////////////////////////////
        
   		shyMeasurer . init ( ) ;
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
