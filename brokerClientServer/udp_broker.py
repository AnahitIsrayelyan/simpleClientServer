import socket

def main():
    print("Configuring local address...")
    broker_address = ('', 8082)

    print("Creating socket...")
    socket_broker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Binding socket to local address...")
    socket_broker.bind(broker_address)

    print("Waiting for connections...")
    while True:
        data, client_address = socket_broker.recvfrom(1024)   # maximum number of bytes to be received in a single call 
        if not data:
            break

        # Split the request to get the conversion and text parts.
        request_parts = data.decode('utf-8').strip().split(':')
        if len(request_parts) != 2:
            print("Invalid request received.")
            continue

        convert_to, text_to_convert = request_parts

        # Determine which server to forward the message to based on the client request.
        if convert_to == 'toupper':
            server_address = ('localhost', 8080)  # Redirect to the toupper server
        elif convert_to == 'tolower':
            server_address = ('localhost', 8081)  # Redirect to the tolower server
        else:
            print("Invalid request received.")
            continue 

        # Forward the message to the appropriate server and receive the response.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(text_to_convert.encode('utf-8'), server_address)
        response, _ = client_socket.recvfrom(1024)   # received data, address of the sender (source address)
        client_socket.close()

        # Send the response back to the client.
        socket_broker.sendto(response, client_address)

if __name__ == '__main__':
    main()
