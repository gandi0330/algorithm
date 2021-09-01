n = int(input())

dp_pre = [0,0,0]
dp_now = [1,1,1]

for _ in range(1, n):
    dp_pre = dp_now[:]
    dp_now = [sum(dp_pre),dp_pre[0]+dp_pre[1], dp_pre[0]+dp_pre[2]]
    
    print(dp_now)

print(sum(dp_now) % 9901)
    

