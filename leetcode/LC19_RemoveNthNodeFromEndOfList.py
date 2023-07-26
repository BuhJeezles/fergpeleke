# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        currNode = head
        currSpace = head
        prevNode = None

        # finding the node n spaces away from currNum
        for i in range(n):
            currSpace = currSpace.next

        # iterate til currSpace hits the end of the linked list
        while currSpace != None:
            # when the nth from the end is found, assign previous node's .next value as the one after (skipping current node) 
            prevNode = currNode
            currNode = currNode.next
            currSpace = currSpace.next

        # edge case
        if prevNode == None:
            if currNode.next == None:
                return None
            # edge case (removing first item)
            head = currNode.next

        else:
            prevNode.next = currNode.next

        return head

        


        
        




        

