"""

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


    def transplant(self, T, u, v):
        """
        CLRS p. 296
        """
        # u.p == None:
        #     T.root = v
        if u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def minimum(self, root):
        """
        CLRS p. 291
        """
        x = root
        while x.left != None:
            x = x.left
        return x

    #def deleteBST(self, root, val):
    def deleteBST(self, T, z):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        """
        CLRS p. 298
        """
        if z.left == None:
            self.transplant(T, z, z.right)
        elif z.right == None:   
            self.transplant(T, z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.transplant(T, y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(T,z,y)
            y.left = z.left
            y.left.p = y




if __name__ == "__main__":
    left2l = TreeNode(1)
    right2l = TreeNode(3)

    left1 = TreeNode(2, left2l, right2l)
    right1 = TreeNode(7)
    
    root = TreeNode(4,left1,right1)

    s = Solution()

    s.inorderTreeWalk(x=root)

    s.deleteBST(root,right2l)

    walk = list()
    s.inorderTreeWalk(x=root, op=walk.append)

    assert [1, 2, 4, 7] == walk

    