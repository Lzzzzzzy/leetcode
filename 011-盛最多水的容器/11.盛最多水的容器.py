#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
# 盛水最多=围成的面积最大,面积=底*高,高由最短的边决定. 
# 思路1: 暴力枚举法,双指针遍历
# 时间复杂度O(n^2)
# 结果: Time Limit Exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                current_area = w * h
                area = current_area if current_area > area else area
        return area


# 思路2: 双指针,指向数组两边.依次向内移动短边,直到双指针相遇.
# 时间复杂度: O(n)
# 结果: runtime beats 75.52 %, memory usage beats 69.19 %
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0
        while j > i:
            h = min(height[i], height[j])
            current_area = (j - i) * h
            if current_area > area:
                area = current_area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area

# @lc code=end

