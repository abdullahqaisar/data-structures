from linked_list import Linked_List

my_linked_list = Linked_List()

for i in range(1, 7):
    my_linked_list.insert_node(i)

my_linked_list.traverse()

print("Middle Element", my_linked_list.get_middle())

my_linked_list.delete_node(2)
my_linked_list.delete_node(10)

my_linked_list.traverse()
print("Middle Element", my_linked_list.get_middle())
