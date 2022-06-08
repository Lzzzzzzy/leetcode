#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start

# 思路: 每行就是一个字符串,通过direct控制上下的方向.
# 遍历字符串,逐行向上/向下将遍历的字符顺序放到该行的字符串末尾.如果向下到了最后一行或者向上到了第一行,则翻转方向.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        l = ["" for _ in range(numRows)]
        direct = True
        cur_row = 0
        for i in range(len(s)):
            l[cur_row] += s[i]
            if direct:
                cur_row += 1
            else:
                cur_row -= 1
            if cur_row == numRows - 1 or cur_row == 0:
                direct = not direct

        ret = "".join(l)
        return ret


# @lc code=end
