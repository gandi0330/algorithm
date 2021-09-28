# url : https://www.acmicpc.net/problem/2529
# 난이도 : silver 2


n = int(input())
signs = input().split()
visited = [False] * 10

mn, mx = "",""

def cal(left, right, op):
    if op == '<':
        return left < right
    else:
        return left > right

def recur(l, s):
    global mn, mx
    if l == n + 1:
        if mn == "":
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not visited[i]:
            if l == 0 or cal(s[-1], str(i), signs[l-1]):
                visited[i] = True
                recur(l+1, s + str(i))
                visited[i] = False

recur(0,"")
print(mx)
print(mn)
        