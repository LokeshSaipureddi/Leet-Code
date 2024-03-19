class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"}":"{", ")":"(", "]":"["}
        stack = []
        for i in s:
            if i ==')' or i =="}" or i=="]":
                if len(stack) == 0:
                    return False
                elem = stack.pop()
                if elem!=paren[i]:
                    return False
            elif i =='(' or i =="{" or i=="[":
                stack.append(i)
        if stack:
            return False
        return True