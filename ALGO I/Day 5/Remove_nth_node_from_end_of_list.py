# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp!=None:
            length+=1
            temp=temp.next
        if length==n:
            return head.next
        target=length-n
        i=1
        res=head
        temp=head.next
        while temp:
            if i==target:
                res.next=temp.next
            res=res.next
            temp=temp.next
            i+=1
        return head