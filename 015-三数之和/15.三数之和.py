#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

# 思路: 对列表排序,列表有序后更容易排除重复解.遍历列表,双指针遍历指定元素后的切片,找到三数之和为0的所有组合
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        i = 0
        rets = []
        for i in range(len(nums)):
            # 排除重复解
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    rets.append([nums[i], nums[l], nums[r]])
                    # 排除左右边界的重复解
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return rets

# @lc code=end

