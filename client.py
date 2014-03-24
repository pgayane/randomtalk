#!/usr/bin/env python 

import socket
from dialogexpert import DialogExpert

def start_client():
    d = DialogExpert(1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(('', 11002)) 

    while True:
        d.think()
        m = d.get_random_message()

        print 'You:', m
        s.send(m)
        answer = s.recv(1024)
        print 'Server:', answer 

    s.close()

if __name__ == '__main__':
    start_client()