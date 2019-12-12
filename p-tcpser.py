#nama berkas: p_tcpser.py
#TCP serevr untuk client p_tcpcli.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
primt 'TCP server sudah siap"
data = ''
