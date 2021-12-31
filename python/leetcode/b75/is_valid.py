class Solution:
    def isValid(self, s: str) -> bool:
        # Runtime: 39 ms, faster than 19.44% of Python3 online submissions for Valid Parentheses.
        # Memory Usage: 14.2 MB, less than 65.09% of Python3 online submissions for Valid Parentheses.
        
        # Time: O(n) (size of s)
        # Space: stack - O(n), dict O(1) since nothing is being added

        stack = []
        res = {'(':')', '{': '}', '[': ']'}
        
        for i in s:
            if i in res:
                stack.append(i)
                continue
            else:
                if stack and i == res[stack.pop()]:
                    continue
                else:
                    return False
                
        return stack == []
        
        
s = Solution()
print(s.isValid("()(){}"))