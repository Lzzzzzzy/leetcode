#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
import re

# 思路:正则表达式
class Solution:
    MAX_INT = 2**31 - 1
    MIN_INT = -(2**31)

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(s)
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num, self.MAX_INT), self.MIN_INT)


# @lc code=end
