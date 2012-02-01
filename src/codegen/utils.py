class exception ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )

def merge ( * args ) :
    return args [ 0 ]
