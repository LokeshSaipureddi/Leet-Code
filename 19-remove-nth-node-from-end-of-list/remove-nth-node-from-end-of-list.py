# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        temp = head
        while temp:
            leng  = leng + 1
            temp = temp.next
        n = leng - n
        if n==0:
            return head.next
        dummy = ListNode(0,head)
        curr = dummy
        k = 0
        while curr:
            if k == n:
                temp = curr.next
                curr.next = temp.next
                temp.next = None
            k = k + 1
            curr = curr.next  
        return dummy.next      