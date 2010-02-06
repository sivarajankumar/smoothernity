//
//  EAGLView.m
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "EAGLView.h"

#import "ES1Renderer.h"

@implementation EAGLView

@synthesize animating;

// You must implement this method
+ (Class) layerClass
{
    return [CAEAGLLayer class];
}

//The GL view is stored in the nib file. When it's unarchived it's sent -initWithCoder:
- (id) initWithCoder:(NSCoder*)coder
{    
    if ((self = [super initWithCoder:coder]))
	{
        // Get the layer
        CAEAGLLayer *eaglLayer = (CAEAGLLayer *)self.layer;
        
        eaglLayer.opaque = TRUE;
        eaglLayer.drawableProperties = [NSDictionary dictionaryWithObjectsAndKeys:
                                        [NSNumber numberWithBool:FALSE], kEAGLDrawablePropertyRetainedBacking, kEAGLColorFormatRGBA8, kEAGLDrawablePropertyColorFormat, nil];
		
		renderer = [[ES1Renderer alloc] init];
		
		if (!renderer)
		{
			[self release];
			return nil;
		}
        
		animating = FALSE;
		timeTotal = 0;
		frames = 0;
		timeMin = 100000;
		timeMax = 0;
		frameMax = -1;
		frameMin = -1;
		framesMissed = 0;
		lastMissedFrame = 0;
		frameMissed = false;
		for ( int i = 0; i < HISTORY_SIZE; i++ )
			timeHistory [ i ] = 0;
	}
	
    return self;
}

- (void) drawView:(id)sender
{
	CFAbsoluteTime frameTime = CFAbsoluteTimeGetCurrent ();
    [renderer render :frameMissed];
	frameTime = CFAbsoluteTimeGetCurrent () - frameTime;
	frameMissed = ( frameTime > 1.0 / 60.0 );
	
	if ( frames < HISTORY_SIZE )
	{
		timeHistory [ frames ] = frameTime;
		if ( frameTime > timeMax )
		{
			timeMax = frameTime;
			frameMax = frames;
		}
		if ( frameTime < timeMin )
		{
			timeMin = frameTime;
			frameMin = frames;
		}
		if ( frameMissed )
		{
			++framesMissed;
			lastMissedFrame = frames;
		}
		timeTotal += frameTime;
		++frames;
	}
	[ NSTimer 
	    scheduledTimerWithTimeInterval : 0.0
		target : self
	    selector : @ selector ( drawView : )
	    userInfo : nil
	    repeats : NO
	 ] ;
}

- (void) layoutSubviews
{
	[renderer resizeFromLayer:(CAEAGLLayer*)self.layer];
    [self drawView:nil];
}

- (void) startAnimation
{
	NSLog(@"start animation");
	if (!animating)
	{
		[NSTimer scheduledTimerWithTimeInterval:0.0 target:self selector:@selector(drawView:) userInfo:nil repeats:NO];
		NSLog(@"timer");
		animating = TRUE;
	}
}

- (void)stopAnimation
{
	double timeAvgInMs = ( ( double ) ( timeTotal * 1000.0 ) ) / ( double ) frames;
	double timeMinInMs = ( double ) ( timeMin * 1000.0 );
	double timeMaxInMs = ( double ) ( timeMax * 1000.0 );
	NSLog ( @"stop animation" );
	NSLog ( @"frames: %i", frames );
	NSLog ( @"missed: %i last: %i", framesMissed, lastMissedFrame );
	NSLog ( @"avg: %f ms", timeAvgInMs );
	NSLog ( @"min: %i %%", ( int ) ( timeMinInMs * 100.0 / timeAvgInMs ) );
	NSLog ( @"max: %i %%", ( int ) ( timeMaxInMs * 100.0 / timeAvgInMs ) );
	
//	NSLog ( @"frames history:" );
//	for ( int i = 0; i < frames; i++ )
//		NSLog ( @"% 3i: %f ms", i, ( double ) ( timeHistory [ i ] * 1000.0 ) );
	
	if (animating)
		animating = FALSE;
}

- (void) dealloc
{
    [renderer release];
	
    [super dealloc];
}

@end
