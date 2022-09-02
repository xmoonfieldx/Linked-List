class SinglyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def print(self):
        z=self.head
        while z.next!=None:
            print(z.data,end=' ')
            z=z.next
        print(z.data)
    
    def insert(self,data):
        x=SinglyLinkedListNode(data)
        if self.head==None:
            self.head=x
            self.tail=x
        if self.head==self.tail:
            self.head.next=x
            self.tail=x
        elif data>self.tail.data:
            self.tail.next=x
            self.tail=x
        else:
            temp=self.head
            prev=temp
            while temp.data<data:
                if temp.next==None:
                    break
                prev=temp
                temp=temp.next
            prev.next=x
            x.next=temp
            temp.tail=x
            
    def remove(self,data):
        temp=self.head
        prev=self.head
        while temp:
            if temp.data==data:
                prev.next=temp.next
            prev=temp
            temp=temp.next
        
if __name__ == "__main__":
    llist = SinglyLinkedList()
    k=['Alpha','Charlie','Bravo','Echo','Foxtrot','Zulu','Delta']
    for i in range(len(k)):
        llist.insert(k[i])
    l=input()
    llist.remove(l)
    llist.print()
