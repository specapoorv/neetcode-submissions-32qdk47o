class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        l, r = list1, list2

        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            
            curr = curr.next

        # Attach remaining
        curr.next = l if l else r

        return dummy.next