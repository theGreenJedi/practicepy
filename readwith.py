filename = input( 'Enter File Name:' )

try :
  with open( filename , 'r' ) as file :
  data = file.read()
  print( 'File' , filename , 'Closed:' , file.closed )
  print( data )

except ( FileNotFoundError ) :
  print( 'The Program Cannot Find File', filename  )

	