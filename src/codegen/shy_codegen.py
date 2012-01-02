from hashlib import md5
from os . path import dirname
from copy import deepcopy

class tokenizer :
    def __init__ ( self , lines ) :
        self . _input = deepcopy ( lines )
        self . _output = [ ]
        self . _char = None
        self . _token = ''
        self . _indent = 0
        self . _state = self . _state_first_char
        self . _closing_char = None
        self . _new_line = True
    def run ( self ) :
        while self . _input :
            self . _state ( )
        return self . _output
    def _state_first_char ( self ) :
        if self . _input [ 0 ] :
            self . _char = self . _input [ 0 ] [ 0 ]
            self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            self . _state = self . _state_recognize_char
        else :
            self . _state = self . _state_new_line
    def _state_new_line ( self ) :
        if self . _input [ 0 ] :
            self . _state = self . _state_first_char
        else :
            self . _input = self . _input [ 1 : ]
            self . _indent = 0
            self . _token = ''
            self . _new_line = True
    def _state_recognize_char ( self ) :
        if self . _char == ' ' :
            self . _state = self . _state_whitespace
        elif self . _char . isalpha ( ) :
            self . _state = self . _state_word
        elif self . _char . isdigit ( ) :
            self . _state = self . _state_number
        elif self . _char in [ "'" , '[' ] :
            self . _state = self . _state_citation_begin
        else :
            self . _state = self . _state_arbitrary_token
    def _state_whitespace ( self ) :
        self . _indent += 1
        self . _token = ''
        self . _state = self . _state_first_char
    def _state_word ( self ) :
        if self . _char . isalpha ( ) \
        or self . _char . isdigit ( ) \
        or self . _char == '_' :
            self . _token += self . _char
            if self . _input [ 0 ] :
                self . _char = self . _input [ 0 ] [ 0 ]
                self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            else :
                self . _write_token ( )
                self . _state = self . _state_new_line
        elif self . _char == ' ' :
            self . _write_token ( )
            self . _state = self . _state_recognize_char
        else :
            raise Exception ( 'Wrong char "%s" in word' % self . _char )
    def _state_number ( self ) :
        if self . _char . isdigit ( ) :
            self . _token += self . _char
            if self . _input [ 0 ] :
                self . _char = self . _input [ 0 ] [ 0 ]
                self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            else :
                self . _write_token ( )
                self . _state = self . _state_new_line
        elif self . _char == ' ' :
            self . _write_token ( )
            self . _state = self . _state_recognize_char
        else :
            raise Exception ( 'Wrong char "%s" in number' % self . _char )
    def _state_citation_begin ( self ) :
        self . _token += self . _char
        self . _closing_char = { "'" : "'" , '[' : ']' } [ self . _char ]
        if self . _input [ 0 ] :
            self . _char = self . _input [ 0 ] [ 0 ]
            self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            self . _state = self . _state_citation_content
        else :
            raise Exception ( 'Opening tag "%s" at the end of the line' % self . _char )
    def _state_citation_content ( self ) :
        if self . _char == self . _closing_char :
            self . _state = self . _state_citation_end
        else :
            self . _token += self . _char
            if self . _input [ 0 ] :
                self . _char = self . _input [ 0 ] [ 0 ]
                self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            else :
                raise Exception ( 'End of the line encountered in citation' )
    def _state_citation_end ( self ) :
        self . _token += self . _char
        if self . _input [ 0 ] :
            self . _char = self . _input [ 0 ] [ 0 ]
            self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            if self . _char == ' ' :
                self . _write_token ( )
                self . _state = self . _state_recognize_char
            else :
                raise Exception ( 'Unexpected character "%s" after closing tag "%s"' % ( self . _char , self . _closing_char ) )
        else :
            self . _write_token ( )
            self . _state = self . _state_new_line
    def _state_arbitrary_token ( self ) :
        if self . _char == ' ' :
            self . _check_arbitrary_token ( )
            self . _write_token ( )
            self . _state = self . _state_whitespace
        else :
            self . _token += self . _char
            if self . _input [ 0 ] :
                self . _char = self . _input [ 0 ] [ 0 ]
                self . _input [ 0 ] = self . _input [ 0 ] [ 1 : ]
            else :
                self . _check_arbitrary_token ( )
                self . _write_token ( )
                self . _state = self . _state_new_line
    def _check_arbitrary_token ( self ) :
        if self . _token not in [ '_' , '-' , '/' , '{' , '}' , '<-' , '->' ] :
            raise Exception ( 'Unknown arbitrary token "%s"' % self . _token )
    def _write_token ( self ) :
        if self . _new_line :
            self . _output . append ( [ ] )
            self . _new_line = False
        self . _output [ - 1 ] . append ( ( self . _indent , self . _token ) )
        self . _indent += len ( self . _token )
        self . _token = ''

