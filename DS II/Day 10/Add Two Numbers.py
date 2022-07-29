# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        res=ListNode()
        curr3=res
        carry=0
        while curr1 or curr2 or carry:
            curr3.next=ListNode()
            curr3=curr3.next
            if curr1:
                val1=curr1.val
            else:
                val1=0
            if curr2:
                val2=curr2.val
            else:
                val2=0
            carry,data=divmod(val1+val2+carry,10)
            curr3.val=data
            if curr1:
                curr1=curr1.next
            else:
                curr1=None
            if curr2:
                curr2=curr2.next
            else:
                curr2=None
        return res.next