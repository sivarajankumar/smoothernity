template < typename mediator >
class shy_logic_main_menu_meshes_placement
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_main_menu_meshes_placement_consts_type
    {
    public :
        _logic_main_menu_meshes_placement_consts_type ( ) ;
    public :
        num_fract vertical_shift_period_in_seconds ;
        num_fract vertical_shift_phase_per_col ;
        num_fract vertical_shift_amplitude ;
        num_fract horizontal_shift_period_in_seconds ;
        num_fract horizontal_shift_phase_per_row ;
        num_fract horizontal_shift_amplitude ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;
    
    class _logic_main_menu_meshes_place_state_type
    {
    public :
        num_whole requested ;
        num_whole current_mesh_index ;
        vector_data position ;
        vector_data vertical_position_delta ;
        vector_data horizontal_position_delta ;
    } ;
    
    class _logic_main_menu_meshes_count_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole meshes ;
    } ;

    class _logic_main_menu_mesh_row_col_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_index ;
        num_whole replied ;
        num_whole row ;
        num_whole col ;
    } ;

    class _logic_main_menu_mesh_id_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_index ;
        num_whole replied ;
        engine_render_mesh_id mesh ;
    } ;

    class _logic_main_menu_layout_position_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        vector_data position ;
        num_fract scale ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_meshes_place ) ;
    void receive ( typename messages :: logic_main_menu_meshes_count_reply ) ;
    void receive ( typename messages :: logic_main_menu_mesh_row_col_reply ) ;
    void receive ( typename messages :: logic_main_menu_mesh_id_reply ) ;
    void receive ( typename messages :: logic_main_menu_layout_position_reply ) ;
private :
    void _proceed_with_placement ( ) ;
    void _obtain_meshes_count ( ) ;
    void _obtain_first_mesh_row_col ( ) ;
    void _obtain_current_mesh_row_col ( ) ;
    void _obtain_current_mesh_id ( ) ;
    void _obtain_layout_position ( ) ;
    void _layout_position_received ( ) ;
    void _compute_horizontal_position_delta ( ) ;
    void _compute_vertical_position_delta ( ) ;
    void _compute_position ( ) ;
    void _place_current_mesh ( ) ;
    void _move_to_next_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > _logic_main_menu_stateless_consts ;
    const _logic_main_menu_meshes_placement_consts_type _logic_main_menu_meshes_placement_consts ;

    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_meshes_place_state_type _logic_main_menu_meshes_place_state ;
    _logic_main_menu_meshes_count_state_type _logic_main_menu_meshes_count_state ;
    _logic_main_menu_mesh_row_col_state_type _logic_main_menu_mesh_row_col_state ;
    _logic_main_menu_mesh_id_state_type _logic_main_menu_mesh_id_state ;
    _logic_main_menu_layout_position_state_type _logic_main_menu_layout_position_state ;
} ;

