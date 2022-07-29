class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = [root]
                
        while len(q) > 0:
            ql = len(q)
            for i in range(ql):
                cur = q.pop(0)
                if i + 1 < ql:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
        return root