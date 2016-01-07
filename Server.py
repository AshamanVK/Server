#!/usr/bin/python2
# work with network
import socket


def main():
    # my machine will be host + some port
    host = '127.0.0.1'
    port = 5000

    # creating socket object
    sock = socket.socket()

    # bind socket to a host and port
    sock.bind((host, port))

    # servet start listening a connections
    sock.listen(1)

    while True:
        # accepting connection
        # and get new socket + client addres
        conn, addr = sock.accept()
        print 'Connection from: ', str(addr)

        # data = recived data from connection
        data = conn.recv(1024)

        if not data:
            break
        print 'from connected user:', str(data)
        data = str(data) + 'Your head looks like billiard ball\n\n'
        print 'sending:', str(data)
        conn.send(data)

        # closing connection
        conn.close()
    conn.close()

# I dunno what the fuck is it
if __name__ == '__main__':
    main()
