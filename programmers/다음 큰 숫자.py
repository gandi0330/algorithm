# url : https://programmers.co.kr/learn/courses/30/lessons/12911
# 난이도 : level 2



def solution(n):

    one_cnt = bin(n)[2:].count('1')
    
    while True:
        n += 1 

        if bin(n)[2:].count('1') == one_cnt:
            return n


print(solution(78))
