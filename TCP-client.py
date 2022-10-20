import sys
import socket
import os

def main():
    serverName = str(sys.argv[1])
    serverPort = int(sys.argv[2])
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    filename = str(sys.argv[3])
    file = open(filename, "r", encoding="utf8")
    data = file.read()

    file_size = os.path.getsize(filename)
    clientSocket.send(str(file_size).encode("utf-8"))
    clientSocket.recv(1024).decode("utf-8")

    clientSocket.send(filename.encode('utf-8'))
    msg = clientSocket.recv(1024).decode('utf-8')
    print(f"[server]: {msg}")

    clientSocket.send(data.encode('utf-8'))
    msg = clientSocket.recv(1024).decode('utf-8')
    print(f"[server]: {msg}")

    file.close()
    clientSocket.close()

if __name__ == "__main__":
    main()