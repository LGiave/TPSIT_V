import random
import math
import socket
ip='127.0.0.1'
port=10000
N=4391
g=1000
b=random.randrange(1,N)
key= pow(g,b,N)

bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
bob.bind((ip,port))
bob.listen()
print("online")
conn,ip=bob.accept()
data = conn.recv(4096) 
d=data.decode()
A=pow(int(d),b,N)
conn.sendall((str(key).encode()))
print(A)
bob.close()

