class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        a = head
        b = head.next
        while b != None:
            temp = b.next
            b.next = a
            a = b
            b = temp
        head.next = None
        return a
