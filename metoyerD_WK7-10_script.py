#!/usr/bin/env python3
"""
Simple TCP MD5 Server
----------------------
This script acts as a standalone TCP server that listens on port 5555.
For each client connection, it:
  1. Receives a message (up to 4096 bytes).
  2. Computes the MD5 hash of the message.
  3. Sends the MD5 digest (hexadecimal string) back to the client.
The server continues running until terminated by the user.
"""

import socket
import hashlib

def main():
    # Create a TCP socket using IPv4
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to all available interfaces on port 5555
    server_socket.bind(("0.0.0.0", 5555))
    
    # Start listening; allow up to 5 queued connections
    server_socket.listen(5)
    print("Listening on 0.0.0.0:5555...")
    
    # Main server loop
    while True:
        # Accept an incoming connection from a client
        client_socket, client_addr = server_socket.accept()
        print("Accepted connection from {}:{}".format(client_addr[0], client_addr[1]))
        
        # Receive data from the client (up to 4096 bytes)
        data = client_socket.recv(4096)
        if data:
            # Compute the MD5 hash of the received data
            md5_digest = hashlib.md5(data).hexdigest()
            print("Received message: {}".format(data.decode(errors='replace')))
            print("Computed MD5 digest: {}".format(md5_digest))
            
            # Send the MD5 digest back to the client as a byte string
            client_socket.send(md5_digest.encode())
        else:
            print("No data received from {}:{}".format(client_addr[0], client_addr[1]))
        
        # Close the client connection
        client_socket.close()
        print("Closed connection from {}:{}".format(client_addr[0], client_addr[1]))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer terminated by user.")
