class Solution:
    def twoSum(self, nums, target: int):
        res = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
        
        
s = Solution()
print(s.twoSum([56,4,3645,5646,2],
5648))
