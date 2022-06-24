#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


# 思路: 回溯法,剪枝
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(l, r, s):
            if l > n or r > n:
                return
            if l == r == n:
                ret.append(s)
            if l < r:
                return
            dfs(l+1, r, s+"(")
            dfs(l, r+1, s+")")
        dfs(0, 0, "")
        return ret


# @lc code=end

