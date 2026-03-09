import socket
import threading

HOST = "127.0.0.1"
PORT = 5000
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            break

def send_messages(client_socket):
    while True:
        message = input()
        if message == "quit":
            client_socket.sendall("QUIT".encode())
            client_socket.close()
            break
        elif message == "users":
            client_socket.sendall("USERS".encode())
        else:
            client_socket.sendall(f"MSG {message}".encode())

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    username = input("Enter username: ")
    client.sendall(f"JOIN {username}".encode())
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()
    send_messages(client)

if __name__ == "__main__":
    start_client()
