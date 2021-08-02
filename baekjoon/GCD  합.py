def gcd(num1, num2):
    num1, num2 = min(num1, num2), max(num1, num2)
    
    for i in range(num1,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i



import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))[1:]


    gcd_sum = 0
    for i in range(len(num_list) - 1):
        for j in range(i+1, len(num_list)):
            gcd_sum += gcd(num_list[i], num_list[j])

    
    print(gcd_sum)