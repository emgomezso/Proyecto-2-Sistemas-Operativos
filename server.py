from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread, Lock

## Definicion del mutex global
mutex = Lock()

## Funciones para los servicios
def traductor(pathstr):
        searchstr = pathstr.replace("/traductor?palabra=","")
        if searchstr == "hola":
            answer = "Hola en ingles es: Hello"
        elif searchstr == "adios":
            answer = "Adios en ingles es: Bye"
        elif searchstr == "si":
            answer = "Si en ingles es: Yes"
        elif searchstr == "no":
            answer = "No en ingles es: No"
        else:
            answer = "' " + searchstr + "' no esta definida en el traductor"          
        return answer

def diccionario(pathstr):
        searchstr = pathstr.replace("/diccionario?palabra=","")
        if searchstr == "mmu":
            answer = "Unidad de gestion de memoria"
        elif searchstr == "cpu":
            answer = "Unidad de procesamiento central"
        elif searchstr == "hdd":
            answer = "Disco duro"
        elif searchstr == "ram":
            answer = "Memoria de acceso aleatorio"
        elif searchstr == "windows":
            answer = "Una mierda"
        else:
            answer = "' " + searchstr + "' no esta definida en el diccionario"          
        return answer

## Definicion de clase HTTPServer usando threads
class ThreadedHTTPServer(HTTPServer):
    def process_request(self, request, client_address):
        thread = Thread(target=self.__new_request, args=(self.RequestHandlerClass, request, client_address, self))
        thread.start()
    def __new_request(self, handlerClass, request, address, server):
        handlerClass(request, address, server)
        self.shutdown_request(request)

## Definicion de clase manejadora de los GET requests
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        client_address = str(self.client_address[0])
        client_port = str(self.client_address[1])
        client_log = "Thread: " + client_port + " - URL usado: "+ self.path +"\n"
        mutex.acquire()
        try:
            logfile = open("server.log", "a")
            logfile.write(client_log)
            logfile.close()
        finally:
            mutex.release()
        if "/traductor" in self.path:
            searchstr = self.path.replace("/traductor?palabra=","")
            clientanswer = traductor(searchstr)
        elif "/diccionario" in self.path:
            searchstr = self.path.replace("/diccionario?palabra=","")
            clientanswer = diccionario(searchstr)
        else:
            clientanswer = "Servicio no definido"     
        self.wfile.write(bytes(clientanswer, "utf8"))

## Levantando HTTP Server y enviando la clase manejadora
server = ThreadedHTTPServer(('0.0.0.0', 12345), Handler)
server.serve_forever()