import socket
import time

# 1. create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect to remote server
client_socket.connect(('192.168.1.9',50510))

# 3. Ask user to enter a message
message = input('Enter a message you want to send:')

# 4. send that message to the server
client_socket.send(message.encode('utf-8'))
time.sleep(2)
# 5. Close the socket
client_socket.close()
