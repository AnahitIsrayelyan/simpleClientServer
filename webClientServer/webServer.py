import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

def handle_client(client_connection):
    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split('\r\n')
    filename = headers[0].split()[1]

    # Check if the client wants to close the connection
    if "Connection: Close" in headers:
        print("Close request received. Server is closing...")
        client_connection.close()
        return 'Close'

    # Get the content of the file
    if filename == '/':
        filename = '/index.html'
    if filename[0] != '/':
            filename = '/' + filename
    try:
        fin = open('public' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    # Send HTTP response
    client_connection.sendall(response.encode())
    client_connection.close()
    return 'Keep-Alive'

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)
    print("You can also connect from real web browser typing 'http://127.0.0.1:8080/index.html'.")

    while True:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()
        if handle_client(client_connection) == 'Close':
            break

    # Close socket after breaking the loop
    server_socket.close()
