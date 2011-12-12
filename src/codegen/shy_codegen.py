def shy_generate ( lines ) :
    return _shy_generate_common_h ( )

def _shy_generate_common_h ( ) :
    return { 'src/common/shy_common.h' :
        'class shy_common\n'
        '{\n'
        'public :\n'
        '    static void init ( ) ;\n'
        '    static void done ( ) ;\n'
        '    static void next_frame ( ) ;\n'
        '} ;\n' }
