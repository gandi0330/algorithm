n = int(input())

# 최소 입력값인 1을 대입했을 때 d[3]을 초기화 시키기 위한 최소 d 크기
d = [0] * (n + 3)

d[2] = 1
d[3] = 1

for i in range(4,n+1):

    sub_list = []
    if i % 3 == 0:
        sub_list.append(d[i//3])

    if i % 2 == 0:
        sub_list.append(d[i//2])

    sub_list.append(d[i-1])

    d[i] = min(sub_list) + 1

print(d[n])