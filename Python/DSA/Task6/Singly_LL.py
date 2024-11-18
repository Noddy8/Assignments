class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Singly:
    def __init__(self,head=None):
        self.head=head

    def print(self):
        if self.head is None:
            print('LIST IS EMPTY')
            return
        itr= self.head
        llstr=''
        while itr:
            llstr+=str(itr.data) + '-->'
            itr=itr.next
        print(llstr)

    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)

    def insert_at(self,index,data):
        if index<0 or index> self.get_len():
            raise Exception("INVALID INDEX")
        
        if index==0:
            self.insert_at_beg(data)
            return
    
        count=0
        itr=self.head
        while itr:
            if count==index -1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def remove_at_end(self):
        if self.head is None:
            print('LIST IS EMPTY')

        else:
            pass


    def remove_at(self,index):
        if index<0 or index> self.get_len():
            raise Exception("INVALID INDEX")
        
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1


if __name__=='__main__':
    sll=Singly()
    sll.insert_values([12,'Two',91,'end'])
    sll.print()
    sll.insert_at_beg(5)
    sll.print()
    sll.insert_at(1,3)
    sll.print()
    sll.remove_at(7)
    sll.print()