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
            merged_lists = []
            for i in range(0, len(lists), 2):
                #0 to 4, step = 2 -> 0, 2, 4
                if i==(len(lists) - 1):
                    merged = lists[i]
                else:
                    ll1, ll2 = lists[i], lists[i+1]
                    merged = self.merge2ll(ll1, ll2)
                merged_lists.append(merged)
            lists = merged_lists[:] #shallow copy 
        
        return lists[0]
    
    def merge2ll(self, ll1, ll2):
            dummy = ListNode()
            curr = dummy
            while ll1 and ll2:
                if ll1.val < ll2.val:
                    curr.next = ll1
                    ll1 = ll1.next
                else:
                    curr.next = ll2
                    ll2 = ll2.next
                curr = curr.next
            
            curr.next = ll1 if ll1 else ll2

            return dummy.next