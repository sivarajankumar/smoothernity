//
//  EAGLView.h
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <QuartzCore/QuartzCore.h>

#import "ESRenderer.h"

#define HISTORY_SIZE 300

// This class wraps the CAEAGLLayer from CoreAnimation into a convenient UIView subclass.
// The view content is basically an EAGL surface you render your OpenGL scene into.
// Note that setting the view non-opaque will only work if the EAGL surface has an alpha channel.
@interface EAGLView : UIView
{    
@private
	id <ESRenderer> renderer;
	
	BOOL animating;
	// Use of the CADisplayLink class is the preferred method for controlling your animation timing.
	// CADisplayLink will link to the main display and fire every vsync when added to a given run-loop.
	// The NSTimer class is used only as fallback when running on a pre 3.1 device where CADisplayLink
	// isn't available.
	CFAbsoluteTime timeTotal;
	CFAbsoluteTime timeMax;
	CFAbsoluteTime timeMin;
	CFAbsoluteTime timeHistory [ HISTORY_SIZE ];
	int frameMax;
	int frameMin;
	int frames;
	int framesMissed;
	int lastMissedFrame;
	bool frameMissed;
}

@property (readonly, nonatomic, getter=isAnimating) BOOL animating;

- (void) startAnimation;
- (void) stopAnimation;
- (void) drawView:(id)sender;

@end
