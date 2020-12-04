import random
import math
import socket
ip='127.0.0.1'
port=10000
N=4391
g=1000
a=random.randrange(1,N)
key= pow(g,a,N)

alice=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alice.connect((ip,port))
alice.sendall((str(key).encode()))
data= alice.recv(4096)  
B=pow(int(data.decode()),a,N)
print(B)
alice.close()

