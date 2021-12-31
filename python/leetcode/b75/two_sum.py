from typing import List
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ################################################################
        # Runtime: 56 ms, faster than 90.33% of Python3 online submissions for Two Sum.
        # Memory Usage: 15.3 MB, less than 41.28% of Python3 online submissions for Two Sum.
        ################################################################
        ### Brute Force: O(n^2)
        
        
        # Time: O(n)
        # Space: O(n)
        res = {} 
            
        for i, j in enumerate(nums):
            m = target - j
            
            if m in res:
                return [res[m], i]
            else:
                res[j] = i
    
s = Solution()
print(s.twoSum([2,7,11,15], 9))