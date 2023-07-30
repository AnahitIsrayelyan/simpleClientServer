# simpleClientServerPrograms

#brokerClientServer

Architecture: Broker Pattern

The provided code implements a simple broker pattern for communication between multiple clients and servers. In this architecture, a central "broker" server acts as an intermediary that receives requests from clients, forwards them to appropriate servers, and then relays the responses back to the clients. The clients do not directly communicate with the servers; instead, they send their requests to the broker, which handles the routing and distribution of messages.

Components:

    Client (udp_client.py):
        The client program is responsible for sending requests to the broker and receiving the responses.
        It takes two arguments from the command line: broker_hostname and broker_port, indicating the address of the broker server to connect to.
        The client can send requests to convert text to lowercase or uppercase using the format tolower:text or toupper:text.
        It communicates with the broker using UDP sockets.

    Server 1 (udp_tolower.py):

        This server listens for incoming UDP requests on port 8081.
        When it receives a request, it converts the text to lowercase and sends the response back to the broker.

    Server 2 (udp_toupper.py):

        This server listens for incoming UDP requests on port 8080.
        When it receives a request, it converts the text to uppercase and sends the response back to the broker.

    Broker (udp_broker.py):

        The broker server listens for incoming UDP requests on port 8082.
        It receives requests from the client and extracts the conversion type and text to be converted.
        Based on the conversion type, it determines the appropriate server (Server 1 or Server 2) to forward the request.
        It communicates with both Server 1 and Server 2 using separate UDP sockets.
        The broker receives the response from the chosen server and sends it back to the client.

Usage:

    Run the broker server: python broker.py
    Run Server 1: python udp_toupper.py
    Run Server 2: python udp_tolower.py
    Run the client, providing the broker's hostname and port as arguments: python udp_client.py localhost 8082

Note:

    Ensure that all components (broker, server1, server2) and the client are running on the same machine for simplicity.
    The provided code does not handle error cases extensively. In a production environment, additional error handling and input validations
    should be implemented.


#webClientServer

This is a basic implementation of a web client-server program in Python. The program supports a simple HTTP-based protocol, where the client can request a file from the server using a GET request, and the server responds with the file content if it exists. The client can choose to keep the connection alive for multiple requests or close it after each request.
Client

Components:

    The client sends GET requests to the server, specifying the filename (link) as input. It then receives and prints the server's response. The
    client can repeatedly send requests and has the option to continue running the program or close the connection.
    Server

    The server listens on a specific IP address and port number, awaiting incoming client connections. Upon receiving a request, it parses the 
    HTTP headers to extract the requested filename. If the client requests to close the connection, the server terminates gracefully. Otherwise, 
    it attempts to retrieve the content of the requested file (if exists) and sends it back to the client as the HTTP response.

Note:

    Please note that this implementation is minimalistic and serves as an educational example. In a real-world scenario, you would need to 
    handle various edge cases, implement error handling, and possibly consider using a more robust web server framework for production use.
Usage:

    To run the program, start the server first and then run the client. The server serves files from the "public" directory, and the client can 
    request files by providing the filename (e.g., /index.html). You can also connect from real web browser typing 'http://127.0.0.1:8080/index.html'.


