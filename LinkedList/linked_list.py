from node import Node


#Linked List that is automatically sorted in ascending order
class Linked_List:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        
        elif self.head.value < value:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
            
            previous.next = new_node
            new_node.next = runner

    def traverse(self):
        if self.head is None:
            print("List is Empty")
        else:
            runner = self.head
            while (runner is not None):
                print(runner.value, end=" ")
                runner = runner.next
            print()
    
    def delete_node(self, value):
        if self.head is None:
            return False
        
        elif self.head.value == value:
            self.head = self.head.next
            return True
        
        elif self.head.next is not None:
            previous = self.head
            runner = self.head.next
            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
            
            if (runner is not None) and (runner.value == value):
                previous.next = runner.next
                return True
            else:
                return False


