N=100000

while N>1:

    div,count=2,0

    while div<=N/2 and count==0:

        if N%div==0:

            count+=1

        div+=1

    if count==0:

        print(N)

    N-=1