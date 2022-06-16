#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start

# 思路: 从大往小遍历map得到数字对应的字符串
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
            }
        ret = ""
        for k, v in roman_map.items():
            n = num // k
            ret += n*v
            num %= k
        return ret

# @lc code=end

