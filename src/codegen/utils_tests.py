import unittest
import utils

class merge_test_case ( unittest . TestCase ) :
    def test_empty ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { } ) , { } )
        ae ( m ( { } , { } ) , { } )
        ae ( m ( { } , { } , { } ) , { } )
        ae ( m ( [ ] , [ ] , [ ] ) , [ ] )

if __name__ == '__main__' :
    unittest . main ( )
