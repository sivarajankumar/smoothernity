import shy_codegen
import unittest

class tokenize_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . text = None
        self . tokens = None
    def tearDown ( self ) :
        self . assertEqual ( shy_codegen . tokenizer ( self . text ) . run ( ) , self . tokens )
        self . assertEqual ( shy_codegen . stringize ( self . tokens ) , self . text )
    def test_empty ( self ) :
        self . text = [ ]
        self . tokens = [ ]
    def test_token ( self ) :
        self . text = [ 'test' ]
        self . tokens = [ [ ( 0 , 'test' ) ] ]
    def test_tokens ( self ) :
        self . text = \
            [ '  test1 test2   test3'
            , '    test4' ]
        self . tokens = \
            [ [ ( 2 , 'test1' ) 
              , ( 8 , 'test2' )
              , ( 16 , 'test3' ) ]
            , [ ( 4 , 'test4' ) ] ]
    def test_same_name ( self ) :
        self . text = [ 'test test' ]
        self . tokens = \
            [ [ ( 0 , 'test' )
              , ( 5 , 'test' ) ] ]
    def test_short ( self ) :
        self . text = [ 'test t' ]
        self . tokens = \
            [ [ ( 0 , 'test' )
              , ( 5 , 't' ) ] ]
    def test_overlap ( self ) :
        self . text = \
            [ 'test1'
            , '     test2' ]
        self . tokens = \
            [ [ ( 0 , 'test1' ) ]
            , [ ( 5 , 'test2' ) ] ]
    def test_string ( self ) :
        self . text = [ "'test1 test2' test3" ]
        self . tokens = \
            [ [ ( 0 , "'test1 test2'" )
              , ( 14 , 'test3' )
              ] ]
    def test_underscore ( self ) :
        self . text = [ '_' ]
        self . tokens = [ [ ( 0 , '_' ) ] ]
    def test_divide ( self ) :
        self . text = [ '/' ]
        self . tokens = [ [ ( 0 , '/' ) ] ]
    def test_left_arrow ( self ) :
        self . text = [ '<-' ]
        self . tokens = [ [ ( 0 , '<-' ) ] ]
    def test_underscore_in_word ( self ) :
        self . text = [ 'some_word' ]
        self . tokens = [ [ ( 0 , 'some_word' ) ] ]
    def test_number ( self ) :
        self . text = [ '123' ]
        self . tokens = [ [ ( 0 , '123' ) ] ]

class preprocess_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . i = None
        self . o = None
    def tearDown ( self ) :
        self . assertEqual ( shy_codegen . preprocessor ( self . i ) . run ( ) , self . o )
    def test_empty ( self ) :
        self . i = self . o = [ ]
    def test_plain_text ( self ) :
        self . i = self . o = [ 'first line' , 'second line' ]
    def test_empty_lines ( self ) :
        self . i = [ '' , '' ]
        self . o = [ ]
    def test_copy_paste_same_line ( self ) :
        self . i = [ 'copy foo test1 bar' , 'paste replace test1 with test22' ]
        self . o = [ 'foo test22 bar' ]
    def test_copy_paste_multi_token ( self ) :
        self . i = [ 'copy foo test1 bar' , 'paste replace test1 with test22 test33' ]
        self . o = [ 'foo test22 test33 bar' ]
    def test_copy_paste_multi_replace ( self ) :
        self . i = [ 'copy foo bar' 
                   , 'paste replace foo with test1' 
                   , '      replace bar with test2' ]
        self . o = [ 'test1 test2' ]
    def test_copy_paste_substring ( self ) :
        self . i = [ 'copy footest1bar' , 'paste replace test1 with test22' ]
        self . o = [ 'footest22bar' ]
    def test_copy_paste_multi_substring ( self ) :
        self . i = [ 'copy footest1bartest1foo' , 'paste replace test1 with test2' ]
        self . o = [ 'footest2bartest2foo' ]
    def test_copy_paste_multi_line ( self ) :
        self . i = [ 'copy foo test1 bar'
                   , 'paste replace test1 with'
                   , '          test22'
                   , '          test33' ]
        self . o = [ 'foo test22' 
                   , '    test33 bar' ]
    def test_copy_paste_multi_line_substring ( self ) :
        self . i = [ 'copy footest1bar'
                   , 'paste replace test1 with'
                   , '          test22'
                   , '          test33' ]
        self . o = [ 'footest22' 
                   , 'test33bar' ]
    def test_copy_paste_multi_line_multi_substring ( self ) :
        self . i = [ 'copy bla footest1bartest1foo  bla'
                   , '     bla footest1bartest1foo  bla'
                   , 'paste replace test1 with'
                   , '          test22'
                   , '          test33' ]
        self . o = [ 'bla footest22' 
                   , '    test33bartest22' 
                   , '    test33foo  bla'
                   , 'bla footest22' 
                   , '    test33bartest22' 
                   , '    test33foo  bla' ]
    def test_indents ( self ) :
        self . i = [ '  copy'
                   , '    foo test1'
                   , '      bar'
                   , '      test1'
                   , '        foobar'
                   , '  paste'
                   , '    replace test1 with test222' ]
        self . o = [ '  foo test222' 
                   , '    bar'
                   , '    test222'
                   , '      foobar' ]
    def test_plain_text_after_paste ( self ) :
        self . i = [ '  copy test1'
                   , '  paste replace test1 with test222'
                   , '  next line' ]
        self . o = [ '  test222' 
                   , '  next line' ]

