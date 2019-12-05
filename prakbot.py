import socket

hostname='localhost'
pesan=''

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hostname,50003))
print ('CLIENT BOT IS READY')

while pesan.lower() != 'q':
    pesan = input('Pertanyaan:')
    s.send(pesan)
    if pesan.lower() != 'q':
        response=s.recv(1024)
        print ('Jawaban:',response)
        s.close()
