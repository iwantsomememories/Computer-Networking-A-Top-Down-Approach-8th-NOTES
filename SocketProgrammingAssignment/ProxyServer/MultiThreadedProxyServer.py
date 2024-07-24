from socket import *
import threading
import argparse
import fcntl

class ClientHandler(threading.Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
    
    def run(self):
        message = self.socket.recv(1024).decode()
        print(message)

        # Extract the filename from the given message
        filename = message.split()[1].partition("/")[2]
        print('Request file: ',filename)
        fileExist = "false"
        filetouse = "/" + filename
        try:
            # Check whether the file exist in the cache
            f = open(filetouse[1:], "r") 
            outputdata = f.readlines() 
            fileExist = "true"
            # ProxyServer finds a cache hit and generates a response message
            self.socket.send("HTTP/1.0 200 OK\r\n".encode()) 
            self.socket.send("Content-Type:text/html\r\n\r\n".encode())
            
            for line in outputdata:
                self.socket.send(line.encode())
            self.socket.send("\r\n".encode())

            print('\n\nRead from cache\n\n')
        except IOError:
            if fileExist == "false": 
            # Create a socket on the proxyserver
                c = socket(AF_INET, SOCK_STREAM)
                c.settimeout(2)
                hostn = filename.replace("www.","",1) 
                print(hostn) 
                try:
                    # Connect to the socket to port 80
                    c.connect((hostn, 80))
        

                    # print(f'DEBUG: Connect to {hostn} - success.')

                    # Create a temporary file on this socket and ask port 80 for the file requested by the client
                    fileobj = c.makefile('rwb', 0)
                    # NOTICE: Unbuffered streams must be binary.
                    fileobj.write(("GET "+"http://" + filename + " HTTP/1.0\n\n").encode())

                    # print(f'DEBUG: Request to {hostn} - success.') 

                    # Read the response into buffer
                    buffer = fileobj.readlines()
        

                    # print(f'DEBUG: Read from {hostn} - success.')

                    # Create a new file in the cache for the requested file. 
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    
                    tmpFile = open("./" + filename,"wb")
                    fcntl.flock(tmpFile, fcntl.LOCK_EX)
                    # Avoid resource access conflicts between threads

                    write_flag = False
                    # print(f'DEBUG: Open file {filename} - success.')
                    for line in buffer:
                        if write_flag:
                            tmpFile.write(line)
                            print(line)
                        if(line.decode() == '\r\n'):
                            write_flag = True
                        # Filter out the header of response
                        self.socket.send(line)
                    
                    fcntl.flock(tmpFile, fcntl.LOCK_UN)


                except TimeoutError:
                    self.socket.send('HTTP/1.1 404 Not Found\n\n404 Not Found. Fuck!\n'.encode())
                    print(f"No reply from {hostn}")
                except OSError as e:
                    print("Illegal request") 
                    print(e.args)
                finally:
                    c.close()
            else:
            # HTTP response message for file not found
                print('File Not Found')
    
        self.socket.close()

def main(ip):
    # Create a server socket, bind it to a port and start listening
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    serverPort = 12000
    tcpSerSock.bind((ip, serverPort))
    tcpSerSock.listen(5)

    while 1:
        # Strat receiving data from the client
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:', addr)

        ClientHandler(tcpCliSock).start()

    tcpSerSock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', "--ip", type=str, default='127.0.0.1', metavar="", help='IP address of the ProxyServer')
    args = parser.parse_args()

    main(args.ip)

