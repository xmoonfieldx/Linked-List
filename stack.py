class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        print("Pushing:",data)
        x=node(data)
        if self.top!=None:
            x.next=self.top
        self.top=x
    
    def pop(self):
        if self.top==None:
            print("Stack underflow")
            return 
        else:
            x=self.top.data
            self.top=self.top.next
            print("Popped:",x)
    
    def peak(self):
        print("Top element",self.top.data)
    
    def view(self):
        x=self.top
        while x.next!=None:
            print(x.data,end=" ")
            x=x.next
        print(x.data)
if __name__ == "__main__":
    s=stack()
    for i in range(1,11):
        s.push(i)
    s.pop()
    s.peak()
    s.view()
        
        
