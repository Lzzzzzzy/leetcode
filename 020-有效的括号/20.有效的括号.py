#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
# 思路:用栈来判断括号是否成对
# 时间复杂度:O(n)
# runtime beats 99.78 %, memory usage beats 71.5 %
class Solution:
    def isValid(self, s: str) -> bool:
        # 如果str的长度为奇数,则必定不成对
        if len(s) % 2 == 1:
            return False
        symbol_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i not in symbol_map:
                stack.append(i)
            else:
                # 如果有右括号,但栈内没有元素,则不成对
                if not stack:
                    return False
                value = stack.pop()
                # 判断括号是否闭合
                if value != symbol_map[i]:
                    return False
        # 如果循环完后栈内依然有元素,则不成对
        if stack:
            return False
        return True

# @lc code=end

