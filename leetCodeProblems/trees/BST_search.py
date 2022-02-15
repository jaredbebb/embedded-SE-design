"""
700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        if val == None:
            return None
        if  (val == root.val):
            return root
        elif val < root.val:
            if root.left != None:
                return self.searchBST(root.left, val)
        elif root.right != None:
                return self.searchBST(root.right, val)
        else:
            return None

    
if __name__ == "__main__":
    left2l = TreeNode(1)
    right2l = TreeNode(3)
    left1 = TreeNode(2, left2l, right2l)
    right1 = TreeNode(7)
    root = TreeNode(4,left1,right1)

    s = Solution()
    node = s.searchBST(root,2)
    print(node)

    assert left1 == node
