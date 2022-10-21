
import os
import socket
import sys


def main():
    serverHost = socket.gethostbyname(socket.gethostname())
    print(serverHost)
    serverPort = int(sys.argv[1])
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(1)

    current_directory = os.getcwd()
    directory = "transmitted"
    path = os.path.join(current_directory, directory)

    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    while True:
        connectionSocket, addr = serverSocket.accept()

        file_size = int(connectionSocket.recv(1024).decode('utf-8'))
        print(f"received file size: {file_size}")
        connectionSocket.send("size received".encode('utf-8'))

        filename = connectionSocket.recv(1024).decode('utf-8')
        print(f"receiving the filename")
        file = open(f"{path}\{str(filename)}", "w")
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