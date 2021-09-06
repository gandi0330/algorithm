# url : https://www.acmicpc.net/problem/1476
# 난이도 : silver 5

e, s, m = map(int,input().split())

E, S, M = 1, 1, 1
cnt = 1
while True:
    if e == E and s == S and m == M:
        break
    else:
        E = E % 15 + 1
        S = S % 28 + 1
        M = M % 19 + 1
        cnt += 1

print(cnt)
