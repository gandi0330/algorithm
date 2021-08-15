# 2021-08-15
# https://leetcode.com/problems/valid-parentheses/
# 난이도 별 1


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack_ = []
        for char in s:
            if char in ('(', '[', '{'):
                stack_.append(char)
            else:
                if len(stack_) == 0:
                    return False
            
                pop_char = stack_.pop()
                
                if char == ')' and pop_char == '(' :
                    continue
                elif char == ']' and pop_char == '[' :
                    continue
                elif char == '}' and pop_char == '{' :
                    continue
                else:
                    return False
                
        if stack_ :
            return False
        else:
            return True