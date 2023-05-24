# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples
Input: `nums = [2,7,11,15], target = 9`<br>
Output: `[0,1]`<br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

### Constraints

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

--- 
## Solution

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0,l):
            for j in range(0,l):
                if i == j:
                    continue
                # print(i,j,nums[i]+nums[j] == target)
                if nums[i] + nums[j] == target:
                    return i,j
```

### Explanation

Not added yet

---
### With ❤️ by Abel Roy.