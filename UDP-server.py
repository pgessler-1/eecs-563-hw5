from importlib.metadata import files
from multiprocessing import connection
import socket
import sys


def main():
    serverHost = socket.gethostbyname(socket.gethostname())
    packetSize = 1024
    serverPort = int(sys.argv[1])
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverHost, serverPort))

    while True:
        file_size, clientaddr = serverSocket.recvfrom(2048)
        print(f"[RECV] received file size: {file_size.decode('utf-8')}")
        serverSocket.sendto("File Size received".encode('utf-8'), clientaddr)
        

        filename, clientaddr = serverSocket.recvfrom(2048)
        print(f"[RECV] receiving the filename")
        file = open(f"transmitted\{filename.decode('utf-8')}", "w")
        serverSocket.sendto("Filename received".encode('utf-8'), clientaddr)
        fileSize = int(file_size.decode('utf-8'))
        currentByteLoc = 0
        packetCount = 0

        while (fileSize > currentByteLoc):
            data, clientaddr = serverSocket.recvfrom(packetSize)
            print(f"receiving data: packet {packetCount}")
            # print(data)
            file.write(str(data.decode('utf-8')))
            serverSocket.sendto(f"data received: packet {packetCount}".encode('utf-8'), clientaddr)
            packetCount += 1
            currentByteLoc += packetSize
        file.close()
        
        break
if __name__ == "__main__":
    main()