#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', 6789))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = f'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: {len(outputdata)}\n\n'
        connectionSocket.send(header.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        response = 'HTTP/1.1 404 Not Found\n\n404 Not Found. Fuck!\n'
        
        connectionSocket.send(response.encode())

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data