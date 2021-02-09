import socket
import logging

def input_control():
    while 1:
        try:
            move = int(input("Fai la tua mossa: \n")) # controlla che l'imput sia corretto
            if move < 0 or  move > 8:
                print ("Non è un numero valido!")
            else:
                return str(move) # restituisce la mossa da inviare al server
        except ValueError: # controlla che venga inserito un numero e non del testo
              print ("Non è un numero valido!")

ip_server = '127.0.0.1'
porta_server = 2512

logging.basicConfig(level = logging.DEBUG, filename="logging_client.log", filemode="a")
logger = logging.getLogger()

#creazione del socket TCP IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#connessione al server
client.connect((ip_server,porta_server))

logger.info("connesso al server")

n=int(client.recv(4096).decode) # id assegnato dal server 

while(True):
    #leggo il messaggio
    messaggio = client.recv(4096).decode() 

    if (messaggio)==n: # se il messaggio è uguale all'id del client inizia il turno
        client.sendall(input_control().encode) # invio della mossa
    elif messaggio=="Hai vinto" or messaggio=="Hai perso" or messaggio=="Patta":
        print(messaggio)
        break
    else:
        print(messaggio)   

#chiusura del socket
client.close()