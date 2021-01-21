"""
Client ECHO UDP 
"""
import socket

server_ip = "127.0.0.1"
server_port = 7989

#creazione del socket
s= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#funzionamento (legge il messaggio e lo invia al server e poi stampa ciò che gli viene restituito)
data_send= input("Inserire il messaggio: ")
print ("send: " + data_send)
data_send=data_send.encode()
server_address=(server_ip,server_port)
s.sendto(data_send, server_address)
data_received, _ = s.recvfrom(4096)
data_received=data_received.decode()
print ("received: " + data_received)

#chiusura del socket
s.close()