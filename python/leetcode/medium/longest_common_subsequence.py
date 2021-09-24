import math
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        seen1 = {}
        seen2 = {}
        seen3 = {}
        res = 0
        if len(text1)==0 or len(text2)==0: return 0
        for i in range(len(text1)):
            seen1[text1[i]] = i
            
        for j in range(len(text2)):
            seen2[text2[j]] = j
            
        for each in seen1:
            for ea in seen2:
                if each == ea:
                    i = min(seen1[each], seen2[ea])
                    seen3[each] = i

                
                
        
        return res

s = Solution()        
print(s.longestCommonSubsequence(
"psnw",
"vozsh"))