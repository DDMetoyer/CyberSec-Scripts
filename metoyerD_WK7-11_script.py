#!/usr/bin/env python3
"""
Simple TCP Client for MD5 Hash Server
--------------------------------------
This client connects to the TCP server on port 5555, sends a message,
receives an MD5 digest as a response, and prints the digest.
"""

import socket

def main():
    # Server configuration: use localhost and port 5555
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 5555

    # Create a TCP socket (IPv4)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the MD5 server
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")

        # Define the message to send
        message = "Hello, server! This is a test message."
        client_socket.sendall(message.encode())
        print("Sent message:", message)

        # Receive the MD5 digest response (up to 1024 bytes)
        response = client_socket.recv(1024)
        if response:
            print("Received MD5 digest:", response.decode())
        else:
            print("No response received.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
