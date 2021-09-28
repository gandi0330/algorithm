n, m = map(int,input().split())


def count_5 (i):
    cnt_5 = 0
    while i != 0:
        i = i // 5
        cnt_5 += i
    return cnt_5


def count_2 (i):
    cnt_2 = 0
    while i != 0:
        i = i // 2
        cnt_2 += i
    return cnt_2
    

print(min(count_5(n)-count_5(m)-count_5(n-m), count_2(n)-count_2(m)-count_2(n-m)))