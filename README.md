Client-server Chat Application

This project is a simple multi-client chat application developed using Python and TCP socket programming.

Features-

Multiple clients can connect to the server simultaneously

Each user joins the chat with a username

Messages are broadcast to all connected users

Join and leave notifications

Command to display connected users- "users"

Client can exit using "quit"

Message timestamps

Server message logging in chat.log

Technologies Used

Python 

Socket Programming (TCP)

Multithreading

How to Run the Project

Step 1: Start the Server

Open a terminal and run:

python server.py

You should see:

Server started on 127.0.0.1:5000

Step 2: Start the Client

Open another terminal and run:

python client.py

Enter a username when prompted.

Step 3: Start Multiple Clients

Run the client program in multiple terminals to simulate multiple users chatting with each other.

Available Commands

Normal text

Sends a chat message to all connected users.

users

Displays a list of currently connected users.

quit

Leaves the chat and disconnects from the server.

You can see the server logs in the chat.log file. This file is created automatically when the server runs.

example of client- 

Enter username: Deepali tomar

hello

[20:58:24] Tanu tomar joined the chat. Type users to see who is online or quit to leave

[20:58:27] Tanu tomar: Hii

[20:58:54] Vansh tomar joined the chat. Type users to see who is online or quit to leave

[20:58:58] Vansh tomar: Helloooo

[21:00:54] Tanu tomar has left the chat

[21:01:06] Vansh tomar has left the chat

quit
