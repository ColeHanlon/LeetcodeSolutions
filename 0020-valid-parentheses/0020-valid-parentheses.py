class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif s[i] == ')' and stack.pop() != '(' :
                    return False
                elif s[i] == ']' and stack.pop() != '[' :
                    return False
                elif s[i] == '}' and stack.pop() != '{' :
                    return False
                
        
        return not stack