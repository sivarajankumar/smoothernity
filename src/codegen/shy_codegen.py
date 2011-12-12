def shy_generate ( lines ) :
    res = { }
    res . update ( _shy_generate_common_h ( ) )
    res . update ( _shy_generate_common_hpp ( ) )
    return res

def _shy_generate_common_h ( ) :
    return { 'src/common/shy_common.h' :
        'class shy_common\n'
        '{\n'
        'public :\n'
        '    static void init ( ) ;\n'
        '    static void done ( ) ;\n'
        '    static void next_frame ( ) ;\n'
        '} ;\n' }

def _shy_generate_common_hpp ( ) :
    return  { 'src/common/shy_common.hpp' :
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
