#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self) -> None:
        self.dp_map = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 1:
            if amount % coins[0] != 0:
                return -1
            return int(amount / coins[0])
        if self.dp_map.get(amount):
            return self.dp_map.get(amount)
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = amount + 1
        for coin in coins:
            sub_problem = self.coinChange(coins, amount - coin)
            if sub_problem == -1:
                continue
            res = min(res, sub_problem + 1)
        ret = -1 if res == amount + 1 else res
        self.dp_map[amount] = ret
        return ret


# @lc code=end
