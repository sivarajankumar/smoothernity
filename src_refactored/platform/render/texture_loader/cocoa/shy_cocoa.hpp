@interface shy_guts_loader : so_called_lib_cocoa_NSObject
{
@private
    so_called_lib_std_bool _is_ready ;
    so_called_lib_std_bool _should_quit ;
    so_called_lib_std_int32_t _resource_index ;
    void * _buffer ;
    so_called_lib_std_int32_t _side_size ;
}
- ( void ) thread_run ;
- ( void ) thread_stop ;
- ( so_called_lib_std_bool ) loader_ready ;
- ( void ) load_texture_from_png_resource : ( so_called_lib_std_int32_t ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( so_called_lib_std_int32_t ) max_samples_count
    ;
- ( void ) _thread_main_method ;
- ( void ) _perform_load ;
@end

@implementation shy_guts_loader

- ( id ) init
{
    self = [ super init ] ;
    _is_ready = so_called_lib_std_true ;
    _should_quit = so_called_lib_std_false ;
    _resource_index = 0 ;
    _buffer = 0 ;
    _side_size = 0 ;
    return self ;
}

- ( void ) dealloc
{
    [ super dealloc ] ;
}

- ( so_called_lib_std_bool ) loader_ready
{
    return _is_ready ;
}

- ( void ) thread_run
{
    [ self performSelectorInBackground : @selector ( _thread_main_method ) withObject : nil ] ;
}

- ( void ) thread_stop
{
    _should_quit = so_called_lib_std_true ;
}

- ( void ) load_texture_from_png_resource : ( so_called_lib_std_int32_t ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( so_called_lib_std_int32_t ) side_size
{
    if ( _is_ready )
    {
        _resource_index = resource_index ;
        _buffer = buffer ;
        _side_size = side_size ;
        _is_ready = so_called_lib_std_false ;
    }
}

- ( void ) _thread_main_method
{
    so_called_lib_cocoa_NSAutoreleasePool * pool = [ [ so_called_lib_cocoa_NSAutoreleasePool alloc ] init ] ;
    while ( ! _should_quit )
    {
        [ so_called_lib_cocoa_NSThread sleepForTimeInterval : 0.1 ] ;
        if ( ! _is_ready )
        {
            [ self _perform_load ] ;
            _is_ready = so_called_lib_std_true ;
        }
    }
    [ pool release ] ;
    [ self release ] ;
}

- ( void ) _perform_load
{
    so_called_lib_cocoa_NSUInteger width ;
    so_called_lib_cocoa_NSUInteger height ;
    so_called_lib_cocoa_NSURL * url = nil ;
    so_called_lib_cocoa_CGDataProviderRef src ;
    so_called_lib_cocoa_CGImageRef image ;
    so_called_lib_cocoa_CGContextRef context = nil ;
    so_called_lib_cocoa_CGColorSpaceRef color_space ;
    url = [ so_called_lib_cocoa_NSURL fileURLWithPath : [ [ so_called_lib_cocoa_NSBundle mainBundle ] pathForResource : 
        [ so_called_lib_cocoa_NSString stringWithFormat : @"texture_resource_%i" , ( so_called_lib_std_int32_t ) _resource_index ] 
        ofType : @"png"
        ] ] ;
    src = so_called_lib_cocoa_CGDataProviderCreateWithURL ( ( so_called_lib_cocoa_CFURLRef ) url ) ;
    if ( src )
    {
        image = so_called_lib_cocoa_CGImageCreateWithPNGDataProvider 
            ( src 
            , 0 
            , so_called_lib_std_false 
            , so_called_lib_cocoa_kCGRenderingIntentDefault 
            ) ;
        so_called_lib_cocoa_CGDataProviderRelease ( src ) ;
        width = so_called_lib_cocoa_CGImageGetWidth ( image ) ;
        height = so_called_lib_cocoa_CGImageGetHeight ( image ) ;
        if ( width == ( so_called_lib_cocoa_NSUInteger ) _side_size && height == ( so_called_lib_cocoa_NSUInteger ) _side_size )
        {
            color_space = so_called_lib_cocoa_CGColorSpaceCreateDeviceRGB ( ) ;
            context = so_called_lib_cocoa_CGBitmapContextCreate 
                ( _buffer
                , width 
                , height 
                , 8 
                , 4 * width 
                , color_space 
                , so_called_lib_cocoa_kCGImageAlphaPremultipliedFirst | so_called_lib_cocoa_kCGBitmapByteOrder32Host 
                ) ;
            so_called_lib_cocoa_CGColorSpaceRelease ( color_space ) ;
            so_called_lib_cocoa_CGContextTranslateCTM ( context , 0 , height ) ;
            so_called_lib_cocoa_CGContextScaleCTM ( context , 1 , - 1 ) ;
            so_called_lib_cocoa_CGContextSetBlendMode ( context , so_called_lib_cocoa_kCGBlendModeCopy ) ;
            so_called_lib_cocoa_CGContextDrawImage ( context , so_called_lib_cocoa_CGRectMake ( 0 , 0 , width , height ) , image ) ;
            so_called_lib_cocoa_CGContextRelease ( context ) ;
        }
        so_called_lib_cocoa_CGImageRelease ( image ) ;
    }
}

@end

namespace shy_guts
{
    static shy_guts_loader * loader = 0 ;
}

void shy_platform_render_texture_loader_cocoa :: init ( )
{
    shy_guts_loader * loader = [ [ shy_guts_loader alloc ] init ] ;
    [ loader thread_run ] ;
    shy_guts :: loader = loader ;
}

void shy_platform_render_texture_loader_cocoa :: done ( )
{
    shy_guts_loader * loader = shy_guts :: loader ;
    [ loader thread_stop ] ;
    shy_guts :: loader = nil ;
}

void shy_platform_render_texture_loader_cocoa :: _load_resource
    ( so_called_type_platform_render_texture_loader_cocoa_resource_id resource_id 
    , so_called_type_platform_math_num_whole size_pow2_base 
    , so_called_type_platform_render_texel_data * texels 
    )
{
    so_called_lib_std_int32_t size_pow2_base_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    shy_guts_loader * loader = shy_guts :: loader ;
    [ loader 
        load_texture_from_png_resource : resource_id . _resource_id 
        to_buffer : ( void * ) texels
        with_side_size_of : 1 << size_pow2_base_int
    ] ;
}

void shy_platform_render_texture_loader_cocoa :: create_resource_id 
    ( so_called_type_platform_render_texture_loader_cocoa_resource_id & resource_id 
    , so_called_type_platform_math_num_whole resource_index 
    )
{
    so_called_platform_math_insider :: num_whole_value_get ( resource_id . _resource_id , resource_index ) ;
}

void shy_platform_render_texture_loader_cocoa :: ready ( so_called_type_platform_math_num_whole & is_ready )
{
    shy_guts_loader * loader = shy_guts :: loader ;
    so_called_platform_math_insider :: num_whole_value_set ( is_ready , [ loader loader_ready ] ) ;
}

