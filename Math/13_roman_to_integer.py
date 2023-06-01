# 13. Roman to Integer
# =================================

## Solution
def func(i):
    if i == "M":
        val = 1000
    elif i == "D":
        val = 500
    elif i == "C":
        val = 100
    elif i == "L":
        val = 50
    elif i == "X":
        val = 10
    elif i == "V":
        val = 5
    elif i == "I":
        val = 1
    else:
        return 0
    return val

class Solution:

    def romanToInt(self, s: str) -> int:
        val = 0
        order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        for i in range(len(s)):
            indx = order.index(s[i])
            if i == 0:
                val += func(s[i])
                continue

            prev_indx = order.index(s[i-1])
            if prev_indx >= indx:
                val += func(s[i])
            else:
                new_val = func(s[i]) - func(s[i-1])
                val += (new_val - func(s[i-1]))
        return val

## Check Solution
if __name__ == '__main__':
    s = "MCMXCIV"
    output = 1994
    print("Output :", Solution().romanToInt(s))
    print("Solution :", output)
