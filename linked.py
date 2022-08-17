#To do 
#Add element to head
#Add element to tail
#Delete element
#Print elements
#Reverse the linked list
import math
import random
class SinglyLinkedListNode:
    def __init__(self,node_data):
        self.data=node_data
        self.next=None

class  SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert_node(self,data):
        x=SinglyLinkedListNode(data)
        if self.head==None:
            self.head=x
        else:
            self.tail.next=x
        self.tail=x
        
    def print_list(self):
        z=self.head
        while z.next !=None:
            print(z.data,end=' ')
            z=z.next
        print(z.data)
        
    def insert_head(self,data):
        x=SinglyLinkedListNode(data)
        x.next=self.head
        self.head=x
    
    def insert_tail(self,data):
        x=SinglyLinkedListNode(data)
        z=self.head
        while z.next!=None:
            z=z.next
        z.next=x
    
    def delete(self,position):
        z=self.head
        for i in range(position-1):
            z=z.next
        z.next=z.next.next
        
    def reverse(self):
        z=self.head
        nxt = None
        while z:
            temp=z.next
            z.next=nxt
            nxt=z
            z=temp

if __name__ == '__main__':
    llist=SinglyLinkedList()
    n=int(input())
    for i in range(n):
        data=int(input())
        llist.insert_node(data)
    llist.insert_head(3)
    llist.insert_tail(5)
    llist.insert_tail(4)
    llist.print_list()
    llist.delete(3)
    llist.print_list()
    llist.reverse()
    llist.print_list()
