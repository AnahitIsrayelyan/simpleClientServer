import socket

def main():
    print("Configuring local address...")
    server_address = ('', 8080)

    print("Creating socket...")
    socket_listen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Binding socket to local address...")
    socket_listen.bind(server_address)

    print("Waiting for connections...")
    while True:
        data, client_address = socket_listen.recvfrom(1024)
        if not data:
            break
 
        print(f"Connection established with {client_address[0]}:{client_address[1]}")

        data = data.decode('utf-8').upper().encode('utf-8')
        socket_listen.sendto(data, client_address)

if __name__ == '__main__':
    main()
