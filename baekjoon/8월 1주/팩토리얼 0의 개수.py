n = int(input())

num = 1

for i in range(1,n+1) :
    num *= i

zero_stack = 0
for i in str(num)[::-1]:
    if int(i) == 0:
        zero_stack += 1
    
    else:
        break

print(zero_stack)