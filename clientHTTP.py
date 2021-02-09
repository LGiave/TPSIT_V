import socket,requests

pswlist=[]
pswlist.append(('luca','giavelli'))
serverip='127.0.0.1'
serverporta=5000

addr=(serverip,serverporta)

url='127.0.0.1:5000'
client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

body = {'username = mario & password = rossi'}
content_type="application/x-www-form-urlencoded",
content_length=len(body)

client.sendall((addr),)
risp=client.recv(4096)
print(risp.decode())
n=0
while n<=len(pswlist):
    client.sendall(addr,pswlist[n].encode())
    risp=client.recv(4096)
    print(risp.decode())
    n+1

