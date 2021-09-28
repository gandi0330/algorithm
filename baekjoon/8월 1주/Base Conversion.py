a, b = map(int, input().split())
_ = input()
num_list = list(map(int,input().split()))




# A진법 -> 10진법

a_10 = 0
for idx, num in enumerate(num_list[::-1]):
    a_10 += (a ** idx) * num


# 10진법 ->  B진법

answer = []

while True:
    if a_10 < b:
        answer.append(a_10)
        break
    else:
        a_10, r  = divmod(a_10, b)
        answer.append(r)

print(' '.join([str(i) for i in answer[::-1]]))
