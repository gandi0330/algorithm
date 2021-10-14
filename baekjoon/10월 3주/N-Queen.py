# url : https://www.acmicpc.net/problem/9663
# 난이도 : gold5

n = int(input())

cnt = 0

def rec(sol, n):
    global cnt 

    # sol 길이가 n과 같아질 때 경우의 수 1 증가
    if len(sol) == n:
        cnt += 1
        return

    for i in range(n):
        for j in range(len(sol)):
            if sol[j] == i or len(sol) - j + sol[j] == i or -len(sol) + j + sol[j] == i:
                return
        else:
            rec(sol+[i],n)
    
for i in range(n):
    rec([i],n)

print(cnt)


    