import socket as sk

def main():
    HOST = '127.0.0.1'
    PORT = 50005
    name = raw_input("Enter your Nickname:") 
    print "Hey ",name,"!!!"  
    a = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
    a.bind((HOST,PORT))
    a.listen(2)
    con,add = a.accept()
    con.send(name)
    name1 = con.recv(100)
    while(1):
        val = raw_input("[You]  \t:")
        if val==' ':
            exit()
        con.send(val)
        str_rec = con.recv(100)
        print "[",name1,"]\t:",str_rec
    con.close()
main()
