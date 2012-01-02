from hashlib import md5
from os . path import dirname
from copy import deepcopy

def tokenize ( lines ) :
    res = [ ]
    for line in lines :
        indent = 0
        tline = [ ]
        for word in line . split ( ' ' ) :
            if len ( word ) > 0 :
                tline . append ( ( indent , word ) )
            indent += len ( word ) + 1
        res . append ( tline )
    return res

def stringize ( tlines ) :
    res = [ ]
    for tokens in tlines :
        res . append ( '' )
        for indent , token in tokens :
            res [ - 1 ] += ' ' * ( indent - len ( res [ - 1 ] ) )
            res [ - 1 ] += token
    return res

def _tokens_in_line ( tlines ) :
    return tlines [ 0 ]

def _lines_count ( tlines ) :
    return len ( tlines ) > 0

def _first_token ( tlines ) :
    return tlines [ 0 ] [ 0 ]

def _trim_last_empty_line ( tlines ) :
    if not tlines [ - 1 ] :
        return tlines [ : - 1 ]
    else :
        return tlines

def _make_last_empty_line ( tlines ) :
    if tlines :
        if tlines [ - 1 ] :
            return tlines + [ [ ] ]
        else :
            return tlines
    else :
        return [ [ ] ]

def _pop_first_token ( tlines ) :
    tlines [ 0 ] = tlines [ 0 ] [ 1 : ]

def _add_last_token ( tlines , indent , token ) :
    tlines [ - 1 ] . append ( ( indent , token ) )

def _pop_first_line ( tlines ) :
    return tlines [ 1 : ]

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
        self . _tlines = tlines
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
    def _state_itoken ( self , itoken ) :
        return _token_state ( itoken = itoken )
    def _state_eol ( self ) :
        return _token_state ( eol = True )
    def _state_eof ( self ) :
        return _token_state ( eof = True )

