# 1. Two Sum
# ---------------------------------------------
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in an array that add up to a given target.

        Args:
            nums: Array of numbers
            target: Target Sum
        
        Returns:
            List of indices of the two numbers
        """
        l = len(nums)
        for i in range(0,l):
            for j in range(0,l):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return i,j

## Check Solution
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    output = [0,1]
    print("Output :", Solution().twoSum(nums,target))
    print("Solution :", output)
