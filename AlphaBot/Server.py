import socket 

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind()
socket.listen()
conn, add = socket.accept()
while True:
    percorso=input()
    conn.sendall(percorso.encode)
