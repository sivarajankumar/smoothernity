#ifndef _shy_macosx_lib_cocoa_injections_included
#define _shy_macosx_lib_cocoa_injections_included

#include <AudioToolbox/ExtendedAudioFile.h>
#include <Cocoa/Cocoa.h>

#define so_called_lib_cocoa_CGBitmapContextCreate CGBitmapContextCreate
#define so_called_lib_cocoa_CGColorSpaceCreateDeviceRGB CGColorSpaceCreateDeviceRGB
#define so_called_lib_cocoa_CGColorSpaceRelease CGColorSpaceRelease
#define so_called_lib_cocoa_CGContextDrawImage CGContextDrawImage
#define so_called_lib_cocoa_CGContextRelease CGContextRelease
#define so_called_lib_cocoa_CGContextScaleCTM CGContextScaleCTM
#define so_called_lib_cocoa_CGContextSetBlendMode CGContextSetBlendMode
#define so_called_lib_cocoa_CGContextTranslateCTM CGContextTranslateCTM
#define so_called_lib_cocoa_CGDataProviderCreateWithURL CGDataProviderCreateWithURL
#define so_called_lib_cocoa_CGDataProviderRelease CGDataProviderRelease
#define so_called_lib_cocoa_CGImageCreateWithPNGDataProvider CGImageCreateWithPNGDataProvider
#define so_called_lib_cocoa_CGImageGetHeight CGImageGetHeight
#define so_called_lib_cocoa_CGImageGetWidth CGImageGetWidth
#define so_called_lib_cocoa_CGImageRelease CGImageRelease
#define so_called_lib_cocoa_CGRectMake CGRectMake
#define so_called_lib_cocoa_kCGBitmapByteOrder32Host kCGBitmapByteOrder32Host 
#define so_called_lib_cocoa_kCGBlendModeCopy kCGBlendModeCopy
#define so_called_lib_cocoa_kCGImageAlphaPremultipliedFirst kCGImageAlphaPremultipliedFirst
#define so_called_lib_cocoa_kCGRenderingIntentDefault kCGRenderingIntentDefault

typedef AudioBufferList so_called_lib_cocoa_AudioBufferList ;
typedef AudioStreamBasicDescription so_called_lib_cocoa_AudioStreamBasicDescription ;
typedef CFURLRef so_called_lib_cocoa_CFURLRef ;
typedef CGColorSpaceRef so_called_lib_cocoa_CGColorSpaceRef ;
typedef CGContextRef so_called_lib_cocoa_CGContextRef ;
typedef CGDataProviderRef so_called_lib_cocoa_CGDataProviderRef ;
typedef CGImageRef so_called_lib_cocoa_CGImageRef ;
typedef ExtAudioFileRef so_called_lib_cocoa_ExtAudioFileRef ;
typedef NSAutoreleasePool so_called_lib_cocoa_NSAutoreleasePool ;
typedef NSBundle so_called_lib_cocoa_NSBundle ;
typedef NSObject so_called_lib_cocoa_NSObject ;
typedef NSString so_called_lib_cocoa_NSString ;
typedef NSThread so_called_lib_cocoa_NSThread ;
typedef NSUInteger so_called_lib_cocoa_NSUInteger ;
typedef NSURL so_called_lib_cocoa_NSURL ;
typedef SInt64 so_called_lib_cocoa_SInt64 ;
typedef UInt32 so_called_lib_cocoa_UInt32 ;

#endif
