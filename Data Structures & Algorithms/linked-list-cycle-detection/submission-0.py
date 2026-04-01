# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # {} will create dict, {1, 2, 3} will create set
        ll = head
        while ll:
            if ll not in seen:
                seen.add(ll)
            else:
                return True
            ll = ll.next
        return False

        