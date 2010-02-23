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

// This class wraps the CAEAGLLayer from CoreAnimation into a convenient UIView subclass.
// The view content is basically an EAGL surface you render your OpenGL scene into.
// Note that setting the view non-opaque will only work if the EAGL surface has an alpha channel.
@interface EAGLView : UIView
{    
@private
	id <ESRenderer> renderer;
	
	BOOL animating;
}

@property (readonly, nonatomic, getter=isAnimating) BOOL animating;

- (void) startAnimation;
- (void) stopAnimation;
- (void) drawView:(id)sender;

@end
