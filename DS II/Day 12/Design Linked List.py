class SNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"({__class__.__name__})(value:{self.val}, next:{self.next})"
    

class MyLinkedList:

    # use leading __ to prevent object attributes to be modified outside of the class
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def get(self, index: int) -> int:
        if not self.__index_in_range(index):
            return -1              
        node = None
        for i in range(index+1):
            if i == 0:
                node = self.__head
            else:
                node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        if self.__head:
            new_node = SNode(val, self.__head)
            self.__head = new_node
        else:
            # this is the first node of the linked list
            new_node = SNode(val, None)
            self.__head = new_node
            self.__tail = new_node
        self.__length += 1

    def addAtTail(self, val: int) -> None:
        if self.__tail:
            new_node = SNode(val, None)
            self.__tail.next = new_node
            self.__tail = new_node
            self.__length += 1
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.__index_in_range(index):
            return -1

        if index == self.__length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.__length:
            i = 1
            prev = None
            while i <= index:
                if i == 1:
                    prev = self.__head
                else:
                    prev = prev.next
                i += 1
            new_node = SNode(val, prev.next)
            prev.next = new_node
            self.__length += 1
                

    def deleteAtIndex(self, index: int) -> None:
        if not self.__index_in_range(index):
            return -1

        if self.__length == 1:
            self.__head = None
            self.__tail = None
            self.__length = 0
        else:                    
            prev = None
            for i in range(index):
                if i == 0:
                    prev = self.__head
                else:
                    prev = prev.next
            if prev is None:
                self.__head = self.__head.next
            elif prev.next.next is None:
                prev.next = None
                self.__tail = prev
            else:
                cur = prev.next
                prev.next = cur.next
                cur.next = None
            self.__length -= 1     

    # to control whether index is in the correct range, this is a private method
    def __index_in_range(self, index):
        if index < 0 or index >= self.__length:
            return False
        else:
            return True

    # for the use of built-in len() function
    def __len__(self):
        return self.__length

    # to represent the readable object 
    def __repr__(self) -> str:
        node = self.__head
        rep_str = ''
        if node:
            while node.next:
                rep_str += (str(node.val) + "->")
                node = node.next
            rep_str += str(node.val)
        return f"({__class__.__name__})([{rep_str}])"  