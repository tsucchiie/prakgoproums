import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50006))
print ("Program komunikasi dengan data diri")
while pesan.lower() != 'q':
    pesan = input('Pertanyaan: ')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print ('Jawaban: ', response)
    else:
        print ('Siap!!!')
        break
s.close()