def stringize ( tlines ) :
    res = [ ]
    for tokens in tlines :
        res . append ( '' )
        for indent , token in tokens :
            assert indent >= len ( res [ - 1 ] )
            res [ - 1 ] += ' ' * ( indent - len ( res [ - 1 ] ) )
            res [ - 1 ] += token
    return res

class _token_state :
    def __init__ ( self , itoken = None , eol = False , eof = False ) :
        self . _itoken = itoken
        self . _eol = eol
        self . _eof = eof
    def itoken ( self ) :
        return self . _itoken
    def eol ( self ) :
        return self . _eol
    def eof ( self ) :
        return self . _eof

class _input_tokens :
    def __init__ ( self , tlines ) :
        self . _tlines = deepcopy ( tlines )
        self . _state = _token_state ( )
    def next_token ( self ) :
        if self . _tlines :
            if self . _tlines [ 0 ] :
                self . _state = self . _state_itoken ( self . _tlines [ 0 ] [ 0 ] )
                self . _tlines [ 0 ] = self . _tlines [ 0 ] [ 1 : ]
            else :
                self . _tlines = self . _tlines [ 1 : ]
                self . _state = self . _state_eol ( )
        else :
            self . _state = self . _state_eof ( )
    def next_itoken ( self ) :
        self . _state = _token_state ( )
        while True :
            if self . state ( ) . eof ( ) :
                raise Exception ( 'No more itokens' )
            elif self . state ( ) . itoken ( ) :
                break
            else :
                self . next_token ( )
    def state ( self ) :
        return self . _state
    def tokens_count ( self ) :
        return len ( [ t for tline in self . _tlines for t in tline ] )
    def _state_itoken ( self , itoken ) :
        return _token_state ( itoken = itoken )
    def _state_eol ( self ) :
        return _token_state ( eol = True )
    def _state_eof ( self ) :
        return _token_state ( eof = True )

class _output_tokens :
    def __init__ ( self ) :
        self . _tlines = [ ]
        self . _newline = False
    def itoken ( self , indent , token ) :
        if not self . _tlines :
            self . _tlines . append ( [ ] )
        if self . _newline :
            if self . _tlines [ - 1 ] :
                self . _tlines . append ( [ ] )
            self . _newline = False
        self . _tlines [ - 1 ] . append ( ( indent , token ) )
    def new_line ( self ) :
        self . _newline = True
    def get_contents ( self ) :
        return self . _tlines
    def tokens ( self , tokens ) :
        self . _tlines += tokens

