template < typename mediator >
class shy_logic_main_menu_letters_meshes_creation_director
{
    typedef typename mediator :: logic_main_menu_letters_meshes_stateless :: logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_create ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_creation_finished ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_letters_meshes_stateless_consts_type > _logic_main_menu_letters_meshes_stateless_consts ;
    num_whole _creation_in_progress ;
    num_fract _time_passed ;
} ;

template < typename mediator >
void shy_logic_main_menu_letters_meshes_creation_director < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_creation_director < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_letters_meshes_stateless_consts ( _logic_main_menu_letters_meshes_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _creation_in_progress = _platform_math_consts . get ( ) . whole_false ;
    _time_passed = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_creation_director < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_create )
{
    _creation_in_progress = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_creation_director < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_creation_finished )
{
    _creation_in_progress = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_letters_meshes_creation_director < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _creation_in_progress ) )
    {
        num_fract frame_time ;
        num_fract time_between_creation ;

        time_between_creation = _logic_main_menu_letters_meshes_stateless_consts . get ( ) . time_between_creation ;

        platform_math :: make_num_fract ( frame_time , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _time_passed , frame_time ) ;

        while ( platform_conditions :: fract_greater_than_fract ( _time_passed , time_between_creation ) )
        {
            platform_math :: sub_from_fract ( _time_passed , time_between_creation ) ;
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_mesh_create_next ( ) ) ;
            if ( platform_conditions :: whole_is_true ( _creation_in_progress ) )
                break ;
        }
    }
}
