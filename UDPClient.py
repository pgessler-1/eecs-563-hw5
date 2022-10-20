from fileinput import filename
import sys
import socket
import os

def main():
    # serverName = '10.104.192.45'
    serverName = str(sys.argv[1])
    # serverPort = 12000
    serverPort = int(sys.argv[2])
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    filename = str(sys.argv[3])
    file = open(filename, "r", encoding='utf-8')
    data = file.read()

    # file_size = os.path.getsize(filename)

    clientSocket.sendto(filename.encode('utf-8'), (serverName, serverPort))
    msg, clientaddr = clientSocket.recvfrom(2048)
    msg.decode('utf-8')
    print(f"[server]: {msg}")


    clientSocket.sendto(data.encode('utf-8'), (serverName, serverPort))
    msg, clientaddr = clientSocket.recvfrom(2048)
    msg.decode('utf-8')
    print(f"[server]: {msg}")

    file.close()
    clientSocket.close()

if __name__ == "__main__":
    main()