# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=ListNode(next=head)
        slow,fast=head,head
        a=0
        while fast:
            if slow.val!=fast.val:
                slow.next=fast
                slow=fast      
            fast=fast.next
            if not fast:
                slow.next=fast
        return q.next        
        