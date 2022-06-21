#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start

# 15和16题思路相似,都采用排序+双指针算法
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ret = None
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sums = nums[i] + nums[l] + nums[r]
                diff = sums-target
                if ret is None or abs(diff) < abs(ret-target):
                    ret = sums
                if diff == 0:
                    return sums
                if diff > 0:
                    r -= 1
                else:
                    l += 1
        return ret

# @lc code=end

