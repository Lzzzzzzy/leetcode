#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start

# 思路: 小数在大数前面就做减法,否则做加法
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
            }
        ret = 0
        for i in range(len(s)):
            num = roman_map[s[i]]
            if i+1 == len(s) or num >= roman_map[s[i+1]]:
                ret += num
            else:
                ret -= num
        return ret
# @lc code=end

