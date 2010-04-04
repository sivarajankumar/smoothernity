#import "iphone_sound_loader.h"

@implementation sound_loader

- ( id ) init
{
   	self = [ super init ] ;
	return self ;
}

- ( void ) dealloc
{
	[ super dealloc ] ;
}

- ( void ) load_16_bit_44100_khz_stereo_samples_from_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_max_samples_count_of : ( int ) max_samples_count
    put_loaded_samples_count_to : ( int * ) loaded_samples_count
{
    NSBundle * bundle = [ NSBundle mainBundle ] ;
    CFURLRef file_url = ( CFURLRef ) [ [ NSURL fileURLWithPath : [ bundle 
        pathForResource : [ NSString stringWithFormat : @"stereo_sound_resource_%i" , resource_index ] 
        ofType : @"mp3" 
        ] ] retain ] ;
        
    SInt64 file_length_in_frames = 0 ;
    AudioStreamBasicDescription file_format ;
    UInt32 property_size = sizeof ( file_format ) ;
    ExtAudioFileRef ext_ref = 0 ;
    AudioStreamBasicDescription output_format ;
                 
    ExtAudioFileOpenURL ( file_url , & ext_ref ) ;
    ExtAudioFileGetProperty ( ext_ref , kExtAudioFileProperty_FileDataFormat , & property_size , & file_format ) ;
                    
    output_format . mSampleRate = 44100 ;
    output_format . mChannelsPerFrame = 2 ;
    output_format . mFormatID = kAudioFormatLinearPCM ;
    output_format . mBytesPerPacket = 2 * output_format . mChannelsPerFrame ;
    output_format . mFramesPerPacket = 1 ;
    output_format . mBytesPerFrame = 2 * output_format . mChannelsPerFrame ;
    output_format . mBitsPerChannel = 16 ;
    output_format . mFormatFlags = kAudioFormatFlagsNativeEndian | kAudioFormatFlagIsPacked | kAudioFormatFlagIsSignedInteger ;
                    
    ExtAudioFileSetProperty ( ext_ref , kExtAudioFileProperty_ClientDataFormat , sizeof ( output_format ) , & output_format ) ;
    property_size = sizeof ( file_length_in_frames ) ;
    ExtAudioFileGetProperty ( ext_ref , kExtAudioFileProperty_FileLengthFrames , & property_size , & file_length_in_frames ) ;
    
    AudioBufferList data_buffer ;
    data_buffer . mNumberBuffers = 1 ;
    data_buffer . mBuffers [ 0 ] . mDataByteSize = file_length_in_frames * output_format . mBytesPerFrame ;
    data_buffer . mBuffers [ 0 ] . mNumberChannels = output_format . mChannelsPerFrame ;
    data_buffer . mBuffers [ 0 ] . mData = buffer ;
    
    ExtAudioFileRead ( ext_ref , ( UInt32 * ) & file_length_in_frames , & data_buffer ) ;
    * loaded_samples_count = file_length_in_frames ;
    ExtAudioFileDispose ( ext_ref ) ;
    CFRelease ( file_url ) ;
}

@end
