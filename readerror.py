
file = open( 'nonsuch.txt' , 'r' )
data = file.read()
file.close()
print( data )