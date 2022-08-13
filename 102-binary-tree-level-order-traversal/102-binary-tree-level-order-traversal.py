# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(root, level=0):
            # Checking root to see if is None
            if root is None:
                return
            else:
                if len(result) == level:
                    result.append([])
                result[level].append(root.val)
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
                
        dfs(root)
        return result
    