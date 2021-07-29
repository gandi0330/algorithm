n = int(input())
A = list(map(int,input().split()))

answer = [-1] * n

A_count = {i : 0 for i in set(A)}

for i in A:
    A_count[i] += 1

stack_ = []

for idx, num in enumerate(A):
    if len(stack_) == 0:
        stack_.append(idx)
    
    elif A_count[num] <= A_count[A[stack_[-1]]] :
        stack_.append(idx)
    
    else :
        while True:
            if len(stack_) != 0 and A_count[num] > A_count[A[stack_[-1]]] :
                answer[stack_.pop()] = num
            
            else :
                stack_.append(idx)
                break

print(' '.join([str(i) for i in answer]))