#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from copy import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        used = [False for _ in nums]
        self.backref(nums, used, [])
        return self.ret

    def backref(self, nums, used, track):
        if len(track) == len(nums):
            res = copy(track)
            self.ret.append(res)
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            track.append(nums[i])
            used[i] = True
            self.backref(nums, used, track)
            used[i] = False
            track.remove(nums[i])
        return


# @lc code=end
