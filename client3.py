import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
print "program komunikasi tentang data diri"
while pesan.lower() != 'q':
    pesan = raw_input('pertanyaan: ')
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print 'Jawaban:', response
s.close()
          