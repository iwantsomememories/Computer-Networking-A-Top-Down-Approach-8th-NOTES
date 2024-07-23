from socket import *
import base64
import getpass

msg = "good good study, day day up!"
contenttype = "text/plain"
subject = "hello"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = '****'

# Sender and Receiver
fromAddress = '****@163.com'
toAddress = '****@qq.com'

def send_email(mailserver, fromAddress, toAddress, username, password, msg):

    # Create socket called clientSocket and establish a TCP connection with mailserver
    #Fill in start 
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 25))
    #Fill in end
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'EHLO fanqie.chaodan\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Recv to heloCommand: ", recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Auth information (Encode with base64)
    base64str = ('\x00'+username+'\x00'+password).encode()
    base64str = base64.b64encode(base64str)
    authMsg = 'AUTH PLAIN '.encode()+base64str+'\n'.encode()
    clientSocket.send(authMsg)
    recv = clientSocket.recv(1024).decode()
    print("Recv to auth: ",recv)

    
    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfromCommand = f'MAIL FROM: <{fromAddress}>\r\n'
    clientSocket.send(mailfromCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Recv to mailfromCommand: ", recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response. 
    # Fill in start
    rcpttoCommand = f'RCPT TO: <{toAddress}>\r\n'
    clientSocket.send(rcpttoCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Recv to rcpttoCommand: ", recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response. 
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv = clientSocket.recv(1024).decode()
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
    clientSocket.send(message.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send('\r\n.\r\n'.encode())
    recv = clientSocket.recv(1024).decode()
    print("Recv to endCommand: ", recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print("Recv to quitCommand: ", recv)
    if recv[:3] != '221':
        print('221 reply not received from server.')
    # Fill in end

    clientSocket.close()

if __name__ == '__main__':
    username = input("username: ")
    password = getpass.getpass("password: ")
    send_email(mailserver, fromAddress, toAddress, username, password, msg)