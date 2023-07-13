# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root3 = root1
        if root1 != None and root2 != None:
            root3.val = root1.val + root2.val
            root3.left, root3.right = self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right,root2.right)

        elif root1 == None:
            root3 = root2
            
        elif root2 == None:
            root3 = root1

        return root3

        
        # if there's an item in the position for both
            # add them together and create node for merged tree
            # recursively call on the left and right nodes to do this again
        # elif there's one for tree 1
            # put in number from tree 1 into merged tree
        # elif there's one for tree 2:
            # put in number from tree 2 into merged tree