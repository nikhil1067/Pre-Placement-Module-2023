class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:

    def __init__(self):
        self.head=None
        
    def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def insertAtEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while (last.next):
            last=last.next
        last.next=new_node

    def deleteNode(self,position):
        if self.head is None:
            return
        temp=self.head
        if position==0:
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
        
    def printList(self):
        temp=self.head
        while temp:
            print(str(temp.data)+" ",end="")
            temp=temp.next
            
ll=linkedlist()
ll.insertAtEnd(1)
ll.insertAtBeginning(2)
ll.insertAtBeginning(3)
ll.insertAtEnd(4)
ll.insertAfter(ll.head.next, 5)
print("Linked List:")
ll.printList()
ll.deleteNode(3)
print("\nAfter deleting an element:")
ll.printList()



Result: 	Linked List:
		3 2 5 1 4 
		After deleting an element:
		3 2 5 4 