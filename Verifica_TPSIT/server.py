import socket 
import threading 
import logging 

my_ip = '127.0.0.1'
porta = 2512

logging.basicConfig(level = logging.DEBUG, filename="logging_server.log", filemode="a")
logger = logging.getLogger()

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

clienti=[]

class ClientThread(threading.Thread):
    def __init__(self,server,connessione,n,client):
        threading.Thread.__init__(self)
        self.server = server
        self.connessione = connessione
        self.num = n
        self.client = client

def check(): # controllo tutte celle piene
      for t in range(0,8):
          if board[t] == 0: return False
      return True

def run(self):
    clienti[0].connessione.sendall(str(0).encode())     #assegno id al client per gestione turni
    clienti[1].connessione.sendall(str(1).encode())
    while 1:
        if(vittoria1(board)==False): #controllo vittoria
            invia_dati_client(clienti[0].connessione,str(1).encode()) #invio turno client
            risultato1 = int(ricevi_dati_client(clienti[0].connessione).decode()) #ricevo mossa
            if board[risultato1]==0:    #controllo cella vuota
                board[risultato1] = 1   
            else:   # se piena controllo che ci siano ancora celle libere 
                if(check()==False): # se ci sono ancora celle libere richiedo una nuova mossa
                    invia_dati_client(clienti[0].connessione,str("Cella piena").encode())
                    invia_dati_client(clienti[0].connessione,str(board).encode())
                    invia_dati_client(clienti[0].connessione,str(1).encode())
                    risultato1 = int(ricevi_dati_client(clienti[0].connessione).decode())
                else: # se invece nessuno ha vinto e le celle sono tutte piene dichiara pareggio
                    invia_dati_client(clienti[0].connessione,str("Patta").encode())
                    break
        else: #in caso di vittoria comunica l'esito ai client
            invia_dati_client(clienti[0].connessione,str("Hai vinto").encode())
            invia_dati_client(clienti[1].connessione,str("Hai perso").encode())
            break
        if(vittoria2(board)==False):
            invia_dati_client(clienti[1].connessione,str(2).encode())
            risultato2 = int(ricevi_dati_client(clienti[1].connessione).decode())
            if board[risultato2]==0:
                board[risultato2] = 2
            else:
                if(check()==False):
                    invia_dati_client(clienti[1].connessione,str("Cella piena").encode())
                    invia_dati_client(clienti[1].connessione,str(board).encode())
                    invia_dati_client(clienti[1].connessione,str(1).encode())
                    risultato2 = int(ricevi_dati_client(clienti[1].connessione).decode())
                else:
                    invia_dati_client(clienti[1].connessione,str("Patta").encode())
                    break
        else: 
            invia_dati_client(clienti[1].connessione,str("Hai vinto").encode())
            invia_dati_client(clienti[0].connessione,str("Hai perso").encode())
            break

def vittoria1(board): #verifica se qualcuno ha vinto
    if board[1] == board[2] == board[3] == 1:
        return True
    if board[4] == board[5] == board[6] == 1:
        return True
    if board[7] == board[8] == board[9] == 1:
        return True
    if board[1] == board[4] == board[7] == 1:
        return True
    if board[2] == board[5] == board[8] == 1:
        return True
    if board[3] == board[6] == board[9] == 1:
        return True
    if board[1] == board[5] == board[9] == 1:
        return True
    if board[3] == board[5] == board[7] == 1:
        return True
    return False

def vittoria2(board):
    if board[1] == board[2] == board[3] == 2:
        return True
    if board[4] == board[5] == board[6] == 2:
        return True
    if board[7] == board[8] == board[9] == 2:
        return True
    if board[1] == board[4] == board[7] == 2:
        return True
    if board[2] == board[5] == board[8] == 2:
        return True
    if board[3] == board[6] == board[9] == 2:
        return True
    if board[1] == board[5] == board[9] == 2:
        return True
    if board[3] == board[5] == board[7] == 2:
        return True
    return False

def crea_server():
    global my_ip
    global porta

    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((my_ip, porta))   

    #comunicazione dei dati del server all'utente
    logger.info(f"\nIl server è online:  \t {my_ip}:{porta}")

    #attesa di una connessione
    server.listen()

    return server

def ricevi_dati_client(connessione):
    #ricevo una stringa dal client
    risultato = connessione.recv(4096) 
    risultato = risultato.decode()
    return risultato

def connetti_client(server):
    try:
        #accettazione delle eventuali connessioni
        connessione, client = server.accept() 
    except: 
        connessione = None
        logger.error("4.1, errore nella creazione della connessione")
    return connessione, client 

def invia_dati_client(connessione, data):
    try:
        data= data.encode()
        #restituisco il risultato al client
        connessione.sendall(data)
    except:
        logger.error("3.1, connessione persa")

def chiusura_server(server):
    #chiusura del socket
    server.close()
    logger.info(f"Il server è stato chiuso")

# chiede all'utente di muovere

def main():

    server = crea_server()
    n = 1
    while(1):
        connessione, client = connetti_client(server)
        c = ClientThread(server,connessione,n,client)
        clienti.append(c)
        c.start()
        n = n+1

    chiusura_server(server)

if __name__ == "__main__":
    main()
