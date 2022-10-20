from fileinput import filename
import sys
import socket
import os

def main():
    serverName = str(sys.argv[1])
    packetSize = 1024
    serverPort = int(sys.argv[2])
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    filename = str(sys.argv[3])
    file = open(filename, "r", encoding='utf-8')
    fileSize = os.path.getsize(filename)
    data = file.read()

    clientSocket.sendto(str(fileSize).encode('utf-8'), (serverName, serverPort))
    msg, clientaddr = clientSocket.recvfrom(2048)
    print(f"[server]: {msg.decode('utf-8')}")

    clientSocket.sendto(filename.encode('utf-8'), (serverName, serverPort))
    msg, clientaddr = clientSocket.recvfrom(2048)
    print(f"[server]: {msg.decode('utf-8')}")

    currentByteLoc = 0
    while(fileSize > currentByteLoc):
        clientSocket.sendto(data[currentByteLoc: currentByteLoc+packetSize].encode('utf-8'), (serverName, serverPort))
        msg, clientaddr = clientSocket.recvfrom(2048)
        print(f"[server]: {msg.decode('utf-8')}")
        currentByteLoc += packetSize
        if(currentByteLoc >= fileSize):
            break

    file.close()
    clientSocket.close()

if __name__ == "__main__":
    main()