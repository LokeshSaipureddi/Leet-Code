class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backTracking(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return 
            if openCount < n:
                stack.append('(')
                backTracking(openCount + 1, closeCount)
                stack.pop()
            if closeCount < openCount:
                stack.append(')')
                backTracking(openCount, closeCount+1)    
                stack.pop()
        backTracking(0,0)
        return res           