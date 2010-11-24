template < typename mediator >
class shy_logic_main_menu_letters_animation_unselection_weight
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: logic_main_menu_letters_animation_stateless :: logic_main_menu_letters_animation_stateless_consts_type logic_main_menu_letters_animation_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_letters_animation_unselection_weight_state_type
    {
    public :
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole row_unselected ;
        num_whole unselected_row_index ;
        num_fract weight ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_fract time ;
    } ;
    
public :
    shy_logic_main_menu_letters_animation_unselection_weight ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_select_row ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_unselect_row ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    shy_logic_main_menu_letters_animation_unselection_weight < mediator > & operator= ( const shy_logic_main_menu_letters_animation_unselection_weight < mediator > & ) ;
    void _proceed_with_weight ( ) ;
    void _compute_weight ( ) ;
    void _compute_identity_weight ( ) ;
    void _reply_weight ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_letters_animation_stateless_consts_type > _logic_main_menu_letters_animation_stateless_consts ;
    
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_letters_animation_unselection_weight_state_type _logic_main_menu_letters_animation_unselection_weight_state ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: shy_logic_main_menu_letters_animation_unselection_weight ( )
{
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_letters_animation_stateless_consts ( _logic_main_menu_letters_animation_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_animation_unselection_weight_state . row_unselected ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_request msg )
{
    _logic_main_menu_letters_animation_unselection_weight_state . requested_row = msg . row ;
    _logic_main_menu_letters_animation_unselection_weight_state . requested_col = msg . col ;
    _proceed_with_weight ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_select_row msg )
{
    _logic_main_menu_letters_animation_unselection_weight_state . row_unselected = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_letters_animation_unselection_weight_state . unselected_row_index = msg . row ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_unselection_weight_unselect_row msg )
{
    _logic_main_menu_letters_animation_unselection_weight_state . row_unselected = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_animation_unselection_weight_state . unselected_row_index = msg . row ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: _proceed_with_weight ( )
{
    num_whole row_unselected ;
    num_whole unselected_row_index ;
    num_whole requested_row ;
    
    row_unselected = _logic_main_menu_letters_animation_unselection_weight_state . row_unselected ;
    unselected_row_index = _logic_main_menu_letters_animation_unselection_weight_state . unselected_row_index ;
    requested_row = _logic_main_menu_letters_animation_unselection_weight_state . requested_row ;
    
    if ( platform_conditions :: whole_is_true ( row_unselected )
      && platform_conditions :: wholes_are_equal ( unselected_row_index , requested_row )
       )
    {
        _compute_weight ( ) ;
    }
    else
        _compute_identity_weight ( ) ;
    _reply_weight ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: _compute_weight ( )
{
    num_fract time_to_begin ;
    num_fract time_from_begin_to_end ;
    num_fract time_begin ;
    num_fract time_end ;
    num_fract time ;
    num_fract weight_begin ;
    num_fract weight_end ;
    num_fract weight ;
    
    time_to_begin = _logic_main_menu_letters_animation_stateless_consts . get ( ) . unselection_weight_time_to_begin ;
    time_from_begin_to_end = _logic_main_menu_letters_animation_stateless_consts . get ( ) . unselection_weight_time_from_begin_to_end ;
    time = _logic_main_menu_update_state . time ;
    weight_begin = _platform_math_consts . get ( ) . fract_1 ;
    weight_end = _platform_math_consts . get ( ) . fract_0 ;
    
    time_begin = time_to_begin ;
    platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end ) ;
    
    engine_math :: hard_in_easy_out 
        ( weight
        , time
        , weight_begin
        , time_begin
        , weight_end
        , time_end
        ) ;
        
    _logic_main_menu_letters_animation_unselection_weight_state . weight = weight ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: _compute_identity_weight ( )
{
    _logic_main_menu_letters_animation_unselection_weight_state . weight = _platform_math_consts . get ( ) . fract_1 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_unselection_weight < mediator > :: _reply_weight ( )
{
    typename messages :: logic_main_menu_letters_animation_unselection_weight_reply msg ;
    msg . row = _logic_main_menu_letters_animation_unselection_weight_state . requested_row ;
    msg . col = _logic_main_menu_letters_animation_unselection_weight_state . requested_col ;
    msg . weight = _logic_main_menu_letters_animation_unselection_weight_state . weight ;
    _mediator . get ( ) . send ( msg ) ;
}
