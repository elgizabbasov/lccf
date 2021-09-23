class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        L = 0
        output = 0
        strs = {}
        if len(s) == 0: return 0
        
        for r in range(len(s)):
            if s[r] in strs:
                if strs[s[r]] < L: output = max(output, r-L+1)
                else: L = strs[s[r]] + 1
            else: output = max(output, r-L+1)
            
            strs[s[r]] = r
            
        return output
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("abcabcbb"))
