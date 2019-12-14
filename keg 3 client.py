import socket
hostname='localhost'
pesan =''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50009))
print 'menghitung luas persegi panjang'
while pesan.lower() !='keluar':
    pesan = raw_input('pesan:')
    s.send(pesan)
    if pesan.lower()=='keluar':
        response = s.recv(1024)
        print 'response:-'
        s.close()
        break
    elif pesan.lower() != 'keluar':
        response = s.recv(1024)
        print "response:",response
s.close()
