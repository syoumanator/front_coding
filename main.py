from http.server import BaseHTTPRequestHandler, HTTPServer
from config import Path_html

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс обработки запросов"""


    def do_GET(self):
        """ Метод для обработки GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(Path_html, encoding="utf-8") as file:
            content = file.read()
        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        """ Метод для обработки POST-запросов"""
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data)
        response = f"Received POST data: {post_data.decode('utf-8')}"
        print(response)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
