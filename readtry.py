try :
	file = open( 'nonsuch.txt' , 'r' )
	data = file.read()
	file.close()
	print( data )

except ( FileNotFoundError ) :
	print( 'The Program Cannot Find A File'  )