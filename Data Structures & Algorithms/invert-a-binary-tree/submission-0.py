# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None
        
        new = root
        #swap order of nodes
        temp = new.right

        new.right = self.invertTree(new.left) if new.left is not None else None
        new.left = self.invertTree(temp) if temp is not None else None
        return new
        #recurse



#brute force - go down tree and swap left and right O(1) per layer O(n) overall and O(1) * n = O(n) aux space

        