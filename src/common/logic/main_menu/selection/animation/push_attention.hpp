template < typename mediator >
class shy_logic_main_menu_selection_animation_push_attention
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_selection_animation_push_attention_consts_type
    {
    public :
        _logic_main_menu_selection_animation_push_attention_consts_type ( ) ;
    public :
        num_fract horizontal_scale_min ;
        num_fract horizontal_scale_max ;
        num_fract vertical_scale_min ;
        num_fract vertical_scale_max ;
        num_fract period_in_seconds ;
    } ;

    class _logic_main_menu_selection_animation_push_attention_transform_state_type
    {
    public :
        num_fract horizontal_scale ;
        num_fract vertical_scale ;
    } ;

    class _logic_main_menu_update_state_type
    {
    public :
        num_whole update_permitted ;
        num_fract time ;
    } ;

public :
    shy_logic_main_menu_selection_animation_push_attention ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_push_attention_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
private :
    void _reply_transform ( ) ;
    void _compute_horizontal_scale ( ) ;
    void _compute_vertical_scale ( ) ;
    void _compute_animation_scale
        ( num_fract & scale
        , num_fract scale_min
        , num_fract scale_max
        , num_fract period_in_seconds
        ) ;
    shy_logic_main_menu_selection_animation_push_attention < mediator > & operator= ( const shy_logic_main_menu_selection_animation_push_attention < mediator > & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_animation_push_attention_consts_type _logic_main_menu_selection_animation_push_attention_consts ;
    
    _logic_main_menu_selection_animation_push_attention_transform_state_type _logic_main_menu_selection_animation_push_attention_transform_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_push_attention < mediator > 
:: _logic_main_menu_selection_animation_push_attention_consts_type 
:: _logic_main_menu_selection_animation_push_attention_consts_type ( )
{
    platform_math :: make_num_fract ( horizontal_scale_min , 195 , 200 ) ;
    platform_math :: make_num_fract ( horizontal_scale_max , 200 , 200 ) ;
    platform_math :: make_num_fract ( vertical_scale_min , 200 , 100 ) ;
    platform_math :: make_num_fract ( vertical_scale_max , 210 , 100 ) ;
    platform_math :: make_num_fract ( period_in_seconds , 4 , 10 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_animation_push_attention < mediator > :: shy_logic_main_menu_selection_animation_push_attention ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . update_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . update_permitted ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_push_attention_transform_request )
{
    _compute_horizontal_scale ( ) ;
    _compute_vertical_scale ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_push_attention_transform_reply msg ;
    msg . scale_x = _logic_main_menu_selection_animation_push_attention_transform_state . horizontal_scale ;
    msg . scale_y = _logic_main_menu_selection_animation_push_attention_transform_state . vertical_scale ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: _compute_horizontal_scale ( )
{
    _compute_animation_scale
        ( _logic_main_menu_selection_animation_push_attention_transform_state . horizontal_scale
        , _logic_main_menu_selection_animation_push_attention_consts . horizontal_scale_min
        , _logic_main_menu_selection_animation_push_attention_consts . horizontal_scale_max
        , _logic_main_menu_selection_animation_push_attention_consts . period_in_seconds
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: _compute_vertical_scale ( )
{
    _compute_animation_scale
        ( _logic_main_menu_selection_animation_push_attention_transform_state . vertical_scale
        , _logic_main_menu_selection_animation_push_attention_consts . vertical_scale_min
        , _logic_main_menu_selection_animation_push_attention_consts . vertical_scale_max
        , _logic_main_menu_selection_animation_push_attention_consts . period_in_seconds
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_attention < mediator > :: _compute_animation_scale 
    ( num_fract & scale
    , num_fract scale_min
    , num_fract scale_max
    , num_fract period_in_seconds
    )
{
    num_fract time ;
    num_fract phase ;
    num_fract amplitude ;
    num_fract offset ;
    
    time = _logic_main_menu_update_state . time ;
    
    platform_math :: div_fracts ( phase , time , period_in_seconds ) ;
    platform_math :: mul_fract_by ( phase , _platform_math_consts . get ( ) . fract_2pi ) ;
    
    platform_math :: sub_fracts ( amplitude , scale_max , scale_min ) ;
    platform_math :: div_fract_by ( amplitude , _platform_math_consts . get ( ) . fract_2 ) ;
    
    platform_math :: add_fracts ( offset , scale_max , scale_min ) ;
    platform_math :: div_fract_by ( offset , _platform_math_consts . get ( ) . fract_2 ) ;
    
    platform_math :: sin ( scale , phase ) ;
    platform_math :: mul_fract_by ( scale , amplitude ) ;
    platform_math :: add_to_fract ( scale , offset ) ;        
}
