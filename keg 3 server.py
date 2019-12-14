import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50009))
s.listen(5)
print "server siap"
perintah = ''
p = 0
l = 0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item[0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan:",perintah
        if len(item) == 2:
            if perintah == 'panjang':
                p = int(item[1])
                komm.send('panjang disimpan')
            elif perintah == 'lebar':
                l = int(item[1])
                komm.send('lebar disimpan')
            else:
                komm.send('pesan tidak diterima')
        elif perintah == 'hitung':
            L = float(p*l)
            response ='luas persegi panjang dengan panjang{} lebar{} adalah{}'.format(p,l,L)
            komm.send(response)
        else:
            komm.send('pesan tidak diketahui')
            
