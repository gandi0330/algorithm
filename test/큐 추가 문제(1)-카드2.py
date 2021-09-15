# 버리고 , 제일 밑으로 내리고 반복 
# 마지막 카드의 수는 ?

# 제일 밑으로 내리는 방법 (O(n))
# 1. 덱
# 2. 원형 큐로 front end 다 뒤로 
from collections import deque

n = int(input())

card = deque([i+1 for i in range(n)])

while True:
    if len(card) == 1 :
        print(card[0])
        break

    card.popleft()
    card.append(card.popleft())

#------------------------------


