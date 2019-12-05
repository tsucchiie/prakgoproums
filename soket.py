#socket
import socket               # Import socket module

host = socket.gethostname() # Get local machine name
port = 50003               # Reserve a port for your service.

s = socket.socket()         # Create a socket object
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

data={
    'nama':'Arindra Hning',
    'nim':'L200190065',
    'angkatan':'2019',
    'alamat':'Solo'
   }

while True:
   c, addr = s.accept()     # Establish connection with client.

   ask=c.recv(1024)
   print ('Got connection from', addr)
   
   if ask in data:
      c.send(data[ask])
   else:
      break
   c.close()                # Close the connection
