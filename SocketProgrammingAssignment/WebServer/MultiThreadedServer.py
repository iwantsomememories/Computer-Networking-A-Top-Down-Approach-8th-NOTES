import threading
from socket import *

print_lock = threading.Lock()

class ClientHandler(threading.Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        try:
            message = self.socket.recv(2048).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            #Send one HTTP header line into socket
            header = f'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: {len(outputdata)}\n\n'
            print_lock.acquire()
            print(threading.current_thread().name)
            print(header)
            print_lock.release()
            self.socket.send(header.encode())
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                self.socket.send(outputdata[i].encode())
            self.socket.send("\n".encode())
            self.socket.close()
        except IOError:
            #Send response message for file not found
            response = 'HTTP/1.1 404 Not Found\n\n404 Not Found. Fuck!\n'
            
            self.socket.send(response.encode())

            #Close client socket
            self.socket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 12000))

    serverSocket.listen(5)

    while True:
        try:
            #Establish the connection
            print('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()
            print(f"Accepted from addr: {addr}")
            ClientHandler(connectionSocket).start()
        except:
            print('Exit')

            break

if __name__ == '__main__':
    main()