template < typename mediator >
shy_logic_main_menu_meshes_placement < mediator > :: _logic_main_menu_meshes_placement_consts_type :: _logic_main_menu_meshes_placement_consts_type ( )
{
    platform_math :: make_num_fract ( vertical_shift_period_in_seconds , 2 , 1 ) ;
    platform_math :: make_num_fract ( vertical_shift_phase_per_col , 1 , 10 ) ;
    platform_math :: make_num_fract ( vertical_shift_amplitude , 1 , 3 ) ;
    platform_math :: make_num_fract ( horizontal_shift_period_in_seconds , 4 , 1 ) ;
    platform_math :: make_num_fract ( horizontal_shift_phase_per_row , 1 , 5 ) ;
    platform_math :: make_num_fract ( horizontal_shift_amplitude , 1 , 2 ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_stateless_consts ( _logic_main_menu_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . launch_permitted ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_meshes_place )
{
    _logic_main_menu_meshes_place_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_placement ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_meshes_count_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_count_state . requested ) )
    {
        _logic_main_menu_meshes_count_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_meshes_count_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_meshes_count_state . meshes = msg . meshes ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_mesh_row_col_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_row_col_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_mesh_row_col_state . requested_index , msg . index )
       )
    {
        _logic_main_menu_mesh_row_col_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_mesh_row_col_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_mesh_row_col_state . row = msg . row ;
        _logic_main_menu_mesh_row_col_state . col = msg . col ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_mesh_id_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_id_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_mesh_id_state . requested_index , msg . index )
       )
    {
        _logic_main_menu_mesh_id_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_mesh_id_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_mesh_id_state . mesh = msg . mesh ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: receive ( typename messages :: logic_main_menu_layout_position_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_layout_position_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_layout_position_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_layout_position_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_layout_position_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_layout_position_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_layout_position_state . position = msg . position ;
        _logic_main_menu_layout_position_state . scale = msg . scale ;
        _proceed_with_placement ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _proceed_with_placement ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_place_state . requested ) )
    {
        _logic_main_menu_meshes_place_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_meshes_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_count_state . replied ) )
    {
        _logic_main_menu_meshes_count_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_first_mesh_row_col ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_row_col_state . replied ) )
    {
        _logic_main_menu_mesh_row_col_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_current_mesh_id ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_mesh_id_state . replied ) )
    {
        _logic_main_menu_mesh_id_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_layout_position ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_layout_position_state . replied ) )
    {
        _logic_main_menu_layout_position_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _layout_position_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _obtain_meshes_count ( )
{
    _logic_main_menu_meshes_count_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_meshes_count_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _obtain_first_mesh_row_col ( )
{
    _logic_main_menu_meshes_place_state . current_mesh_index = _platform_math_consts . get ( ) . whole_0 ;
    _obtain_current_mesh_row_col ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _obtain_current_mesh_row_col ( )
{
    _logic_main_menu_mesh_row_col_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_mesh_row_col_state . requested_index = _logic_main_menu_meshes_place_state . current_mesh_index ;
    typename messages :: logic_main_menu_mesh_row_col_request msg ;
    msg . index = _logic_main_menu_meshes_place_state . current_mesh_index ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _obtain_current_mesh_id ( )
{
    _logic_main_menu_mesh_id_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_mesh_id_state . requested_index = _logic_main_menu_meshes_place_state . current_mesh_index ;
    typename messages :: logic_main_menu_mesh_id_request msg ;
    msg . index = _logic_main_menu_meshes_place_state . current_mesh_index ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _obtain_layout_position ( )
{
    _logic_main_menu_layout_position_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_layout_position_state . requested_row = _logic_main_menu_mesh_row_col_state . row ;
    _logic_main_menu_layout_position_state . requested_col = _logic_main_menu_mesh_row_col_state . col ;
    typename messages :: logic_main_menu_layout_position_request msg ;
    msg . row = _logic_main_menu_mesh_row_col_state . row ;
    msg . col = _logic_main_menu_mesh_row_col_state . col ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _layout_position_received ( )
{
    _compute_horizontal_position_delta ( ) ;
    _compute_vertical_position_delta ( ) ;
    _compute_position ( ) ;
    _place_current_mesh ( ) ;
    _move_to_next_mesh ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _compute_position ( )
{
    vector_data vertical_position_delta ;
    vector_data horizontal_position_delta ;
    vector_data layout_position ;
    vector_data position ;
    
    vertical_position_delta = _logic_main_menu_meshes_place_state . vertical_position_delta ;
    horizontal_position_delta = _logic_main_menu_meshes_place_state . horizontal_position_delta ;
    layout_position = _logic_main_menu_layout_position_state . position ;
    
    platform_vector :: add ( position , vertical_position_delta , horizontal_position_delta ) ;
    platform_vector :: add_to ( position , layout_position ) ;
    
    _logic_main_menu_meshes_place_state . position = position ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _compute_horizontal_position_delta ( )
{
    vector_data horizontal_position_delta ;
    num_fract zero ;
    num_fract row ;
    num_fract phase_shift ;
    num_fract phase ;
    num_fract delta ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    platform_math :: make_fract_from_whole ( row , _logic_main_menu_mesh_row_col_state . row ) ;
    platform_math :: mul_fracts ( phase_shift , row , _logic_main_menu_meshes_placement_consts . horizontal_shift_phase_per_row ) ;
    
    platform_math :: div_fracts ( phase , _logic_main_menu_update_state . time , _logic_main_menu_meshes_placement_consts . horizontal_shift_period_in_seconds ) ;
    platform_math :: add_to_fract ( phase , phase_shift ) ;
    platform_math :: mul_fract_by ( phase , _platform_math_consts . get ( ) . fract_2pi ) ;
    
    platform_math :: sin ( delta , phase ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_meshes_placement_consts . horizontal_shift_amplitude ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_layout_position_state . scale ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size ) ;
    
    platform_vector :: xyz ( horizontal_position_delta , delta , zero , zero ) ;
    
    _logic_main_menu_meshes_place_state . horizontal_position_delta = horizontal_position_delta ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _compute_vertical_position_delta ( )
{
    vector_data vertical_position_delta ;
    num_fract zero ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    platform_vector :: xyz ( vertical_position_delta , zero , zero , zero ) ;
    _logic_main_menu_meshes_place_state . vertical_position_delta = vertical_position_delta ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _place_current_mesh ( )
{
    matrix_data transform ;
    vector_data position ;
    num_fract scale ;
    num_fract zero ;
    
    position = _logic_main_menu_meshes_place_state . position ;
    scale = _logic_main_menu_layout_position_state . scale ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_matrix :: set_origin ( transform , position ) ;
    platform_matrix :: set_axis_x ( transform , scale , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , scale , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , scale ) ;
    
    typename messages :: engine_render_mesh_set_transform msg ;
    msg . transform = transform ;
    msg . mesh = _logic_main_menu_mesh_id_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_placement < mediator > :: _move_to_next_mesh ( )
{
    platform_math :: inc_whole ( _logic_main_menu_meshes_place_state . current_mesh_index ) ;
    if ( platform_conditions :: whole_less_than_whole ( _logic_main_menu_meshes_place_state . current_mesh_index , _logic_main_menu_meshes_count_state . meshes ) )
        _obtain_current_mesh_row_col ( ) ;
}
