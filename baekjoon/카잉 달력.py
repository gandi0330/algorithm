import sys

n = int(input())

for _ in range(n):
    m,n,x,y = map(int, sys.stdin.readline().split())

    X,Y= 1,1
    year = 1

    if x - X > n :
        Y = (Y + x - X) % n + 1
    else :
        Y = Y + x - X

    year += (x-X)
    X = x
    

    while True:
        print(X,Y,year)
        if Y == y:
            print(year)
            break
        
        elif year > m*n :
            print(-1)
            break

        else:
            if Y + m > n :
                Y = (Y + m) % (n+1) + 1
            else:
                Y = Y + m
            year += m
        
