# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        carry = 0
        res = ListNode()
        curr = res
        while n1 or n2 or carry:
            a = n1.val if n1 else 0
            b = n2.val if n2 else 0
            sum = a+b+carry
            carry = sum // 10
            val = sum % 10
            curr.next = ListNode(val)
            curr = curr.next
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        return res.next

