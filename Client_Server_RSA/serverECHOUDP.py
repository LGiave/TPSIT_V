"""
Server ECHO UDP 
"""
import socket

server_ip = "127.0.0.1"
server_port = 7898

#creazione del socket
s= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#bind del server per esporlo sulla rete
s.bind((server_ip, server_port))
print("bind")

while True:
    #funzionamento (legge il messaggio e lo restituisce)
    data, address = s.recvfrom(4096)
    print (data.decode())
    s.sendto(data, address)

#chiusura del socket
s.close()