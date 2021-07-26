n, k = map(int,input().split())

yo_li = list(range(1,n+1))
answer = []
pointer = n - 1
d = n
while yo_li :
    pointer += k
    pointer %= d

    answer.append(str(yo_li.pop(pointer)))
    pointer -= 1
    d -= 1
print('<',end='')
print(', '.join(answer), end='>')