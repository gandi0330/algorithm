n = int(input())
num_list = [0] + list(map(int,input().split()))

i = 1
while i <= n:
    if i % 2 == 0 and num_list[i] % 2 == 0:
        i += 1
    elif i % 2 == 1 and num_list[i] % 2 == 1:
        i += 1
    else:
        print('NO')
        break

else:
    print('YES')