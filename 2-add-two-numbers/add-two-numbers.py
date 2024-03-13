# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = l1, l2
        newNode = ListNode()
        temp = newNode
        carry = 0
        while temp1 or temp2 :
            t = ListNode()
            if temp1 is None:
                value = temp2.val + carry 
                temp2 = temp2.next 
            elif temp2 is None:
                value = temp1.val + carry
                temp1 = temp1.next
            else:
                value = temp1.val + temp2.val + carry
                temp1 = temp1.next
                temp2 = temp2.next
            if value>=10:
                carry = value//10
                value = value%10
            else:
                carry = 0  
            t.val = value    
            temp.next = t
            temp = t 
        if carry:
            t = ListNode()
            t.val = carry
            temp.next = t
        return newNode.next