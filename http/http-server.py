#Protocolo de transferencia de hyper texto
#Hyper text transference protocol


#Também é possivel usar a framework flash para levantar servidores web com python


from http.server import BaseHTTPRequestHandler,HTTPServer
#Coisas necessárias apenas para servidor http
#RequestHandler = manipula as requisições
#HttpServer = levanta o servidor

HOST = 'localhost'
PORT = 5000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)#Vai responder OK
        self.send_header('Content-type','text/html')#Cabeçalho/Header
        #Header = Cabeçalho do protocolo http
        self.end_headers()#Serve para fechar o cabeçalho

        self.wfile.write(bytes("<html><head><title> AULA HTTP </title></head>", "utf-8"))
        #Utiliza aspas triplas para fazer uma string multiline
        #Nesse metodo iremos colocar a mensagem do site(o conteudo dele)
        self.wfile.write(bytes("<body>","utf-8"))
        self.wfile.write(bytes("<p>Servidor http de exemplo.</p>" , "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    def do_POST(self):
        pass
    def do_DELETE(self):
        pass
    def do_PUT(self):
        pass

webServer = HTTPServer((HOST,PORT), MyHandler)
print(f"Servidor iniciado em http://{HOST}:{PORT}")
webServer.serve_forever()


    
