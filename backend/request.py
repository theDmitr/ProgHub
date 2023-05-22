class Request: 
    def __init__(self, http_request_str):
        headers = http_request_str.split("\r\n\r\n")[0]
        body = http_request_str.split("\r\n\r\n")[1]
        self.headers = {line[:line.index(":")]: line[line.index(":") + 2:] for line in headers.split("\r\n")[1:]}
        self.method, self.path, self.version = headers.split("\r\n")[0].split()
        self.path = self.path[1:]
        self.accept = Request.parse_accept(self.path, self.headers["Accept"])
    
    def parse_accept(path, accept):
        acc = ""
        type = path.split(".")[-1]
        if "html" in accept or type == "html" or path.find(".") == -1: acc = "html"
        elif "css" in accept or type == "css": acc = "css"
        elif "js" in accept or type == "js": acc = "js"
        elif "image" in accept: acc = "image"
        else: acc = accept
        return acc