class reify_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        class file_mock :
            def __init__ ( self , to_read = str ( ) ) :
                self . _to_read = to_read
                self . _written = [ ]
            def write ( self , what ) :
                self . _written . append ( what )
            def read ( self ) :
                return self . _to_read
            def _open ( self ) :
                return self
        class trace_mock :
            def __init__ ( self ) :
                self . _write_errors = [ ]
                self . _created = [ ]
                self . _overwritten = [ ]
                self . _dir_created = [ ]
            def write_error ( self , name , error ) :
                self . _write_errors . append ( ( name , error ) )
            def created ( self , name ) :
                self . _created . append ( name )
            def overwritten ( self , name ) :
                self . _overwritten . append ( name )
            def dir_created ( self , name ) :
                self . _dir_created . append ( name )
        class options_mock :
            def __init__ ( self ) :
                self . _file_prefix = ''
            def file_prefix ( self ) :
                return self . _file_prefix
        class os_mock :
            def __init__ ( self ) :
                self . _makedirs = [ ]
            def makedirs ( self , dir ) :
                self . _makedirs . append ( dir )
        def open_mock ( name , mode ) :
            return self . fs [ name ] [ mode ] . _open ( )
        self . fm = file_mock
        self . fs = { }
        self . t = trace_mock ( )
        self . op = options_mock ( )
        self . om = os_mock ( )
        self . r = lambda x : shy_codegen . reify ( x , open_mock , self . t , self . op , self . om )
    def test_overwrite_file ( self ) :
        self . fs = {
            'file1' : { 'r' : self . fm ( 'contents1' ) } ,
            'file2' : { 'r' : self . fm ( 'contents2' ) ,
                        'w' : self . fm ( ) } }
        self . r ( { 'file1' : 'contents1' , 'file2' : 'contents3' } )
        f = self . fs [ 'file2' ] [ 'w' ]
        self . assertEqual ( f . _written , [ 'contents3' ] )
        self . assertEqual ( self . t . _overwritten , [ 'file2' ] )
    def test_create_new_file ( self ) :
        class file_ex :
            def _open ( self ) :
                raise Exception ( )
        self . fs = { 'file1' : {
            'r' : file_ex ( ) ,
            'w' : self . fm ( ) } }
        self . r ( { 'file1' : 'contents1' } )
        f = self . fs [ 'file1' ] [ 'w' ]
        self . assertEqual ( f . _written , [ 'contents1' ] )
        self . assertEqual ( self . t . _created , [ 'file1' ] )
    def test_order ( self ) :
        self . fs = {
            'file1' : { 'w' : self . fm ( ) } ,
            'file2' : { 'w' : self . fm ( ) } ,
            'file3' : { 'w' : self . fm ( ) } }
        self . r ( { 'file1' : 'c1' , 'file2' : 'c2' , 'file3' : 'c3' } )
        self . assertEqual ( self . t . _created , [ 'file1' , 'file2' , 'file3' ] )
    def test_write_error ( self ) :
        class file_ex :
            def _open ( self ) :
                raise Exception ( 'error1' )
        self . fs = { 'file1' : { 
            'r' : file_ex ( ) ,
            'w' : file_ex ( ) } }
        self . r ( { 'file1' : 'contents1' } )
        self . assertEqual ( self . t . _write_errors , [ ( 'file1' , 'error1' ) ] )
    def test_file_prefix ( self ) :
        self . op . _file_prefix = 'prefix1'
        self . fs = { 'prefix1file1' : {
            'r' : self . fm ( ) ,
            'w' : self . fm ( ) } }
        self . r ( { 'file1' : 'contents1' } )
        f = self . fs [ 'prefix1file1' ] [ 'w' ]
        self . assertEqual ( f . _written , [ 'contents1' ] )
    def test_create_path ( self ) :
        self . op . _file_prefix = 'prefix1/'
        self . fs = { 'prefix1/dir1/file1' : { 'w' : self . fm ( ) } }
        self . r ( { 'dir1/file1' : 'contents1' } )
        self . assertEqual ( self . om . _makedirs , [ 'prefix1/dir1' ] )
        self . assertEqual ( self . t . _dir_created , [ 'prefix1/dir1' ] )
    def test_create_path_error ( self ) :
        def makedirs_ex ( dirs ) :
            raise Exception ( )
        self . om . makedirs = makedirs_ex
        self . op . _file_prefix = 'prefix1/'
        self . fs = { 'prefix1/dir1/file1' : { 'w' : self . fm ( ) } }
        self . r ( { 'dir1/file1' : 'contents1' } )
        f = self . fs [ 'prefix1/dir1/file1' ] [ 'w' ]
        self . assertEqual ( f . _written , [ 'contents1' ] )
        self . assertEqual ( self . t . _dir_created , [ ] )

