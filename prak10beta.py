import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('',50003))
s.listen(5)

print '[!] SERVER IS READY[!]'

data='' #var
usrdat={
    'nama':'Arindra Hning',
    'nim':'L200190065',
    'angkatan':'2019',
    'alamat':'Solo'
    }

while data.lower() != 'q':
    komm,addr=s.accept()
    
    while data.lower() != 'q':
        data=komm.recv(1024)
        
        if data.lower() == 'q':
            s.close()
            break
        
        print 'pernyataan',data

        if usrdat.has_key(data):
            komm.send(usrdat[data])
        else:
            komm.send('there is no',data)

##while True:
##    addr=s.accept()
##    data=addr.recv(1024)
##    print 'pernyataan',data
##    if data in usrdat:
##        addr.send(usrdat[data])
##    else:
##        addr.send('there is no',data)

