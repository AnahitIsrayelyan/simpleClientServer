import socket
import sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

def send_get_request(filename, connection):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Create a GET request
    request = f"GET {filename} HTTP/1.0\r\nHost: {SERVER_HOST}\r\nConnection: {connection}\r\n\r\n"

    # Send the GET request to the server
    client_socket.sendall(request.encode())

    # Receive and print the response from the server
    response = client_socket.recv(4096).decode()
    print(response)

    client_socket.close()

if __name__ == "__main__":
    while True:
        # Get the filename (link) from the command-line argument
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        else:
            filename = input("Enter the link (e.g., /index.html): ")
        again = input("Do you want to run the program again? (y/n): ").lower()

        # Send the GET request

        if again == 'y' or again == 'yes':
            send_get_request(filename, 'Keep-Alive')
            continue
        else:
            send_get_request(filename, 'Close')
            break


