n, k = map(int,input().split())

fac = [0] * 11
fac[0] = 1
fac[1] = 1

for i in range(2,11):
    fac[i] = i*fac[i-1]

print(int(fac[n]/(fac[n-k]*fac[k])))