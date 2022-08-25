#linked list implementation
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    #insert node at begining
    def insert_node(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("empty linked list")
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
            

        itr.next=Node(data,None)
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count=count+1
            itr=itr.next
        print(count)
    def remove_node(self,index):
        if index==0:
            self.head=self.head.next
            return
       
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count=count+1
    def insert_at(self,index,data):
        if index==0:
            node=Node(data,self.head)
            self.head=node
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count=count+1
            itr=itr.next


    def insert_values(self,values):
        self.head=None
        for i in values:
            self.insert_end(i)
                
            
            
        


        
    
                
          
               
           
                
            
        
            
        
            


if __name__=='__main__':
     l1=LinkedList()
     l1.insert_node(4)
     l1.insert_node(5)
     l1.insert_end(9)
     l1.insert_end(8)
     l1.print()
     l1.remove_node(2)
     l1.print()
     l1.insert_at(2,2)
     l1.print()
  
   
    
