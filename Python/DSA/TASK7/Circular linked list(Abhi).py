class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def add_to_front(self, new_node):
        if self.list_is_empty():
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        # update the tail to be the new node
        self.tail = new_node
    
    def add_to_back(self, new_node):
        if self.list_is_empty():
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node   


    def remove_first(self):
        if self.list_is_empty():
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
        if self.list_is_empty():
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



  
    def list_is_empty(self):
        return not self.tail

    def __str__(self):
        if self.list_is_empty():
            return "Empty List"
        current = self.tail.next
        nodes = []
        while current != self.tail:
            nodes.append(str(current.value))
            current = current.next
        nodes.append(str(current.value))
        return "->".join(nodes)


if __name__ == '__main__':
    my_list = CircularLinkedList()
    print(f"My list is empty? {my_list.list_is_empty()}")

    my_list.add_to_front(Node(5))
    my_list.add_to_front(Node(4))
    my_list.add_to_front(Node(3))
    my_list.add_to_front(Node(2))
    my_list.add_to_front(Node(1))
    my_list.add_to_back(Node(1))
    my_list.add_to_back(Node(2))
    my_list.add_to_back(Node(3))
    my_list.add_to_back(Node(4))
    my_list.add_to_back(Node(5))
    print(my_list)

    my_list.remove_first()
    print(my_list)

    my_list.remove_last()
    print(my_list)
      