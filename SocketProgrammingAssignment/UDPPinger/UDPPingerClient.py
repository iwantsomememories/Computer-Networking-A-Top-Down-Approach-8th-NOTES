from socket import *
import time
import argparse

def repeat_ten_ping(ip, port):
    total_rtt = 0
    max_rtt = 0
    min_rtt = 1000
    receive_packets = 0

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    for i in range(1, 11):
        send_time = time.time()
        message = f'Ping {i} {send_time}'
        clientSocket.sendto(message.encode(), (ip, port))
        try:
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            rtt = (time.time() - send_time)*1000

            total_rtt += rtt
            max_rtt = max(max_rtt, rtt)
            min_rtt = min(min_rtt, rtt)
            receive_packets += 1

            print(f'Response from {serverAddress}: sequence={i} length={len(modifiedMessage)}bytes RTT={rtt:.2f}ms')
        except TimeoutError:
            print('Request timed out')
    
    print(f'--- {ip} ping statistics ---')
    print(f'10 packets transmitted, {receive_packets} received, {(10-receive_packets)/10*100:.2f}% packet loss, time {total_rtt:.3f}ms')
    print(f'rtt min/avg/max = {min_rtt:.3f}/{total_rtt/10:.3f}/{max_rtt:.3f} ms')
    
    clientSocket.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', "--ip", type=str, default='127.0.0.1', metavar="", help='IP address of the Server')
    parser.add_argument('-P',"--port", type=int, default=12000, metavar="", help='Port of the Server')
    args = parser.parse_args()

    repeat_ten_ping(args.ip, args.port)



