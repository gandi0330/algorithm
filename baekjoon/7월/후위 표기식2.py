import sys

n = int(sys.stdin.readline())

strs = input()

dict_ = {i : int(sys.stdin.readline())  for i in sorted(filter(lambda x : x.isalpha(), set(strs))) }


stack_ = []

for char in strs:
    if char.isalpha() :
        stack_.append(dict_[char])
    else:
        num2 = stack_.pop()
        num1 = stack_.pop()

        if char == '+' :
            stack_.append(num1+num2)
        elif char == '-' :
            stack_.append(num1-num2)
        elif char == '*' :
            stack_.append(num1*num2)
        elif char == '/' :
            stack_.append(num1/num2)

print('{:.2f}'.format(stack_.pop()))