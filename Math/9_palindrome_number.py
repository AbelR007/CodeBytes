# 9. Palindrome Number
# =====================================

## Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

## Check Solution
if __name__ == '__main__':
    x = 121
    output = True
    print("Output :", Solution().isPalindrome(x))
    print("Solution :", output)

