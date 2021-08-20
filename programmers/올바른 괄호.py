# url : https://programmers.co.kr/learn/courses/30/lessons/12909
# 난이도 : level 2



def solution(s):
    answer = True
    
    stack_ = []
    
    for char in s:
        if char == '(' :
            stack_.append('(')
        else:
            if stack_ == [] :
                return False
            else:
                stack_.pop()
    
    if  stack_ != [] :
        return False
    return True