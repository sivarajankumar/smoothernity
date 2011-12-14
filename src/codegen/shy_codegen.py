def reify ( data , open_func ) :
    for name , contents in data . items ( ) :
        open_func ( name , 'w' ) . write ( contents )

def generate ( lines ) :
    res = { }
    res . update ( _generate_common_h ( ) )
    res . update ( _generate_common_hpp ( ) )
    res . update ( _generate_common_injections_h ( ) )
    res . update ( _generate_common_injections_cpp ( ) )
    res . update ( _generate_loadable_h ( ) )
    res . update ( _generate_loadable_hpp ( ) )
    res . update ( _generate_loadable_injections_h ( ) )
    res . update ( _generate_loadable_injections_cpp ( ) )
    return res

def _generate_common_h ( ) :
    return { 'src/common/shy_common.h' :
        'class shy_common\n'
        '{\n'
        'public :\n'
        '    static void init ( ) ;\n'
        '    static void done ( ) ;\n'
        '    static void next_frame ( ) ;\n'
        '} ;\n' }

def _generate_common_hpp ( ) :
    return { 'src/common/shy_common.hpp' :
        'void shy_common :: init ( )\n'
        '{\n'
        '}\n'
        '\n'
        'void shy_common :: done ( )\n'
        '{\n'
        '}\n'
        '\n'
        'void shy_common :: next_frame ( )\n'
        '{\n'
        '}\n' }

def _generate_common_injections_h ( ) :
    return { 'src/common/shy_common_injections.h' :
        '#ifndef _shy_common_injections_included\n'
        '#define _shy_common_injections_included\n'
        '\n'
        '#include "src/common/shy_common.h"\n'
        'typedef shy_common so_called_common ;\n' }

def _generate_common_injections_cpp ( ) :
    return { 'src/common/shy_common_injections.cpp' :
        '#include "src/common/shy_common_injections.h"\n'
        '#include "src/common/shy_common.hpp"\n' }

def _generate_loadable_h ( ) :
    return { 'src/loadable/shy_loadable.h' :
        'class shy_loadable\n'
        '{\n'
        'public :\n'
        '    static void load ( ) ;\n'
        '} ;\n' }

def _generate_loadable_hpp ( ) :
    return { 'src/loadable/shy_loadable.hpp' :
        'void shy_loadable :: load ( )\n'
        '{\n'
        '}\n' }

def _generate_loadable_injections_h ( ) :
    return { 'src/loadable/shy_loadable_injections.h' :
        '#ifndef _shy_loadable_injections_included\n'
        '#define _shy_loadable_injections_included\n'
        '\n'
        '#include "src/loadable/shy_loadable.h"\n'
        'typedef shy_loadable so_called_loadable ;\n' }

def _generate_loadable_injections_cpp ( ) :
    return { 'src/loadable/shy_loadable_injections.cpp' :
        '#include "src/loadable/shy_loadable_injections.h"\n'
        '#include "src/loadable/shy_loadable.hpp"\n' }
