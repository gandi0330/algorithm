def gcd (li):
    
    n = li[0]
    for i in range(1, len(li)):
        m = li[i]

        n,m = max(n,m), min(n,m)
        while m !=0:
            n,m = m,n%m
        
    return n

import sys

_, s = map(int,sys.stdin.readline().split())
num_li = list(map(int,sys.stdin.readline().split()))

for i in range(len(num_li)):
    num_li[i] = max(s, num_li[i]) - min(s, num_li[i])

print(gcd(num_li))


