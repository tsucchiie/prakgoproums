import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50006))
s.listen(5)
print ("Serveer pejawab otomatis sudah siap")
data = ''
kamus = {
    'nama' : 'Ghalel Gutur W',
    'nim' : 'L200190093',
    'angkatan' : '2019'
    }

while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print ("Pertanyaan:", data)
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('pertanyaan tidak relevan')
