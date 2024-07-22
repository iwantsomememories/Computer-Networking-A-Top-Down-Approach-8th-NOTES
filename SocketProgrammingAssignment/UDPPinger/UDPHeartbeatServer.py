import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

start_time = float(time.time())
last_receive_time = start_time

while True:
    try:
        serverSocket.settimeout(0.1)
        message, address = serverSocket.recvfrom(1024)
        last_receive_time = float(time.time())
        message = message.decode()
        send_time = float(message.split()[2])
        print(f'Packet {message.split()[1]} : {(last_receive_time - send_time)*1000:.2f}ms')

        rand = random.randint(0, 10)
        if rand >= 4:
            serverSocket.sendto(message.upper().encode(), address)
    except TimeoutError:
        if last_receive_time == start_time:
            continue
        if time.time() - last_receive_time >= 1.0:
            print('Heartbeat pause')
            break
        else:
            print('Packet loss')

serverSocket.close()