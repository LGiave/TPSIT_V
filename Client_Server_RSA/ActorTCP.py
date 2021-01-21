"""
Server ACTOR UDP 
"""
import socket
import threading

ip = '192.168.0.123'    #IL MIO IP
porta = 7000
ip_server = '192.168.0.119' #IP DEL SERVER A CUI INVIO
porta_server = 7000     

while True:
    """
    CREATE SOCKET
    """
    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((ip, porta))   

    #comunicazione dei dati del server all'utente
    print(f"\nIl Server è online \t {ip}:{porta}")

    #creazione del socket TCP IPv4
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    """
    SERVER
    """
    #attesa di una connessione
    server.listen()
    #accettazione delle eventuali connessioni
    connessione, indirizzo_client = server.accept()

    #lettura dei dati inviati dall'utente
    data = connessione.recv(4096)  

    #comunicazione dei dati del calcolo all'utente
    print(str(indirizzo_client) + ": \t" + data.decode())    

    #chiusura del socket
    server.close()

    """
    CLIENT
    """
    #connessione al server
    client.connect((ip_server,porta_server))

    #invio dei dati al server
    client.sendall(data)

    #comunicazione risultato all'utente
    print(f"inviato a {ip_server}" + data.decode())

    client.close()


