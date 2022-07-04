#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路: 遍历整棵树(前序遍历)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.ret = True
        self.traverse(p, q)
        return self.ret

    def traverse(self, node1, node2):
        if not node1 and not node2:
            return
        if not node1 or not node2:
            self.ret = False
            return
        if node1.val != node2.val:
            self.ret = False
            return
        self.traverse(node1.left, node2.left)
        self.traverse(node1.right, node2.right)


# @lc code=end
