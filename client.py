#nama berkas: p_tcpcli.py
#client TCP untuk server p-tcpser.py
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
while pesan.lower() != 'q':
    pesan = raw_input('Kirim: ')
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print 'Diterima:', response
s.close()
