# def solution(a):
    
#     answer = []
#     for s in a:
        
#         answer.append(cal(s))
    
#     return answer
        
# def cal (s):
    

#     l = len(s)
    
    
    
# #     while True:
# #         a_cnt = s.count('a')
# #         if l >= 2*a_cnt and s[0:a_cnt] == 'b'*a_cnt and s[-1*a_cnt:] == 'b'*a_cnt :
            
# #             s = s.strip('b'*a_cnt)
# #             l -= 2*a_cnt
# #         elif l > 1 and s[0] == 'a' :
# #             s = s[1:]
# #             l -= 1
# #         elif l > 1 and s[-1] == 'a' :
# #             s = s[:-1]
# #             l -= 1
# #         elif s == 'a' : 
# #             return True
        
# #         else:
# #             return False

# #     # b_cnt = s_list.count('b')
# #     # s = ''.join(s_list)
# #     # if b_cnt % 2 != 0 :
# #     #     return False
# #     # else:
# #     #     for _ in range(b_cnt//2):
# #     #         start =s.find('b')
# #     #         end = s.rfind('b')
            
# #     #         s = s[start+1:end]
            
# #     #     if list(set([*s])) == ['a']:
# #     #         return True
# #     #     else :
# #     #         return False
    

# # print(solution(["bbabb","bab","bab"]))



def solution(a):
    
    answer = []
    for s in a:
        answer.append(cal(s))
    
    return answer
        
def cal (s):
    

    l = len(s)
    
    
    while True:
        a_cnt = s.count('a')
        if l >= 2*a_cnt and s[0:a_cnt] == 'b'*a_cnt and s[-1*a_cnt:] == 'b'*a_cnt :
            s = s[a_cnt:-a_cnt]
            l -= 2*a_cnt
        elif l > 1 and s[0] == 'a' :
            s = s[1:]
            l -= 1
        elif l > 1 and s[-1] == 'a' :
            s = s[:-1]
            l -= 1
        elif s == 'a' : 
            return True
        
        else:
            return False
print(solution(["bbabb"]))