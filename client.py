import socket as sk

s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)#socket obj with IPV4 and TCP

s.connect(('127.0.0.1',50005))

name = raw_input("Enter your Nickname:") 
print "Hey ",name,"!!!"
s.send(name)
name1 = s.recv(100)

while(1):
    str_rec = s.recv(100) #get server send
    print "[",name1,"]\t:",str_rec
    val = raw_input("[You]    \t:")
    s.send(val)
