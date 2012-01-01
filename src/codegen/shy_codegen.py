from hashlib import md5
from os . path import dirname

def tokenize ( lines ) :
    res = [ ]
    for line in lines :
        for word in line . split ( ' ' ) :
            if len ( word ) > 0 :
                res . append ( ( line . find ( word ) , word ) )
    return res

def stringize ( tokens ) :
    res = [ ]
    for indent , token in tokens :
        if len ( res ) == 0 or indent < len ( res [ - 1 ] ) :
            res . append ( '' )
        res [ - 1 ] += ' ' * ( indent - len ( res [ - 1 ] ) )
        res [ - 1 ] += token
    return res

def preprocess ( lines ) :
    res = [ ]
    tokens = tokenize ( lines )
    while len ( tokens ) > 0 :
        indent , token = tokens [ 0 ]
        if token == 'copy' :
            tokens , r = _copy_paste ( tokens )
            res += r
        else :
            tokens = tokens [ 1 : ]
            res += [ ( indent , token ) ]
    return stringize ( res )

def _copy_paste ( tokens ) :
    tokens , body , copy_indent = _copy_paste_read_body ( tokens )
    res = [ ]
    while len ( tokens ) > 0 :
        indent , token = tokens [ 0 ]
        if indent == copy_indent and token == 'paste' :
            tokens , paste = _copy_paste_do_paste ( tokens , body , copy_indent )
            res += paste
        else :
            break
    return tokens , res

def _copy_paste_do_paste ( tokens , body , copy_indent ) :
    indent , token = tokens [ 0 ]
    tokens = tokens [ 1 : ]
    assert token == 'paste'
    tokens , replaces = _copy_paste_read_replaces ( tokens )
    res = [ ]
    for indent , token in body :
        for replace_what , replace_with in replaces . items ( ) :
            if replace_what in token :
                token = token . replace (
                    replace_what , '' . join ( stringize ( replace_with ) ) )
        res . append ( ( indent , token ) )
    return tokens , res

def _copy_paste_read_replaces ( tokens ) :
    replaces = { }
    first_indent , token = tokens [ 0 ]
    while len ( tokens ) > 0 :
        indent , token = tokens [ 0 ]
        if indent == first_indent and token == 'replace' :
            tokens , what = _copy_paste_read_replace_what ( tokens )
            tokens , with_what = _copy_paste_read_replace_with_what ( tokens , first_indent )
            replaces [ '' . join ( stringize ( what ) ) ] = with_what
        else :
            break
    return tokens , replaces

def _copy_paste_read_replace_what ( tokens ) :
    indent , token = tokens [ 0 ]
    tokens = tokens [ 1 : ]
    assert token == 'replace'
    first_indent , token = tokens [ 0 ]
    what = [ ]
    while len ( tokens ) > 0 :
        indent , token = tokens [ 0 ]
        if token == 'with' or indent < first_indent :
            break
        else :
            what . append ( ( indent - first_indent , token ) )
            tokens = tokens [ 1 : ]
    return tokens , what

def _copy_paste_read_replace_with_what ( tokens , replace_indent ) :
    indent , token = tokens [ 0 ]
    tokens = tokens [ 1 : ]
    assert token == 'with'
    assert indent > replace_indent
    first_indent , token = tokens [ 0 ]
    with_what = [ ]
    while len ( tokens ) > 0 :
        indent , token = tokens [ 0 ]
        if indent >= first_indent :
            with_what . append ( ( indent - first_indent , token ) )
            tokens = tokens [ 1 : ]
        else :
            break
    return tokens , with_what

def _copy_paste_read_body ( tokens ) :
    indent , token = tokens [ 0 ]
    tokens = tokens [ 1 : ]
    assert token == 'copy'
    first_indent = indent
    body = [ ]
    while len ( tokens ) > 0 :
        indent , token = tokens [ 0 ]
        if indent <= first_indent :
            break
        tokens = tokens [ 1 : ]
        body . append ( ( indent - first_indent - len ( 'copy' ) - 1 , token ) )
    return tokens , body , first_indent

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
        
    reify ( generate ( stdin . readlines ( ) ) , open , trace ( ) , options ( ) , os )
