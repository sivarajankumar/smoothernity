#include <DXUT.h>
#include <Windowsx.h>

#include "src/facade/shy_facade_injections.h"
#include "src/injections/lib/std/false/shy_false.h"
#include "src/injections/lib/std/int32/t/shy_t.h"
#include "src/injections/lib/std/true/shy_true.h"
#include "src/injections/platform/mouse/insider/shy_insider.h"
#include "src/injections/platform/render/insider/shy_insider.h"

void smoothernity_application_init ( )
{
    so_called_platform_mouse_insider :: set_enabled ( so_called_lib_std_true ) ;
    so_called_facade :: application_init ( ) ;
}

void smoothernity_application_done ( )
{
    so_called_facade :: application_done ( ) ;
}

void smoothernity_game_init ( )
{
    so_called_facade :: game_init ( ) ;
}

void smoothernity_game_done ( )
{
    so_called_facade :: game_done ( ) ;
}

void smoothernity_set_mouse_position ( so_called_lib_std_int32_t x_pixel , so_called_lib_std_int32_t y_pixel )
{
    HRESULT hr ;
    D3DVIEWPORT9 viewport ;
    V ( DXUTGetD3D9Device ( ) -> GetViewport ( & viewport ) ) ;
    so_called_lib_std_float x = 2.0f * ( - 0.5f + so_called_lib_std_float ( x_pixel ) / so_called_lib_std_float ( viewport . Width ) ) ;
    so_called_lib_std_float y = 2.0f * ( - 0.5f + so_called_lib_std_float ( y_pixel ) / so_called_lib_std_float ( viewport . Height ) ) ;
    if ( viewport . Width > viewport . Height )
        x *= so_called_lib_std_float ( viewport . Width ) / so_called_lib_std_float ( viewport . Height ) ;
    else
        y *= so_called_lib_std_float ( viewport . Height ) / so_called_lib_std_float ( viewport . Width ) ;
    so_called_platform_mouse_insider :: set_x ( x ) ;
    so_called_platform_mouse_insider :: set_y ( - y ) ;
}

//--------------------------------------------------------------------------------------
// Called right before creating a D3D9 or D3D11 device, allowing the app to modify the device settings as needed
//--------------------------------------------------------------------------------------
bool CALLBACK ModifyDeviceSettings ( DXUTDeviceSettings * pDeviceSettings , void * pUserContext )
{
    pDeviceSettings -> d3d9 . pp . SwapEffect = D3DSWAPEFFECT_COPY ;
    pDeviceSettings -> d3d9 . pp . PresentationInterval = D3DPRESENT_INTERVAL_ONE ;
    return true ;
}

//--------------------------------------------------------------------------------------
// Handle updates to the scene.  This is called regardless of which D3D API is used
//--------------------------------------------------------------------------------------
void CALLBACK OnFrameMove ( double fTime , float fElapsedTime , void * pUserContext )
{
}

//--------------------------------------------------------------------------------------
// Handle messages to the application
//--------------------------------------------------------------------------------------
LRESULT CALLBACK MsgProc ( HWND hWnd , UINT uMsg , WPARAM wParam , LPARAM lParam ,
                           bool * pbNoFurtherProcessing , void * pUserContext )
{
    if ( uMsg == WM_MOUSEMOVE )
    {
        int xPos = GET_X_LPARAM ( lParam ) ;
        int yPos = GET_Y_LPARAM ( lParam ) ;
        smoothernity_set_mouse_position ( xPos , yPos ) ;
    }
    return 0 ;
}

//--------------------------------------------------------------------------------------
// Handle key presses
//--------------------------------------------------------------------------------------
void CALLBACK OnKeyboard ( UINT nChar , bool bKeyDown , bool bAltDown , void * pUserContext )
{
}

//--------------------------------------------------------------------------------------
// Handle mouse button presses
//--------------------------------------------------------------------------------------
void CALLBACK OnMouse ( bool bLeftButtonDown , bool bRightButtonDown , bool bMiddleButtonDown ,
                        bool bSideButton1Down , bool bSideButton2Down , int nMouseWheelDelta ,
                        int xPos , int yPos , void * pUserContext )
{
    smoothernity_set_mouse_position ( xPos , yPos ) ;
    so_called_platform_mouse_insider :: set_left_button_down ( bLeftButtonDown ) ;
}

//--------------------------------------------------------------------------------------
// Call if device was removed.  Return true to find a new device, false to quit
//--------------------------------------------------------------------------------------
bool CALLBACK OnDeviceRemoved ( void * pUserContext )
{
    return true ;
}

//--------------------------------------------------------------------------------------
// Rejects any D3D9 devices that aren't acceptable to the app by returning false
//--------------------------------------------------------------------------------------
bool CALLBACK IsD3D9DeviceAcceptable ( D3DCAPS9 * pCaps , D3DFORMAT AdapterFormat , D3DFORMAT BackBufferFormat ,
                                       bool bWindowed , void * pUserContext )
{
    // Typically want to skip back buffer formats that don't support alpha blending
    IDirect3D9 * pD3D = DXUTGetD3D9Object ( ) ;
    if ( FAILED ( pD3D -> CheckDeviceFormat ( pCaps -> AdapterOrdinal , pCaps -> DeviceType ,
                                              AdapterFormat , D3DUSAGE_QUERY_POSTPIXELSHADER_BLENDING ,
                                              D3DRTYPE_TEXTURE , BackBufferFormat ) ) )
        return false ;

    return true ;
}

