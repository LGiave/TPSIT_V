import socket 
import AlphaBot
server=('',7500)
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(server)

while True:
    alphabot=AlphaBot.AlphaBot()
    percorso = socket.recv(4096) 
    steps=(percorso.decode).split(',')
    alphabot.setMotor()
    while True:
        if steps[1][1]=='f':
            alphabot.forward(steps[1][1:])
            steps.remove(1)
        elif steps[1][1]=='b':
            alphabot.backward(steps[1][1:])
            steps.remove(1)
        elif steps[1][1]=='l':
            alphabot.left(steps[1][1:])
            steps.remove(1)
        else:
            alphabot.right(steps[1][1:])
            steps.remove(1)


