import sys

n = int(input())

num_list = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)

index = 0
while index < n:
    if num_list[index] <= 0:
        break
    index += 1

plus_list = num_list[:index]
minus_list = num_list[index:][::-1]


answer = 0
for i in range(0, len(plus_list) -1, 2):
    if plus_list[i+1] != 1:
        answer += plus_list[i] * plus_list[i+1]
    else:
        answer += plus_list[i] + plus_list[i+1]
    
if len(plus_list) % 2 == 1:
    answer += plus_list[len(plus_list)-1]



for i in range(0, len(minus_list)-1, 2):
    answer += minus_list[i] * minus_list[i+1]

if len(minus_list) % 2 == 1:
    answer += minus_list[len(minus_list)-1]

print(answer)