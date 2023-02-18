import socket
import time
from datetime import datetime

hname = socket.gethostname()
IPf = socket.gethostbyname(hname)
# Setting up the Proxy server
prox_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prox_server.bind((IPf, 8080)) #8080 usually used for proxies and HTTP and TCP protocols 
prox_server.listen(1) #Listening for 1 Client

while True:
    # Accepting incoming connections
    client_socket, client_address = prox_server.accept()
    print("Connection has been accepted from:", client_address)
    try:
        # Receiving Client request
        request = client_socket.recv(4096).decode()
        if not request:
            raise ValueError("Request received was empty")
        #Code taken from https://www.freecodecamp.org/news/python-get-current-time
        print("Request has been received:", request," [",datetime.now().strftime("%H:%M:%S"),"] ") #Assignment asks to output "Exact" time which I'm assuming is this

        # Getting the Destination server's IP address
        req_parts = request.split()
        dest_address = req_parts[4] #Splitting the request in order to just get the IP part
        print("Destination IP address:", dest_address)

        # Forwarding the request to the Destination server
        dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest_socket.connect((dest_address, 80))#Port 80 used for HTTP protocols
        dest_socket.sendall(request.encode())

        # Receiving the response from the Destination server
        response = dest_socket.recv(4096)
        print("Response received:", response," [", datetime.now().strftime("%H:%M:%S"),"] ") #Assignment asks to output "Exact" time which I'm assuming is this

        # Sending the response back to the Client
        client_socket.sendall(response)

    except Exception as error:
        print("Error:", error)

    finally:
        # Closing the sockets
        client_socket.close()
        dest_socket.close()
        print("Connection has been closed.")

