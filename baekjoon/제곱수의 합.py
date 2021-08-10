n = int(input())

k = int(n ** 0.5)

cnt = 0

while n :

    if k ** 2 > n:
        k -= 1
    else : 
        n -= k**2
        cnt +=  1
   

print(cnt)
