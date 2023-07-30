import socket
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python udp_client.py broker_hostname broker_port")
        return 

    broker_hostname = sys.argv[1]
    broker_port = int(sys.argv[2])

    print("Configuring broker address...")
    broker_address = (broker_hostname, broker_port)

    print(f"Creating socket...")
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Connected.")
    print("To send data, enter 'tolower:text' or 'toupper:text' (type 'exit' to quit).")

    while True:
        request = input("Enter request: ").strip().lower()
        if request == 'exit':
            break

        # Split the request to get the conversion and text parts.
        try:
            convert_to, text_to_convert = request.split(':', 1)
        except ValueError:
            print("Invalid request format. Use 'tolower:text' or 'toupper:text'")
            continue

        if convert_to not in ['tolower', 'toupper']:
            print("Invalid request format. Use 'tolower:text' or 'toupper:text'")
            continue

        # Send the request to the broker.
        request_msg = f"{convert_to}:{text_to_convert}"
        socket_client.sendto(request_msg.encode('utf-8'), broker_address)

        # Receive and display the response from the broker.
        data, _ = socket_client.recvfrom(4096)
        print(f"Converted text: {data.decode('utf-8')}")

    print("Closing socket...")
    socket_client.close()

if __name__ == '__main__':
    main()
