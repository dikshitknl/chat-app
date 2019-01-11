import socket as sk
s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)#socket obj with IPV4 and TCP
s.connect(('127.0.0.1',50022))
while(1):
    str_rec = s.recv(100)#get server send
    print str_rec
