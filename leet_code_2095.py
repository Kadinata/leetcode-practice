'''
LeetCode 2095: Delete the Middle Node of a Linked List (Medium)

Problem:
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Solution Explanation:
Let there be two pointers. One pointer iterates over every other node in the list. Let's call this pointer the "fast" pointer. 
The other pointer iterates over every node in the list. Let's call this pointer the "slow" pointer.
If both pointers iterate over the linked-list in the same loop, by the time the "fast" pointer reaches the end of the list,
the "slow" pointer would be pointing to the node in the middle of the list, i.e. the node we want to delete.
However, we need to know the node preceding the node in the middle in order to delete the middle node.
In other words, we'd need to delay the "slow" pointer by one node. The slow pointer needs to start not at the head of the list,
but rather at a node pointing to the head of the list, i.e. we need to create a dummy node with the head as the next node and
point the slow node there.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None

        fast_pointer = head

        # Point the slow pointer to a dummy node to delay it by 1 node.
        slow_pointer = ListNode()
        slow_pointer.next = head

        # Iterate over the list. Advance the fast pointer by 2 nodes
        # and advance the slow pointer by one node.
        while fast_pointer is not None:
            fast_pointer = fast_pointer.next
            if fast_pointer is not None:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
        
        # By the time the fast pointer reaches the end of the list,
        # the next node after the node at the slow pointer should be
        # the node we want to remove.
        slow_pointer.next = slow_pointer.next.next
        return head
