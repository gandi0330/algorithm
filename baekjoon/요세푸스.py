n, k = map(int,input().split())

# 1부터 n까지 list
yo_li = list(range(1,n+1))
answer = []

# yo_li의 값을 가리킬 인덱스 (yo_li의 마지막 인덱스로 초기화)
pointer = n - 1

# yo_li의 크기
d = n

while yo_li :
    # pointer에 k 만큼 더한 값의 나머지를 pointer에 넣는다
    pointer += k
    pointer %= d

    # pointer가 가리키는 값을 yo_li에서 지우면서 answer 리스트에 넣는다 (나중에 join하기 위해 str값으로 변환)
    answer.append(str(yo_li.pop(pointer)))

    # 가리키던 값이 지워졌으므로 pointer를 한칸 왼쪽으로 옮기고 d 값도 줄인다
    pointer -= 1
    d -= 1

print('<',end='')
print(', '.join(answer), end='>')