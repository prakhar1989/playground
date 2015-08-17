class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in cache:
                return [cache[x], i + 1]
            cache[target-x] = i + 1
        return results


s = Solution()
print s.twoSum([2, 11, 7, 15], 9)
print s.twoSum([3, 2, 4], 6)
