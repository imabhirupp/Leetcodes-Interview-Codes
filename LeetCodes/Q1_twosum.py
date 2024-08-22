# Brute Force Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # nums[i] is the num1
            for j in range(i + 1, len(nums)): # nums[j] is the num2
                if nums[i] + nums[j] == target:
                    return [i, j]
