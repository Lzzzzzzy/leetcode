#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start

# 思路1: 把数字转为字符串,双指针分别从头尾开始遍历,相遇时如果数字都一样,则为回文数
# 时间复杂度: O(n/2)
# runtime beats 62.7 %, memory usage beats 49.08 %
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 10 and x >= 0:
            return True
        x = str(x)
        i, j = 0, len(x)-1
        while j > i:
            if x[j] != x[i]:
                return False
            j -= 1
            i += 1
        return True

# 思路2: 题目要求不将数字变为字符串,则可以使用整数翻转的方式,如果翻转前和翻转后的数相等,则为回文数
# runtime beats 62.7 %, memory usage beats 22.6 %
from copy import deepcopy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        ret = 0
        num = deepcopy(x)
        while num > 0:
            n = num % 10
            num = num // 10
            ret = ret * 10 + n
        if ret == x:
            return True
        return False
# @lc code=end

