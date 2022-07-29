# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        temp1=head
        temp2=temp1.next
        while temp2:
            temp1.val,temp2.val=temp2.val,temp1.val
            if temp2.next==None:
                break
            temp1,temp2=temp1.next.next,temp2.next.next
        return head