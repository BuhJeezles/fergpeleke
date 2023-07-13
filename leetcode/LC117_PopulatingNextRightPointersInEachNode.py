"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # write this WITHOUT using a helper function
        
        # recursively using a helper function
        def recursiveConnect(meNode, parent = None):
            # base case
            if meNode == None:
                return
            
            # doing stuff
            if parent == None:
                meNode.next = None
            elif meNode == parent.left:
                meNode.next = parent.right
            else:
                if parent.next != None:
                    meNode.next = parent.next.left
                else:
                    meNode.next = None

            # recursively calling itself
            recursiveConnect(meNode.left, meNode)
            recursiveConnect(meNode.right, meNode)

        recursiveConnect(root)
        return root

            



            

            



            








        '''
        # edge case for empty tree
        if root == None:
            return None

        # base cases
        # if root.left and root.right exist, root.left.next = root.right
        elif root.left != None and root.right != None:
            root.left.next = root.right

        root.left = self.connect(root.left)
        root.right = self.connect(root.right)

        return root


        #TODO - figure out how to do .next for the non-.right-chain .right's
        '''
