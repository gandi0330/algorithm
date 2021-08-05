strs = input()

op_stack = []
answer = ''

for char in strs:
    if char.isalpha():
        answer += char
    else:

        if char == '(':
            op_stack.append(char)
        
        elif char == '*' or char == '/':
            while len(op_stack) != 0 and op_stack[-1] in ['*','/']:
                answer += op_stack.pop()
            
            op_stack.append(char)
        
        elif char == '+' or char == '-':
            while len(op_stack) != 0 and op_stack[-1] != '(':
                answer += op_stack.pop()

            op_stack.append(char)
        
        else : # char == ')'
            while op_stack[-1] != '(':
                answer += op_stack.pop()
            
            op_stack.pop()
        
while len(op_stack) != 0:
    answer += op_stack.pop()

print(answer)