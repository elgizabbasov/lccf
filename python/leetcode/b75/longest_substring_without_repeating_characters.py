class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Start a pointer in the middle of string, current longest count is 1
        # Compare the left and right letters with itself (middle)
            # if left equals to you:
                # move yourself to the left, add old count to list and reset the count to 1
            # else:
                # add one to the count, and go 1 more left 
            # if right equals to you:
                # move yourself to right, add old count to list and reset count to 1
            # else:
                #
        # Return maximum of lengths in the list
        
        
        
        ### Below Doesnt work
        l = []
        t = 1
        
        if s == "": return 0


        return max(l)
    
s = Solution()
print(s.lengthOfLongestSubstring("pofpdopfdopfo"))