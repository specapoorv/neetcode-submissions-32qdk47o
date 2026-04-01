class Solution:
    def reverseKGroup(self, head, k):
        fast, slow = head, head
        last_slow = None

        while fast:
            count = 0
            temp = fast

            # check if k nodes exist
            for _ in range(k):
                if temp is None:
                    break
                temp = temp.next
                count += 1

            if count == k:
                fast = temp
                new_head = self.reverse(slow, fast)

                # connect previous part
                if last_slow:
                    last_slow.next = new_head
                else:
                    head = new_head

                # connect tail to next part
                slow.next = fast

                # move pointers
                last_slow = slow
                slow = fast
            else:
                if last_slow:
                    last_slow.next = slow
                break

        return head

    def reverse(self, head, stop):
        prev = None
        curr = head

        while curr != stop:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev