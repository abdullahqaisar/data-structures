from linked_list import Linked_List

my_linked_list = Linked_List()

my_linked_list.insert_node(2)
my_linked_list.insert_node(3)
my_linked_list.insert_node(4)
my_linked_list.insert_node(10)
my_linked_list.insert_node(7)

my_linked_list.traverse()

print(my_linked_list.delete_node(2))
print(my_linked_list.delete_node(10))
my_linked_list.traverse()
