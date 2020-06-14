# O(n) time: iterate through all brackets in s
# O(n) space: worst case, all brackets in s are stored in stack because there are no matches

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [-1]
        
        for bracket in s:
            if (stack[-1] == '(' and bracket == ')') or (stack[-1] == '[' and bracket == ']') or (stack[-1] == '{' and bracket == '}'):
                stack.pop()
            else:
                stack.append(bracket)
        
        return stack == [-1]