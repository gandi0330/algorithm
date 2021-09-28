city = int(input())
distance = list(map(int,input().split()))
oil_price = list(map(int,input().split()))

min_price = 1000000000
answer = 0

for i in range(len(oil_price)-1):
    if oil_price[i] < min_price:
        min_price = oil_price[i]
    
    answer += min_price * distance[i]

print(answer)