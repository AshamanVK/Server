#!/usr/bin/python2
# work with network
import socket


def read_all(x):
    msg = ''
    while True:
        data = x.recv(1)
        print len(data)
        if data == '':
            break
        msg += data
        print msg
    print 'This is the end!', msg
    return msg


def main():
    # my machine will be host + some port
    host = '127.0.0.1'
    port = 5000

    # creating socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind socket to a host and port
    sock.bind((host, port))

    # servet start listening a connections
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        print 'I hear connection from:', addr
        print 'Waiting for message...'
        msg = read_all(conn)
        print 'Recived:', msg
        conn.sendall(msg)
    print 'Connection closed.'
    conn.close()


if __name__ == '__main__':
    main()
