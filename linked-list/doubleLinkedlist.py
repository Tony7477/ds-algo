class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head is None:
            new_node=Node(data)
            new_node.prev=None
            self.head=new_node
            return

        itr=self.head
        new_node=Node(data)
        while itr:
            itr=itr.next
        new_node.prev=itr
        itr.next=new_node
        new_node.next=None
        
        
            
        
        
        
