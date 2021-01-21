import random

def euclide(a, b):
    while(b != 0):
        a,b=b,a%b
    return a

p=2713
q=4013

msg=input("inserisci messaggio")

n=p*q

MCD=euclide(p,q)
m=(p-1)*(q-1)/MCD

c=random.randrange(1,m)
x=euclide(c,m)

while x!=1:
    c=random.randrange(1,m)
    x=euclide(c,m)

d=random.randrange(0,m)
y=(c*d)%m

pub=(c,n)

while y!=1:
    d=random.randrange(0,m)
    y=(c*d)%m

priv=(d,n)

msg_cript=[(ord(char) ** d) % n for char in msg]
cript=str(msg_cript)

msg_decript=[chr((char ** c) % n) for char in msg_cript]
decript=str(msg_decript)

print(cript)
print(decript)