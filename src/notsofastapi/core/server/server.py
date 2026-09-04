"""Server init file"""

import socket
from notsofastapi import settings
from notsofastapi.http import HttpParser, HttpResponse
from notsofastapi.views.views import MyView


def run_server():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        response = MyView()._process_request(parsed_request)
        print(f"{parsed_request.decoded_request[0]} {response.status}")
        client_socket.send(response.encode_response())
