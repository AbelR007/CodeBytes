# 58. Length of Last Word
# ====================================

## Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        val = 0
        flag = False
        for i in range(1,l+1):
            if s[-i].isalpha() is True:
                flag = True
            if flag == True:
                if s[-i].isspace() is True:
                    break
                val+=1
        return val

## Check Solution [Not needed]
if __name__ == '__main__':
    s = "Hello World"
    output = 5
    print("Output :", Solution().lengthOfLastWord(s))
    print("Solution :", output)
