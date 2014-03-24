#!/usr/bin/env python 

import socket
from dialogexpert import DialogExpert

class Server():

    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # empty address for localhost
        # and some large port number
        self.serversocket.bind(('', 11002))

        # only one client is allowed
        # max allowed is 5, for more clients thread is used
        self.serversocket.listen(1)

        self.dialog_expert = DialogExpert(2)


    def talk(self):
        wants_to_talk = True        
        
        while wants_to_talk:
            message = self.client.recv(1024)
            if message:
                print 'Client:', message
                self.dialog_expert.think()
                answer = self.dialog_expert.get_random_message()
                self.client.send(answer)
                print 'Server:', answer
            else:
                print 'bye!'
                break

    def connect_to_client(self):
        self.client, address = self.serversocket.accept()
        print 'client accepted'

    def __del__(self):
        self.serversocket.close()


def main():
    server = Server()
    server.connect_to_client()
    server.talk()

if __name__ == "__main__":
    main()