class preprocessor :

    def __init__ ( self , lines ) :
        self . _input = _input_tokens ( tokenizer ( lines ) . run ( ) )
        self . _output = _output_tokens ( )
        self . _state = None
        self . _indent = None
        self . _token = None
        self . _copy_indent = None
        self . _copy_body = None
        self . _copy_body_indent = None
        self . _replaces = None
        self . _replace_indent = None
        self . _replace_what = None
        self . _replace_what_indent = None
        self . _replace_with_what = None
        self . _replace_with_what_indent = None

    def run ( self ) :
        self . _state = self . _state_read_token
        self . _input . next_token ( )
        while not self . _input . state ( ) . eof ( ) :
            self . _state ( )
        return stringize ( self . _output . get_contents ( ) )

    def _state_read_token ( self ) :
        if self . _input . state ( ) . itoken ( ) :
            self . _indent , self . _token = self . _input . state ( ) . itoken ( )
            self . _state = self . _state_recognize_token
        elif self . _input . state ( ) . eol ( ) :
            self . _state = self . _state_new_line

    def _state_new_line ( self ) :
        assert self . _input . state ( ) . eol ( )
        self . _output . new_line ( )
        self . _input . next_token ( )
        self . _state = self . _state_read_token

    def _state_recognize_token ( self ) :
        assert self . _input . state ( ) . itoken ( )
        if self . _token == 'copy' :
            self . _state = self . _state_copy_paste_begin
        else :
            self . _state = self . _state_write_token

    def _state_write_token ( self ) :
        self . _output . itoken ( self . _indent , self . _token )
        self . _input . next_token ( )
        self . _state = self . _state_read_token

    def _state_copy_paste_begin ( self ) :
        assert self . _token == 'copy'
        self . _copy_indent = self . _indent
        self . _input . next_itoken ( )
        self . _indent , self . _token = self . _input . state ( ) . itoken ( )
        self . _copy_body_indent = self . _indent
        self . _copy_body = _output_tokens ( )
        self . _state = self . _state_copy_paste_read_body_token

    def _state_copy_paste_read_body ( self ) :
        if self . _input . state ( ) . itoken ( ) :
            self . _indent , self . _token = self . _input . state ( ) . itoken ( )
            self . _state = self . _state_copy_paste_read_body_token
        elif self . _input . state ( ) . eol ( ) :
            self . _state = self . _state_copy_paste_read_body_new_line

    def _state_copy_paste_read_body_token ( self ) :
        if self . _indent > self . _copy_indent :
            self . _copy_body . itoken ( self . _indent - self . _copy_body_indent , self . _token )
            self . _input . next_token ( )
            self . _state = self . _state_copy_paste_read_body
        else :
            self . _state = self . _state_copy_paste_read_paste

    def _state_copy_paste_read_body_new_line ( self ) :            
        self . _copy_body . new_line ( )
        self . _input . next_token ( )
        self . _state = self . _state_copy_paste_read_body

    def _state_copy_paste_read_paste ( self ) :
        assert self . _input . state ( ) . itoken ( )
        if self . _indent == self . _copy_indent :
            if self . _token == 'paste' :
                self . _input . next_itoken ( )
                self . _indent , self . _token = self . _input . state ( ) . itoken ( )
                self . _state = self . _state_copy_paste_read_replace_begin
            else :
                raise Exception ( 'Expected "paste", got "%s" instead', self . _token )
        else :
            raise Exception ( 'Unexpected indent of "paste" section' )

    def _state_copy_paste_read_replace_begin ( self ) :
        if self . _indent > self . _copy_indent :
            self . _replaces = { }
            self . _replace_indent = self . _indent
            self . _state = self . _state_copy_paste_read_replace_keyword
        else :
            raise Exception ( 'Unexpected first indent of "replace" section' )

    def _state_copy_paste_read_replace_keyword ( self ) :
        if self . _indent == self . _replace_indent :
            if self . _token == 'replace' :
                self . _input . next_token ( )
                self . _state = self . _state_copy_paste_read_replace_what_begin
            else :
                raise Exception ( 'Expected "replace", got "%s" instead', self . _token )
        else :
            raise Exception ( 'Unexpected indent of "replace" section' )

    def _state_copy_paste_read_replace_what_begin ( self ) :
        if self . _input . state ( ) . itoken ( ) :
            self . _indent , self . _token = self . _input . state ( ) . itoken ( )
            self . _replace_what_indent = self . _indent
            self . _replace_what = _output_tokens ( )
            self . _input . next_token ( )
            self . _state = self . _state_copy_paste_read_replace_what_body
        else :
            raise Exception ( 'Expected token after "replace" keyword' )

    def _state_copy_paste_read_replace_what_body ( self ) :
        if self . _input . state ( ) . itoken ( ) :
            self . _indent , self . _token = self . _input . state ( ) . itoken ( )
            assert self . _indent >= self . _replace_what_indent
            if self . _token == 'with' :
                self . _input . next_itoken ( )
                self . _indent , self . _token = self . _input . state ( ) . itoken ( )
                self . _state = self . _state_copy_paste_read_replace_with_what_begin
            else :
                self . _replace_what . itoken ( 
                    self . _indent - self . _replace_what_indent , self . _token )
                self . _input . next_token ( )
        else :
            raise Exception ( 'Expected token in "replace what" section' )

    def _state_copy_paste_read_replace_with_what_begin ( self ) :
        if self . _indent > self . _replace_indent :
            self . _replace_with_what = _output_tokens ( )
            self . _replace_with_what_indent = self . _indent
            self . _state = self . _state_copy_paste_read_replace_with_what_token
        else :
            raise Exception ( 'Unexpected indent in "replace with" section' )

    def _state_copy_paste_read_replace_with_what_body ( self ) :
        if self . _input . state ( ) . itoken ( ) :
            self . _indent , self . _token = self . _input . state ( ) . itoken ( )
            self . _state = self . _state_copy_paste_read_replace_with_what_token
        elif self . _input . state ( ) . eol ( ) :
            self . _state = self . _state_copy_paste_read_replace_with_what_new_line

    def _state_copy_paste_read_replace_with_what_token ( self ) :
        if self . _indent >= self . _replace_with_what_indent :
            self . _replace_with_what . itoken (
                self . _indent - self . _replace_with_what_indent , self . _token )
            self . _input . next_token ( )
            self . _state = self . _state_copy_paste_read_replace_with_what_body
        else :
            what = '' . join ( stringize ( self . _replace_what . get_contents ( ) ) )
            with_what = self . _replace_with_what . get_contents ( )
            self . _replaces [ what ] = with_what
            if self . _token == 'replace' :
                self . _state = self . _state_copy_paste_read_replace_keyword
            else :
                self . _state = self . _state_copy_paste_do_paste_begin

    def _state_copy_paste_read_replace_with_what_new_line ( self ) :
        self . _replace_with_what . new_line ( )
        self . _input . next_token ( )
        self . _state = self . _state_copy_paste_read_replace_with_what_body

    def _state_copy_paste_do_paste_begin ( self ) :
        self . _state = self . _state_copy_paste_do_paste_end

    def _state_copy_paste_do_paste_end ( self ) :
        if self . _token == 'paste' :
            self . _state = self . _state_copy_paste_read_paste
        else :
            self . _state = self . _state_read_token

    def _copy_paste ( self ) :
        body , copy_indent = self . _copy_paste_read_body ( )
        while True :
            if self . _input . state ( ) . itoken ( ) :
                indent , token = self . _input . state ( ) . itoken ( )
                if indent == copy_indent and token == 'paste' :
                    self . _copy_paste_do_paste ( body )
                else :
                    break
            elif self . _input . state ( ) . eof ( ) :
                break
            else :
                self . _input . next_token ( )
        self . _output . new_line ( )

    def _copy_paste_do_paste ( self , body ) :
        indent , token = self . _input . state ( ) . itoken ( )
        assert token == 'paste'
        self . _input . next_itoken ( )
        replaces = self . _copy_paste_read_replaces ( )
        buf = body . get_contents ( )
        for replace_what , replace_with in replaces . items ( ) :
            buf = self . _copy_paste_do_replace ( buf , replace_what , replace_with )
        self . _output . tokens ( buf )

    def _copy_paste_do_replace ( self , arg_body , what , arg_with_what ) :
        res = _output_tokens ( )
        shift_indent = 0
        body = _input_tokens ( arg_body )
        while True :
            if body . state ( ) . itoken ( ) :
                indent , token = body . state ( ) . itoken ( )
                body . next_token ( )
                indent += shift_indent
                if what in token :
                    parts = token . split ( what )
                    res_indent , res_token = indent , ''
                    shift_indent = - len ( token )
                    for part in parts [ : - 1 ] :
                        res_token += part
                        shift_indent += len ( part )
                        with_what = _input_tokens ( arg_with_what )
                        while with_what . tokens_count ( ) :
                            if with_what . state ( ) . itoken ( ) :
                                with_indent , with_token = with_what . state ( ) . itoken ( )
                                with_what . next_token ( )
                                res_indent += with_indent
                                res_token += with_token
                                res . itoken ( res_indent , res_token )
                                shift_indent = len ( stringize ( [ res . get_contents ( ) [ - 1 ] ] ) [ 0 ] ) - indent - len ( token )
                                res_indent , res_token = indent , ''
                            elif with_what . state ( ) . eol ( ) :
                                with_what . next_token ( )
                                res . new_line ( )
                                shift_indent = - len ( token )
                            elif with_what . state ( ) . eof ( ) :
                                break
                            else :
                                with_what . next_token ( )
                        while True :
                            if with_what . state ( ) . itoken ( ) :
                                with_indent , with_token = with_what . state ( ) . itoken ( )
                                res_token += with_token
                                res_indent += with_indent
                                break
                            elif with_what . state ( ) . eol ( ) :
                                with_what . next_token ( )
                                res . new_line ( )
                                shift_indent = - len ( token )
                            elif with_what . state ( ) . eof ( ) :
                                break
                            else :
                                with_what . next_token ( )
                    res_token += parts [ - 1 ]
                    res . itoken ( res_indent , res_token )
                    shift_indent = len ( stringize ( [ res . get_contents ( ) [ - 1 ] ] ) [ 0 ] ) - indent - len ( token )
                else :
                    res . itoken ( indent , token )
            elif body . state ( ) . eol ( ) :
                body . next_token ( )
                shift_indent = 0
                res . new_line ( )
            elif body . state ( ) . eof ( ) :
                break
            else :
                body . next_token ( )
        return res . get_contents ( )