class essential_files_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . fs = shy_codegen . generate ( [ ] )
    def test_common_h ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/common/shy_common.h' ] ,
            'class shy_common\n'
            '{\n'
            'public :\n'
            '    static void init ( ) ;\n'
            '    static void done ( ) ;\n'
            '    static void next_frame ( ) ;\n'
            '} ;\n' )
    def test_common_hpp ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/common/shy_common.hpp' ] ,
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
        self . assertEqual ( self . fs [ 'autogenerated/common/shy_common_injections.h' ] ,
            '#ifndef _shy_common_injections_included\n'
            '#define _shy_common_injections_included\n'
            '\n'
            '#include "autogenerated/common/shy_common.h"\n'
            'typedef shy_common so_called_common ;\n'
            '\n'
            '#endif\n' )
    def test_common_injections_cpp ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/common/shy_common_injections.cpp' ] ,
            '#include "autogenerated/common/shy_common_injections.h"\n'
            '#include "autogenerated/common/shy_common.hpp"\n' )
    def test_loadable_h ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/loadable/shy_loadable.h' ] ,
            'class shy_loadable\n'
            '{\n'
            'public :\n'
            '    static void load ( ) ;\n'
            '} ;\n' )
    def test_loadable_hpp ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/loadable/shy_loadable.hpp' ] ,
            'void shy_loadable :: load ( )\n'
            '{\n'
            '}\n' )
    def test_loadable_injections_h ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/loadable/shy_loadable_injections.h' ] ,
            '#ifndef _shy_loadable_injections_included\n'
            '#define _shy_loadable_injections_included\n'
            '\n'
            '#include "autogenerated/loadable/shy_loadable.h"\n'
            'typedef shy_loadable so_called_loadable ;\n'
            '\n'
            '#endif\n' )
    def test_loadable_injections_cpp ( self ) :
        self . assertEqual ( self . fs [ 'autogenerated/loadable/shy_loadable_injections.cpp' ] ,
            '#include "autogenerated/loadable/shy_loadable_injections.h"\n'
            '#include "autogenerated/loadable/shy_loadable.hpp"\n' )

if __name__ == '__main__' :
    unittest . main ( )
