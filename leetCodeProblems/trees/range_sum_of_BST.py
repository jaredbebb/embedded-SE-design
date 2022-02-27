"""
938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.SUM = 0
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root!= None:
            self.rangeSumBST(root.left, low, high)
            if root.val >= low and root.val <= high:
                self.SUM += root.val
            self.rangeSumBST(root.right, low, high)
        return self.SUM


if __name__ == "__main__":

    left1 = TreeNode(3)
    rightl = TreeNode(7)

    left = TreeNode(5, left1, rightl)

    right2 = TreeNode(18)
    right = TreeNode(15, None, right2)
    
    root = TreeNode(10,left,right)

    s = Solution()
    val = s.rangeSumBST(root = root, low = 7, high = 15)
    assert 32 == val
