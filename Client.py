import socket


def main():
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    message = raw_input('->')
    while message != 'q':
        sock.send(message)
        answer = sock.recv(1024)
        print 'Recived from server:', answer
        message = raw_input('->')
    sock.close()

if __name__ == '__main__':
    main()
