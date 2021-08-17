n = int(input())

if n == 0 :
    print(0)
else:

    answer = ''
    while n != 0:
        n, r = divmod(n,-2)

        if r == -1 :
            n += 1
            r = 1
        
        answer += str(r)

    print(answer[::-1])