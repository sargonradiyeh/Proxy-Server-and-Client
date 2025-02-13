# Proxy Server and Client

## Overview
This project implements a simple proxy server that forwards HTTP requests from a client to a destination web server. The proxy server captures and processes requests, forwards them, receives responses, and relays them back to the client while logging the exact time of transactions.

## Features
- **Proxy Server (`server.py`)**
  - Listens for incoming client connections on port `8080`
  - Receives HTTP requests from clients
  - Extracts and forwards the request to the destination web server (port `80` for HTTP)
  - Captures and relays the response back to the client
  - Logs connection details and exact timestamps

- **Client (`client.py`)**
  - Prompts the user to enter a website's IP address
  - Sends an HTTP request to the proxy server
  - Captures and displays the response from the proxy
  - Measures and prints the round-trip time
  - Retrieves and displays the client's physical MAC address

## Installation and Setup
### Prerequisites
- Python 3.x
- A network connection
- Administrative privileges (if required to bind to port `8080`)

### Running the Proxy Server
1. Open a terminal and navigate to the directory containing `server.py`.
2. Run the following command:
   ```sh
   python server.py
   ```
3. The server will start listening on port `8080`.

### Running the Client
1. Open another terminal and navigate to the directory containing `client.py`.
2. Run the following command:
   ```sh
   python client.py
   ```
3. When prompted, enter the IP address of a website you want to request.
4. The client will send the request via the proxy server and display the response.

## Code Structure
### `server.py` (Proxy Server)
- Sets up a socket server on `8080`
- Accepts client connections
- Extracts the destination server's IP from the client request
- Forwards the request to the destination server and retrieves the response
- Sends the response back to the client
- Logs connection details and exact timestamps

### `client.py` (Client Application)
- Retrieves the system's hostname and IP address
- Captures the physical MAC address
- Accepts a website IP from user input
- Sends an HTTP request to the proxy server
- Measures round-trip time for the request-response cycle
- Displays the response and MAC address

## Example Output
### Client Side
```
Enter the website's IP: 93.184.216.34
Request has been sent: GET / HTTP/1.1\r\nHost: 93.184.216.34\r\n\r\n  [12:34:56]
Response has been received: HTTP/1.1 200 OK ...
Round-trip time: 0.234 seconds
Physical MAC Address: aa:bb:cc:dd:ee:ff
```

### Server Side
```
Connection has been accepted from: ('192.168.1.2', 54321)
Request has been received: GET / HTTP/1.1\r\nHost: 93.184.216.34\r\n\r\n  [12:34:56]
Destination IP address: 93.184.216.34
Response received: HTTP/1.1 200 OK ... [12:34:57]
Connection has been closed.
```

## Limitations
- This proxy only works with HTTP (port `80`) and does not support HTTPS.
- The client must manually enter the destination server's IP address.
- The server only handles one client at a time (configured with `listen(1)`).
- The proxy does not cache responses or optimize network traffic.

## Possible Future Enhancements
- Implement support for HTTPS forwarding
- Enable multi-client handling using threading
- Add logging to store request and response history
- Implement a caching mechanism to reduce redundant requests



