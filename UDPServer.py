from multiprocessing import connection
import socket
import sys


def main():
    # serverHost = '10.104.192.45'
    serverHost = socket.gethostbyname(socket.gethostname())
    #serverPort = 12000
    serverPort = int(sys.argv[1])
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverHost, serverPort))

    while True:

        

        filename, clientaddr = serverSocket.recvfrom(2048)
        filename.decode('utf-8')
        print(f"[RECV] receiving the filename")
        file = open(filename, "w")
        serverSocket.sendto("Filename received".encode('utf-8'), clientaddr)

        data, clientaddr = serverSocket.recvfrom(2048)
        data.decode('utf-8')
        print(f"receiving the data")
        print(data)
        file.write(str(data))
        serverSocket.sendto("data received".encode('utf-8'), clientaddr)
        file.close()
        
        break
if __name__ == "__main__":
    main()