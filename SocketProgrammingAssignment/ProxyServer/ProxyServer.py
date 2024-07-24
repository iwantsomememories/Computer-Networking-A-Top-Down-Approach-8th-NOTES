from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
serverPort = 12000
tcpSerSock.bind(('', serverPort))
tcpSerSock.listen(5)
# Fill in end.

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)

    message = tcpCliSock.recv(1024).decode()
    print(message)

    # Extract the filename from the given message
    # print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print('Request file: ',filename)
    fileExist = "false"
    filetouse = "/" + filename
    # print(filetouse)

    try:
        # Check whether the file exist in the cache
        f = open(filetouse[1:], "r") 
        outputdata = f.readlines() 
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode()) 
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
        # Fill in start.
        for line in outputdata:
            tcpCliSock.send(line.encode())
        tcpCliSock.send("\r\n".encode())
        # Fill in end.
        print('Read from cache\n\n') 
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false": 
        # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            c.settimeout(2)
            hostn = filename.replace("www.","",1) 
            print(hostn) 
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                # Fill in end.

                # print(f'DEBUG: Connect to {hostn} - success.')

                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                # NOTICE: Unbuffered streams must be binary.
                fileobj.write(("GET "+"http://" + filename + " HTTP/1.0\n\n").encode())

                # print(f'DEBUG: Request to {hostn} - success.') 

                # Read the response into buffer
                # Fill in start.
                buffer = fileobj.readlines()
                # Fill in end.

                print(f'DEBUG: Read from {hostn} - success.')

                # Create a new file in the cache for the requested file. 
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb")
                flag = False
                # print(f'DEBUG: Open file {filename} - success.')

                # Fill in start.
                for line in buffer:
                    if flag:
                        tmpFile.write(line)
                        print(line)
                    if(line.decode() == '\r\n'):
                        flag = True
                    # Filter out the header of response
                    tcpCliSock.send(line)

                tmpFile.close()
                # Fill in end.
            except TimeoutError:
                print(f"No reply from {hostn}")
                tcpCliSock.send('HTTP/1.1 404 Not Found\n\n404 Not Found. Fuck!\n'.encode())
            except OSError as e:
                print("Illegal request") 
                print(e.args)
            finally:
                c.close()
        else:
        # HTTP response message for file not found
        # Fill in start.
            print('File Not Found')
            break
        # Fill in end.
    
    # Close the client and the server sockets 
    tcpCliSock.close() 

# Fill in start.
tcpSerSock.close()
# Fill in end.