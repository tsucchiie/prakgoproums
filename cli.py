
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 50003               # Reserve a port for your service.

s.connect((host, port))

pull=''
while pull != "end":
    send=input('masukkan input:')
    s.send(pull)
    resp=s.recv(1024)
    print response
    
s.close                     # Close the socket when done
