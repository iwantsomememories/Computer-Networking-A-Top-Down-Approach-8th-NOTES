from socket import *
import argparse

def request(ip, port, path):
    clientSocket = socket(AF_INET, SOCK_STREAM)

    #Establish the connection
    clientSocket.connect((ip, port))

    #Send one HTTP GET into socket
    request_line = f'GET /{path} HTTP/1.1\n'
    header = f'Host: {ip}\nConnection: close\n'
    clientSocket.send(request_line.encode())
    clientSocket.send(header.encode())
    clientSocket.send('\n'.encode())

    response = clientSocket.recv(2048)
    print("From Server: ")
    print(response.decode())

    clientSocket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', "--ip", type=str, default='127.0.0.1', metavar="", help='IP address of the Server')
    parser.add_argument('-P',"--port", type=int, default=6789, metavar="", help='Port of the Server')
    parser.add_argument('-p', "--path", type=str, default='HelloWorld.html', metavar="", help='Path of the requested file')
    args = parser.parse_args()

    request(args.ip, args.port, args.path)


