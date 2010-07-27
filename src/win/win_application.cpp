#include "DXUT.h"
#include "../common/facade.hpp"
#include "win_platform.hpp"

static shy_win_platform_insider * g_platform = 0 ;
static shy_facade < shy_platform < shy_win_platform_insider > > * g_facade = 0 ;

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
		g_facade -> render ( ) ;
		g_facade -> update ( ) ;
        V ( pd3dDevice -> EndScene ( ) ) ;
    }
}


//--------------------------------------------------------------------------------------
// Release D3D9 resources created in the OnD3D9ResetDevice callback 
//--------------------------------------------------------------------------------------
void CALLBACK OnD3D9LostDevice ( void * pUserContext )
{
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
int WINAPI wWinMain ( HINSTANCE hInstance , HINSTANCE hPrevInstance , LPWSTR lpCmdLine , int nCmdShow )
{
    // Enable run-time memory check for debug builds.
#if defined(DEBUG) | defined(_DEBUG)
    _CrtSetDbgFlag ( _CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF ) ;
#endif

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
    DXUTCreateWindow ( L"Smoothernity" ) ;

    // Only require 10-level hardware
    DXUTCreateDevice ( D3D_FEATURE_LEVEL_10_0 , true , 640 , 480 ) ;

    g_platform = new shy_win_platform_insider ( ) ;
    g_facade = new shy_facade < shy_platform < shy_win_platform_insider > > ( g_platform -> platform ) ;
    g_facade -> init ( ) ;
    DXUTMainLoop ( ) ; // Enter into the DXUT render loop
    g_facade -> done ( ) ;
    delete g_facade ;
    delete g_platform ;
    g_facade = 0 ;
    g_platform = 0 ;

    return DXUTGetExitCode ( ) ;
}
