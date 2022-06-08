#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

# 思路: 滑动窗口法.假定左边框和右边框的起始位置都为0.要找到最长子串,需要右边框尽量靠近尾部,左边框尽量靠近头部.
# 由于题目规定是无重复字符,使用一个set记录窗口内已有的字符.
# 循环移动右边框,每移动一次对比一下是否有重复字符.如果没有重复字符,则继续右移,否则需要右移左边框,直到窗口内没有重复字符.
# 每当找到重复字符时,需要对比记录一下最大长度.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_len = 0
        l, r = 0, 0
        sub = set()
        while r < len(s):
            while s[r] in sub:
                max_len = max(r - l, max_len)
                sub.remove(s[l])
                l += 1

            sub.add(s[r])
            r += 1
        max_len = max(r - l, max_len)
        return max_len


# @lc code=end
