class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')':'(',']':'[','}':'{'}
        stack=[]
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif len(stack)==0:
                return False
            elif s[i]==')' or s[i]==']' or s[i]=='}':
                element = stack.pop()
                if element != paren[s[i]]:
                    return False
        if stack:
            return False
        return True