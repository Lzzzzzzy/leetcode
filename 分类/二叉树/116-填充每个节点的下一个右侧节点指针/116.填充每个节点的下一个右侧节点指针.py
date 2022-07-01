#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, left, right):
        if not left or not right:
            return
        left.next = right
        self.traverse(left.left, left.right)
        self.traverse(left.right, right.left)
        self.traverse(right.left, right.right)


# @lc code=end
