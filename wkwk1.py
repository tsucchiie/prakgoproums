import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50007))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
kamus = {'nama': 'naufalputrap',
         'nim': 'L200190027',
         'angkatan': '19',
         'keluar': 'siap',}
while data.lower() != 'q' :
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'pertanyaan:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('pertanyaan anda tidak relevan')
