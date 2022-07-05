#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 遍历整颗树
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.ret = True
        self.isSame(root.left, root.right)
        return self.ret

    def isSame(self, node1, node2):
        if not node1 and not node2:
            return
        if not node1 or not node2:
            self.ret = False
            return
        if node1.val != node2.val:
            self.ret = False
            return
        self.isSame(node1.left, node2.right)
        self.isSame(node1.right, node2.left)


# @lc code=end
