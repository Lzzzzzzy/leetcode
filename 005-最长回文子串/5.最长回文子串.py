#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start

# 思路: 遍历字符串中所有字符,向两边延伸,找到最长回文子串即可
# 注意: 奇数回文和偶数回文不同,需要分开处理
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        palindrome = ""
        for i in range(len(s)):
            # 奇数回文
            l, r = i, i
            while s[l] == s[r]:
                l -= 1
                r += 1
                if l < 0 or r > len(s) - 1:
                    break
            if r - l - 1 > len(palindrome):
                palindrome = s[l + 1 : r]

            # 偶数回文
            l, r = i - 1, i
            while s[l] == s[r]:
                l -= 1
                r += 1
                if l < 0 or r > len(s) - 1:
                    break
            if r - l - 1 > len(palindrome):
                palindrome = s[l + 1 : r]

        return palindrome


# @lc code=end
