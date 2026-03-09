import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

clients = []
usernames = {}
def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def log_message(message):
    print(message)
    with open("chat.log", "a") as f:
        f.write(message + "\n")
def broadcast(message, sender_socket=None):
    timestamped_message = f"[{get_timestamp()}] {message}"
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(timestamped_message.encode())
            except:
                remove_client(client)
    log_message(timestamped_message)

def remove_client(client):
    if client in clients:
        username = usernames.get(client, "Unknown")
        clients.remove(client)
        del usernames[client]
        leave_message = f"{username} has left the chat"
        log_message(f"[{get_timestamp()}] {username} left")
        broadcast(leave_message)
        client.close()
def handle_client(client_socket, address):
    log_message(f"[{get_timestamp()}] Connection from {address}")
    try:
        join_message = client_socket.recv(1024).decode()
        if join_message.startswith("JOIN"):
            username = join_message.split(" ", 1)[1].strip()
            usernames[client_socket] = username
            clients.append(client_socket)
            join_text = f"{username} joined the chat. Type /users to see who is online or /quit to leave"
            broadcast(join_text, client_socket)
        while True:
            message = client_socket.recv(1024).decode()

            if not message:
                break
            if message.startswith("MSG"):
                text = message.split(" ", 1)[1]
                username = usernames.get(client_socket, "User")
                broadcast(f"{username}: {text}", client_socket)
            elif message.startswith("USERS"):
                user_list = ", ".join(usernames.values())
                client_socket.sendall(f"[{get_timestamp()}] Connected users: {user_list}".encode())
            elif message.startswith("QUIT"):
                break
    except Exception as e:
        log_message(f"[{get_timestamp()}] Error: {e}")
    remove_client(client_socket)
    log_message(f"[{get_timestamp()}] Disconnected: {address}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    log_message(f"[{get_timestamp()}] Server started on {HOST}:{PORT}")
    while True:
        client_socket, address = server.accept()
        log_message(f"[{get_timestamp()}] Accepted connection from {address}")
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()
if __name__ == "__main__":
    start_server()