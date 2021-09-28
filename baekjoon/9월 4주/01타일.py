# url : https://www.acmicpc.net/problem/1904
# 난이도 : silver 3

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)

else:

    dp1 = 1
    dp2 = 2

    for i in range(2,n):
        dp = (dp1 + dp2) % 15746
        dp1 = dp2
        dp2 = dp

    print(dp)