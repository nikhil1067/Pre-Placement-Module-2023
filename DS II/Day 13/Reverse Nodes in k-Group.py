class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start,end = None,None
        if head:
            start = head
            end = head
            #To store the last node of the previous reversed batch
            lastBatch = ListNode(-1,None) 
        else:
            return head

        newHead = None

        while True:
            #Pivot end pointer to the last node of the set to be reversed
            i = 1
            while i < k and end:
                end = end.next
                i += 1

            #If there isn't enough nodes left, break
            if not end:
                break

            #If this is the new head of the first reversed set, make it the head
            if not newHead:
                newHead = end

            #Set the node after the last node as None for reverse purpose
            nextStart = end.next
            end.next = None

            prv = lastBatch
            cur = start
            while cur:
                tmp = cur.next
                cur.next = prv
                prv = cur
                cur = tmp

            #Reconnect and resetting everything
            lastBatch.next = prv #Connect last node of prev batch to first node of cur batch
            lastBatch = start #Make "last node of prev batch" the last node of cur batch
            start.next = nextStart #Connect last node of cur batch to next batch
            start,end = nextStart,nextStart #Reset start/end nodes for next batch

        return newHead