//--------------------------------------------------------------------------------------
// Create any D3D9 resources that will live through a device reset (D3DPOOL_MANAGED)
// and aren't tied to the back buffer size
//--------------------------------------------------------------------------------------
HRESULT CALLBACK OnD3D9CreateDevice ( IDirect3DDevice9 * pd3dDevice , const D3DSURFACE_DESC * pBackBufferSurfaceDesc ,
                                      void * pUserContext )
{
    return S_OK ;
}

//--------------------------------------------------------------------------------------
// Create any D3D9 resources that won't live through a device reset (D3DPOOL_DEFAULT) 
// or that are tied to the back buffer size 
//--------------------------------------------------------------------------------------
HRESULT CALLBACK OnD3D9ResetDevice ( IDirect3DDevice9 * pd3dDevice , const D3DSURFACE_DESC * pBackBufferSurfaceDesc ,
                                     void * pUserContext )
{
    smoothernity_game_init ( ) ;
    return S_OK ;
}

//--------------------------------------------------------------------------------------
// Render the scene using the D3D9 device
//--------------------------------------------------------------------------------------
void CALLBACK OnD3D9FrameRender ( IDirect3DDevice9 * pd3dDevice , double fTime , float fElapsedTime , void * pUserContext )
{
    HRESULT hr ;

    // Render the scene
    if ( SUCCEEDED ( pd3dDevice -> BeginScene ( ) ) )
    {
        so_called_facade :: next_frame ( ) ;
        V ( pd3dDevice -> EndScene ( ) ) ;
    }
}

//--------------------------------------------------------------------------------------
// Release D3D9 resources created in the OnD3D9ResetDevice callback 
//--------------------------------------------------------------------------------------
void CALLBACK OnD3D9LostDevice ( void * pUserContext )
{
    smoothernity_game_done ( ) ;
}

//--------------------------------------------------------------------------------------
// Release D3D9 resources created in the OnD3D9CreateDevice callback 
//--------------------------------------------------------------------------------------
void CALLBACK OnD3D9DestroyDevice ( void * pUserContext )
{
}

//--------------------------------------------------------------------------------------
// Initialize everything and go into a render loop
//--------------------------------------------------------------------------------------
#ifdef NDEBUG
int WINAPI wWinMain ( HINSTANCE , HINSTANCE , LPWSTR , int )
#endif
#ifdef DEBUG
int main ( int , char * * )
#endif
{
    // Enable run-time memory check for debug builds.
#if defined(DEBUG) | defined(_DEBUG)
    _CrtSetDbgFlag ( _CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF ) ;
#endif

    smoothernity_application_init ( ) ;

    // DXUT will create and use the best device (either D3D9 or D3D11) 
    // that is available on the system depending on which D3D callbacks are set below

    // Set general DXUT callbacks
    DXUTSetCallbackFrameMove ( OnFrameMove ) ;
    DXUTSetCallbackKeyboard ( OnKeyboard ) ;
    DXUTSetCallbackMouse ( OnMouse ) ;
    DXUTSetCallbackMsgProc ( MsgProc ) ;
    DXUTSetCallbackDeviceChanging ( ModifyDeviceSettings ) ;
    DXUTSetCallbackDeviceRemoved ( OnDeviceRemoved ) ;

    // Set the D3D9 DXUT callbacks. Remove these sets if the app doesn't need to support D3D9
    DXUTSetCallbackD3D9DeviceAcceptable ( IsD3D9DeviceAcceptable ) ;
    DXUTSetCallbackD3D9DeviceCreated ( OnD3D9CreateDevice ) ;
    DXUTSetCallbackD3D9DeviceReset ( OnD3D9ResetDevice ) ;
    DXUTSetCallbackD3D9FrameRender ( OnD3D9FrameRender ) ;
    DXUTSetCallbackD3D9DeviceLost ( OnD3D9LostDevice ) ;
    DXUTSetCallbackD3D9DeviceDestroyed ( OnD3D9DestroyDevice ) ;

    DXUTInit ( true , true , NULL ) ; // Parse the command line, show msgboxes on error, no extra command line params
    DXUTSetCursorSettings ( true , true ) ; // Show the cursor and clip it when in full screen
    DXUTCreateWindow ( L"Smoothernity version 2011-12-10" ) ;

    // Only require 10-level hardware
    DXUTCreateDevice ( D3D_FEATURE_LEVEL_10_0 , true , 640 , 480 ) ;

    DXUTMainLoop ( ) ; // Enter into the DXUT render loop

    smoothernity_application_done ( ) ;

    return DXUTGetExitCode ( ) ;
}
