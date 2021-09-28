k = input()

stack_ = [] 
back = ''
count = 0

for s in k :
    if back == '' :
        back = s

    elif back == '(' and s == ')' :
        count += len(stack_)
        back = s

    elif back == '(' and s == '(' :
        stack_.append(s)

    elif back == ')' and s == '(' :
        back = s

    elif back == ')' and s == ')' :
        count += 1
        stack_.pop()

print(count) 