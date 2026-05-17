# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        h = head
        count = 0

        while h:
            count += 1
            h = h.next

        print(count)

        if n == count:
            return head.next

        toRemove = count - n - 1

        h = head

        for i in range(toRemove):
            h = h.next
        
        if h:
            if h.next:
                h.next = h.next.next
                return head
        return None

        