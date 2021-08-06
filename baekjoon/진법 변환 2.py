n, b = map(int, input().split())

answer = ''

while True :
    if n < b:
        r = n % b 
        if r >= 10 :
            answer += chr(r-10 + ord('A'))
        else:
            answer += str(r)
        break
    else:
        n, r = divmod(n, b)
        if r >= 10 :
            answer += chr(r-10 + ord('A'))
        else :
            answer += str(r)


print(answer[::-1])