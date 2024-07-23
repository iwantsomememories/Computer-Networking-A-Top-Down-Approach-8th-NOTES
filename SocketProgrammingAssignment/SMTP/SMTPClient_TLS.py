import socket
import base64
import getpass
import ssl

msg = "good good study, day day up!"
contenttype = "text/plain"
subject = "hello"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
port = 587

# Sender and Receiver
fromAddress = '****@gmail.com'
toAddress = '****@qq.com'

def send_email(mailserver, port, fromAddress, toAddress, username, password, msg):
    context = ssl.create_default_context()

    # Create secure socket called clientSocket and establish a TCP connection with mailserver
    with socket.create_connection((mailserver, port)) as clientSocket:
        recv = clientSocket.recv(1024).decode()
        print(recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')

        # Send EHLO command and print server response.
        ehloCommand = 'EHLO fanqie.chaodan\r\n'
        clientSocket.send(ehloCommand.encode())
        recv = clientSocket.recv(1024).decode()
        print("Recv to ehloCommand: ", recv)
        if recv[:3] != '250':
            print('250 reply not received from server.')

        # Send StartTLS command and print server response.
        starttlsCommand = 'STARTTLS\r\n'
        clientSocket.send(starttlsCommand.encode())
        recv = clientSocket.recv(1024).decode()
        print("Recv to STARTTLS: ", recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')

        # Secure the socket
        with context.wrap_socket(clientSocket, server_hostname=mailserver) as secureSocket:

            # Send EHLO again after STARTTLS
            secureSocket.sendall('EHLO fanqie.chaodan\r\n'.encode())
            recv = secureSocket.recv(1024).decode()
            print("Recv to ehloCommand: ", recv)
            if recv[:3] != '250':
                print('250 reply not received from server.')

            # Auth information (Encode with base64)
            base64str = ('\x00'+username+'\x00'+password).encode()
            base64str = base64.b64encode(base64str)
            authMsg = 'AUTH PLAIN '.encode()+base64str+'\n'.encode()
            secureSocket.send(authMsg)
            recv = secureSocket.recv(1024).decode()
            print("Recv to AUTH: ",recv)
            if recv[:3] != '235':
                print('Auth failed.')

            
            # Send MAIL FROM command and print server response.
            # Fill in start
            mailfromCommand = f'MAIL FROM: <{fromAddress}>\r\n'
            secureSocket.send(mailfromCommand.encode())
            recv = secureSocket.recv(1024).decode()
            print("Recv to mailfromCommand: ", recv)
            if recv[:3] != '250':
                print('250 reply not received from server.')
            # Fill in end

            # Send RCPT TO command and print server response. 
            # Fill in start
            rcpttoCommand = f'RCPT TO: <{toAddress}>\r\n'
            secureSocket.send(rcpttoCommand.encode())
            recv = secureSocket.recv(1024).decode()
            print("Recv to rcpttoCommand: ", recv)
            if recv[:3] != '250':
                print('250 reply not received from server.')
            # Fill in end

            # Send DATA command and print server response. 
            # Fill in start
            dataCommand = 'DATA\r\n'
            secureSocket.send(dataCommand.encode())
            recv = secureSocket.recv(1024).decode()
            print("Recv to dataCommand: ", recv)
            if recv[:3] != '354':
                print('354 reply not received from server.')
            # Fill in end

            # Send message data.
            # Fill in start
            message = 'from:' + fromAddress + '\r\n'
            message += 'to:' + toAddress + '\r\n'
            message += 'subject:' + subject + '\r\n'
            message += 'Content-Type:' + contenttype + '\t\n'
            message += '\r\n' + msg
            

            secureSocket.send(message.encode())
            # Fill in end

            # Message ends with a single period.
            # Fill in start
            secureSocket.send('\r\n.\r\n'.encode())
            recv = secureSocket.recv(1024).decode()
            print("Recv to endCommand: ", recv)
            if recv[:3] != '250':
                print('250 reply not received from server.')
            # Fill in end

            # Send QUIT command and get server response.
            # Fill in start
            quitCommand = 'QUIT\r\n'
            secureSocket.send(quitCommand.encode())
            recv = secureSocket.recv(1024).decode()
            print("Recv to quitCommand: ", recv)
            if recv[:3] != '221':
                print('221 reply not received from server.')
            # Fill in end

if __name__ == '__main__':
    username = input("username: ")
    password = getpass.getpass("password: ")
    send_email(mailserver, port, fromAddress, toAddress, username, password, msg)