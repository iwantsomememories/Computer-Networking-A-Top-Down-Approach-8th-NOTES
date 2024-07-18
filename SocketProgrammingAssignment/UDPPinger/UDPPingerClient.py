from socket import *
import time
import argparse

def repeat_ten_ping(ip, port):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    for i in range(1, 11):
        send_time = time.time()
        message = f'Ping {i} {send_time}'
        clientSocket.sendto(message.encode(), (ip, port))
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            recv_time = time.time()
            print(f'Response from {serverAddress}: sequence={i} length={len(modifiedMessage)} bytes RTT={(recv_time-send_time)*100:{4}.{2}}ms')
        except TimeoutError:
            print('Request timed out')
    
    clientSocket.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', "--ip", type=str, default='127.0.0.1', metavar="", help='IP address of the Server')
    parser.add_argument('-P',"--port", type=int, default=12000, metavar="", help='Port of the Server')
    args = parser.parse_args()

    repeat_ten_ping(args.ip, args.port)



