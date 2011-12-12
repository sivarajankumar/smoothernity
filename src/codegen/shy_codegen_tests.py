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

if __name__ == '__main__' :
    unittest . main ( )
