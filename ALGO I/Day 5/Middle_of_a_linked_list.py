# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        index=n//2
        i=0
        res=head
        while res:
            if i==index:
                return res
            res=res.next
            i+=1