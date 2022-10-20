
import socket
import sys


def main():
    # serverHost = '127.0.0.1'
    serverHost = socket.gethostbyname(socket.gethostname())
    print(serverHost)
    # serverPort = 12000
    serverPort = int(sys.argv[1])
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()

        file_size = int(connectionSocket.recv(1024).decode('utf-8'))
        print(f"received file size: {file_size}")
        connectionSocket.send("size received".encode('utf-8'))

        filename = connectionSocket.recv(1024).decode('utf-8')
        print(f"[RECV] receiving the filename")
        file = open(f"transmitted\{str(filename)}", "w")
        connectionSocket.send("Filename received".encode('utf-8'))

        data = connectionSocket.recv(file_size).decode('utf-8')
        print(f"receiving the data")
        print(data)
        file.write(data)
        connectionSocket.send("data received".encode('utf-8'))
        file.close()
        
        connectionSocket.close()
        break

if __name__ == "__main__":
    main()