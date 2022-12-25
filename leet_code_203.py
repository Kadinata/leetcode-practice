'''
LeetCode 203: Remove Linked List Elements (Easy)

Problem:
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if head is None:
            return None

        # The value at the head node (and at the following nodes) might be the value 
        # we want to remove. If this is the case, keep advancing the head pointer down 
        # the list until the value of the head node is no longer the value we want to remove.
        while (head is not None) and (head.val == val):
            head = head.next

        current_node = head

        # Now traverse the linked list and remove nodes with the value we want to remove.
        while current_node:

            # There might be multiple nodes in succession with the value we want to remove.
            # If we find the next node is a node we want to remove, stay on the current node
            # and keep removing nodes until the value of the next node is no longer the value
            # we want to remove
            while ((current_node.next is not None) and (current_node.next.val == val)):
                current_node.next = current_node.next.next
            current_node = current_node.next

        return head
