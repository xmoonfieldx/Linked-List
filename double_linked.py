class SinglyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        
    def print(self):
        z=self.head
        while z.next!=None:
            print(z.data,end=' ')
            z=z.next
        print(z.data)
    
    def rev(self):
        tail = self.head
        n=1
        while (tail.next != None):
            tail = tail.next
            n+=1
        for i in range(n):
            print(tail.data)
            tail=tail.prev
            
    def insert(self,data):
        x=SinglyLinkedListNode(data)
        if self.head==None:
            self.head=x
        else:
            z=self.head
            while z.next!=None:
                z=z.next
            z.next=x
            x.prev=z
        self.head.prev=x
        
if __name__ == "__main__":
    llist = SinglyLinkedList()
    k=['Alpha','Charlie','Bravo','Echo','Foxtrot','Zulu','Delta']
    for i in range(len(k)):
        llist.insert(k[i])
    llist.print()
    llist.rev()
