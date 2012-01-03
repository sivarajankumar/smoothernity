import unittest
import lexer
import tokens

class tokens_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . l = lexer . lexer ( )
        tokens . setup ( self . l )
    def test_underscore ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '_' ] ) ,
            [ { 'type' : 'underscore' , 'value' : '_' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . whitespace_exception , p , [ '__' ] )
        ar ( lexer . whitespace_exception , p , [ '_test' ] )
    def test_number_whole ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '123 -45 - 56 true false' ] ) ,
            [ { 'type' : 'number_whole' , 'value' : '123' }
            , { 'type' : 'number_whole' , 'value' : '-45' }
            , { 'type' : 'number_whole' , 'value' : '- 56' }
            , { 'type' : 'number_whole' , 'value' : 'true' }
            , { 'type' : 'number_whole' , 'value' : 'false' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . whitespace_exception , p , [ '123test' ] )
        ar ( lexer . token_exception , p , [ '--123' ] )
        ar ( lexer . token_exception , p , [ '- - 123' ] )
    def test_number_fract ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '12/34 -5/6 - 78 / 90' ] ) ,
            [ { 'type' : 'number_fract' , 'value' : '12/34' }
            , { 'type' : 'number_fract' , 'value' : '-5/6' }
            , { 'type' : 'number_fract' , 'value' : '- 78 / 90' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . token_exception , p , [ '1 /' ] )
        ar ( lexer . token_exception , p , [ '1 / / 2' ] )
        ar ( lexer . token_exception , p , [ '1 / 2 / 3' ] )
    def test_id ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ 'test test1 test_22' ] ) ,
            [ { 'type' : 'id' , 'value' : 'test' }
            , { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'id' , 'value' : 'test_22' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . token_exception , p , [ 'TEST' ] )
    def test_indents ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ 'test1' , '  test2' ] ) ,
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'eol' }
            , { 'type' : 'indent' , 'delta' : 2 }
            , { 'type' : 'id' , 'value' : 'test2' }
            , { 'type' : 'eol' }
            , { 'type' : 'dedent' , 'delta' : - 2 }
            , { 'type' : 'eof' } ] )
    def test_arrows ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '<- ->' ] ) ,
            [ { 'type' : 'left_arrow' , 'value' : '<-' }
            , { 'type' : 'right_arrow' , 'value' : '->' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . token_exception , p , [ '<<--' ] )
        ar ( lexer . token_exception , p , [ '-->>' ] )
        ar ( lexer . token_exception , p , [ '< -' ] )
        ar ( lexer . token_exception , p , [ '- >' ] )
    def test_curly_brackets ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '{ }' ] ) ,
            [ { 'type' : 'curly_open' , 'value' : '{' }
            , { 'type' : 'curly_close' , 'value' : '}' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . whitespace_exception , p , [ '{}' ] )
    def test_parentheses ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '( )' ] ) ,
            [ { 'type' : 'paren_open' , 'value' : '(' }
            , { 'type' : 'paren_close' , 'value' : ')' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . whitespace_exception , p , [ '()' ] )
    def test_string ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ "'some tokens' 'NO CHECKS HERE'" ] ) ,
            [ { 'type' : 'string' , 'value' : "'some tokens'" }
            , { 'type' : 'string' , 'value' : "'NO CHECKS HERE'" }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . token_exception , p , [ "'" ] )
        ar ( lexer . token_exception , p , [ "'test" ] )
        ar ( lexer . whitespace_exception , p , [ "test'" ] )
    def test_expression ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '[some tokens] [NO CHECKS HERE]' ] ) ,
            [ { 'type' : 'expression' , 'value' : '[some tokens]' }
            , { 'type' : 'expression' , 'value' : '[NO CHECKS HERE]' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . token_exception , p , [ '[' ] )
        ar ( lexer . token_exception , p , [ '[test' ] )
        ar ( lexer . whitespace_exception , p , [ 'test]' ] )
    def test_keywords ( self ) :
        def check ( kw ) :
            p = self . l . parse
            self . assertEqual ( p ( [ kw ] ) ,
                [ { 'type' : 'keyword' , 'value' : kw } 
                , { 'type' : 'eol' }
                , { 'type' : 'eof' } ] )
            self . assertEqual ( p ( [ kw + '_test' ] ) ,
                [ { 'type' : 'id' , 'value' : kw + '_test' } 
                , { 'type' : 'eol' }
                , { 'type' : 'eof' } ] )
        kws = \
            [ 'system' , 'machine' , 'state' , 'consts' , 'on' , 'to' , 'is'
            , 'command' , 'if' , 'do' , 'input' , 'entry' , 'exit' , 'initial'
            , 'discard' , 'vars' , 'ops' , 'receive' , 'request' , 'module'
            , 'trace' , 'with' , 'else' , 'while' , 'args' , 'proc' , 'init'
            , 'done' , 'copy' , 'paste' , 'replace' , 'module_name' , 'types'
            , 'reply' , 'messages' , 'stateless' , 'elif' , 'module_queue'
            , 'any' , 'all' , 'send' ]
        for kw in kws :
            check ( kw )
            
if __name__ == '__main__' :
    unittest . main ( )
