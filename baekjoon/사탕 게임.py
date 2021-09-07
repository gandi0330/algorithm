import sys

n = int(input())

candy = [[*sys.stdin.readline()] for _ in range(n)]

answer = 0

def check():
    global answer, n, candy

    for i in range(n):
        sub = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                sub += 1
            else :
                answer = max(answer, sub)
                sub = 1
        
        if answer == n :
            return answer
    for i in range(n):
        sub = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i] :
                sub += 1
            else:
                answer = max(answer, sub)
                sub = 1

        if answer == n :
            return answer

            
for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        check()
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

for i in range(n-1):
    for j in range(n):
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        check()
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]


print(answer)