# 2021-08-15 
# https://leetcode.com/problems/remove-duplicate-letters
# 난이도 별 3

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack_s = [*s][::-1]
        stack_main = []
        
        for _ in range(len(stack_s)):
            char = stack_s.pop()
            if char not in stack_main :
                stack_main.append(char)
                
            
            else:
                for sub_char in stack_main[stack_main.index(char):] :
                    if sub_char < char :
                        for sub_subchar in stack_main[stack_main.index(char):stack_main.index(sub_char)]:
                            if sub_subchar > char and sub_subchar not in stack_s:
                                break
                        else :
                            stack_main.pop(stack_main.index(char))
                            stack_main.append(char)
                            
            
        answer = ''
        while stack_main:
            answer += stack_main.pop()
            
        return answer[::-1]