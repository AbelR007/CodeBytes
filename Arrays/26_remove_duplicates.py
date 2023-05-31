# 26. Remove Duplicates on Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Solution
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = set(nums)
        k = len(m)
        x = list(m)
        for i in range(len(nums) - len(x)):
            x.append('_')
        return k, x

# Check Solution
if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    output = [0,1,2,3,4,'_','_','_','_','_']
    k = Solution().removeDuplicates(nums)
    print(k)
    print(k == output)

# Time Complexity: O(n)