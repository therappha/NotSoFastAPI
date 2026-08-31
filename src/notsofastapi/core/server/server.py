"""Server init file"""

import socket
from notsofastapi import settings
from notsofastapi.http import HttpParser


def run_server():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((settings.IP_ADDRESS, settings.PORT))
    mysocket.listen(1)
    print(f"Started Server at: {settings.IP_ADDRESS}:{settings.PORT}")

    while True:
        client_socket, client_address = mysocket.accept()
        request = client_socket.recv(65535)
        parsed_request = HttpParser.parse_request(request)
        if not parsed_request:
            client_socket.close()
            continue

        if request == b"":
            client_socket.close()
            print("connection closed")
        client_socket.send(
            "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello World!".encode("utf-8")
        )
