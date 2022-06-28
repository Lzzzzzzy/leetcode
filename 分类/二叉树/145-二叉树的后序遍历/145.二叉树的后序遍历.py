#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路1: 遍历整颗树
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        self.traverse(root)
        return self.ret

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.ret.append(root.val)


# 思路2: 分解子树
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        ret.extend(left)
        ret.extend(right)
        ret.append(root.val)
        return ret


# @lc code=end
