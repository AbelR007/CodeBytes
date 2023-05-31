# 1. Two Sum
# Problem
"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
"""

# Solution
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
                # print(i,j,nums[i]+nums[j] == target)
                if nums[i] + nums[j] == target:
                    return i,j

# Check Solution
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    output = (0,1)
    my_output=  Solution().twoSum(nums, target)
    print(my_output == output)
    print("My Output : ", my_output)
    print("Solution Output : ", output)

# Time Complexity : O(n2)
# Space Complexity : O(1)
