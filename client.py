import socket
import time
from datetime import datetime
import uuid

#Code taken from https://pythontic.com/modules/socket/gethostname
hname = socket.gethostname()
IPf = socket.gethostbyname(hname)
# Getting Physical MAC address
#Code taken from https://www.codespeedy.com/how-to-get-mac-address-of-a-device-in-python/
mac_address_dum = uuid.getnode()
mac_address = ':'.join(['{:02x}'.format((mac_address_dum >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])

# Setting up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Taking website IP as input
web_ip = input("Enter the website's IP: ")

# Sending the request to the proxy server
request = "GET / HTTP/1.1\r\nHost: "+web_ip+"\r\n\r\n" #Imitating syntax on Network Programming Lecture 6 PPT
stime = time.time()
client_socket.connect((IPf, 8080))
client_socket.sendall(request.encode())
print("Request has been sent:", request," [",datetime.now().strftime("%H:%M:%S"),"] ")#Assignment asks to output "Exact" time which I'm assuming is this

# Receiving the response from the proxy server
response = client_socket.recv(4096)
etime = time.time()
print("Response has been received:", response.decode())
print("Round-trip time: ", round((etime - stime),3) ,"seconds")
print("Physical MAC Address:", mac_address)

# Closing the socket
client_socket.close()

