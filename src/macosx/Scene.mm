/*
 Scene.m
 A delegate object used by MyOpenGLView and MainController to render a simple scene.

 Troy Stephens

 Copyright (c) 2003, Apple Computer, Inc., all rights reserved.
*/
/*
 IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc. ("Apple") in
 consideration of your agreement to the following terms, and your use, installation, 
 modification or redistribution of this Apple software constitutes acceptance of these 
 terms.  If you do not agree with these terms, please do not use, install, modify or 
 redistribute this Apple software.
 
 In consideration of your agreement to abide by the following terms, and subject to these 
 terms, Apple grants you a personal, non-exclusive license, under Apple’s copyrights in 
 this original Apple software (the "Apple Software"), to use, reproduce, modify and 
 redistribute the Apple Software, with or without modifications, in source and/or binary 
 forms; provided that if you redistribute the Apple Software in its entirety and without 
 modifications, you must retain this notice and the following text and disclaimers in all 
 such redistributions of the Apple Software.  Neither the name, trademarks, service marks 
 or logos of Apple Computer, Inc. may be used to endorse or promote products derived from 
 the Apple Software without specific prior written permission from Apple. Except as expressly
 stated in this notice, no other rights or licenses, express or implied, are granted by Apple
 herein, including but not limited to any patent rights that may be infringed by your 
 derivative works or by other works in which the Apple Software may be incorporated.
 
 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, 
 EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, 
 MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS 
 USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
 
 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL 
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
 OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, 
 REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND 
 WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR 
 OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#import "Scene.h"
#import "Texturing.h"
#import <OpenGL/glu.h>

@implementation Scene

- init
{
    self = [super init];
    if (self) {
		measurer = new shy_measurer_facade < shy_macosx_platform > ( ) ;
    }
    return self;
}

- (void)dealloc
{
	measurer -> done ( ) ;
	delete measurer ;
    [super dealloc];
}

- (void)setViewportRect:(NSRect)bounds
{
    glViewport( bounds.origin.x, bounds.origin.y, bounds.size.width, bounds.size.height);
	measurer -> init ( ) ;
}

// This method renders our scene.  We could optimize it in any of several ways, including factoring out the repeated OpenGL initialization calls and either hanging onto the GLU quadric object or creating a display list thet draws the Earth, but the details of how it's implemented aren't important here.  The main thing to note is that we've factored our drawing code out of our NSOpenGLView subclass to enable MainController to use it when rendering in FullScreen mode.
- (void)render
{
	measurer -> render ( ) ;
	measurer -> update ( ) ;
    glFinish();
}

@end
