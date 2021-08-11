import sys

max_n = 100000
mod_num = 1000000009


t = int(input())

d = [[0]*3 for _ in range(max_n)]

d[0][0] = d[1][1] = d[2][0] = d[2][1] = d[2][2] = 1


for i in range(3,max_n):
    # 현재 수에서 1로 끝나는 수는 이전 수에서 2와 3으로 끝난 수에 1을 추가하면 된다
    d[i][0] = d[i-1][1]+d[i-1][2]
    d[i][0] %=  mod_num
    # 현재 수에서 2로 끝나는 수는 -2한 수에서 1과 3으로 끝난 수에 2를 추가하면 된다
    d[i][1] = d[i-2][0]+d[i-2][2]
    d[i][1] %= mod_num
    # 현재 수에서 3으로 끝나는 수는 -3한 수에서 1과 2로 끝나는 수에 3을 추가하면 된다
    d[i][2] = d[i-3][0]+d[i-3][1]
    d[i][2] %= mod_num

for _ in range(t):
    n = int(sys.stdin.readline())

    print(sum(d[n-1]) % mod_num)


