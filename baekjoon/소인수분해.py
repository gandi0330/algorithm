
def soinsu (n):
    num = 2
    while n > 1:
        if n % num == 0 :
            print(num)
            n //= num
        else:
            num += 1

import sys
n = int(sys.stdin.readline())

soinsu(n)
