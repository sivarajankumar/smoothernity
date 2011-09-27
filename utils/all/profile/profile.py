import frames

ops_frame = { }
index = 0
for frame in frames . frames :
    index += 1
    values = 0
    for name , value in frame . items ( ) :
        values += value
    if values not in ops_frame :
        ops_frame [ values ] = [ ]
    ops_frame [ values ] . append ( index )

print "operations" , "frames"
for values , indices in reversed ( sorted ( ops_frame . items ( ) ) ) :
    print "% 8i % 4i %s" % ( values , len ( indices ) , indices [ : 10 ] )
