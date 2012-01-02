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

def preprocess ( lines ) :
    res = [ [ ] ]
    tlines = tokenize ( lines )
    while tlines :
        if tlines [ 0 ] :
            indent , token = tlines [ 0 ] [ 0 ]
            if token == 'copy' :
                if not res [ - 1 ] :
                    res = res [ : - 1 ]
                tlines , res = _copy_paste ( tlines , res )
                if res [ - 1 ] :
                    res . append ( [ ] )
            else :
                tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
                res [ - 1 ] . append ( ( indent , token ) )
        else :
            tlines = tlines [ 1 : ]
            if res [ - 1 ] :
                res . append ( [ ] )
    if not res [ - 1 ] :
        res = res [ : - 1 ]
    return stringize ( res )

def _copy_paste ( tlines , res ) :
    tlines , body , copy_indent = _copy_paste_read_body ( tlines )
    while tlines :
        indent , token = tlines [ 0 ] [ 0 ]
        if indent == copy_indent and token == 'paste' :
            tlines , res = _copy_paste_do_paste ( tlines , body , res )
        else :
            break
    return tlines , res

def _copy_paste_do_paste ( tlines , body , res ) :
    indent , token = tlines [ 0 ] [ 0 ]
    tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
    if not tlines [ 0 ] :
        tlines = tlines [ 1 : ]
    assert token == 'paste'
    tlines , replaces = _copy_paste_read_replaces ( tlines )
    buf = deepcopy ( body )
    for replace_what , replace_with in replaces . items ( ) :
        buf = _copy_paste_do_replace ( buf , replace_what , replace_with )
    res += buf
    return tlines , res

def _copy_paste_do_replace ( body , what , with_what_args ) :
    res = [ [ ] ]
    shift_indent = 0
    while body :
        if body [ 0 ] :
            indent , token = body [ 0 ] [ 0 ]
            body [ 0 ] = body [ 0 ] [ 1 : ]
            indent += shift_indent
            if what in token :
                parts = token . split ( what )
                res_indent , res_token = indent , ''
                for part in parts [ : - 1 ] :
                    res_token += part
                    with_what = deepcopy ( with_what_args )
                    while len ( [ t for tline in with_what for t in tline ] ) > 1 :
                        if with_what [ 0 ] :
                            with_indent , with_token = with_what [ 0 ] [ 0 ]
                            with_what [ 0 ] = with_what [ 0 ] [ 1 : ]
                            res_indent += with_indent
                            res_token += with_token
                            res [ - 1 ] . append ( ( res_indent , res_token ) )
                            res_indent , res_token = indent , ''
                        else :
                            with_what = with_what [ 1 : ]
                            if res [ - 1 ] :
                                res . append ( [ ] )
                    while with_what and not with_what [ 0 ] :
                        with_what = with_what [ 1 : ]
                        if res [ - 1 ] :
                            res . append ( [ ] )
                    with_indent , with_token = with_what [ 0 ] [ 0 ]
                    res_token += with_token
                    res_indent += with_indent
                res_token += parts [ - 1 ]
                res [ - 1 ] . append ( ( res_indent , res_token ) )
                shift_indent = len ( res_token ) - len ( token )
            else :
                res [ - 1 ] . append ( ( indent , token ) )
        else :
            body = body [ 1 : ]
            shift_indent = 0
            if res [ - 1 ] :
                res . append ( [ ] )
    if not res [ - 1 ] :
        res = res [ : - 1 ]
    return res

def _copy_paste_read_replaces ( tlines ) :
    replaces = { }
    first_indent , token = tlines [ 0 ] [ 0 ]
    while tlines :
        indent , token = tlines [ 0 ] [ 0 ]
        if indent == first_indent and token == 'replace' :
            tlines , what = _copy_paste_read_replace_what ( tlines )
            tlines , with_what = _copy_paste_read_replace_with_what ( tlines , first_indent )
            replaces [ '' . join ( stringize ( what ) ) ] = with_what
        else :
            break
    return tlines , replaces

def _copy_paste_read_replace_what ( tlines ) :
    indent , token = tlines [ 0 ] [ 0 ]
    tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
    if not tlines [ 0 ] :
        tlines = tlines [ 1 : ]
    assert token == 'replace'
    first_indent , token = tlines [ 0 ] [ 0 ]
    what = [ [ ] ]
    while tlines :
        if tlines [ 0 ] :
            indent , token = tlines [ 0 ] [ 0 ]
            if token == 'with' or indent < first_indent :
                break
            else :
                what [ - 1 ] . append ( ( indent - first_indent , token ) )
                tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
        else :
            tlines = tlines [ 1 : ]
            what . append ( [ ] )
    if not what [ - 1 ] :
        what = what [ : - 1 ]
    return tlines , what

def _copy_paste_read_replace_with_what ( tlines , replace_indent ) :
    indent , token = tlines [ 0 ] [ 0 ]
    tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
    if not tlines [ 0 ] :
        tlines = tlines [ 1 : ]
    assert token == 'with'
    assert indent > replace_indent
    first_indent , token = tlines [ 0 ] [ 0 ]
    with_what = [ [ ] ]
    while tlines :
        if tlines [ 0 ] :
            indent , token = tlines [ 0 ] [ 0 ]
            if indent >= first_indent :
                with_what [ - 1 ] . append ( ( indent - first_indent , token ) )
                tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
            else :
                break
        else :
            tlines = tlines [ 1 : ]
            with_what . append ( [ ] )
    if not with_what [ - 1 ] :
        with_what = with_what [ : - 1 ]
    return tlines , with_what

def _copy_paste_read_body ( tlines ) :
    copy_indent , token = tlines [ 0 ] [ 0 ]
    tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
    if not tlines [ 0 ] :
        tlines = tlines [ 1 : ]
    assert token == 'copy'
    indent , token = tlines [ 0 ] [ 0 ]
    first_indent = indent
    body = [ [ ] ]
    while tlines :
        if tlines [ 0 ] :
            indent , token = tlines [ 0 ] [ 0 ]
            if indent <= copy_indent :
                break
            tlines [ 0 ] = tlines [ 0 ] [ 1 : ]
            body [ - 1 ] . append ( ( indent - first_indent + copy_indent , token ) )
        else :
            tlines = tlines [ 1 : ]
            body . append ( [ ] )
    if not body [ - 1 ] :
        body = body [ : - 1 ]
    return tlines , body , copy_indent

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
