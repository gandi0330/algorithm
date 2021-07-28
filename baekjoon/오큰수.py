
# def nge (num_list):
#     answer = ''
#     for i in range(len(num_list)):
#         for j in range(i+1, len(num_list)):
#             # 현재 num_list의 값보다 큰 값을 찾으면 오큰수로 설정 후 break
#             if num_list[i] < num_list[j]:
#                 answer+= str(num_list[j]) + ' '
#                 break
#         # 반복문을 정상적으로 통과(오큰4수를 찾지 못함)하면 오큰수에 -1 저장
#         else :
#             answer += '-1 ' 
    
#     return answer.rstrip()

# _ = input()
# num_list = list(map(int, input().split()))

# print(range(num_list))

n = int(input())
num_list = list(map(int, input().split()))

answer = [-1 for _ in range(n)]

stack_ = []

for idx, num in enumerate(num_list):
    if len(stack_) == 0 :
        stack_.append(idx)
    
    elif num_list[stack_[-1]] > num :
        stack_.append(idx)
    
    else :
        while True:
            if len(stack_) != 0 and num_list[stack_[-1]] < num :
                answer[stack_.pop()] = num
            else :
                stack_.append(idx)
                break

print(' '.join([str(i) for i in answer]))