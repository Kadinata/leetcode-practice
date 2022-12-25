'''
LeetCode 98: Validate Binary Search Tree (Medium)

Link:
https://leetcode.com/problems/validate-binary-search-tree/

Problem:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Solution Explanation:
An inorder traversal of a valid BST would yield a list of values sorted in ascending order.
Therefore, the validity of a binary tree can be determined using the following method:
1. Perform inorder traversal of the tree and store each value of the tree nodes in an array.
2. Verify the array is sorted in an ascending order.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Helper function to perform an inorder traversal of a binary tree
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        result.extend(self.inOrderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inOrderTraversal(root.right))
        return result

    # Solution
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        if not root.left and not root.right:
            return True

        # Step 1: perform inorder traversal on the tree
        traversed_tree = self.inOrderTraversal(root)

        # Step 2: Verify the result of the inorder traversal is an 
        # array sorted in ascending order.
        n = traversed_tree[0]
        for m in traversed_tree[1:]:
            if n >= m: 
                return False
            n = m
        
        return True