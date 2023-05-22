import socket, ssl
from threading import Thread
from request import Request

class Server:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.handler_func = Server.handler
        self.running = False

    def run_listener(self):
        self.running = True
        thread = Thread(target = self.run_handler)
        thread.start()
        thread.join()
    
    def run_handler(self):
        while self.running:
            connection, address = self.sock.accept()
            Thread(target = self.handle, args = [connection, address]).start()

    def stop_listener(self):
        self.running = False
    
    def handle(self, connection, address):
        try:
            request = None
            while not request:
                request = connection.recv(1024).decode()
            self.handler_func(connection, address, Request(request))
        except UnicodeDecodeError:
            pass
        except Exception as e:
            print(e)
        finally:
            connection.close()
    
    def set_handler_func(self, handler_func):
        self.handler_func = handler_func
        return self
    
    @staticmethod
    def handler(connection, address, request):
        response = "<p>Test</p>"
        connection.sendall(response.encode())
