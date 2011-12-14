import shy_codegen
import unittest

class essential_files_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . fs = shy_codegen . generate ( [ ] )
    def test_common_h ( self ) :
        self . assertEqual ( self . fs [ 'src/common/shy_common.h' ] ,
            'class shy_common\n'
            '{\n'
            'public :\n'
            '    static void init ( ) ;\n'
            '    static void done ( ) ;\n'
            '    static void next_frame ( ) ;\n'
            '} ;\n' )
    def test_common_hpp ( self ) :
        self . assertEqual ( self . fs [ 'src/common/shy_common.hpp' ] ,
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
    def test_common_injections_h ( self ) :
        self . assertEqual ( self . fs [ 'src/common/shy_common_injections.h' ] ,
            '#ifndef _shy_common_injections_included\n'
            '#define _shy_common_injections_included\n'
            '\n'
            '#include "src/common/shy_common.h"\n'
            'typedef shy_common so_called_common ;\n' )
    def test_common_injections_cpp ( self ) :
        self . assertEqual ( self . fs [ 'src/common/shy_common_injections.cpp' ] ,
            '#include "src/common/shy_common_injections.h"\n'
            '#include "src/common/shy_common.hpp"\n' )
    def test_loadable_h ( self ) :
        self . assertEqual ( self . fs [ 'src/loadable/shy_loadable.h' ] ,
            'class shy_loadable\n'
            '{\n'
            'public :\n'
            '    static void load ( ) ;\n'
            '} ;\n' )
    def test_loadable_hpp ( self ) :
        self . assertEqual ( self . fs [ 'src/loadable/shy_loadable.hpp' ] ,
            'void shy_loadable :: load ( )\n'
            '{\n'
            '}\n' )
    def test_loadable_injections_h ( self ) :
        self . assertEqual ( self . fs [ 'src/loadable/shy_loadable_injections.h' ] ,
            '#ifndef _shy_loadable_injections_included\n'
            '#define _shy_loadable_injections_included\n'
            '\n'
            '#include "src/loadable/shy_loadable.h"\n'
            'typedef shy_loadable so_called_loadable ;\n' )
    def test_loadable_injections_cpp ( self ) :
        self . assertEqual ( self . fs [ 'src/loadable/shy_loadable_injections.cpp' ] ,
            '#include "src/loadable/shy_loadable_injections.h"\n'
            '#include "src/loadable/shy_loadable.hpp"\n' )

if __name__ == '__main__' :
    unittest . main ( )
