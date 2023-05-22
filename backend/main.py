from server import Server
from request import Request

def get_file_string(link) -> str:
    buffer = ""
    try:
        with open(link, "r", encoding="utf-8") as f:
            buffer += "".join(f.readlines())
    except:
        pass
    return buffer

def get_file_bytes(link) -> bytes:
    return open(link, "rb").read()

def handler_func(connection, address, request):
    request.path = request.path.replace("-", "/")

    if request.method == "GET":
        if request.path == "":
            base = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
            connection.sendall((base + get_file_string("../frontend/index.html")).encode())
        
        elif request.accept == "html":
            base = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
            connection.sendall((base + get_file_string("../frontend/templates/" + request.path + ".html")).encode())
        
        elif request.accept == "css":
            base = "HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=UTF-8\r\n\r\n"
            connection.sendall((base + get_file_string("../frontend/" + request.path)).encode())
        
        elif request.accept == "js":
            base = "HTTP/1.1 200 OK\r\nContent-Type: text/js; charset=UTF-8\r\n\r\n"
            connection.sendall((base + get_file_string("../frontend/" + request.path)).encode())
        
        elif request.accept == "image":
            img_bytes = get_file_bytes("../frontend/" + request.path)
            base = f"HTTP/1.1 200 OK\r\nContent-Type: image/*\r\nContent-Length: {str(len(img_bytes)).encode()}\r\n\r\n"
            connection.sendall(base.encode() + img_bytes)

server = Server("", 80).set_handler_func(handler_func)
server.run_listener()