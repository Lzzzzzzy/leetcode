#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start

# 思路: 两两比较
# runtime beats 56.67 %, memory usage beats 85.3 %
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        # 如果是空数组,直接返回空
        if not strs:
            return prefix
        # 如果数组只有一个字符串,返回
        if len(strs) == 1:
            return strs[0]
        
        # 以第0个元素作为基础
        prefix = strs[0]
        
        # 从第1个元素开始遍历,两个指针分别指向prefix和该元素,比较字符串中的字母是否相等
        for s in strs[1:]:
            for i in range(len(prefix)):
                # 如果遍历到元素末尾或不同字母时,截取prefix,跳出循环
                if i == len(s) or s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            # 如果prefix已经为空,则直接返回
            if not prefix:
                return prefix
        return prefix


# leetcode上看到的python专属骚套路:
# zip函数: 将对象中对应的元素打包成tuples，然后返回由这些tuples组成的list。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for l in zip(*strs):
            if len(set(l)) == 1:
                prefix += l[0]
            else:
                break
        return prefix

# @lc code=end

