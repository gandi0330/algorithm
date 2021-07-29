k = input()

split_f = []
sub_k = ''
in_ = False
for i in k:

    if i.isalpha() == True : sub_k += i
    elif i == '(' : 
        in_ = True
        if sub_k != '':
            split_f.append(sub_k)
        sub_k = ''
    elif i == ')' : 
        in_ = False
        if sub_k != '':
            split_f.append(sub_k)
        sub_k = ''
    elif i in ['+','-'] and in_ == False :
        if len(sub_k) >= 3:
            split_f.append(sub_k)
            sub_k = i
        else :
            sub_k += i
            split_f.append(sub_k)
            sub_k = ''
    elif i.isalpha() == 0 and i in sub_k :
        split_f.append(sub_k)
        sub_k = i
    else:
        sub_k += i

if len(sub_k) != 0 :
    split_f.append(sub_k)

print(split_f)

stack_alpha = []
stack_operator = []

answer = []
sub_answer = ''
for idx, word in enumerate(split_f[::-1]):
    if len(word) == 1:
        while len(stack_alpha) != 0:
            sub_answer += stack_alpha.pop()

        while len(stack_operator) != 0:
            sub_answer += stack_operator.pop()

        sub_answer += word[0]
        answer.append(sub_answer)
        sub_answer = ''
    elif len(word) == 2:
        if word[0].isalpha() : 
            a, b = word[0], word[1]
        else : 
            a,b = word[1], word[0]


        while len(stack_alpha) != 0:
            sub_answer += stack_alpha.pop()
        sub_answer = a + sub_answer

        while len(stack_operator) != 0:
            sub_answer += stack_operator.pop()

        sub_answer += b
        answer.append(sub_answer)
        sub_answer = ''
    elif len(word) == 3:
        stack_alpha.append(word[2])
        stack_operator.append(word[1])
        stack_alpha.append(word[0])

        if idx == len(split_f)-1:
            while len(stack_alpha) != 0:
                sub_answer += stack_alpha.pop()
            
            while len(stack_operator) != 0:
                sub_answer += stack_operator.pop()

            answer.append(sub_answer)
            sub_answer = ''
    else :
        for i in word:
            if i.isalpha() : stack_alpha.append(i)
            else : stack_operator.append(i)


print(''.join(answer[::-1]))
