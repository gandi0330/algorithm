import sys

def stack_cal(n):

    nums = [int(sys.stdin.readline()) for _ in range(n)]

    stack1 = [i for i in range(n,0,-1)]
    stack2 = []

    answer = []
    for num in nums:
        
        while  True :
            if len(stack2) != 0 and stack2[-1] == num :
                stack2.pop()
                answer.append('-')
                break
            
            elif stack1 == [] :
                break

            elif stack1[-1] != num:
                stack2.append(stack1.pop())
                answer.append('+')
                

            elif stack1[-1] == num:
                stack2.append(stack1.pop())
                answer.append('+')
                stack2.pop()
                answer.append('-')
                break
            
            else :
                return "NO"
            

    return '\n'.join(answer)
    
   


n = int(sys.stdin.readline())

print(stack_cal(n))

