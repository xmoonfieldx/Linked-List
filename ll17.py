class SinglyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        x=SinglyLinkedListNode(data)
        if self.head==None:
            self.head=x
        else:
            self.tail.next=x
        self.tail=x
        
    #1 Print elements of linked list
    def prints(self):
        x=self.head
        while x.next!=None:
            print(x.data,end=" ")
            x=x.next
        print(x.data)
        
    #2 Insert a node at the tail of a linked list
    def itail(self,data):
        z=SinglyLinkedListNode(data)
        #Alternate Method
        #x=self.head
        #while x.next!=None:
            #x=x.next
        #x.next=z
        self.tail.next=z
        self.tail=z
        
    #3 Insert a node at the head of a linked list
    def ihead(self,data):
        z=SinglyLinkedListNode(data)  
        z.next=self.head
        self.head=z
    
    #4 Insert a node at specific position of a linked list
    def imid(self,data,pos):
        z=SinglyLinkedListNode(data)
        x=self.head
        if pos==0:
            z.next=self.head
            self.head=z
        else:
            for i in range(pos-1):
                x=x.next
            z.next=x.next
            x.next=z
    
    #5 Delete a node
    def delete(self,data):
        x=self.head
        if x.data==data:
            self.head=x.next
        while x.next.data!=data:
            x=x.next
        x.next=x.next.next

#6 Reverse a linked list
def rev(llist):
    nxt=None
    while llist:
        tmp=llist.next
        llist.next=nxt
        nxt=llist
        llist=tmp
    return nxt
def printsf(llist):
    while llist.next!=None:
        print(llist.data,end=" ")
        llist=llist.next
    print(llist.data)
    
#7 Compare 2 linked lists
def compare(llist1,llist2):
    while llist1.next!=None and llist2.next!=None:
        if llist1.next==None:
            return 0
        if llist2.next==None:
            return 0
        if llist1.data!=llist2.data:
            return 0
        llist1=llist1.next
        llist2=llist2.next
    if llist1.data!=llist2.data:
        return 0
    return 1
    
if __name__ == "__main__":
    llist = SinglyLinkedList()
    for i in range(10):
        llist.insert(i)
    print("Print elements of linked list")
    llist.prints()
    print("Insert a node at the tail of a linked list")
    llist.itail(10)
    llist.prints()
    print("Insert a node at the head of a linked list")
    llist.ihead(11)
    llist.prints()
    print("Insert a node at specific position of a linked list")
    llist.imid(12,1)
    llist.prints()
    print("Delete a node")
    llist.delete(12)
    llist.prints()
    print("Reverse a linked list")
    llist1=rev(llist.head)
    printsf(llist1)
    print("Compare 2 linked lists")
    print(compare(llist.head,llist1))
    
    
