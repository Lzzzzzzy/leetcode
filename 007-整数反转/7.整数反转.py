#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
import math

# @lc code=start

# 思路: 用给定的数取模得到个位数,ret依次*10+个位数实现翻转
# runtime beats 93.9 %, memory beats 92.94 %
class Solution:
    MAX_INT = 2**31 - 1
    MIN_INT = -(2**31)

    def is_int32(self, x: int) -> bool:
        try:
            return x >= self.MIN_INT and x < self.MAX_INT
        except:
            return False

    def reverse(self, x: int) -> int:
        ret = 0
        minus = x < 0

        x = abs(x)
        while x > 0:
            last_num = x % 10
            ret = ret * 10 + last_num
            x = math.floor(x / 10)
        ret = ret * -1 if minus else ret
        return ret if self.is_int32(ret) else 0


# @lc code=end
