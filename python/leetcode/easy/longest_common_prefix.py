class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # Time: O(n)
        # Space: O(n)
        
        prefix=[]
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
        return "".join(prefix)
    
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))

        
            
            
                
    