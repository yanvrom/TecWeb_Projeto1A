import socket
from pathlib import Path
from utils import extract_route, read_file, build_response, load_template
from views import index, edit
from database import Database

db = Database('notes')


CUR_DIR = Path(__file__).parent
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    print(f"A rota é {route}")

    filepath = CUR_DIR / route
    if filepath.is_file():
        response = build_response() + read_file(filepath)
    elif route == '':
        response = index(request)
    elif route.startswith("delete"):
        id = route.split("/")[1]
        db.delete(id)
        response = build_response(code=303, reason='See Other', headers='Location: /')
    elif route.startswith("edit") and route.split("/")[1].isnumeric():
        id = route.split("/")[1]
        response = edit(request, id)
    else:
        response = build_response(code=404, body= load_template("404.html"))
        
    client_connection.sendall(response)

    client_connection.close()

server_socket.close()