#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start

# 思路: 回溯算法:用一个tmp保存临时结果,每次循环时将tmp和下一个列表组合,即每次都是2个数组组合
# 当遍历到letters最后一个数组的时候,记录最终结果
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letters_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        if len(digits) == 1:
            return num_letters_map[digits]
        letters = []
        for d in digits:
            letters.append(num_letters_map[d])
        # 记录最终结果
        ret = []
        # 临时结果
        tmp = letters[0]
        for i in range(1, len(letters)):
            l = tmp
            r = letters[i]
            # 每次循环时清空
            tmp = []
            # 数组两两组合
            for m in l:
                for n in r:
                    s = m+n
                    # 遍历到最后一个数组时放入最终结果
                    if i == len(letters)-1:
                        ret.append(s)
                    else:
                        tmp.append(s)
        return ret


# leetcode思路: 使用队列,将各数字对应元素依次入队,出队时依次和队列内的元素组合重新入队
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letters_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        # 初始化队列
        queued = [""]
        for d in digits:
            for _ in range(len(queued)):
                tmp = queued.pop(0)
                for letter in num_letters_map[d]:
                    s = tmp+letter
                    queued.append(s)
        return queued
# @lc code=end

