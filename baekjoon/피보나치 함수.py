import sys
n = int(sys.stdin.readline())

for _ in range(n):

    num = int(sys.stdin.readline())

    d = [[0, 0]] * 41 # dp table

    d[0] = [1, 0]
    d[1] = [0, 1]

    for i in range(2, num+1) : #fibonacchi(2) 부터 fibonacchi(num)까지 올라가며 계산한다
        d[i] = [d[i-1][0] + d[i-2][0] , d[i-1][1] + d[i-2][1]]

    print(d[num][0], d[num][1])


