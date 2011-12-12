import shy_codegen
import unittest

class shy_codegen_test_case ( unittest . TestCase ) :
    def test_common_h ( self ) :
        fs = shy_codegen . shy_generate ( [ ] )
        self . assertEqual ( fs [ 'src/common/shy_common.h' ] ,
            'class shy_common\n'
            '{\n'
            'public :\n'
            '    static void init ( ) ;\n'
            '    static void done ( ) ;\n'
            '    static void next_frame ( ) ;\n'
            '} ;\n' )
    def test_common_hpp ( self ) :
        fs = shy_codegen . shy_generate ( [ ] )
        self . assertEqual ( fs [ 'src/common/shy_common.hpp' ] ,
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
            '}\n' )

if __name__ == '__main__' :
    unittest . main ( )
