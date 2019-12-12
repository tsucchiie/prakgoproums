import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
kamus = {'nama': 'Apalah artinya sebuah nama',
         'umur': 'Saya lebih muda dari anda',
         'alamat': 'Sebuah tempat yang nyaman di tepi bukit',
         'motto': 'Malu bertanya sesat di jalan',
         'kuliah': 'program studi informatika UMS'}
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
