import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for each letter in s check if left and right chars are equal, 
        # go left and right, until the length of string finishes or chars not eq,
        # grab the length, 
        # choose the string with the highest length
        
        # Time: O(n^2)
        # Space: O(1)
        
        start = 0
        end = 0
        if len(s) == 0: return ""
        
        for i in range(len(s)):
            len1 = self.startFromMid(s, i, i)
            len2 = self.startFromMid(s, i, i+1)
            flen = max(len1, len2)
            
            if flen > end - start:
                start = math.ceil(i - (flen-1)/2)
                end = math.floor(i + flen/2)
        
        return s[start:end+1]
            
            
    def startFromMid(self, s: str, i: int, j: int):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return j-i-1

s = Solution()        
print(s.longestPalindrome("cbbd"))