def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        INT_MAX = sys.maxsize
        temp=head
        
        while temp:
            if temp.val == INT_MAX:
                return temp
            temp.val = INT_MAX
            temp = temp.next
        
        return None