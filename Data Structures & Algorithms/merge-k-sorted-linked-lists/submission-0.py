# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            dummy = ListNode()
            curr = dummy
            ll1 =  lists[0]
            ll2 = lists[1]
            while ll1 and ll2:
                if ll1.val < ll2.val:
                    curr.next = ll1
                    ll1 = ll1.next
                else:
                    curr.next = ll2
                    ll2 = ll2.next
                curr = curr.next
            
            curr.next = ll1 if ll1 else ll2
            
            lists.pop(0)
            lists.pop(0)
            lists.append(dummy.next)
        
        return lists[0]
            
    




        