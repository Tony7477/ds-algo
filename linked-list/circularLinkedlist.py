class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        

class CircularLinkedlist:
    def __init__(self):
        self.head=None
        
    
    def insert_end(self,data):
     
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
            return
        itr=self.head
        while itr.next:
            
            if itr.next==self.head:
                break
            itr=itr.next
        itr.next=Node(data,self.head)
        
                 
            
           
           
        
        
    
    def print(self):
        itr=self.head
        while itr.next:
            print(str(itr.data)+"-->")
            if itr.next==self.head:
                break
                print(str(itr.data)+"-->")
                itr=itr.next
            


            
    
    
    

if __name__=='__main__':
    cl=CircularLinkedlist()
    cl.insert_end(2)
    cl.insert_end(3)
    cl.print()




