class Node:

    def __init__(self, new_value, next_node=None):
        self.value = new_value
        self.next = next_node


class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, value):
        new_Node = Node(value)

        if self.head == None:
            self.head = new_Node
        else:
            new_Node.next = self.head
            self.head = new_Node
    
    def pop(self):
        if self.head == None:
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.value

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print("")


s = Stack()
s.push(1)
s.push(2)
s.push(3)

s.traverse()

print(s.pop())