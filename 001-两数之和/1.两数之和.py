#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

# 思路: 遍历nums列表,通过找到target - 当前数字 的方法找到需要的另一个数字.
# 每遍历一个数字时,放入map中.遍历的过程中从map中取另一个数字的index,时间复杂度为O(1).
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        num_map = {}
        while i < len(nums):
            remain_num = target - nums[i]
            if remain_num in num_map.keys():
                remain_num_index = num_map.get(remain_num)
                return [i, remain_num_index]
            num_map[nums[i]] = i
            i += 1


# @lc code=end
