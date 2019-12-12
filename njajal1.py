#nama berkas: p_tcpser.py
#TCP serevr untuk client p_tcpcli.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print 'TCP server sudah siap'
data = ''

while True:
    komm, addr = s.accept()
    while data != 'Q' and data != 'q':
        data = komm.recv(1024)
        print 'Diterima:', data
        komm.send(data.upper()) #data dikirim balik
        s.close()
        if data == 'Q' or data == 'q':
            break
