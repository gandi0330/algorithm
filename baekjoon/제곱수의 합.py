n = int(input())

d = [0] + [i for i in range(1,n+1)]

for i in range(2, n+1):
    for j in range(1,int(d[i] **0.5)+1):
        if d[i] > d[i - j*j]  :
            d[i] =  d[i - j*j] + 1
        
print(d[n]) 