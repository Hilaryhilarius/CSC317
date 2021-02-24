import socket
import time

hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)




# 1. create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect to remote server
client_socket.connect(('10.200.3.221', 50001))

# 3. Have client create HTTP request
method = input('Method: ')
url = input('URL: ')
version = input('Version: ')
host = input('Host: ')
connection = input('Connection: ')

entity_body = input('Entity body: ')

req = str(method)+' '+str(url)+' '+str(version)+'\n'+"Host: "+host+'\n'+"Connection: "+connection+'\n\n'+entity_body



# 4. send that message to the server
client_socket.send((hostName + ": " +'\n'+req).encode('utf-8'))
time.sleep(2)

# 5. Close the socket
client_socket.close()
