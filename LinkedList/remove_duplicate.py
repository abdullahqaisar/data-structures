# Remove duplicate element from sorted Linked List

# Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
# Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way


#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    n=head
    head=n
    while n.next!=None:
        if n.data==n.next.data:
            n.next=n.next.next
        else:
            n=n.next
        if n==None:
            return head
           
    return head