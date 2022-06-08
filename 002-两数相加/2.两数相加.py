#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# [2,4,3][5,6,4]
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 思路: 遍历l1和l2各node,对应node的数字相加,如果相加结果>9,则出现一个进位.在下次相加时需要加上进位1
# 用列表(result)记录各节点,加完之后在最后一个节点(result[-1])的next上加上新增的节点
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        has_carry = 0
        result = []
        while l1 or l2:
            if l1:
                l1_num = l1.val
                l1 = l1.next
            else:
                l1_num = 0
            if l2:
                l2_num = l2.val
                l2 = l2.next
            else:
                l2_num = 0
            sum = l1_num + l2_num + has_carry
            has_carry = 0
            if sum > 9:
                sum = int(str(sum)[-1])
                has_carry = 1
            node = ListNode(val=sum)
            if result:
                last_node = result[-1]
                last_node.next = node
            result.append(node)

        if has_carry:
            node = ListNode(val=has_carry)
            last_node = result[-1] if result else None
            if last_node:
                last_node.next = node
        return result[0]


# @lc code=end
