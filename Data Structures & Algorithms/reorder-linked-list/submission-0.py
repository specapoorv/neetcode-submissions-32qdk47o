# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #print("mid", slow.val)
        second = slow.next
        slow.next = None
        #now slow is at mid so we reverse the list after slow then we will have to half and we will merge them 
        #3 -> 4 -> 5 , go to 3, store 4, change pointer of 3, move both prev and curr forward

        prev = None
        curr = second
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        left = head
        right = prev
        while right:
            next_l = left.next
            next_r = right.next
            left.next = right
            right.next = next_l

            left = next_l
            right = next_r
            
        return 
    
array = [1,2,3,4,5]
listnode = [ListNode(i) for i in array]
for i, node in enumerate(listnode):
    if i == len(listnode) - 1:
        node.next = None
    else:
        node.next = listnode[i+1]

sol = Solution()
sol.reorderList(head = listnode[0])

head = listnode[0]
while head:
    print(head.val)
    head = head.next