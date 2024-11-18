class Node:
    def __init__(self,value):
        self.value=value
        self.next = None

class Circular_ll:
    def __init__(self):
        self.tail=None
         
    def add_to_front(self,new_node):
        if self.empty_list():
            self.tail=new_node
            new_node.next = new_node
        else:
            new_node.next =self.tail.next
            self.tail.next=new_node
            self.tail=new_node

    def add_to_back(self,new_node):
        if self.empty_list():
            self.tail=new_node
            new_node.next = new_node
        else:
            new_node.next =self.tail.next
            self.tail.next=new_node
            self.tail =new_node

    def remove_first(self):
        if self.empty_list():
            print("Warning: List is empty")
            return

        if self.tail.next == self.tail:
            self.tail.next = None
            self.tail = None
            return
        
        first_node = self.tail.next
        second_node = first_node.next
        self.tail.next = second_node

    def remove_last(self):
        if self.empty_list():
            print("The list is empty")
            return

        if self.tail.next == self.tail:
            self.tail.next = None
            self.tail = None
            return

        last_node = self.tail
        prev_to_last_node = last_node.next
        while prev_to_last_node.next != last_node:
            prev_to_last_node = prev_to_last_node.next

        prev_to_last_node.next = last_node.next
        self.tail = prev_to_last_node
        last_node.next = None 
    
    def empty_list(self):
        return not self.tail

    def __str__(self):
        if self.empty_list():
            return "Empty List"
        current = self.tail.next
        nodes = []
        while current != self.tail:
            nodes.append(str(current.value))
            current = current.next
        nodes.append(str(current.value))
        return "->".join(nodes)

if __name__ == '__main__':
    cll=Circular_ll()
    cll.add_to_back(Node(23))
    cll.add_to_back(Node(56))
    cll.add_to_back(Node(78))
    cll.add_to_back(Node(34))
    cll.add_to_back(Node(53))
    cll.add_to_back(Node(42))
    cll.add_to_back(Node(12))
    cll.add_to_back(Node(35))
    cll.add_to_back(Node(78))
    cll.add_to_back(Node(61))
    cll.add_to_back(Node(90))
    cll.add_to_back(Node(102))
    
    cll.add_to_front(Node(22))
    cll.remove_first()
    cll.add_to_back(Node(19))
    print(cll)