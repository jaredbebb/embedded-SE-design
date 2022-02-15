"""
701. Insert into a Binary Search Tree
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTreeWalk(self, x, op=print):
        """
        CLRS p. 288
        """
        if x is not None:
            self.inorderTreeWalk(x.left, op)
            op(x.val)
            self.inorderTreeWalk(x.right, op)


    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        """
        CLRS p. 294
        """
        y = None
        x = root
        z = TreeNode(val)
        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            else: 
                x = x.right
        if y == None:
            root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        return root



if __name__ == "__main__":
    left2l = TreeNode(1)
    right2l = TreeNode(3)

    left1 = TreeNode(2, left2l, right2l)
    right1 = TreeNode(7)
    
    root = TreeNode(4,left1,right1)

    s = Solution()

    s.inorderTreeWalk(x=root)

    node = s.insertIntoBST(root,5)

    walk = list()
    s.inorderTreeWalk(x=root, op=walk.append)

    assert [1, 2, 3, 4, 5, 7] == walk

    