#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路: 增加一个虚拟的头,以便头指针被删除之后无法找到head.因为要删除倒数第n个节点,而且采用一次循环,那么考虑双指针
# 先分别使两个指针指向虚拟头节点,让右边的指针和左边的指针相差n,那么当右边的指针指向链表尾部时,要删除的节点就是左边指针的next节点
# 例如: [1,2,3,4,5] 2,则要删除的节点为4.使左右指针相差2时,当右边指针指向5的时候,左边指针指向3,要删除的也就是3的next节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l, r = 0, 0
        # 虚拟头节点
        empty_head = ListNode(0, head)
        ln, rn = empty_head, empty_head
        # 移动右指针,使左右相差N
        while r-l<n:
            r += 1
            rn = rn.next
        # 当左右相差n时,则一起移动,直到右指针指向链表尾节点
        while r-l == n and rn.next:
            l+=1
            r+=1
            ln = ln.next
            rn = rn.next
        # 删除链表节点,即让next节点指向next.next
        ln.next = ln.next.next
        # 返回链表头
        return empty_head.next

# @lc code=end

