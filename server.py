import socket

hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)

print('hostName: ',hostName)
print('hostIP: ',hostIP)

server_ip = '192.168.1.9'
server_port = 50510
# exercise : how to find if the port is in use:
        # 1. using command line in linux
        # 2. using pthon program

server_addr = (server_ip, server_port)

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_addr)
server_socket.listen(5)
conn, address = server_socket.accept()
message = conn.recv(1024).decode('utf-8')
print(message)
conn.close()

server_socket.close()
