card = int(input())
cardpack = [0] + list(map(int,input().split()))

d = [0] * (card + 1)

d[1] = cardpack[1]


for i in range(2,card+1):
    d[i] = cardpack[i]
    for j in range(1,i):
        d[i] = min(d[i], d[j] + d[i-j])


print(d[card])

