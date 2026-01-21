# binary tree, 
# full binary tree(strict binary tree),
#  complete binary tree,
# perfect bt,
# balance bt,
# degenerate bt

#AVL tree , bst, binary etc study

#preorder, inorder, postorder, level order traversals

#leetcode

'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def p(r,res):
            if r:
                res.append(r.val)
                p(r.left,res)
                p(r.right,res)
            return res
        return p(root,[])
'''

'''class Solution:
    def inorderTraversal(self, root):
        def dfs(r, res):
            if r:
                dfs(r.left, res)    # Left
                res.append(r.val)   # Root
                dfs(r.right, res)   # Right
            return res
        
        return dfs(root, [])
'''

''' class Solution:
    def postorderTraversal(self, root):
        def dfs(r, res):
            if r:
                dfs(r.left, res)    # Left
                dfs(r.right, res)   # Right
                res.append(r.val)   # Root
            return res
        
        return dfs(root, [])
'''