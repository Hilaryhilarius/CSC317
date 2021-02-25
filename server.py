import socket
import time

hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)

print('hostName: ',hostName)
print('hostIP: ',hostIP)

server_ip = '10.200.3.221'
server_port = 50001
# exercise : how to find if the port is in use:
        # 1. using command line in linux
        # 2. using pthon program

server_addr = (server_ip, server_port)

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_addr)
server_socket.listen(5)

conn, address = server_socket.accept()

message = conn.recv(1024).decode('utf-8')

#split the received request into its components
message.splitlines()
reqLine = message[0]
reqLine.split()
method = reqLine[0]
url = reqLine[1]
version = reqLine[2]

#check if url exists and opens file if it does
try:
        openfile = open(pdf)
        openfile.close()
except IOError:
        print("File not found or not accessible")

print(message)
conn.close()
time.sleep(50)

server_socket.close()