class preprocessor :

    def __init__ ( self , lines ) :
        self . _input = _input_tokens ( tokenize ( lines ) )
        self . _output = [ [ ] ]

    def run ( self ) :
        while True :
            if self . _input . state ( ) . itoken ( ) :
                indent , token = self . _input . state ( ) . itoken ( )
                if token == 'copy' :
                    self . _copy_paste ( )
                else :
                    _add_last_token ( self . _output , indent , token )
                    self . _input . next_token ( )
            elif self . _input . state ( ) . eol ( ) :
                self . _output = _make_last_empty_line ( self . _output )
                self . _input . next_token ( )
            elif self . _input . state ( ) . eof ( ) :
                break
            else :
                self . _input . next_token ( )
        self . _output = _trim_last_empty_line ( self . _output )
        return stringize ( self . _output )

    def _copy_paste ( self ) :
        self . _output = _trim_last_empty_line ( self . _output )
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
        self . _output = _make_last_empty_line ( self . _output )

    def _copy_paste_read_body ( self ) :
        copy_indent , token = self . _input . state ( ) . itoken ( )
        assert token == 'copy'
        self . _input . next_itoken ( )
        indent , token = self . _input . state ( ) . itoken ( )
        first_indent = indent
        body = [ [ ] ]
        while True :
            if self . _input . state ( ) . itoken ( ) :
                indent , token = self . _input . state ( ) . itoken ( )
                if indent <= copy_indent :
                    break
                self . _input . next_token ( )
                body [ - 1 ] . append ( ( indent - first_indent + copy_indent , token ) )
            elif self . _input . state ( ) . eol ( ) :
                self . _input . next_token ( )
                body . append ( [ ] )
            elif self . _input . state ( ) . eof ( ) :
                break
        if not body [ - 1 ] :
            body = body [ : - 1 ]
        return body , copy_indent

    def _copy_paste_do_paste ( self , body ) :
        indent , token = self . _input . state ( ) . itoken ( )
        assert token == 'paste'
        self . _input . next_itoken ( )
        replaces = self . _copy_paste_read_replaces ( )
        buf = deepcopy ( body )
        for replace_what , replace_with in replaces . items ( ) :
            buf = self . _copy_paste_do_replace ( buf , replace_what , replace_with )
        self . _output += buf

    def _copy_paste_read_replaces ( self ) :
        replaces = { }
        first_indent , token = self . _input . state ( ) . itoken ( )
        assert token == 'replace'
        while True :
            if self . _input . state ( ) . itoken ( ) :
                indent , token = self . _input . state ( ) . itoken ( )
                if indent == first_indent and token == 'replace' :
                    what = self . _copy_paste_read_replace_what ( )
                    with_what = self . _copy_paste_read_replace_with_what ( first_indent )
                    replaces [ '' . join ( stringize ( what ) ) ] = with_what
                else :
                    break
            elif self . _input . state ( ) . eof ( ) :
                break
            else :
                self . _input . next_token ( )
        return replaces

    def _copy_paste_read_replace_what ( self ) :
        indent , token = self . _input . state ( ) . itoken ( )
        assert token == 'replace'
        self . _input . next_itoken ( )
        first_indent , token = self . _input . state ( ) . itoken ( )
        what = [ [ ] ]
        while True :
            if self . _input . state ( ) . itoken ( ) :
                indent , token = self . _input . state ( ) . itoken ( )
                if token == 'with' or indent < first_indent :
                    break
                else :
                    what [ - 1 ] . append ( ( indent - first_indent , token ) )
                    self . _input . next_token ( )
            elif self . _input . state ( ) . eol ( ) :
                what . append ( [ ] )
                self . _input . next_token ( )
            elif self . _input . state ( ) . eof ( ) :
                break
            else :
                self . _input . next_token ( )
        if not what [ - 1 ] :
            what = what [ : - 1 ]
        return what

    def _copy_paste_read_replace_with_what ( self , replace_indent ) :
        indent , token = self . _input . state ( ) . itoken ( )
        assert token == 'with'
        assert indent > replace_indent
        self . _input . next_itoken ( )
        first_indent , token = self . _input . state ( ) . itoken ( )
        with_what = [ [ ] ]
        while True :
            if self . _input . state ( ) . itoken ( ) :
                indent , token = self . _input . state ( ) . itoken ( )
                if indent >= first_indent :
                    with_what [ - 1 ] . append ( ( indent - first_indent , token ) )
                    self . _input . next_token ( )
                else :
                    break
            elif self . _input . state ( ) . eol ( ) :
                with_what . append ( [ ] )
                self . _input . next_token ( )
            elif self . _input . state ( ) . eof ( ) :
                break
            else :
                self . _input . next_token ( )
        if not with_what [ - 1 ] :
            with_what = with_what [ : - 1 ]
        return with_what

    def _copy_paste_do_replace ( self , arg_body , what , with_what_args ) :
        res = [ [ ] ]
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
                        with_what = deepcopy ( with_what_args )
                        while len ( [ t for tline in with_what for t in tline ] ) > 1 :
                            if with_what [ 0 ] :
                                with_indent , with_token = with_what [ 0 ] [ 0 ]
                                with_what [ 0 ] = with_what [ 0 ] [ 1 : ]
                                res_indent += with_indent
                                res_token += with_token
                                res [ - 1 ] . append ( ( res_indent , res_token ) )
                                shift_indent = len ( stringize ( [ res [ - 1 ] ] ) [ 0 ] ) - indent - len ( token )
                                res_indent , res_token = indent , ''
                            else :
                                with_what = with_what [ 1 : ]
                                if res [ - 1 ] :
                                    res . append ( [ ] )
                                shift_indent = - len ( token )
                        while with_what and not with_what [ 0 ] :
                            with_what = with_what [ 1 : ]
                            if res [ - 1 ] :
                                res . append ( [ ] )
                            shift_indent = - len ( token )
                        with_indent , with_token = with_what [ 0 ] [ 0 ]
                        res_token += with_token
                        res_indent += with_indent
                    part = parts [ - 1 ]
                    res_token += part
                    res [ - 1 ] . append ( ( res_indent , res_token ) )
                    shift_indent = len ( stringize ( [ res [ - 1 ] ] ) [ 0 ] ) - indent - len ( token )
                else :
                    res [ - 1 ] . append ( ( indent , token ) )
            elif body . state ( ) . eol ( ) :
                body . next_token ( )
                shift_indent = 0
                if res [ - 1 ] :
                    res . append ( [ ] )
            elif body . state ( ) . eof ( ) :
                break
            else :
                body . next_token ( )
        if not res [ - 1 ] :
            res = res [ : - 1 ]
        return res

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
    print '\n' . join ( preprocess ( [ l . replace ( '\n' , '' ) for l in lines ] ) )
    reify ( generate ( lines ) , open , trace ( ) , options ( ) , os )
