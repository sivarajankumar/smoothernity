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
	}
	
    return self;
}

- (void) drawView:(id)sender
{
    [ renderer render ] ;
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
	if (!animating)
	{
		[NSTimer scheduledTimerWithTimeInterval:0.0 target:self selector:@selector(drawView:) userInfo:nil repeats:NO];
		animating = TRUE;
        NSLog(@"start animation");
	}
}

- (void)stopAnimation
{
	if (animating)
		animating = FALSE;
}

- (void) dealloc
{
    [renderer release];
	
    [super dealloc];
}

@end
