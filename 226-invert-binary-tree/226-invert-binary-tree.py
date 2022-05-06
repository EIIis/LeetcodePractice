# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Checks if a root even exist
        if root is None:
            return root
        else:
            # Switching from right -> left and left -> right, using a temporary node to help
            tmp = root.right
            root.right = root.left
            root.left = tmp
        
        # Using DFS to do it recursively on both sides of the tree
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
        
        