# Delete Middle of Linked List

# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
# If the input linked list is NULL or has 1 node, then it should return NULL

def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    length = getLength(head)
    mid = length//2
    previous = head
    current = head.next
    if (previous is None) or (current is None):
        return None
    else:

        mid = mid - 1
            
        while mid is not 0:
            if current is not None:
                previous = current
                current = current.next
            else:
                return None
                
            mid = mid - 1
        previous.next = current.next
        return head
