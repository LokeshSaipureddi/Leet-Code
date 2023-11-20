# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        temp1=ListNode(next=head)
        prev=temp1
        while temp:
            if temp.val==val:
                nxt=temp.next
                prev.next=nxt
                temp.next=None
                temp=nxt    
            else:        
                prev=temp
                temp=temp.next
        return temp1.next       