def reify ( data , open_func , trace , options , os_mod ) :
    for raw_name , contents in sorted ( data . items ( ) ) :
        name = options . file_prefix ( ) + raw_name
        dir = dirname ( name )
        try :
            os_mod . makedirs ( dir )
            trace . dir_created ( dir )
        except :
            pass
        try :
            old_md5 = md5 ( open_func ( name , 'r' ) . read ( ) ) . hexdigest ( )
        except :
            old_md5 = None
        new_md5 = md5 ( contents ) . hexdigest ( )
        if new_md5 != old_md5 :
            try :
                open_func ( name , 'w' ) . write ( contents )
                if old_md5 is None :
                    trace . created ( name )
                else :
                    trace . overwritten ( name )
            except Exception as e :
                trace . write_error ( name , str ( e ) )

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
    return { 'autogenerated/common/shy_common.h' :
        'class shy_common\n'
        '{\n'
        'public :\n'
        '    static void init ( ) ;\n'
        '    static void done ( ) ;\n'
        '    static void next_frame ( ) ;\n'
        '} ;\n' }

def _generate_common_hpp ( ) :
    return { 'autogenerated/common/shy_common.hpp' :
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
    return { 'autogenerated/common/shy_common_injections.h' :
        '#ifndef _shy_common_injections_included\n'
        '#define _shy_common_injections_included\n'
        '\n'
        '#include "autogenerated/common/shy_common.h"\n'
        'typedef shy_common so_called_common ;\n'
        '\n'
        '#endif\n' }

def _generate_common_injections_cpp ( ) :
    return { 'autogenerated/common/shy_common_injections.cpp' :
        '#include "autogenerated/common/shy_common_injections.h"\n'
        '#include "autogenerated/common/shy_common.hpp"\n' }

def _generate_loadable_h ( ) :
    return { 'autogenerated/loadable/shy_loadable.h' :
        'class shy_loadable\n'
        '{\n'
        'public :\n'
        '    static void load ( ) ;\n'
        '} ;\n' }

def _generate_loadable_hpp ( ) :
    return { 'autogenerated/loadable/shy_loadable.hpp' :
        'void shy_loadable :: load ( )\n'
        '{\n'
        '}\n' }

def _generate_loadable_injections_h ( ) :
    return { 'autogenerated/loadable/shy_loadable_injections.h' :
        '#ifndef _shy_loadable_injections_included\n'
        '#define _shy_loadable_injections_included\n'
        '\n'
        '#include "autogenerated/loadable/shy_loadable.h"\n'
        'typedef shy_loadable so_called_loadable ;\n'
        '\n'
        '#endif\n' }

def _generate_loadable_injections_cpp ( ) :
    return { 'autogenerated/loadable/shy_loadable_injections.cpp' :
        '#include "autogenerated/loadable/shy_loadable_injections.h"\n'
        '#include "autogenerated/loadable/shy_loadable.hpp"\n' }

if __name__ == '__main__' :
    from sys import argv
    from sys import stdin
    import os

    class trace :
        def write_error ( self , name , error ) :
            print 'Cannot write file "' + name + '": %s' % error
        def created ( self , name ) :
            print 'File "' + name + '" has been created.'
        def overwritten ( self , name ) :
            print 'File "' + name + '" has been overwritten.'
        def dir_created ( self , name ) :
            print 'Path "' + name + '" has been created.'

    class options :
        def file_prefix ( self ) :
            return argv [ 1 ]
        
    lines = stdin . readlines ( )
    print '\n' . join ( preprocessor ( [ l . replace ( '\n' , '' ) for l in lines ] ) . run ( ) )
    reify ( generate ( lines ) , open , trace ( ) , options ( ) , os )
