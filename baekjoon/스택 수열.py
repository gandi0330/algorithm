import sys

def stack_cal(n):

    nums = [int(sys.stdin.readline()) for _ in range(n)]

    # n 부터 1까지 거꾸로 들어있는 stack1
    stack1 = [i for i in range(n,0,-1)]
    stack2 = []

    answer = []
    for num in nums:
        
        while  True :
            # stack2에 숫자가 있고 top이 num이면 stack2를 pop한다
            if len(stack2) != 0 and stack2[-1] == num :
                stack2.pop()
                answer.append('-')
                break
            
            elif stack1 == [] :
                # stack1이 비어있을 때 stack2가 비어있지 않으면 (stack2의 top이 num이 아니면) "NO"를 리턴 
                if len(stack2) != 0:
                    return "NO"

                # stack1과 stack2 모두 비어있다면 반복문 멈춤
                break
            
            # stack1의 top이 num이 아니라면 stack2로 넘긴다
            elif stack1[-1] != num:
                stack2.append(stack1.pop())
                answer.append('+')
                
            # stack1의 top이 num이라면 stack2로 넘긴 후 stack2에서 pop한다
            elif stack1[-1] == num:
                stack2.append(stack1.pop())
                answer.append('+')
                stack2.pop()
                answer.append('-')
                break
            
            

    return '\n'.join(answer)
    
   


n = int(sys.stdin.readline())

print(stack_cal(n))

