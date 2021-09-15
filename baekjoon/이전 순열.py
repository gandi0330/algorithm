n = int(input())

num_list = list(map(int,input().split()))

idx = n
for i in range(n-1,0,-1):
    if num_list[i] < num_list[i-1] :
        idx = i-1
        break

if idx == n :
    print(-1)
else:
    for i in range(n-1,idx,-1):
        if num_list[idx] > num_list[i] :
            num_list[idx], num_list[i] = num_list[i], num_list[idx]
            break

    num_list = num_list[:idx+1] + sorted(num_list[idx+1:], reverse=True)

    print(*num_list)